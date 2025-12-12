"""
NFT Storage Adoption Breakdown
Pie chart showing storage method distribution
"""

import matplotlib.pyplot as plt
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Storage Adoption',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS/charts/05_storage_adoption'
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

# Storage method breakdown (estimated 2024)
labels = ['IPFS', 'Centralized\n(HTTP)', 'Arweave', 'Fully\nOn-Chain']
sizes = [65, 22, 8, 5]
colors = [MLBLUE, MLRED, MLORANGE, MLGREEN]
explode = (0.05, 0, 0, 0)  # Slightly separate IPFS

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 11, 'fontweight': 'bold'},
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

# Make percentage text white
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)

# Add legend with notes
legend_labels = [
    'IPFS (65%) - Most popular, requires pinning',
    'Centralized (22%) - HTTP URLs, risky',
    'Arweave (8%) - Permanent, growing',
    'On-Chain (5%) - Maximum permanence'
]

ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=9, frameon=True, facecolor='white', edgecolor='#888')

ax.set_title('NFT Metadata Storage Adoption (2024 Estimate)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
