"""
Chart Readability Analyzer for Beamer Slides
Analyzes chart.py files to detect potential readability issues when scaled on slides.

Key issues detected:
1. Font sizes too small (< 11pt is problematic when chart is scaled to 0.5-0.7 textwidth)
2. Too many elements in a single figure
3. Text-heavy diagrams that should be LaTeX instead
4. Multi-panel layouts (subplots) that should be split

Usage:
    python chart_readability_analyzer.py <chart_folder_or_file>
    python chart_readability_analyzer.py --all  # Analyze all charts in project
"""

import ast
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Minimum font sizes for different chart widths on slides
# When chart is at 0.5\textwidth, fonts need to be ~2x larger to appear same size
FONT_SCALING = {
    0.45: 2.2,  # Chart at 45% width needs fonts 2.2x larger
    0.50: 2.0,  # Chart at 50% width needs fonts 2x larger
    0.55: 1.8,
    0.60: 1.7,
    0.65: 1.5,
    0.70: 1.4,
    0.75: 1.3,
    0.80: 1.25,
}

# Slide text is 8pt, so minimum readable font after scaling should be ~8pt
MIN_READABLE_PT = 8
RECOMMENDED_MIN_FONT = 11  # Before scaling


class ChartReadabilityAnalyzer:
    def __init__(self, chart_path: Path):
        self.chart_path = chart_path
        self.issues: List[Dict] = []
        self.warnings: List[Dict] = []
        self.code = ""

    def analyze(self) -> Tuple[List[Dict], List[Dict]]:
        """Analyze chart.py for readability issues."""
        if not self.chart_path.exists():
            self.issues.append({
                'type': 'FILE_NOT_FOUND',
                'message': f'Chart file not found: {self.chart_path}',
                'severity': 'ERROR'
            })
            return self.issues, self.warnings

        self.code = self.chart_path.read_text(encoding='utf-8')

        self._check_font_sizes()
        self._check_subplots()
        self._check_text_density()
        self._check_rcparams()
        self._check_figsize()

        return self.issues, self.warnings

    def _check_font_sizes(self):
        """Check for fontsize parameters that are too small."""
        # Pattern: fontsize=N or fontsize = N
        fontsize_pattern = r'fontsize\s*=\s*(\d+)'
        matches = re.findall(fontsize_pattern, self.code)

        small_fonts = [int(m) for m in matches if int(m) < RECOMMENDED_MIN_FONT]

        if small_fonts:
            self.issues.append({
                'type': 'SMALL_FONT',
                'message': f'Font sizes too small: {small_fonts}. Minimum recommended: {RECOMMENDED_MIN_FONT}pt',
                'severity': 'ERROR',
                'fix': f'Increase all fontsize values to at least {RECOMMENDED_MIN_FONT}'
            })

        # Check for very small fonts (< 8pt) - critical
        critical_fonts = [f for f in small_fonts if f < 8]
        if critical_fonts:
            self.issues.append({
                'type': 'CRITICAL_SMALL_FONT',
                'message': f'Critical: Font sizes {critical_fonts}pt will be unreadable on slides',
                'severity': 'CRITICAL',
                'fix': 'Increase to at least 11pt or simplify chart content'
            })

    def _check_subplots(self):
        """Check for multi-panel layouts that should be split."""
        # Pattern: plt.subplots(N, M) or subplots(N,M) where N*M > 1
        subplot_pattern = r'subplots\s*\(\s*(\d+)\s*,\s*(\d+)'
        matches = re.findall(subplot_pattern, self.code)

        for rows, cols in matches:
            total = int(rows) * int(cols)
            if total > 1:
                self.issues.append({
                    'type': 'MULTI_PANEL',
                    'message': f'Multi-panel layout detected: {rows}x{cols}={total} panels',
                    'severity': 'ERROR',
                    'fix': 'Split into separate chart folders: chart_01a, chart_01b, etc.'
                })

    def _check_text_density(self):
        """Check for charts with too many text elements."""
        # Count ax.text() calls
        text_calls = len(re.findall(r'ax\d?\.text\s*\(', self.code))
        text_calls += len(re.findall(r'\.annotate\s*\(', self.code))

        if text_calls > 15:
            self.warnings.append({
                'type': 'HIGH_TEXT_DENSITY',
                'message': f'High text density: {text_calls} text elements. Consider simplifying.',
                'severity': 'WARNING',
                'fix': 'Reduce text elements or convert to LaTeX bullet points'
            })
        elif text_calls > 25:
            self.issues.append({
                'type': 'EXCESSIVE_TEXT',
                'message': f'Excessive text: {text_calls} elements. This should likely be LaTeX, not a chart.',
                'severity': 'ERROR',
                'fix': 'Convert to LaTeX text/itemize instead of matplotlib figure'
            })

    def _check_rcparams(self):
        """Check if rcParams sets appropriate font sizes."""
        if 'rcParams' in self.code:
            # Check font.size setting
            font_size_match = re.search(r"'font\.size'\s*:\s*(\d+)", self.code)
            if font_size_match:
                size = int(font_size_match.group(1))
                if size < 10:
                    self.warnings.append({
                        'type': 'LOW_RCPARAMS_FONT',
                        'message': f"rcParams font.size={size} is low. Recommend 12+",
                        'severity': 'WARNING',
                        'fix': "Set 'font.size': 12 in rcParams"
                    })
        else:
            self.warnings.append({
                'type': 'NO_RCPARAMS',
                'message': 'No rcParams configuration found',
                'severity': 'INFO',
                'fix': 'Add plt.rcParams.update() with appropriate font sizes'
            })

    def _check_figsize(self):
        """Check figure size for appropriate aspect ratio."""
        figsize_pattern = r'figsize\s*=\s*\(\s*([\d.]+)\s*,\s*([\d.]+)\s*\)'
        match = re.search(figsize_pattern, self.code)

        if match:
            width, height = float(match.group(1)), float(match.group(2))
            aspect = width / height

            # For 16:9 slides, charts should be wider than tall
            if aspect < 1.2:
                self.warnings.append({
                    'type': 'SQUARE_ASPECT',
                    'message': f'Figure aspect ratio {aspect:.2f} is nearly square. Consider wider format.',
                    'severity': 'INFO',
                    'fix': 'Use figsize=(10, 6) for 16:9 slides'
                })

    def get_effective_font_size(self, original_size: int, chart_width_fraction: float) -> float:
        """Calculate effective font size after chart is scaled on slide."""
        # Find the closest width in our scaling table
        closest_width = min(FONT_SCALING.keys(), key=lambda x: abs(x - chart_width_fraction))
        scale_factor = FONT_SCALING[closest_width]

        effective_size = original_size / scale_factor
        return effective_size

    def print_report(self):
        """Print a formatted report of issues and warnings."""
        print(f"\n{'='*60}")
        print(f"Chart Readability Analysis: {self.chart_path.name}")
        print(f"{'='*60}")

        if not self.issues and not self.warnings:
            print("OK - No readability issues detected")
            return

        if self.issues:
            print(f"\nISSUES ({len(self.issues)}):")
            for i, issue in enumerate(self.issues, 1):
                print(f"  {i}. [{issue['severity']}] {issue['type']}")
                print(f"     {issue['message']}")
                if 'fix' in issue:
                    print(f"     FIX: {issue['fix']}")

        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. [{warning['severity']}] {warning['type']}")
                print(f"     {warning['message']}")
                if 'fix' in warning:
                    print(f"     FIX: {warning['fix']}")


