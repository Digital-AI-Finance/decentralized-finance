"""
Chart Text Overlap Detector
Analyzes matplotlib chart scripts to detect potential text overlap issues.

Detection methods:
1. Static analysis: Find text elements with similar coordinates
2. Runtime analysis: Render chart and detect bounding box overlaps

Usage:
    python chart_overlap_detector.py <chart.py>
    python chart_overlap_detector.py --render <chart.py>  # Full render analysis
"""

import ast
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import warnings


class TextElement:
    """Represents a text element in a chart."""
    def __init__(self, x: float, y: float, text: str, fontsize: int,
                 ha: str = 'center', va: str = 'center', line_num: int = 0):
        self.x = x
        self.y = y
        self.text = text
        self.fontsize = fontsize
        self.ha = ha  # horizontal alignment
        self.va = va  # vertical alignment
        self.line_num = line_num

        # Estimate bounding box (rough approximation)
        # Assume each character is ~0.6 * fontsize wide, height is ~1.2 * fontsize
        char_width = 0.006 * fontsize  # in normalized coords (0-1)
        char_height = 0.012 * fontsize

        text_width = len(text) * char_width
        text_height = char_height * (1 + text.count('\n'))

        # Adjust for alignment
        if ha == 'center':
            self.x_min = x - text_width / 2
            self.x_max = x + text_width / 2
        elif ha == 'left':
            self.x_min = x
            self.x_max = x + text_width
        else:  # right
            self.x_min = x - text_width
            self.x_max = x

        if va == 'center':
            self.y_min = y - text_height / 2
            self.y_max = y + text_height / 2
        elif va == 'bottom':
            self.y_min = y
            self.y_max = y + text_height
        else:  # top
            self.y_min = y - text_height
            self.y_max = y

    def overlaps(self, other: 'TextElement', margin: float = 0.02) -> bool:
        """Check if this text element overlaps with another."""
        # Add margin for near-overlaps
        return not (self.x_max + margin < other.x_min or
                    other.x_max + margin < self.x_min or
                    self.y_max + margin < other.y_min or
                    other.y_max + margin < self.y_min)

    def __repr__(self):
        return f"Text('{self.text[:20]}...' at ({self.x:.2f}, {self.y:.2f}), size={self.fontsize})"


