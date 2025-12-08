"""
GitHub Pages Review and Enhancement Tool
Checks links, generates improved index.html with thumbnails/previews
"""

import requests
from pathlib import Path
import json
import subprocess
from datetime import datetime

BASE_URL = "https://digital-ai-finance.github.io/decentralized-finance"
LOCAL_DIR = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto")

# Course structure
MODULES = {
    "A": {"name": "Blockchain Foundations", "color": "#3b82f6", "lessons": list(range(1, 13))},
    "B": {"name": "Ethereum & Smart Contracts", "color": "#8b5cf6", "lessons": list(range(13, 21))},
    "C": {"name": "NFTs & Digital Assets", "color": "#ec4899", "lessons": list(range(21, 29))},
    "D": {"name": "Tokenomics", "color": "#f59e0b", "lessons": list(range(29, 33))},
    "E": {"name": "DeFi Ecosystem", "color": "#10b981", "lessons": list(range(33, 41))},
    "F": {"name": "Advanced Topics", "color": "#ef4444", "lessons": list(range(41, 45))},
    "G": {"name": "Regulation & Future", "color": "#6366f1", "lessons": list(range(45, 49))},
}

CHARTS = [
    {"name": "Hash Avalanche Effect", "path": "charts/hash_avalanche/chart.pdf", "desc": "Demonstrates how small input changes cause large output changes"},
    {"name": "Bitcoin Halving Schedule", "path": "charts/bitcoin_halving/chart.pdf", "desc": "Block reward reduction timeline and supply curve"},
    {"name": "Gas Costs Comparison", "path": "charts/gas_costs_comparison/chart.pdf", "desc": "EVM operation costs across different transaction types"},
    {"name": "AMM Constant Product", "path": "charts/amm_constant_product/chart.pdf", "desc": "x*y=k curve visualization for liquidity pools"},
    {"name": "Impermanent Loss", "path": "charts/impermanent_loss/chart.pdf", "desc": "IL calculation across price divergence scenarios"},
    {"name": "DeFi TVL Growth", "path": "charts/tvl_growth/chart.pdf", "desc": "Total Value Locked historical trends"},
    {"name": "Stablecoin Market Share", "path": "charts/stablecoin_market_share/chart.pdf", "desc": "Distribution of major stablecoins"},
    {"name": "Layer 2 Comparison", "path": "charts/layer2_comparison/chart.pdf", "desc": "Rollup and scaling solution comparison"},
]

LESSON_TITLES = {
    1: "What is Blockchain?", 2: "DLT Concepts", 3: "Hash Functions", 4: "Lab: Hash Experiments",
    5: "Public Key Cryptography", 6: "Bitcoin Protocol", 7: "Proof of Work", 8: "Lab: Wallet Setup",
    9: "Proof of Stake", 10: "Consensus Comparison", 11: "Scalability Trilemma", 12: "Lab: Block Explorer",
    13: "Ethereum Architecture", 14: "Gas Mechanics", 15: "Solidity Fundamentals", 16: "Lab: Contract Interaction",
    17: "ERC-20 Token Standard", 18: "ERC-721 & ERC-1155", 19: "Token Lifecycle", 20: "Lab: Token Analysis",
    21: "NFT Technology Deep Dive", 22: "NFT Metadata & IPFS", 23: "NFT Marketplaces", 24: "Lab: OpenSea Analysis",
    25: "Digital Art & Collectibles", 26: "Gaming NFTs & Metaverse", 27: "RWA Tokenization", 28: "Lab: NFT Evaluation",
    29: "Token Economics", 30: "Distribution & Vesting", 31: "Token Classification", 32: "Lab: Tokenomics Analysis",
    33: "Introduction to DeFi", 34: "AMM Mechanics", 35: "Uniswap Deep Dive", 36: "Lab: Testnet Swap",
    37: "Lending Protocols", 38: "Stablecoin Mechanisms", 39: "Terra/Luna Case Study", 40: "Lab: Testnet Lending",
    41: "Layer 2 Scaling", 42: "Flash Loans", 43: "Smart Contract Security", 44: "Lab: Security Audit",
    45: "Global Regulation", 46: "Swiss FINMA & EU MiCA", 47: "CBDCs & Future", 48: "Course Synthesis",
}

