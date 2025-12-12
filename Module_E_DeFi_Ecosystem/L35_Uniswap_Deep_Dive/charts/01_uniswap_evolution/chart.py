"""
Uniswap Version Evolution Timeline
Showing key features of each version
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Uniswap Evolution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive/charts/01_uniswap_evolution'
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

# Timeline data
versions = ['V1\n(Nov 2018)', 'V2\n(May 2020)', 'V3\n(May 2021)', 'V4\n(Jun 2024)']
x_positions = [0, 1.5, 3, 4.5]
colors = ['#E8F5E9', '#C8E6C9', '#A5D6A7', '#81C784']

# Draw timeline
ax.axhline(y=2, color='gray', linewidth=3, alpha=0.5)

for i, (x, version, color) in enumerate(zip(x_positions, versions, colors)):
    # Version box
    ax.scatter(x, 2, s=1000, color=color, zorder=5, edgecolor='black', linewidth=2)
    ax.annotate(version, xy=(x, 2), ha='center', va='center', fontsize=14, fontweight='bold')

# Key features for each version
features = [
    ['ETH/ERC-20 pairs', 'x*y=k formula', '0.3% fee'],
    ['ERC-20/ERC-20 pairs', 'TWAP oracles', 'Flash swaps'],
    ['Concentrated liquidity', 'Multiple fee tiers', 'NFT positions'],
    ['Hooks (customizable)', 'Singleton contracts', 'Gas savings']
]

for i, (x, feat_list) in enumerate(zip(x_positions, features)):
    for j, feat in enumerate(feat_list):
        ax.annotate(feat, xy=(x, 0.8 - j*0.4), ha='center', fontsize=14,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=colors[i]))

ax.set_xlim(-0.8, 5.3)
ax.set_ylim(-0.5, 3.5)
ax.axis('off')

ax.set_title('Uniswap Version Evolution', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
