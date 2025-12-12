"""
Compile and Verify All LaTeX Lessons
Compiles all .tex files and updates index.html with status indicators.
- Green checkmark: Compilation successful
- Red X: Compilation failed
"""

import re
import subprocess
import sys
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path(__file__).parent


def get_timestamp(filename):
    """Extract timestamp from filename like 20251211_1400_L01_Name.tex"""
    match = re.match(r'^(\d{8}_\d{4})_', filename)
    return match.group(1) if match else None


def get_lesson_id(filename):
    """Extract lesson ID like L01, L02, etc."""
    match = re.search(r'_(L\d{2})_', filename)
    return match.group(1) if match else None


def find_latest_tex_files():
    """Find the latest .tex file for each lesson."""
    tex_files = {}

    for module_dir in sorted(BASE_DIR.glob("Module_*")):
        for lesson_dir in sorted(module_dir.glob("L*")):
            if not lesson_dir.is_dir():
                continue

            # Check for presentations/ subfolder (Modules D, E)
            presentations_dir = lesson_dir / "presentations"
            target_dir = presentations_dir if presentations_dir.exists() else lesson_dir

            # Group tex files by lesson
            lesson_texes = defaultdict(list)
            for tex_file in target_dir.glob("*.tex"):
                if "previous" in str(tex_file) or "temp" in str(tex_file):
                    continue
                timestamp = get_timestamp(tex_file.name)
                lesson_id = get_lesson_id(tex_file.name)
                if timestamp and lesson_id:
                    lesson_texes[lesson_id].append(tex_file)

            # Keep only the latest for each lesson
            for lesson_id, files in lesson_texes.items():
                files.sort(key=lambda x: get_timestamp(x.name), reverse=True)
                tex_files[lesson_id] = files[0]

    return tex_files


def compile_tex(tex_path):
    """Compile a .tex file and return (success, error_message)."""
    tex_dir = tex_path.parent
    tex_name = tex_path.name

    # Create temp directory for aux files
    temp_dir = tex_dir / "temp"
    temp_dir.mkdir(exist_ok=True)

    try:
        # Run pdflatex (twice for references)
        for _ in range(2):
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-output-directory", str(tex_dir), tex_name],
                cwd=tex_dir,
                capture_output=True,
                text=True,
                timeout=120
            )

        # Check if PDF was created
        pdf_name = tex_path.stem + ".pdf"
        pdf_path = tex_dir / pdf_name

        if pdf_path.exists():
            # Move aux files to temp
            for ext in ['.aux', '.log', '.out', '.nav', '.snm', '.toc', '.vrb']:
                aux_file = tex_dir / (tex_path.stem + ext)
                if aux_file.exists():
                    shutil.move(str(aux_file), str(temp_dir / aux_file.name))
            return True, None, pdf_path
        else:
            # Extract error from log
            log_file = tex_dir / (tex_path.stem + ".log")
            error_msg = "PDF not generated"
            if log_file.exists():
                log_content = log_file.read_text(encoding='latin-1')
                error_match = re.search(r'!(.*?)(?=\n\n|\nl\.)', log_content, re.DOTALL)
                if error_match:
                    error_msg = error_match.group(1).strip()[:100]
            return False, error_msg, None

    except subprocess.TimeoutExpired:
        return False, "Compilation timeout (>120s)", None
    except FileNotFoundError:
        return False, "pdflatex not found in PATH", None
    except Exception as e:
        return False, str(e)[:100], None


def update_index_html(results):
    """Update index.html with compilation status indicators."""
    index_path = BASE_DIR / "index.html"

    if not index_path.exists():
        print("ERROR: index.html not found")
        return False

    content = index_path.read_text(encoding='utf-8')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Status icons (inline SVG for better rendering)
    check_icon = f'<span class="compile-status success" title="Compiled: {timestamp}"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></span>'
    error_icon_template = '<span class="compile-status error" title="Error: {error} ({timestamp})"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="3"><path d="M18 6L6 18M6 6l12 12"/></svg></span>'

    # Add CSS if not present
    if 'compile-status' not in content:
        css_addition = '''
    <style>
    .compile-status { margin-left: 8px; display: inline-flex; align-items: center; vertical-align: middle; }
    .compile-status.success svg { stroke: #22c55e; }
    .compile-status.error svg { stroke: #ef4444; }
    .compile-status svg { width: 16px; height: 16px; }
    </style>
    </head>'''
        content = content.replace('</head>', css_addition)

    # Remove old status indicators
    content = re.sub(r'<span class="compile-status.*?</span>', '', content)

    # Update each lesson
    for lesson_id, (success, error_msg, pdf_path) in results.items():
        lesson_num = lesson_id[1:]  # Remove 'L' prefix -> "01", "02", etc.

        # Pattern to find the lesson div and its PDF link
        # Match the lesson div with this number and add status after PDF</a>
        pattern = rf'(<div class="lesson-num"[^>]*>{lesson_num}</div>.*?PDF</a>)'

        if success:
            replacement = rf'\1{check_icon}'
        else:
            error_icon = error_icon_template.format(error=error_msg or "Unknown", timestamp=timestamp)
            replacement = rf'\1{error_icon}'

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write updated content
    index_path.write_text(content, encoding='utf-8')
    return True


def main():
    print("=" * 60)
    print("Compile and Verify All LaTeX Lessons")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Find all tex files
    tex_files = find_latest_tex_files()
    print(f"\nFound {len(tex_files)} lessons to compile\n")

    results = {}
    success_count = 0
    error_count = 0

    for lesson_id in sorted(tex_files.keys()):
        tex_path = tex_files[lesson_id]
        print(f"[{lesson_id}] Compiling: {tex_path.name}...", end=" ", flush=True)

        success, error_msg, pdf_path = compile_tex(tex_path)
        results[lesson_id] = (success, error_msg, pdf_path)

        if success:
            print("OK")
            success_count += 1
        else:
            print(f"FAILED - {error_msg}")
            error_count += 1

    # Update index.html
    print("\nUpdating index.html with status indicators...")
    if update_index_html(results):
        print("index.html updated successfully")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total lessons: {len(tex_files)}")
    print(f"Successful:    {success_count}")
    print(f"Failed:        {error_count}")

    if error_count > 0:
        print("\nFailed lessons:")
        for lesson_id, (success, error_msg, _) in results.items():
            if not success:
                print(f"  - {lesson_id}: {error_msg}")

    return error_count == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
