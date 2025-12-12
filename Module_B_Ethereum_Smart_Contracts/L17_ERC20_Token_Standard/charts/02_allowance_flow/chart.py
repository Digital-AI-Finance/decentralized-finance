"""
ERC-20 Allowance Flow
Shows the approve/transferFrom mechanism
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Allowance Flow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard/charts/02_allowance_flow'
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

# Draw entities
entities = [
    {'name': 'User\n(Alice)', 'x': 0.10, 'y': 0.7, 'color': MLBLUE},
    {'name': 'ERC-20\nToken', 'x': 0.45, 'y': 0.7, 'color': MLPURPLE},
    {'name': 'DEX\nContract', 'x': 0.80, 'y': 0.7, 'color': MLGREEN},
]

box_w = 0.12
box_h = 0.18

for ent in entities:
    box = FancyBboxPatch((ent['x'], ent['y'] - box_h/2), box_w, box_h,
                          boxstyle="round,pad=0.02", facecolor=ent['color'],
                          edgecolor='black', linewidth=2, alpha=0.85)
    ax.add_patch(box)
    ax.text(ent['x'] + box_w/2, ent['y'], ent['name'],
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Step 1: approve
ax.annotate('', xy=(0.45, 0.72), xytext=(0.22, 0.72),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2.5))
ax.text(0.33, 0.80, 'Step 1: approve(DEX, 100)', fontsize=10, ha='center',
        fontweight='bold', color=MLORANGE, family='monospace')

# Step 2: transferFrom (DEX calls token)
ax.annotate('', xy=(0.57, 0.68), xytext=(0.80, 0.68),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2.5))
ax.text(0.68, 0.58, 'Step 2: transferFrom(Alice, Pool, 100)', fontsize=9, ha='center',
        fontweight='bold', color=MLGREEN, family='monospace')

# Show allowance storage
ax.text(0.45 + box_w/2, 0.45, 'allowance[Alice][DEX] = 100',
        ha='center', fontsize=9, family='monospace',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

# After step 2: tokens flow
ax.annotate('', xy=(0.80, 0.35), xytext=(0.22, 0.35),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2, linestyle='--'))
ax.text(0.51, 0.28, 'Tokens move: Alice -> Pool', fontsize=10, ha='center',
        fontweight='bold', color=MLRED)

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.50, 0.08, 'Allowance enables DEX to move user tokens without private key',
        ha='center', fontsize=10, fontweight='bold', bbox=props, color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('ERC-20 Allowance Mechanism', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
