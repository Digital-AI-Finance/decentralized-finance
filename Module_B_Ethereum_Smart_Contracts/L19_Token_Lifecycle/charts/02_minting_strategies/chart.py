"""
Minting Strategies Comparison
Comparing different minting approaches
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Minting Strategies Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle/charts/02_minting_strategies'
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

# Minting strategies
strategies = ['Owner\nControlled', 'Public\nMint', 'Allowlist\n(Mapping)', 'Merkle\nTree']

# Characteristics (scale 1-10)
characteristics = {
    'Decentralization': [2, 9, 5, 5],
    'Gas Efficiency': [8, 7, 4, 9],
    'Sybil Resistance': [9, 2, 8, 8],
    'Flexibility': [9, 6, 6, 7],
}

x = np.arange(len(strategies))
width = 0.2
colors = [MLBLUE, MLGREEN, MLORANGE, MLPURPLE]

for i, (char, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=char,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(strategies, fontsize=10, fontweight='bold')
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add use cases
use_cases = ['Airdrops\nTeam allocation', 'Fair launch\nICO', 'Early access\nVIP sales', 'Large-scale\nWhitelist']
for i, use in enumerate(use_cases):
    ax.text(i, -1.8, use, ha='center', fontsize=8, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Minting Strategies Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
