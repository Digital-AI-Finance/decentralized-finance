"""
Generate ZIP file containing all lecture PDFs
Run this script to create all_lectures.zip for download
"""

import zipfile
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
OUTPUT_FILE = BASE_DIR / "all_lectures.zip"

def find_lecture_pdfs():
    """Find all lecture PDFs in Module directories"""
    pdfs = []
    for module_dir in sorted(BASE_DIR.glob("Module_*")):
        for pdf in module_dir.rglob("*.pdf"):
            # Skip PDFs in previous/ or temp/ folders
            if "previous" not in str(pdf) and "temp" not in str(pdf):
                # Only include lesson PDFs (starting with date pattern)
                if pdf.name[0:8].isdigit():
                    pdfs.append(pdf)
    return sorted(pdfs)

def create_zip():
    """Create ZIP file with all lecture PDFs"""
    pdfs = find_lecture_pdfs()

    print("=" * 60)
    print("Generating all_lectures.zip")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"\nFound {len(pdfs)} lecture PDFs\n")

    with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zf:
        for pdf in pdfs:
            # Create archive name: Module_X/Lxx_Name.pdf
            module_name = pdf.parent.name
            if module_name == "presentations":
                module_name = pdf.parent.parent.name

            # Get module letter
            for part in pdf.parts:
                if part.startswith("Module_"):
                    module_folder = part
                    break

            # Simplified name in ZIP
            archive_name = f"{module_folder}/{module_name}/{pdf.name}"

            zf.write(pdf, archive_name)
            print(f"  Added: {pdf.name}")

    # Get file size
    size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)

    print(f"\n" + "=" * 60)
    print(f"ZIP created: {OUTPUT_FILE}")
    print(f"Total size: {size_mb:.1f} MB")
    print(f"Contains: {len(pdfs)} PDFs")
    print("=" * 60)

    return len(pdfs), size_mb

if __name__ == "__main__":
    create_zip()
