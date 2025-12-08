"""
Fix common LaTeX/Beamer compilation errors
- Add [fragile] option to frames containing verbatim/listings
- Fix other common issues
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto")

def find_all_tex_files():
    """Find all .tex files in module directories"""
    tex_files = []
    for module_dir in BASE_DIR.glob("Module_*"):
        for tex_file in module_dir.rglob("*.tex"):
            if "temp" not in str(tex_file) and "previous" not in str(tex_file):
                tex_files.append(tex_file)
    return sorted(tex_files)

def fix_fragile_frames(content):
    """Add [fragile] to frames containing verbatim or lstlisting"""

    # Pattern to find frames that contain verbatim but don't have [fragile]
    # This regex finds \begin{frame} or \begin{frame}{Title} without [fragile]
    # and checks if the frame contains verbatim

    lines = content.split('\n')
    result = []
    in_frame = False
    frame_start_idx = -1
    frame_has_verbatim = False
    frame_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for frame start
        if '\\begin{frame}' in line:
            in_frame = True
            frame_start_idx = len(result)
            frame_has_verbatim = False
            frame_lines = [line]
            i += 1
            continue

        if in_frame:
            frame_lines.append(line)

            # Check for verbatim or lstlisting
            if '\\begin{verbatim}' in line or '\\begin{lstlisting}' in line:
                frame_has_verbatim = True

            # Check for frame end
            if '\\end{frame}' in line:
                # If frame has verbatim but no [fragile], add it
                if frame_has_verbatim:
                    first_line = frame_lines[0]
                    if '[fragile]' not in first_line:
                        # Add [fragile] after \begin{frame}
                        if '\\begin{frame}{' in first_line:
                            # \begin{frame}{Title} -> \begin{frame}[fragile]{Title}
                            first_line = first_line.replace('\\begin{frame}{', '\\begin{frame}[fragile]{')
                        elif '\\begin{frame}[' in first_line:
                            # Already has options, add fragile
                            first_line = first_line.replace('\\begin{frame}[', '\\begin{frame}[fragile,')
                        else:
                            # \begin{frame} -> \begin{frame}[fragile]
                            first_line = first_line.replace('\\begin{frame}', '\\begin{frame}[fragile]')
                        frame_lines[0] = first_line

                result.extend(frame_lines)
                in_frame = False
                frame_lines = []
                i += 1
                continue
        else:
            result.append(line)

        i += 1

    return '\n'.join(result)

def fix_special_characters(content):
    """Fix special characters that cause issues"""
    # Fix common issues
    # Replace problematic characters
    fixes = [
        ('→', '->'),  # Arrow
        ('←', '<-'),
        ('≤', r'$\leq$'),
        ('≥', r'$\geq$'),
        ('×', r'$\times$'),
        ('÷', r'$\div$'),
        ('∞', r'$\infty$'),
        ('≈', r'$\approx$'),
        ('±', r'$\pm$'),
        ('α', r'$\alpha$'),
        ('β', r'$\beta$'),
        ('γ', r'$\gamma$'),
        ('δ', r'$\delta$'),
        ('∆', r'$\Delta$'),
        ('π', r'$\pi$'),
        ('σ', r'$\sigma$'),
        ('μ', r'$\mu$'),
        ('€', 'EUR'),
        ('£', 'GBP'),
        ('¥', 'JPY'),
    ]

    for old, new in fixes:
        content = content.replace(old, new)

    return content

def fix_percent_in_text(content):
    """Escape % signs that aren't comments"""
    # This is tricky - we need to escape % in text but not in comments
    # For now, skip this as it's complex
    return content

def process_file(tex_path):
    """Process a single .tex file"""
    print(f"Processing: {tex_path.name}")

    try:
        with open(tex_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(tex_path, 'r', encoding='latin-1') as f:
            content = f.read()

    original_content = content

    # Apply fixes
    content = fix_fragile_frames(content)
    content = fix_special_characters(content)

    # Only write if changed
    if content != original_content:
        # Backup original
        backup_dir = tex_path.parent / "previous"
        backup_dir.mkdir(exist_ok=True)
        backup_path = backup_dir / tex_path.name
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Write fixed version
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [FIXED] Changes made")
        return True
    else:
        print(f"  [OK] No changes needed")
        return False

def main():
    print("=" * 60)
    print("LaTeX Error Fix Script")
    print("=" * 60)

    tex_files = find_all_tex_files()
    print(f"\nFound {len(tex_files)} .tex files")

    fixed_count = 0
    for tex_file in tex_files:
        if process_file(tex_file):
            fixed_count += 1

    print("\n" + "=" * 60)
    print(f"Fixed {fixed_count} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
