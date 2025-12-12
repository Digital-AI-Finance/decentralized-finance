"""
Merkle Patricia Trie Structure
Shows node types and path compression
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'MPT Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/04_mpt_structure'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Root node (Branch)
root = FancyBboxPatch((0.40, 0.75), 0.20, 0.12,
                       boxstyle="round,pad=0.01", facecolor=MLBLUE,
                       edgecolor='black', linewidth=2)
ax.add_patch(root)
ax.text(0.50, 0.81, 'Root (Branch)', ha='center', fontsize=10, fontweight='bold', color='white')

# Extension node (left)
ext = FancyBboxPatch((0.15, 0.50), 0.18, 0.12,
                      boxstyle="round,pad=0.01", facecolor=MLORANGE,
                      edgecolor='black', linewidth=1.5)
ax.add_patch(ext)
ax.text(0.24, 0.56, 'Extension', ha='center', fontsize=10, fontweight='bold', color='white')
ax.text(0.24, 0.52, 'path: "a7"', ha='center', fontsize=8, color='white')

# Branch node (right)
branch = FancyBboxPatch((0.67, 0.50), 0.18, 0.12,
                         boxstyle="round,pad=0.01", facecolor=MLBLUE,
                         edgecolor='black', linewidth=1.5)
ax.add_patch(branch)
ax.text(0.76, 0.56, 'Branch', ha='center', fontsize=10, fontweight='bold', color='white')
ax.text(0.76, 0.52, '16 children', ha='center', fontsize=8, color='white')

# Leaf nodes at bottom
leaf_positions = [(0.08, 0.22), (0.28, 0.22), (0.58, 0.22), (0.78, 0.22)]
leaf_labels = ['Leaf\n0xa7f9...', 'Leaf\n0xa8e3...', 'Leaf\n0xb2c1...', 'Leaf\n0xb3d4...']

for (x, y), label in zip(leaf_positions, leaf_labels):
    leaf = FancyBboxPatch((x, y), 0.14, 0.14,
                           boxstyle="round,pad=0.01", facecolor=MLGREEN,
                           edgecolor='black', linewidth=1.5)
    ax.add_patch(leaf)
    ax.text(x + 0.07, y + 0.07, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color='white')

# Connecting lines
# Root to Extension
ax.plot([0.50, 0.24], [0.75, 0.62], 'k-', linewidth=1.5)
ax.text(0.35, 0.70, '0xa', fontsize=9, color='#555')

# Root to Branch
ax.plot([0.50, 0.76], [0.75, 0.62], 'k-', linewidth=1.5)
ax.text(0.65, 0.70, '0xb', fontsize=9, color='#555')

# Extension to Leaves
ax.plot([0.24, 0.15], [0.50, 0.36], 'k-', linewidth=1.5)
ax.plot([0.24, 0.35], [0.50, 0.36], 'k-', linewidth=1.5)

# Branch to Leaves
ax.plot([0.76, 0.65], [0.50, 0.36], 'k-', linewidth=1.5)
ax.plot([0.76, 0.85], [0.50, 0.36], 'k-', linewidth=1.5)

# Node type legend
legend_y = 0.10
ax.add_patch(FancyBboxPatch((0.10, legend_y), 0.08, 0.06, facecolor=MLBLUE))
ax.text(0.22, legend_y + 0.03, 'Branch: 16 children + value', fontsize=9, va='center')

ax.add_patch(FancyBboxPatch((0.45, legend_y), 0.08, 0.06, facecolor=MLORANGE))
ax.text(0.57, legend_y + 0.03, 'Extension: shared prefix', fontsize=9, va='center')

ax.add_patch(FancyBboxPatch((0.75, legend_y), 0.08, 0.06, facecolor=MLGREEN))
ax.text(0.87, legend_y + 0.03, 'Leaf: key + value', fontsize=9, va='center')

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.92)
ax.axis('off')

ax.set_title('Merkle Patricia Trie: Node Types', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
