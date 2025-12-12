"""
Dencun Upgrade Impact
EIP-4844 blob transactions reduce L2 fees
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Dencun Impact',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/07_dencun_impact'
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

# L2 solutions
l2s = ['Arbitrum', 'Optimism', 'Base', 'zkSync', 'Polygon zkEVM']

# Costs before and after Dencun (in USD)
costs_before = [0.50, 0.45, 0.48, 0.40, 0.55]
costs_after = [0.02, 0.01, 0.015, 0.02, 0.025]

x = np.arange(len(l2s))
width = 0.35

bars_before = ax.bar(x - width/2, costs_before, width, label='Before Dencun',
                      color=MLRED, edgecolor='black', linewidth=0.5)
bars_after = ax.bar(x + width/2, costs_after, width, label='After Dencun (March 2024)',
                     color=MLGREEN, edgecolor='black', linewidth=0.5)

# Add value labels
for bar in bars_before:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.02,
            f'${height:.2f}', ha='center', fontsize=14)

for bar in bars_after:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.02,
            f'${height:.3f}', ha='center', fontsize=14)

# Reduction annotation
for i, (before, after) in enumerate(zip(costs_before, costs_after)):
    reduction = (1 - after/before) * 100
    ax.annotate(f'-{reduction:.0f}%', xy=(i, 0.35), fontsize=14,
                ha='center', fontweight='bold', color=MLGREEN)

ax.set_xlabel('Layer 2 Solution', fontsize=16)
ax.set_ylabel('Average Transaction Cost (USD)', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(l2s, fontsize=14)
ax.set_ylim(0, 0.7)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.5, 0.65, 'EIP-4844: Blob transactions reduce L2 data costs by 90%+',
        transform=ax.transAxes, ha='center', fontsize=14, fontweight='bold',
        bbox=props, color=MLGREEN)

ax.set_title('Dencun Upgrade: L2 Fee Reduction', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
