"""
Cleanup Old Lesson Versions
Keeps only the latest timestamped version of each lesson.
Moves older versions to previous/ folders.
"""

import re
import shutil
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent


def get_timestamp(filename):
    """Extract timestamp from filename like 20251211_1400_L01_Name.pdf"""
    match = re.match(r'^(\d{8}_\d{4})_', filename)
    return match.group(1) if match else None


def get_lesson_id(filename):
    """Extract lesson ID like L01, L02, etc."""
    match = re.search(r'_(L\d{2})_', filename)
    return match.group(1) if match else None


def cleanup_lesson_folder(folder_path, dry_run=False):
    """Clean up a single lesson folder, keeping only latest versions."""
    moved = []

    # Check if this is a presentations/ subfolder structure
    presentations_dir = folder_path / "presentations"
    target_dir = presentations_dir if presentations_dir.exists() else folder_path

    # Group files by type and lesson
    pdf_files = defaultdict(list)
    tex_files = defaultdict(list)

    for f in target_dir.iterdir():
        if f.is_file():
            timestamp = get_timestamp(f.name)
            lesson_id = get_lesson_id(f.name)

            if timestamp and lesson_id:
                if f.suffix == '.pdf':
                    pdf_files[lesson_id].append(f)
                elif f.suffix == '.tex':
                    tex_files[lesson_id].append(f)

    # Process PDFs
    for lesson_id, files in pdf_files.items():
        if len(files) > 1:
            # Sort by timestamp descending (latest first)
            files.sort(key=lambda x: get_timestamp(x.name), reverse=True)
            latest = files[0]
            old_files = files[1:]

            # Create previous folder if needed
            prev_dir = target_dir / "previous"
            if not dry_run:
                prev_dir.mkdir(exist_ok=True)

            for old_file in old_files:
                dest = prev_dir / old_file.name
                if not dry_run:
                    shutil.move(str(old_file), str(dest))
                moved.append((old_file, dest))
                print(f"  PDF: {old_file.name} -> previous/")

    # Process TEX files
    for lesson_id, files in tex_files.items():
        if len(files) > 1:
            files.sort(key=lambda x: get_timestamp(x.name), reverse=True)
            latest = files[0]
            old_files = files[1:]

            prev_dir = target_dir / "previous"
            if not dry_run:
                prev_dir.mkdir(exist_ok=True)

            for old_file in old_files:
                dest = prev_dir / old_file.name
                if not dry_run:
                    shutil.move(str(old_file), str(dest))
                moved.append((old_file, dest))
                print(f"  TEX: {old_file.name} -> previous/")

    return moved


def cleanup_orphan_charts(dry_run=False):
    """Delete orphan timestamped chart PDFs in L01/charts/"""
    deleted = []
    charts_dir = BASE_DIR / "Module_A_Blockchain_Foundations" / "L01_What_is_Blockchain" / "charts"

    if not charts_dir.exists():
        return deleted

    for f in charts_dir.iterdir():
        if f.is_file() and f.suffix == '.pdf' and f.name.startswith('2025'):
            # These are orphan PDFs not in subfolders
            if not dry_run:
                f.unlink()
            deleted.append(f)
            print(f"  Deleted orphan: {f.name}")

    return deleted


def main(dry_run=False):
    print("=" * 60)
    print("Cleanup Old Lesson Versions")
    print("=" * 60)

    if dry_run:
        print("\n[DRY RUN - No changes will be made]\n")

    total_moved = []

    # Find all lesson folders
    for module_dir in sorted(BASE_DIR.glob("Module_*")):
        print(f"\n{module_dir.name}")

        for lesson_dir in sorted(module_dir.glob("L*")):
            if lesson_dir.is_dir():
                moved = cleanup_lesson_folder(lesson_dir, dry_run)
                total_moved.extend(moved)

    # Clean up orphan charts
    print("\nCleaning orphan chart PDFs...")
    deleted = cleanup_orphan_charts(dry_run)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files moved to previous/: {len(total_moved)}")
    print(f"Orphan charts deleted: {len(deleted)}")

    if dry_run:
        print("\n[DRY RUN complete - run without --dry-run to execute]")


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv
    main(dry_run=dry_run)
