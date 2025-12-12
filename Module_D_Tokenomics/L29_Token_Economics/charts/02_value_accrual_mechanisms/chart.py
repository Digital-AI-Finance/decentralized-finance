"""
Value Accrual Mechanisms
Horizontal bar showing different ways protocols capture value for token holders
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Value Accrual Mechanisms',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/02_value_accrual_mechanisms'
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

# Mechanisms and their effectiveness metrics
mechanisms = [
    'Fee Distribution\n(GMX: 30% to holders)',
    'Staking Rewards\n(ETH: 3-5% APR)',
    'Token Burns\n(BNB: quarterly)',
    'Protocol Buybacks\n(MKR buyback)',
    'Governance Value\n(UNI: treasury control)'
]

# Effectiveness scores
direct_value = [9, 7, 6, 8, 4]  # Direct value to holders
sustainability = [8, 9, 7, 6, 8]  # Long-term sustainability

y_pos = np.arange(len(mechanisms))
height = 0.35

bars1 = ax.barh(y_pos - height/2, direct_value, height, label='Direct Value to Holders',
                color=MLGREEN, edgecolor='black', linewidth=0.5)
bars2 = ax.barh(y_pos + height/2, sustainability, height, label='Long-term Sustainability',
                color=MLBLUE, edgecolor='black', linewidth=0.5)

# Add value labels
for bar, val in zip(bars1, direct_value):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{val}', va='center', ha='left', fontsize=14, fontweight='bold')
for bar, val in zip(bars2, sustainability):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{val}', va='center', ha='left', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(mechanisms, fontsize=14)
ax.set_xlabel('Effectiveness Score (1-10)', fontsize=15)
ax.set_xlim(0, 11)

ax.legend(loc='lower right', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')

ax.set_title('Value Accrual Mechanisms Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
