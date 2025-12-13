"""
Count Charts Per Lesson
Scans all lesson folders and counts chart.py files in each.
"""

from pathlib import Path
from collections import defaultdict
import re

BASE_DIR = Path(__file__).parent.parent


def count_charts():
    """Count charts per lesson."""
    lesson_charts = defaultdict(list)

    for chart_file in sorted(BASE_DIR.rglob('*/chart.py')):
        path_str = str(chart_file)
        if 'tools' in path_str or path_str.startswith('charts'):
            continue

        # Find the lesson folder
        for parent in chart_file.parents:
            if parent.name.startswith('L') and '_' in parent.name:
                # Check if this folder has a .tex file (real lesson)
                presentations_dir = parent / 'presentations'
                has_tex = (
                    any(parent.glob('*.tex')) or
                    (presentations_dir.exists() and any(presentations_dir.glob('*.tex')))
                )
                if has_tex:
                    lesson_charts[parent.name].append(chart_file.parent.name)
                    break

    return lesson_charts


def main():
    lesson_charts = count_charts()

    # Print formatted table
    print(f"{'#':<4} {'Lesson':<40} {'Charts':>6}")
    print('=' * 52)

    total = 0
    for i, lesson in enumerate(sorted(lesson_charts.keys(),
                                       key=lambda x: int(re.search(r'L(\d+)', x).group(1))), 1):
        charts = lesson_charts[lesson]
        total += len(charts)
        short_name = lesson.replace('_', ' ').replace('Lab ', '[Lab] ')
        print(f"{i:<4} {short_name:<40} {len(charts):>6}")

    print('=' * 52)
    print(f"{'':4} {'TOTAL (48 lessons)':<40} {total:>6}")
    print(f"{'':4} {'Average per lesson':<40} {total/48:>6.1f}")

    # Stats by type
    labs = [l for l in lesson_charts if 'Lab' in l]
    lectures = [l for l in lesson_charts if 'Lab' not in l]
    lab_charts = sum(len(lesson_charts[l]) for l in labs)
    lecture_charts = sum(len(lesson_charts[l]) for l in lectures)

    print(f"\n{'Type':<20} {'Lessons':>8} {'Charts':>8} {'Avg':>6}")
    print('-' * 44)
    print(f"{'Lectures':<20} {len(lectures):>8} {lecture_charts:>8} {lecture_charts/len(lectures):>6.1f}")
    print(f"{'Labs':<20} {len(labs):>8} {lab_charts:>8} {lab_charts/len(labs):>6.1f}")

    # Shared charts
    shared_charts = list((BASE_DIR / 'charts').glob('*/chart.py'))
    print(f"\n{'Shared charts (charts/)':<40} {len(shared_charts):>6}")
    print(f"{'GRAND TOTAL':<40} {total + len(shared_charts):>6}")


if __name__ == "__main__":
    main()
