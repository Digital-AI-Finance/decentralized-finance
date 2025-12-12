"""
DeFi TVL Share by Blockchain
Pie chart showing chain distribution
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Chain TVL Share',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/05_chain_tvl_share'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

# Chain TVL distribution (Dec 2024 approximate)
chains = ['Ethereum', 'Solana', 'BSC', 'Tron', 'Arbitrum', 'Base', 'Polygon', 'Other L2s', 'Other']
shares = [55, 8, 7, 6, 5, 4, 3, 5, 7]

colors = ['#627EEA', '#9945FF', '#F3BA2F', '#FF0013', '#28A0F0', '#0052FF', '#8247E5', '#888888', '#CCCCCC']

explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0)  # Highlight Ethereum

wedges, texts, autotexts = ax.pie(shares, labels=chains, colors=colors,
                                   autopct='%1.1f%%', startangle=90, explode=explode,
                                   pctdistance=0.75, labeldistance=1.1)

# Style the labels
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

# Add annotation
ax.text(0, -1.4, 'Ethereum maintains dominance; Layer 2s growing share rapidly',
        ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('DeFi TVL Distribution by Blockchain (Dec 2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
