"""
Chart Font Size Enforcer
Automatically increases font sizes in chart.py files to meet minimum requirements.

For charts displayed at 0.5-0.7 textwidth on 8pt Beamer slides:
- Minimum font size should be 14pt (titles: 16pt, labels: 14pt, annotations: 12pt)
- This ensures readability after scaling down

Usage:
    python chart_font_enforcer.py <chart.py>           # Check and report
    python chart_font_enforcer.py <chart.py> --fix     # Auto-fix font sizes
    python chart_font_enforcer.py --all                # Check all charts
    python chart_font_enforcer.py --all --fix          # Fix all charts
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Minimum font sizes for readability on scaled charts
MIN_FONTS = {
    'title': 16,
    'header': 16,
    'label': 14,
    'tick': 12,
    'legend': 12,
    'annotation': 12,
    'default': 14,
}

# rcParams minimum values
RCPARAMS_MIN = {
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
}


class ChartFontEnforcer:
    def __init__(self, chart_path: Path):
        self.chart_path = chart_path
        self.original_code = ""
        self.fixed_code = ""
        self.issues: List[Dict] = []
        self.fixes_made: List[str] = []

    def analyze(self) -> List[Dict]:
        """Analyze chart for font size issues."""
        if not self.chart_path.exists():
            self.issues.append({
                'type': 'FILE_NOT_FOUND',
                'message': f'File not found: {self.chart_path}'
            })
            return self.issues

        self.original_code = self.chart_path.read_text(encoding='utf-8')
        self.fixed_code = self.original_code

        self._check_rcparams()
        self._check_fontsize_params()

        return self.issues

    def _check_rcparams(self):
        """Check and fix rcParams font sizes."""
        for param, min_val in RCPARAMS_MIN.items():
            # Pattern: 'param': N or "param": N
            pattern = rf"(['\"]){re.escape(param)}\1\s*:\s*(\d+)"
            match = re.search(pattern, self.fixed_code)

            if match:
                current_val = int(match.group(2))
                if current_val < min_val:
                    self.issues.append({
                        'type': 'RCPARAMS_TOO_SMALL',
                        'param': param,
                        'current': current_val,
                        'minimum': min_val
                    })
                    # Fix it
                    old = match.group(0)
                    new = old.replace(str(current_val), str(min_val))
                    self.fixed_code = self.fixed_code.replace(old, new)
                    self.fixes_made.append(f"rcParams['{param}']: {current_val} -> {min_val}")

    def _check_fontsize_params(self):
        """Check and fix fontsize=N parameters."""
        # Pattern: fontsize=N or fontsize = N
        pattern = r'fontsize\s*=\s*(\d+)'

        def replace_fontsize(match):
            current = int(match.group(1))
            if current < MIN_FONTS['default']:
                new_size = max(MIN_FONTS['default'], int(current * 1.3))  # 30% increase, minimum 14
                self.issues.append({
                    'type': 'FONTSIZE_TOO_SMALL',
                    'current': current,
                    'fixed': new_size
                })
                self.fixes_made.append(f"fontsize: {current} -> {new_size}")
                return f'fontsize={new_size}'
            return match.group(0)

        self.fixed_code = re.sub(pattern, replace_fontsize, self.fixed_code)

    def fix(self) -> bool:
        """Apply fixes to the file."""
        if self.fixed_code != self.original_code:
            self.chart_path.write_text(self.fixed_code, encoding='utf-8')
            return True
        return False

    def print_report(self):
        """Print analysis report."""
        print(f"\n{'='*60}")
        print(f"Font Analysis: {self.chart_path.name}")
        print(f"{'='*60}")

        if not self.issues:
            print("OK - All font sizes meet minimum requirements")
            return

        print(f"\nISSUES FOUND ({len(self.issues)}):")
        for issue in self.issues:
            if issue['type'] == 'RCPARAMS_TOO_SMALL':
                print(f"  - rcParams['{issue['param']}']: {issue['current']}pt < {issue['minimum']}pt minimum")
            elif issue['type'] == 'FONTSIZE_TOO_SMALL':
                print(f"  - fontsize={issue['current']}pt < {MIN_FONTS['default']}pt minimum")

        if self.fixes_made:
            print(f"\nFIXES TO APPLY ({len(self.fixes_made)}):")
            for fix in self.fixes_made:
                print(f"  - {fix}")


def process_all_charts(base_path: Path, fix: bool = False) -> Dict[str, List]:
    """Process all chart.py files in the project."""
    results = {}
    chart_files = list(base_path.rglob('chart.py'))

    print(f"Found {len(chart_files)} chart files\n")

    total_issues = 0
    total_fixed = 0

    for chart_file in sorted(chart_files):
        enforcer = ChartFontEnforcer(chart_file)
        issues = enforcer.analyze()

        if issues:
            enforcer.print_report()
            total_issues += len(issues)

            if fix:
                if enforcer.fix():
                    print(f"  -> FIXED: {chart_file.relative_to(base_path)}")
                    total_fixed += 1

        results[str(chart_file)] = issues

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Charts analyzed: {len(chart_files)}")
    print(f"Total issues: {total_issues}")
    if fix:
        print(f"Charts fixed: {total_fixed}")

    return results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    fix_mode = '--fix' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--fix']

    if '--all' in args:
        # Find project root
        current = Path.cwd()
        while current != current.parent:
            if (current / 'CLAUDE.md').exists() or (current / '.git').exists():
                break
            current = current.parent

        process_all_charts(current, fix=fix_mode)
    else:
        chart_path = Path(args[0])
        if chart_path.is_dir():
            chart_path = chart_path / 'chart.py'

        enforcer = ChartFontEnforcer(chart_path)
        enforcer.analyze()
        enforcer.print_report()

        if fix_mode and enforcer.fixes_made:
            enforcer.fix()
            print(f"\n-> File updated with {len(enforcer.fixes_made)} fixes")


if __name__ == '__main__':
    main()
