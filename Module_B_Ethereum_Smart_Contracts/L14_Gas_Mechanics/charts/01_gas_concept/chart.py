"""
Gas Concept Diagram
Shows what gas is and how it works
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Gas Concept',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/01_gas_concept'
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

# Gas pump icon (left)
pump = FancyBboxPatch((0.05, 0.35), 0.15, 0.40,
                       boxstyle="round,pad=0.02", facecolor=MLORANGE,
                       edgecolor='black', linewidth=2)
ax.add_patch(pump)
ax.text(0.125, 0.60, 'GAS', ha='center', fontsize=16, fontweight='bold', color='white')
ax.text(0.125, 0.45, 'Unit of\nWork', ha='center', fontsize=10, color='white')

# Transaction (center)
tx_box = FancyBboxPatch((0.30, 0.40), 0.18, 0.25,
                         boxstyle="round,pad=0.01", facecolor=MLBLUE,
                         edgecolor='black', linewidth=1.5)
ax.add_patch(tx_box)
ax.text(0.39, 0.55, 'Transaction', ha='center', fontsize=11, fontweight='bold', color='white')
ax.text(0.39, 0.47, 'Uses Gas', ha='center', fontsize=10, color='white')

# Validator (right)
validator_box = FancyBboxPatch((0.58, 0.40), 0.18, 0.25,
                                boxstyle="round,pad=0.01", facecolor=MLGREEN,
                                edgecolor='black', linewidth=1.5)
ax.add_patch(validator_box)
ax.text(0.67, 0.55, 'Validator', ha='center', fontsize=11, fontweight='bold', color='white')
ax.text(0.67, 0.47, 'Earns Fees', ha='center', fontsize=10, color='white')

# Arrows
ax.annotate('', xy=(0.28, 0.52), xytext=(0.22, 0.52),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.annotate('', xy=(0.56, 0.52), xytext=(0.50, 0.52),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Formula at top
ax.text(0.50, 0.85, 'Transaction Fee = Gas Used x Gas Price', ha='center',
        fontsize=14, fontweight='bold', family='monospace')

# Example
ax.text(0.50, 0.75, '21,000 gas x 30 Gwei = 630,000 Gwei = 0.00063 ETH',
        ha='center', fontsize=11, family='monospace', color='#555')

# Three purposes at bottom
purposes = [
    (0.17, 'Prevent DoS', 'Spam attacks\ncost money'),
    (0.50, 'Incentivize', 'Validators earn\nfor computation'),
    (0.83, 'Allocate', 'Prioritize\nhigh-fee TXs'),
]

for x, title, desc in purposes:
    props = dict(boxstyle='round,pad=0.2', facecolor='#E8E8E8', edgecolor='#888')
    ax.text(x, 0.22, title, ha='center', fontsize=11, fontweight='bold', bbox=props)
    ax.text(x, 0.08, desc, ha='center', fontsize=9, color='#555')

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('Gas: Unit of Computational Effort', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
