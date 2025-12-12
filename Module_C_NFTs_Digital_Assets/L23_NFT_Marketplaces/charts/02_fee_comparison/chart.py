"""
NFT Marketplace Fee Comparison
Grouped bar chart showing platform fees and royalty enforcement
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Marketplace Fee Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces/charts/02_fee_comparison'
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

# Marketplaces and their fees
marketplaces = ['Blur', 'OpenSea\n(2024)', 'Magic\nEden', 'LooksRare', 'X2Y2', 'Rarible']
platform_fees = [0, 0.5, 0, 2.0, 0.5, 1.5]  # Platform fees (%)
default_royalties = [0.5, 0, 0, 0, 0, 2.5]  # Default royalty enforcement (%)

x = np.arange(len(marketplaces))
width = 0.35

bars1 = ax.bar(x - width/2, platform_fees, width, label='Platform Fee (%)',
               color=MLBLUE, edgecolor='black', linewidth=0.5, alpha=0.85)
bars2 = ax.bar(x + width/2, default_royalties, width, label='Default Royalty (%)',
               color=MLORANGE, edgecolor='black', linewidth=0.5, alpha=0.85)

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Fee Percentage (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(marketplaces, fontsize=10, fontweight='bold')
ax.set_ylim(0, 4)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Note about optional royalties
ax.text(0.5, -0.12, 'Note: Creator royalties are optional on most platforms (buyer decides)',
        transform=ax.transAxes, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('NFT Marketplace Fee Structures (2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
