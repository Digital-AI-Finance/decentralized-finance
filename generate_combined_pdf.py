"""
Generate combined PDF of all lectures and update ZIP when PDFs change
Monitors for changes and regenerates automatically
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime
from PyPDF2 import PdfMerger

BASE_DIR = Path(__file__).parent
COMBINED_PDF = BASE_DIR / "all_lectures_combined.pdf"
ZIP_FILE = BASE_DIR / "all_lectures.zip"
HASH_FILE = BASE_DIR / ".pdf_hashes.json"


def get_lecture_pdfs():
    """Find all lecture PDFs in Module directories, sorted by lesson number"""
    pdfs = []
    for module_dir in sorted(BASE_DIR.glob("Module_*")):
        for pdf in module_dir.rglob("*.pdf"):
            # Skip PDFs in previous/ or temp/ folders
            if "previous" not in str(pdf) and "temp" not in str(pdf):
                # Only include lesson PDFs (starting with date pattern)
                if pdf.name[0:8].isdigit() and "_L" in pdf.name:
                    pdfs.append(pdf)

    # Sort by lesson number (L01, L02, etc.)
    def get_lesson_num(p):
        name = p.name
        try:
            idx = name.index("_L") + 2
            return int(name[idx:idx+2])
        except:
            return 999

    return sorted(pdfs, key=get_lesson_num)


def compute_file_hash(filepath):
    """Compute MD5 hash of a file"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_hashes():
    """Load previous hashes from file"""
    if HASH_FILE.exists():
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    """Save hashes to file"""
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)


def check_for_changes():
    """Check if any PDFs have changed since last run"""
    pdfs = get_lecture_pdfs()
    old_hashes = load_hashes()
    new_hashes = {}
    changed = []

    for pdf in pdfs:
        key = str(pdf.relative_to(BASE_DIR))
        current_hash = compute_file_hash(pdf)
        new_hashes[key] = current_hash

        if key not in old_hashes or old_hashes[key] != current_hash:
            changed.append(pdf.name)

    # Check for removed files
    for key in old_hashes:
        if key not in new_hashes:
            changed.append(f"REMOVED: {key}")

    return changed, new_hashes


def generate_combined_pdf():
    """Generate combined PDF from all lecture PDFs"""
    pdfs = get_lecture_pdfs()

    print("=" * 60)
    print("Generating Combined Lecture PDF")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"\nFound {len(pdfs)} lecture PDFs\n")

    merger = PdfMerger()

    for pdf in pdfs:
        print(f"  Adding: {pdf.name}")
        merger.append(str(pdf))

    merger.write(str(COMBINED_PDF))
    merger.close()

    size_mb = COMBINED_PDF.stat().st_size / (1024 * 1024)

    print(f"\n" + "=" * 60)
    print(f"Combined PDF: {COMBINED_PDF}")
    print(f"Total size: {size_mb:.1f} MB")
    print(f"Contains: {len(pdfs)} lectures")
    print("=" * 60)

    return len(pdfs), size_mb


def generate_zip():
    """Generate ZIP file with all lecture PDFs"""
    import zipfile

    pdfs = get_lecture_pdfs()

    print(f"\nGenerating ZIP file...")

    with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zf:
        for pdf in pdfs:
            # Get module folder
            for part in pdf.parts:
                if part.startswith("Module_"):
                    module_folder = part
                    break

            # Get lesson folder
            lesson_folder = pdf.parent.name
            if lesson_folder == "presentations":
                lesson_folder = pdf.parent.parent.name

            archive_name = f"{module_folder}/{lesson_folder}/{pdf.name}"
            zf.write(pdf, archive_name)

    size_mb = ZIP_FILE.stat().st_size / (1024 * 1024)
    print(f"ZIP created: {ZIP_FILE} ({size_mb:.1f} MB)")

    return size_mb


def main():
    """Main function - check for changes and regenerate if needed"""
    changed, new_hashes = check_for_changes()

    if not changed and COMBINED_PDF.exists() and ZIP_FILE.exists():
        print("No changes detected. PDFs are up to date.")
        return False

    if changed:
        print(f"Detected {len(changed)} changed files:")
        for f in changed[:10]:
            print(f"  - {f}")
        if len(changed) > 10:
            print(f"  ... and {len(changed) - 10} more")
        print()
    else:
        print("Output files missing. Regenerating...\n")

    # Generate combined PDF
    generate_combined_pdf()

    # Generate ZIP
    generate_zip()

    # Save new hashes
    save_hashes(new_hashes)

    print("\nDone! Files updated.")
    return True


if __name__ == "__main__":
    main()