class ChartOverlapDetector:
    def __init__(self, chart_path: Path):
        self.chart_path = chart_path
        self.text_elements: List[TextElement] = []
        self.patch_elements: List[Dict] = []  # Rectangles, circles, etc.
        self.issues: List[Dict] = []
        self.code = ""

    def analyze(self) -> List[Dict]:
        """Analyze chart for text overlaps."""
        if not self.chart_path.exists():
            self.issues.append({
                'type': 'FILE_NOT_FOUND',
                'message': f'Chart file not found: {self.chart_path}',
                'severity': 'ERROR'
            })
            return self.issues

        self.code = self.chart_path.read_text(encoding='utf-8')

        self._extract_text_elements()
        self._extract_patch_elements()
        self._check_text_text_overlaps()
        self._check_text_patch_overlaps()
        self._check_crowded_regions()

        return self.issues

    def _extract_text_elements(self):
        """Extract text element positions from code."""
        # Pattern for ax.text(x, y, 'text', ..., fontsize=N, ha='...', va='...')
        text_pattern = r"ax\d?\.text\s*\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*['\"]([^'\"]+)['\"]([^)]*)\)"

        for line_num, line in enumerate(self.code.split('\n'), 1):
            match = re.search(text_pattern, line)
            if match:
                x, y, text = float(match.group(1)), float(match.group(2)), match.group(3)
                rest = match.group(4)

                # Extract fontsize
                fontsize_match = re.search(r'fontsize\s*=\s*(\d+)', rest)
                fontsize = int(fontsize_match.group(1)) if fontsize_match else 10

                # Extract alignment
                ha_match = re.search(r"ha\s*=\s*['\"](\w+)['\"]", rest)
                ha = ha_match.group(1) if ha_match else 'center'

                va_match = re.search(r"va\s*=\s*['\"](\w+)['\"]", rest)
                va = va_match.group(1) if va_match else 'center'

                self.text_elements.append(TextElement(x, y, text, fontsize, ha, va, line_num))

    def _extract_patch_elements(self):
        """Extract patch (rectangle, circle) positions from code."""
        # Pattern for Rectangle((x, y), width, height, ...)
        rect_pattern = r"Rectangle\s*\(\s*\(\s*([\d.]+)\s*,\s*([\d.]+)\s*\)\s*,\s*([\d.]+)\s*,\s*([\d.]+)"

        for line_num, line in enumerate(self.code.split('\n'), 1):
            match = re.search(rect_pattern, line)
            if match:
                x, y = float(match.group(1)), float(match.group(2))
                w, h = float(match.group(3)), float(match.group(4))
                self.patch_elements.append({
                    'type': 'rectangle',
                    'x_min': x, 'y_min': y,
                    'x_max': x + w, 'y_max': y + h,
                    'line_num': line_num
                })

        # Pattern for FancyBboxPatch((x, y), width, height, ...)
        fancy_pattern = r"FancyBboxPatch\s*\(\s*\(\s*([\d.]+)\s*,\s*([\d.]+)\s*\)\s*,\s*([\d.]+)\s*,\s*([\d.]+)"

        for line_num, line in enumerate(self.code.split('\n'), 1):
            match = re.search(fancy_pattern, line)
            if match:
                x, y = float(match.group(1)), float(match.group(2))
                w, h = float(match.group(3)), float(match.group(4))
                self.patch_elements.append({
                    'type': 'fancybox',
                    'x_min': x, 'y_min': y,
                    'x_max': x + w, 'y_max': y + h,
                    'line_num': line_num
                })

    def _check_text_text_overlaps(self):
        """Check for overlapping text elements."""
        for i, t1 in enumerate(self.text_elements):
            for t2 in self.text_elements[i+1:]:
                if t1.overlaps(t2):
                    self.issues.append({
                        'type': 'TEXT_OVERLAP',
                        'message': f"Text overlap detected:\n"
                                   f"  Line {t1.line_num}: '{t1.text}' at ({t1.x:.2f}, {t1.y:.2f})\n"
                                   f"  Line {t2.line_num}: '{t2.text}' at ({t2.x:.2f}, {t2.y:.2f})",
                        'severity': 'ERROR',
                        'fix': 'Adjust y positions to separate text elements (typically need 0.05-0.08 spacing)'
                    })

    def _check_text_patch_overlaps(self):
        """Check if text overlaps with patch boundaries (edges)."""
        for text in self.text_elements:
            for patch in self.patch_elements:
                # Check if text is near patch edge (within margin)
                margin = 0.03

                # Check if text center is close to any edge
                near_left = abs(text.x - patch['x_min']) < margin
                near_right = abs(text.x - patch['x_max']) < margin
                near_bottom = abs(text.y - patch['y_min']) < margin
                near_top = abs(text.y - patch['y_max']) < margin

                # Check if text is inside patch y-range
                in_y_range = patch['y_min'] - margin < text.y < patch['y_max'] + margin
                in_x_range = patch['x_min'] - margin < text.x < patch['x_max'] + margin

                if (near_left or near_right) and in_y_range:
                    self.issues.append({
                        'type': 'TEXT_NEAR_EDGE',
                        'message': f"Text near patch edge:\n"
                                   f"  Line {text.line_num}: '{text.text}' at x={text.x:.2f}\n"
                                   f"  Patch edge at x={patch['x_min']:.2f} or x={patch['x_max']:.2f}",
                        'severity': 'WARNING',
                        'fix': 'Move text further from patch edge (adjust x position)'
                    })
                    break

    def _check_crowded_regions(self):
        """Check for regions with too many text elements."""
        # Divide space into grid and count elements per cell
        grid_size = 5
        grid = {}

        for text in self.text_elements:
            cell_x = int(text.x * grid_size)
            cell_y = int(text.y * grid_size)
            key = (cell_x, cell_y)
            if key not in grid:
                grid[key] = []
            grid[key].append(text)

        for (cx, cy), texts in grid.items():
            if len(texts) > 3:
                self.issues.append({
                    'type': 'CROWDED_REGION',
                    'message': f"Crowded region at grid ({cx}, {cy}): {len(texts)} text elements\n"
                               f"  Elements: {[t.text[:15] for t in texts]}",
                    'severity': 'WARNING',
                    'fix': 'Spread text elements across larger area or reduce count'
                })

    def print_report(self):
        """Print analysis report."""
        print(f"\n{'='*60}")
        print(f"Chart Overlap Analysis: {self.chart_path.name}")
        print(f"{'='*60}")
        print(f"Found {len(self.text_elements)} text elements")
        print(f"Found {len(self.patch_elements)} patch elements")

        if not self.issues:
            print("\nOK - No overlap issues detected")
            return

        errors = [i for i in self.issues if i['severity'] == 'ERROR']
        warnings = [i for i in self.issues if i['severity'] == 'WARNING']

        if errors:
            print(f"\nERRORS ({len(errors)}):")
            for i, issue in enumerate(errors, 1):
                print(f"\n  {i}. [{issue['type']}]")
                print(f"     {issue['message']}")
                if 'fix' in issue:
                    print(f"     FIX: {issue['fix']}")

        if warnings:
            print(f"\nWARNINGS ({len(warnings)}):")
            for i, issue in enumerate(warnings, 1):
                print(f"\n  {i}. [{issue['type']}]")
                print(f"     {issue['message']}")
                if 'fix' in issue:
                    print(f"     FIX: {issue['fix']}")


