"""
Solidity Compilation Flow
Shows the path from Solidity source to EVM bytecode
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Solidity Compilation Flow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals/charts/01_solidity_compilation_flow'
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

# Define boxes for compilation stages
stages = [
    {'name': 'Solidity\nSource\n(.sol)', 'x': 0.08, 'color': MLBLUE},
    {'name': 'Compiler\n(solc)', 'x': 0.30, 'color': MLPURPLE},
    {'name': 'Bytecode\n(hex)', 'x': 0.52, 'color': MLORANGE},
    {'name': 'EVM\nExecution', 'x': 0.74, 'color': MLGREEN},
]

box_width = 0.15
box_height = 0.35
y_center = 0.5

for stage in stages:
    box = FancyBboxPatch((stage['x'], y_center - box_height/2), box_width, box_height,
                          boxstyle="round,pad=0.02", facecolor=stage['color'],
                          edgecolor='black', linewidth=2, alpha=0.85)
    ax.add_patch(box)
    ax.text(stage['x'] + box_width/2, y_center, stage['name'],
            ha='center', va='center', fontsize=12, fontweight='bold', color='white')

# Add arrows between stages
arrow_y = y_center
for i in range(len(stages) - 1):
    ax.annotate('', xy=(stages[i+1]['x'] - 0.02, arrow_y),
                xytext=(stages[i]['x'] + box_width + 0.02, arrow_y),
                arrowprops=dict(arrowstyle='->', color='black', lw=2.5))

# Add outputs from compiler
outputs = [
    {'name': 'ABI\n(interface)', 'x': 0.30, 'y': 0.15, 'color': '#888'},
    {'name': 'AST\n(syntax tree)', 'x': 0.44, 'y': 0.15, 'color': '#888'},
]

for output in outputs:
    box = FancyBboxPatch((output['x'], output['y'] - 0.08), 0.12, 0.16,
                          boxstyle="round,pad=0.02", facecolor=output['color'],
                          edgecolor='black', linewidth=1, alpha=0.7)
    ax.add_patch(box)
    ax.text(output['x'] + 0.06, output['y'], output['name'],
            ha='center', va='center', fontsize=9, color='white')

# Arrows from compiler to outputs
ax.annotate('', xy=(0.36, 0.23), xytext=(0.36, y_center - box_height/2),
            arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))
ax.annotate('', xy=(0.50, 0.23), xytext=(0.40, y_center - box_height/2),
            arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

# Add annotations
ax.text(0.15, 0.88, 'pragma solidity ^0.8.0;\ncontract {...}',
        fontsize=9, family='monospace', ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='#E8E8E8', edgecolor='#888'))

ax.text(0.58, 0.88, '0x6080604052...',
        fontsize=9, family='monospace', ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='#E8E8E8', edgecolor='#888'))

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.82, 0.15, 'Deployed to\nBlockchain',
        ha='center', va='center', fontsize=10, fontweight='bold',
        bbox=props, color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Solidity Compilation Pipeline', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
