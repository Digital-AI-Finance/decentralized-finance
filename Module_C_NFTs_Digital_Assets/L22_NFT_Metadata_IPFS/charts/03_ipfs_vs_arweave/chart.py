"""
IPFS vs Arweave Comparison
Comparing the two main decentralized storage solutions
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'IPFS vs Arweave',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS/charts/03_ipfs_vs_arweave'
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

# Comparison dimensions
categories = ['Permanence', 'Cost\n(short-term)', 'Speed', 'Adoption', 'Simplicity']
ipfs_scores = [6, 8, 9, 9, 8]  # Requires pinning
arweave_scores = [10, 5, 6, 6, 7]  # Guaranteed permanent

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, ipfs_scores, width, label='IPFS',
               color=MLBLUE, edgecolor='black', linewidth=0.5, alpha=0.85)
bars2 = ax.bar(x + width/2, arweave_scores, width, label='Arweave',
               color=MLORANGE, edgecolor='black', linewidth=0.5, alpha=0.85)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Key insight
ax.text(0.5, 0.98, 'IPFS: Free + pinning costs | Arweave: One-time permanent storage fee',
        transform=ax.transAxes, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('IPFS vs Arweave: Storage Comparison', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
