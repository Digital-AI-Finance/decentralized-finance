"""
NFT Storage Tradeoffs
Comparing on-chain, IPFS, and centralized storage
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Storage Tradeoffs',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/06_storage_tradeoffs'
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

# Storage options
options = ['Fully\nOn-Chain', 'IPFS\n(Decentralized)', 'Arweave\n(Permanent)', 'Centralized\nServer']

# Metrics (scale 1-10)
metrics = {
    'Permanence': [10, 7, 9, 3],
    'Cost': [1, 7, 6, 9],  # Higher = cheaper
    'Decentralization': [10, 8, 8, 1],
    'Media Flexibility': [2, 9, 9, 10],
}

x = np.arange(len(options))
width = 0.2
colors = [MLGREEN, MLBLUE, MLORANGE, MLRED]

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=metric,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(options, fontsize=14, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Examples
examples = ['Autoglyphs\nChain Runners', 'BAYC\nMost NFTs', 'Atomic NFTs\nPermaweb', 'Early projects\n(Risky!)']
for i, ex in enumerate(examples):
    ax.text(i, -2.0, f'{ex}', ha='center', fontsize=14, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('NFT Storage Options: Tradeoff Analysis', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