def analyze_all_charts(base_path: Path) -> Dict[str, Tuple[List, List]]:
    """Analyze all chart.py files in the project."""
    results = {}

    # Find all chart.py files
    chart_files = list(base_path.rglob('chart.py'))

    print(f"Found {len(chart_files)} chart files to analyze\n")

    total_issues = 0
    total_warnings = 0

    for chart_file in sorted(chart_files):
        analyzer = ChartReadabilityAnalyzer(chart_file)
        issues, warnings = analyzer.analyze()
        results[str(chart_file)] = (issues, warnings)

        if issues or warnings:
            analyzer.print_report()
            total_issues += len(issues)
            total_warnings += len(warnings)

    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(chart_files)} charts analyzed")
    print(f"  Total issues: {total_issues}")
    print(f"  Total warnings: {total_warnings}")
    print(f"{'='*60}")

    return results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

    if arg == '--all':
        # Find project root (look for CLAUDE.md or .git)
        current = Path.cwd()
        while current != current.parent:
            if (current / 'CLAUDE.md').exists() or (current / '.git').exists():
                break
            current = current.parent

        analyze_all_charts(current)
    else:
        path = Path(arg)
        if path.is_dir():
            chart_file = path / 'chart.py'
        else:
            chart_file = path

        analyzer = ChartReadabilityAnalyzer(chart_file)
        analyzer.analyze()
        analyzer.print_report()


if __name__ == '__main__':
    main()
