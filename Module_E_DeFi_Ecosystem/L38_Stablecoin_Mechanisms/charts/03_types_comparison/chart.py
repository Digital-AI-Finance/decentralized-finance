"""
Stablecoin Types Comparison
Horizontal bar showing key features of each type
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Types Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms/charts/03_types_comparison'
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

# Types and their characteristics
types = ['Fiat-backed\n(USDC, USDT)', 'Crypto-backed\n(DAI)', 'Algorithmic\n(UST - failed)']
characteristics = {
    'Collateral Ratio': [100, 150, 0],  # %
    'Censorship Resistance': [20, 70, 90],  # score
    'Peg Reliability': [95, 85, 30],  # score
}

x = np.arange(len(types))
width = 0.25
multiplier = 0

colors = [MLBLUE, MLORANGE, MLGREEN]

for i, (attr, values) in enumerate(characteristics.items()):
    offset = width * i
    bars = ax.bar(x + offset, values, width, label=attr, color=colors[i], edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Score / Percentage', fontsize=12)
ax.set_xticks(x + width)
ax.set_xticklabels(types, fontsize=10)
ax.set_ylim(0, 170)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Stablecoin Types: Key Characteristics', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
