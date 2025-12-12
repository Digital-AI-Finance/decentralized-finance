"""
Token Standards Comparison
ERC-20 vs ERC-721 vs ERC-1155
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Standards Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_Standards/charts/02_token_standards_comparison'
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

# Standards
standards = ['ERC-20', 'ERC-721', 'ERC-1155']

# Features comparison (1 = no support, 5 = full support, 10 = excellent)
features = {
    'Fungibility': [10, 1, 8],
    'Uniqueness': [1, 10, 8],
    'Batch Transfers': [3, 3, 10],
    'Gas Efficiency': [7, 5, 9],
    'Flexibility': [5, 6, 10],
}

x = np.arange(len(standards))
width = 0.15
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]

# Create grouped bar chart
for i, (feat, values) in enumerate(features.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=feat,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.8)

ax.set_ylabel('Support Level (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(standards, fontsize=12, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add use cases
use_cases = [
    'Currencies,\nDeFi tokens',
    'Art, Collectibles,\nDomain names',
    'Gaming items,\nMulti-assets'
]
for i, use in enumerate(use_cases):
    ax.text(i, -1.8, use, ha='center', fontsize=9, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Token Standards Feature Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