def render_and_detect(chart_path: Path) -> List[Dict]:
    """
    Render the chart and detect actual bounding box overlaps.
    This is more accurate but requires matplotlib.
    """
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    issues = []

    # Execute the chart script in isolated namespace
    namespace = {'__name__': '__main__', '__file__': str(chart_path)}

    # Monkey-patch plt.savefig and plt.show to prevent actual output
    original_savefig = plt.savefig
    original_show = plt.show
    original_close = plt.close

    plt.savefig = lambda *args, **kwargs: None
    plt.show = lambda *args, **kwargs: None

    try:
        exec(chart_path.read_text(encoding='utf-8'), namespace)

        # Get current figure
        fig = plt.gcf()
        canvas = FigureCanvasAgg(fig)
        canvas.draw()

        # Get renderer
        renderer = canvas.get_renderer()

        # Collect all text bounding boxes
        text_bboxes = []
        for ax in fig.axes:
            for text in ax.texts:
                bbox = text.get_window_extent(renderer)
                text_bboxes.append({
                    'text': text.get_text()[:30],
                    'bbox': bbox,
                    'position': text.get_position()
                })

        # Check for overlaps
        for i, t1 in enumerate(text_bboxes):
            for t2 in text_bboxes[i+1:]:
                if t1['bbox'].overlaps(t2['bbox']):
                    issues.append({
                        'type': 'RENDERED_OVERLAP',
                        'message': f"Actual overlap detected:\n"
                                   f"  '{t1['text']}' at {t1['position']}\n"
                                   f"  '{t2['text']}' at {t2['position']}",
                        'severity': 'ERROR'
                    })

    except Exception as e:
        issues.append({
            'type': 'RENDER_ERROR',
            'message': f"Could not render chart: {str(e)}",
            'severity': 'WARNING'
        })
    finally:
        plt.savefig = original_savefig
        plt.show = original_show
        plt.close('all')

    return issues


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    render_mode = False
    chart_arg = sys.argv[1]

    if chart_arg == '--render':
        render_mode = True
        chart_arg = sys.argv[2] if len(sys.argv) > 2 else None

    if not chart_arg:
        print("Error: No chart file specified")
        sys.exit(1)

    chart_path = Path(chart_arg)
    if chart_path.is_dir():
        chart_path = chart_path / 'chart.py'

    # Static analysis
    detector = ChartOverlapDetector(chart_path)
    detector.analyze()
    detector.print_report()

    # Optional render analysis
    if render_mode:
        print("\n--- Render Analysis ---")
        render_issues = render_and_detect(chart_path)
        if render_issues:
            for issue in render_issues:
                print(f"[{issue['severity']}] {issue['type']}: {issue['message']}")
        else:
            print("No overlaps detected in rendered output")


if __name__ == '__main__':
    main()
