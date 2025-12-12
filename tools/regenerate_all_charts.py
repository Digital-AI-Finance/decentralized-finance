"""
Regenerate All Charts
Executes all chart.py files in the project to regenerate chart PDFs.
"""

import subprocess
import sys
from pathlib import Path

def regenerate_all_charts(base_path: Path):
    """Find and execute all chart.py files."""
    chart_files = list(base_path.rglob('chart.py'))

    # Exclude tools directory
    chart_files = [f for f in chart_files if 'tools' not in str(f)]

    print(f"Found {len(chart_files)} chart files to regenerate\n")

    success = 0
    failed = 0

    for i, chart_file in enumerate(sorted(chart_files), 1):
        relative = chart_file.relative_to(base_path)
        print(f"[{i}/{len(chart_files)}] Regenerating: {relative}")

        try:
            result = subprocess.run(
                [sys.executable, str(chart_file)],
                cwd=chart_file.parent,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print(f"  -> OK")
                success += 1
            else:
                print(f"  -> ERROR: {result.stderr[:200]}")
                failed += 1

        except subprocess.TimeoutExpired:
            print(f"  -> TIMEOUT")
            failed += 1
        except Exception as e:
            print(f"  -> EXCEPTION: {str(e)[:100]}")
            failed += 1

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total charts: {len(chart_files)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")

    return failed == 0


if __name__ == '__main__':
    # Find project root
    current = Path(__file__).parent.parent

    success = regenerate_all_charts(current)
    sys.exit(0 if success else 1)
