"""
Batch compile all Beamer slides to PDF
Autonomous execution - no user interaction required
"""

import os
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto")
TEMP_DIR = BASE_DIR / "temp"

# Ensure temp directory exists
TEMP_DIR.mkdir(exist_ok=True)

def find_all_tex_files():
    """Find all .tex files in module directories"""
    tex_files = []
    for module_dir in BASE_DIR.glob("Module_*"):
        for tex_file in module_dir.rglob("*.tex"):
            # Skip files in temp or previous folders
            if "temp" not in str(tex_file) and "previous" not in str(tex_file):
                tex_files.append(tex_file)
    return sorted(tex_files)

def compile_tex(tex_path):
    """Compile a single .tex file to PDF"""
    tex_dir = tex_path.parent
    tex_name = tex_path.name
    pdf_name = tex_name.replace(".tex", ".pdf")

    print(f"\n[COMPILING] {tex_name}")

    try:
        # Run pdflatex twice for cross-references
        for run in range(2):
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", tex_name],
                cwd=tex_dir,
                capture_output=True,
                text=True,
                timeout=60
            )

        # Check if PDF was created
        pdf_path = tex_dir / pdf_name
        if pdf_path.exists():
            print(f"  [OK] Created: {pdf_path}")

            # Move aux files to temp
            aux_extensions = [".aux", ".log", ".nav", ".out", ".snm", ".toc", ".vrb"]
            for ext in aux_extensions:
                aux_file = tex_dir / tex_name.replace(".tex", ext)
                if aux_file.exists():
                    try:
                        shutil.move(str(aux_file), str(TEMP_DIR / aux_file.name))
                    except:
                        pass  # Ignore if file is locked

            return True, str(pdf_path)
        else:
            print(f"  [FAIL] PDF not created")
            return False, None

    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] Compilation timed out")
        return False, None
    except FileNotFoundError:
        print(f"  [ERROR] pdflatex not found - install TeX distribution")
        return False, None
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False, None

def main():
    print("=" * 60)
    print("BSc Blockchain Course - Batch PDF Compilation")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    tex_files = find_all_tex_files()
    print(f"\nFound {len(tex_files)} .tex files to compile")

    success_count = 0
    fail_count = 0
    results = []

    for tex_file in tex_files:
        success, pdf_path = compile_tex(tex_file)
        if success:
            success_count += 1
            results.append(f"[OK] {tex_file.name} -> {pdf_path}")
        else:
            fail_count += 1
            results.append(f"[FAIL] {tex_file.name}")

    # Summary
    print("\n" + "=" * 60)
    print("COMPILATION SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(tex_files)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Aux files moved to: {TEMP_DIR}")

    # Write results to file
    report_path = BASE_DIR / "compilation_report.txt"
    with open(report_path, "w") as f:
        f.write(f"Compilation Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total: {len(tex_files)} | Success: {success_count} | Failed: {fail_count}\n\n")
        f.write("\n".join(results))

    print(f"\nReport saved to: {report_path}")

    return success_count, fail_count

if __name__ == "__main__":
    main()