def find_pdf_for_lesson(lesson_num):
    """Find the PDF path for a given lesson number"""
    patterns = [
        f"**/L{lesson_num:02d}_*/**/*.pdf",
        f"**/L{lesson_num:02d}_*/*.pdf",
    ]
    for pattern in patterns:
        pdfs = list(LOCAL_DIR.glob(pattern))
        for pdf in pdfs:
            if "presentations" in str(pdf) or "L" in pdf.name:
                rel = str(pdf.relative_to(LOCAL_DIR)).replace("\\", "/")
                return rel
    return None

def generate_enhanced_html():
    """Generate improved index.html"""

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain, Crypto Economy & NFTs - Course Materials</title>
    <style>
        :root {
            --primary: #1e293b;
            --accent: #3b82f6;
            --success: #10b981;
            --warning: #f59e0b;
            --bg: #f8fafc;
            --card: #ffffff;
            --text: #334155;
            --text-light: #64748b;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }
        .header {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            color: white;
            padding: 60px 20px;
            text-align: center;
        }
        .header h1 { font-size: 2.5rem; margin-bottom: 10px; font-weight: 700; }
        .header p { opacity: 0.9; font-size: 1.1rem; max-width: 600px; margin: 0 auto; }
        .container { max-width: 1400px; margin: 0 auto; padding: 40px 20px; }

        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: -30px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }
        .stat-card {
            background: var(--card);
            padding: 20px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stat-card .num { font-size: 2rem; font-weight: 700; color: var(--accent); }
        .stat-card .label { font-size: 0.85rem; color: var(--text-light); text-transform: uppercase; letter-spacing: 0.5px; }

        h2 {
            font-size: 1.5rem;
            margin: 40px 0 20px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        h2 .badge {
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 20px;
            color: white;
            font-weight: 500;
        }

        .charts-section {
            background: var(--card);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 40px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }
        .chart-card {
            background: var(--bg);
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
            border: 1px solid #e2e8f0;
        }
        .chart-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .chart-card h4 { color: var(--primary); margin-bottom: 8px; font-size: 1rem; }
        .chart-card p { font-size: 0.85rem; color: var(--text-light); margin-bottom: 12px; }
        .chart-card a {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
        }
        .chart-card a:hover { text-decoration: underline; }

        .module {
            background: var(--card);
            border-radius: 16px;
            margin-bottom: 24px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .module-header {
            padding: 20px 24px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .module-header h3 { font-size: 1.1rem; font-weight: 600; }
        .module-header .count {
            background: rgba(255,255,255,0.2);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
        }
        .lessons-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1px;
            background: #e2e8f0;
        }
        .lesson {
            background: var(--card);
            padding: 16px 20px;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: background 0.2s;
        }
        .lesson:hover { background: var(--bg); }
        .lesson-num {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.85rem;
            color: white;
            flex-shrink: 0;
        }
        .lesson-info { flex: 1; min-width: 0; }
        .lesson-title {
            font-size: 0.95rem;
            color: var(--primary);
            font-weight: 500;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .lesson-type {
            font-size: 0.75rem;
            color: var(--text-light);
        }
        .lesson a {
            color: var(--accent);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            white-space: nowrap;
        }
        .lesson a:hover { text-decoration: underline; }
        .lab-badge {
            background: #dcfce7;
            color: #166534;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .resources {
            background: var(--card);
            border-radius: 16px;
            padding: 30px;
            margin-top: 40px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .resources h3 { margin-bottom: 20px; color: var(--primary); }
        .resources-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 16px;
        }
        .resource-link {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 16px;
            background: var(--bg);
            border-radius: 8px;
            color: var(--text);
            text-decoration: none;
            font-size: 0.9rem;
            transition: background 0.2s;
        }
        .resource-link:hover { background: #e2e8f0; }

        footer {
            text-align: center;
            padding: 40px 20px;
            color: var(--text-light);
            font-size: 0.85rem;
        }
        footer a { color: var(--accent); text-decoration: none; }
        footer a:hover { text-decoration: underline; }

        @media (max-width: 768px) {
            .header h1 { font-size: 1.8rem; }
            .stats-bar { gap: 16px; }
            .stat-card { padding: 16px 24px; }
            .lessons-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Blockchain, Crypto Economy & NFTs</h1>
        <p>Comprehensive BSc-level course covering blockchain fundamentals, smart contracts, DeFi, NFTs, and regulatory frameworks</p>
    </div>

    <div class="container">
        <div class="stats-bar">
            <div class="stat-card"><div class="num">48</div><div class="label">Lessons</div></div>
            <div class="stat-card"><div class="num">7</div><div class="label">Modules</div></div>
            <div class="stat-card"><div class="num">11</div><div class="label">Labs</div></div>
            <div class="stat-card"><div class="num">8</div><div class="label">Charts</div></div>
        </div>

        <div class="charts-section">
            <h2>Course Visualizations</h2>
            <div class="charts-grid">
'''

    # Add charts
    for chart in CHARTS:
        html += f'''                <div class="chart-card">
                    <h4>{chart["name"]}</h4>
                    <p>{chart["desc"]}</p>
                    <a href="{chart["path"]}" target="_blank">View PDF</a>
                </div>
'''

    html += '''            </div>
        </div>
'''

    # Add modules
    for mod_key, mod in MODULES.items():
        lesson_count = len(mod["lessons"])
        html += f'''
        <div class="module">
            <div class="module-header" style="background: {mod["color"]}">
                <h3>Module {mod_key}: {mod["name"]}</h3>
                <span class="count">{lesson_count} lessons</span>
            </div>
            <div class="lessons-grid">
'''
        for lesson_num in mod["lessons"]:
            title = LESSON_TITLES.get(lesson_num, f"Lesson {lesson_num}")
            is_lab = "Lab" in title
            pdf_path = find_pdf_for_lesson(lesson_num)

            html += f'''                <div class="lesson">
                    <div class="lesson-num" style="background: {mod["color"]}">{lesson_num:02d}</div>
                    <div class="lesson-info">
                        <div class="lesson-title">{title}</div>
                        <div class="lesson-type">{"<span class='lab-badge'>Lab</span>" if is_lab else "Lecture"}</div>
                    </div>
'''
            if pdf_path:
                html += f'''                    <a href="{pdf_path}" target="_blank">Open PDF</a>
'''
            html += '''                </div>
'''

        html += '''            </div>
        </div>
'''

    # Add resources section
    html += '''
        <div class="resources">
            <h3>Additional Resources</h3>
            <div class="resources-grid">
                <a href="SYLLABUS.md" class="resource-link">Course Syllabus</a>
                <a href="README.md" class="resource-link">README</a>
                <a href="assessments/README.md" class="resource-link">Assessments</a>
                <a href="assessments/quizzes/QUIZ_1_Blockchain_Foundations.md" class="resource-link">Quiz 1</a>
                <a href="assessments/quizzes/QUIZ_2_Ethereum_Basics.md" class="resource-link">Quiz 2</a>
                <a href="assessments/quizzes/QUIZ_3_Tokens_NFTs.md" class="resource-link">Quiz 3</a>
                <a href="assessments/rubrics/RUBRICS.md" class="resource-link">Grading Rubrics</a>
                <a href="https://github.com/Digital-AI-Finance/decentralized-finance" class="resource-link">GitHub Repository</a>
            </div>
        </div>
    </div>

    <footer>
        <p>Digital AI Finance | <a href="https://github.com/Digital-AI-Finance">GitHub</a></p>
        <p style="margin-top: 8px; font-size: 0.8rem;">Course materials for educational purposes</p>
    </footer>
</body>
</html>
'''

    return html

def check_all_links(html_content):
    """Check all links in the HTML"""
    import re
    links = re.findall(r'href="([^"]+)"', html_content)

    results = {"ok": [], "fail": [], "external": []}

    for link in links:
        if link.startswith("http"):
            results["external"].append(link)
            continue

        full_url = f"{BASE_URL}/{link}"
        try:
            resp = requests.head(full_url, timeout=5)
            if resp.status_code == 200:
                results["ok"].append(link)
            else:
                results["fail"].append((link, resp.status_code))
        except Exception as e:
            results["fail"].append((link, str(e)))

    return results

def main():
    print("=" * 60)
    print("GitHub Pages Review & Enhancement")
    print("=" * 60)

    # Generate enhanced HTML
    print("\n[1] Generating enhanced index.html...")
    html = generate_enhanced_html()

    output_path = LOCAL_DIR / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"    Saved to: {output_path}")

    # Check links
    print("\n[2] Checking internal links...")
    results = check_all_links(html)
    print(f"    OK: {len(results['ok'])}")
    print(f"    Failed: {len(results['fail'])}")
    print(f"    External: {len(results['external'])}")

    if results["fail"]:
        print("\n    Failed links:")
        for link, err in results["fail"]:
            print(f"      - {link}: {err}")

    print("\n" + "=" * 60)
    print("DONE - Enhanced index.html generated")
    print(f"View at: {BASE_URL}")
    print("=" * 60)

if __name__ == "__main__":
    main()
