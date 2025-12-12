"""
Stablecoin Trilemma
Shows trade-offs between stability, decentralization, and efficiency
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Stablecoin Trilemma',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms/charts/02_stablecoin_trilemma'
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

# Categories
categories = ['Stability', 'Decentralization', 'Capital\nEfficiency']

# Different stablecoin types (scores 1-10)
usdc = [10, 2, 10]  # Fiat-backed: stable, centralized, efficient
dai = [8, 7, 3]     # Crypto-backed: somewhat stable, decentralized, inefficient
ust = [2, 9, 10]    # Algorithmic (failed): unstable, decentralized, efficient

x = np.arange(len(categories))
width = 0.25

bars1 = ax.bar(x - width, usdc, width, label='USDC (Fiat-backed)', color=MLBLUE, edgecolor='black')
bars2 = ax.bar(x, dai, width, label='DAI (Crypto-backed)', color=MLORANGE, edgecolor='black')
bars3 = ax.bar(x + width, ust, width, label='UST (Algorithmic)', color=MLRED, edgecolor='black', alpha=0.7, hatch='//')

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.text(0.5, -0.15, 'No stablecoin achieves all three perfectly; each type makes trade-offs',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Stablecoin Trilemma: Trade-offs by Type', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
