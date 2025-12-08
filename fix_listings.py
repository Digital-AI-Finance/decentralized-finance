"""
Fix listings language issues - remove undefined language specifications
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

def fix_listings(content):
    """Remove undefined language specifications from listings"""
    # Remove language=solidity or language=Solidity
    content = re.sub(r'language\s*=\s*[Ss]olidity\s*,?\s*', '', content)
    content = re.sub(r'language\s*=\s*[Jj]avascript\s*,?\s*', '', content)
    content = re.sub(r'language\s*=\s*[Jj]son\s*,?\s*', '', content)

    # Clean up empty options like lstlisting[]
    content = re.sub(r'\\begin\{lstlisting\}\[\s*\]', r'\\begin{lstlisting}', content)

    # Also ensure frames with lstlisting have [fragile]
    lines = content.split('\n')
    result = []
    in_frame = False
    frame_start_idx = -1
    frame_has_lstlisting = False
    frame_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if '\\begin{frame}' in line:
            in_frame = True
            frame_start_idx = len(result)
            frame_has_lstlisting = False
            frame_lines = [line]
            i += 1
            continue

        if in_frame:
            frame_lines.append(line)

            if '\\begin{lstlisting}' in line:
                frame_has_lstlisting = True

            if '\\end{frame}' in line:
                if frame_has_lstlisting:
                    first_line = frame_lines[0]
                    if '[fragile]' not in first_line:
                        if '\\begin{frame}{' in first_line:
                            first_line = first_line.replace('\\begin{frame}{', '\\begin{frame}[fragile]{')
                        elif '\\begin{frame}[' in first_line:
                            if 'fragile' not in first_line:
                                first_line = first_line.replace('\\begin{frame}[', '\\begin{frame}[fragile,')
                        else:
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
    content = fix_listings(content)

    if content != original_content:
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [FIXED] Changes made")
        return True
    else:
        print(f"  [OK] No changes needed")
        return False

def main():
    print("=" * 60)
    print("Fix Listings Language Issues")
    print("=" * 60)

    tex_files = find_all_tex_files()
    fixed_count = 0
    for tex_file in tex_files:
        if process_file(tex_file):
            fixed_count += 1

    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()
