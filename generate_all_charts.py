"""Generate all chart PDFs for lessons 28, 29, 31, 33, 42, 45, 46, 47"""
import subprocess
import sys
from pathlib import Path

# Base directory
base = Path(__file__).parent

# Find all chart.py files in the lessons we're working on
lessons = [
    'Module_C_NFTs_Digital_Assets/L28_Lab_NFT_Evaluation',
    'Module_D_Tokenomics/L29_Token_Economics',
    'Module_D_Tokenomics/L31_Token_Classification',
    'Module_E_DeFi_Ecosystem/L33_Intro_DeFi',
    'Module_F_Advanced_Topics/L42_Flash_Loans',
    'Module_G_Regulation_Future/L45_Global_Regulation',
    'Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA',
    'Module_G_Regulation_Future/L47_CBDCs_Future'
]

total_generated = 0
total_errors = 0

for lesson in lessons:
    lesson_path = base / lesson
    if lesson_path.exists():
        chart_files = list(lesson_path.rglob('chart.py'))
        print(f'\n{lesson}: {len(chart_files)} charts')

        for chart_file in sorted(chart_files):
            chart_dir = chart_file.parent
            try:
                result = subprocess.run(
                    [sys.executable, 'chart.py'],
                    cwd=str(chart_dir),
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    pdf_file = chart_dir / 'chart.pdf'
                    if pdf_file.exists():
                        print(f'  [OK] {chart_dir.name}')
                        total_generated += 1
                    else:
                        print(f'  [FAIL] {chart_dir.name} (no PDF created)')
                        total_errors += 1
                else:
                    print(f'  [ERROR] {chart_dir.name}: {result.stderr[:100]}')
                    total_errors += 1
            except Exception as e:
                print(f'  [ERROR] {chart_dir.name}: {str(e)[:100]}')
                total_errors += 1

print(f'\n\nSummary: {total_generated} PDFs generated, {total_errors} errors')
