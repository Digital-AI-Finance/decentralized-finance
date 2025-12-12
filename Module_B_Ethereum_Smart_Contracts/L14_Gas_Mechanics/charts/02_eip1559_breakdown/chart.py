"""
EIP-1559 Fee Breakdown
Shows base fee (burned) vs priority fee (to validator)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'EIP-1559 Breakdown',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/02_eip1559_breakdown'
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

# Total fee bar
total_width = 0.80
bar_height = 0.20
y_pos = 0.55

# Base fee portion (94% = 30/32)
base_fee_width = total_width * 0.94
base_fee = FancyBboxPatch((0.10, y_pos), base_fee_width, bar_height,
                           boxstyle="square", facecolor=MLRED,
                           edgecolor='black', linewidth=1)
ax.add_patch(base_fee)
ax.text(0.10 + base_fee_width/2, y_pos + bar_height/2, 'BASE FEE: 30 Gwei',
        ha='center', va='center', fontsize=15, fontweight='bold', color='white')

# Priority fee portion (6% = 2/32)
priority_width = total_width * 0.06
priority_fee = FancyBboxPatch((0.10 + base_fee_width, y_pos), priority_width, bar_height,
                               boxstyle="square", facecolor=MLGREEN,
                               edgecolor='black', linewidth=1)
ax.add_patch(priority_fee)

# Priority label (outside bar because too small)
ax.text(0.10 + base_fee_width + priority_width + 0.02, y_pos + bar_height/2,
        'Tip: 2', ha='left', va='center', fontsize=14, fontweight='bold', color=MLGREEN)

# Arrow showing flow for Base Fee
ax.annotate('', xy=(0.10 + base_fee_width/2, y_pos - 0.05),
            xytext=(0.10 + base_fee_width/2, y_pos - 0.20),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax.text(0.10 + base_fee_width/2, y_pos - 0.28, 'BURNED', ha='center',
        fontsize=15, fontweight='bold', color=MLRED)
ax.text(0.10 + base_fee_width/2, y_pos - 0.35, '(Removed from supply)',
        ha='center', fontsize=14, color='#555')

# Arrow showing flow for Priority Fee
ax.annotate('', xy=(0.10 + base_fee_width + priority_width/2, y_pos - 0.05),
            xytext=(0.75, y_pos - 0.20),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(0.75, y_pos - 0.28, 'TO VALIDATOR', ha='center',
        fontsize=15, fontweight='bold', color=MLGREEN)
ax.text(0.75, y_pos - 0.35, '(Incentive for inclusion)',
        ha='center', fontsize=14, color='#555')

# Title and labels
ax.text(0.50, 0.88, 'EIP-1559: Transaction Fee Structure', ha='center',
        fontsize=14, fontweight='bold')
ax.text(0.50, 0.80, 'Effective Gas Price = Base Fee + Priority Fee = 32 Gwei',
        ha='center', fontsize=15, family='monospace')

# Max fee explanation
props = dict(boxstyle='round,pad=0.3', facecolor='#E8E8E8', edgecolor='#888')
ax.text(0.50, 0.08, 'Max Fee (user sets cap) >= Base Fee + Priority Fee\nUnused Max Fee is refunded',
        ha='center', fontsize=14, bbox=props)

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('EIP-1559 Fee Breakdown (August 2021)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
