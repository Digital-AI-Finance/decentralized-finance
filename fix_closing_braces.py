"""
Fix LaTeX closing brace errors - replace > with } in \end{...> constructs
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

def fix_closing_braces(content):
    """Fix \end{...> to \end{...}"""
    # Fix common LaTeX environment closing braces
    # Pattern: \end{anyenvname> -> \end{anyenvname}
    content = re.sub(r'\\end\{([^}]+)>', r'\\end{\1}', content)

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
    content = fix_closing_braces(content)

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
    print("Fix LaTeX Closing Braces")
    print("=" * 60)

    tex_files = find_all_tex_files()
    fixed_count = 0
    for tex_file in tex_files:
        if process_file(tex_file):
            fixed_count += 1

    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()
