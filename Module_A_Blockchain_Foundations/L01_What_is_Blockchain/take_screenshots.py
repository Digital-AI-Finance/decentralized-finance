"""
Take screenshots of all PDF pages for review
"""
import fitz  # PyMuPDF
from pathlib import Path

pdf_path = Path(__file__).parent / "20251211_2200_L01_What_is_Blockchain.pdf"
output_dir = Path(__file__).parent / "screenshots"
output_dir.mkdir(exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

print(f"PDF has {len(doc)} pages")

# Convert each page to PNG
for page_num in range(len(doc)):
    page = doc[page_num]
    # High resolution for readability review
    mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
    pix = page.get_pixmap(matrix=mat)

    output_path = output_dir / f"slide_{page_num + 1:02d}.png"
    pix.save(output_path)
    print(f"Saved: {output_path.name}")

doc.close()
print(f"\nAll {len(doc)} screenshots saved to: {output_dir}")
