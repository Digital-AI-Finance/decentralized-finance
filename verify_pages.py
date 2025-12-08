"""
Verify GitHub Pages - Check all PDFs and charts are accessible
"""

import requests
from pathlib import Path
import time

BASE_URL = "https://digital-ai-finance.github.io/decentralized-finance"
LOCAL_DIR = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto")

def find_all_pdfs():
    """Find all PDFs in the local directory"""
    pdfs = []
    for pdf in LOCAL_DIR.rglob("*.pdf"):
        rel_path = pdf.relative_to(LOCAL_DIR)
        # Skip template files
        if "template" in str(rel_path).lower():
            continue
        pdfs.append(str(rel_path).replace("\\", "/"))
    return sorted(pdfs)

def check_url(url):
    """Check if URL is accessible"""
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except:
        return False

def main():
    print("=" * 60)
    print("GitHub Pages Verification")
    print(f"Base URL: {BASE_URL}")
    print("=" * 60)

    # Check index page
    print("\n[1] Checking index.html...")
    index_url = f"{BASE_URL}/index.html"
    if check_url(index_url):
        print(f"    [OK] {index_url}")
    else:
        print(f"    [FAIL] {index_url}")

    # Find all PDFs
    pdfs = find_all_pdfs()
    print(f"\n[2] Found {len(pdfs)} PDFs locally")

    # Check each PDF
    print("\n[3] Checking PDF accessibility...")
    accessible = 0
    failed = []

    for i, pdf in enumerate(pdfs):
        url = f"{BASE_URL}/{pdf}"
        if check_url(url):
            accessible += 1
            print(f"    [{accessible}/{len(pdfs)}] OK: {pdf[:60]}...")
        else:
            failed.append(pdf)
            print(f"    [FAIL] {pdf}")

        # Rate limit
        if i % 10 == 9:
            time.sleep(0.5)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total PDFs: {len(pdfs)}")
    print(f"Accessible: {accessible}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed files:")
        for f in failed:
            print(f"  - {f}")
    else:
        print("\nAll PDFs are accessible on GitHub Pages!")

    print(f"\nView course at: {BASE_URL}")

if __name__ == "__main__":
    main()
