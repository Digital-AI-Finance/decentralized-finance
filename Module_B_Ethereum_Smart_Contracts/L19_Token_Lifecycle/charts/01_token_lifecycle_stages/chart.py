"""
Token Lifecycle Stages
Flow diagram showing complete token lifecycle
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Lifecycle Stages',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle/charts/01_token_lifecycle_stages'
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

# Lifecycle stages as boxes
stages = [
    {'name': 'Deployment', 'x': 0.1, 'color': MLPURPLE, 'desc': 'Contract creation\nInitial setup'},
    {'name': 'Minting', 'x': 0.3, 'color': MLGREEN, 'desc': 'Create tokens\nIncrease supply'},
    {'name': 'Operation', 'x': 0.5, 'color': MLBLUE, 'desc': 'Transfers\nApprovals'},
    {'name': 'Burning', 'x': 0.7, 'color': MLORANGE, 'desc': 'Destroy tokens\nDecrease supply'},
    {'name': 'Upgrade', 'x': 0.9, 'color': MLRED, 'desc': 'New logic\nMigration'},
]

box_width = 0.14
box_height = 0.25

for i, stage in enumerate(stages):
    # Main stage box
    box = FancyBboxPatch((stage['x'] - box_width/2, 0.55), box_width, box_height,
                          boxstyle="round,pad=0.02", facecolor=stage['color'],
                          edgecolor='black', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    ax.text(stage['x'], 0.675, stage['name'], ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Description below
    ax.text(stage['x'], 0.40, stage['desc'], ha='center', va='top',
            fontsize=9, color='#333')

    # Arrow to next stage (except last)
    if i < len(stages) - 1:
        ax.annotate('', xy=(stages[i+1]['x'] - box_width/2 - 0.02, 0.675),
                   xytext=(stage['x'] + box_width/2 + 0.02, 0.675),
                   arrowprops=dict(arrowstyle='->', color='#666', lw=2))

# Cycle arrow from Upgrade back to Operation
ax.annotate('', xy=(0.5, 0.85), xytext=(0.9, 0.85),
           arrowprops=dict(arrowstyle='->', color='#888', lw=1.5,
                          connectionstyle='arc3,rad=0.3'))
ax.text(0.70, 0.93, 'Proxy Upgrade', fontsize=9, ha='center', color='#666')

# Loop from Operation to Burning and back
ax.annotate('', xy=(0.5 + box_width/2, 0.55), xytext=(0.7 - box_width/2, 0.55),
           arrowprops=dict(arrowstyle='<->', color='#888', lw=1.5,
                          connectionstyle='arc3,rad=-0.3'))
ax.text(0.60, 0.48, 'Continuous', fontsize=8, ha='center', color='#666')

# Supply indicator
ax.text(0.30, 0.22, 'Supply +', fontsize=10, fontweight='bold', color=MLGREEN, ha='center')
ax.text(0.70, 0.22, 'Supply -', fontsize=10, fontweight='bold', color=MLORANGE, ha='center')

# Timeline indicator
ax.axhline(y=0.15, xmin=0.08, xmax=0.92, color='#ccc', linestyle='-', lw=2)
ax.text(0.08, 0.10, 'Start', fontsize=9, color='#666')
ax.text(0.92, 0.10, 'Time', fontsize=9, ha='right', color='#666')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Token Lifecycle Stages', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
