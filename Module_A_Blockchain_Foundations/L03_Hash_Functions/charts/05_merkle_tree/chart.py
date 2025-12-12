"""
Merkle Tree Construction Visualization
Shows how transactions are hashed into a tree structure
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Merkle Tree Construction',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/05_merkle_tree'
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

# Tree structure (bottom to top)
# Level 0: Transactions
# Level 1: Transaction hashes
# Level 2: Paired hashes
# Level 3: Root

# Positions
tx_y = 0.12
h1_y = 0.35
h2_y = 0.58
root_y = 0.82

# Transactions (Level 0)
tx_positions = [0.15, 0.38, 0.62, 0.85]
tx_labels = ['Tx1', 'Tx2', 'Tx3', 'Tx4']
tx_colors = [MLBLUE, MLBLUE, MLORANGE, MLBLUE]  # Tx3 highlighted for proof

for x, label, color in zip(tx_positions, tx_labels, tx_colors):
    box = FancyBboxPatch((x - 0.06, tx_y - 0.06), 0.12, 0.12,
                          boxstyle="round,pad=0.01", facecolor='white',
                          edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, tx_y, label, ha='center', va='center', fontsize=15,
            fontweight='bold', color=color)

# Level 1: Hash of each transaction
h1_positions = [0.15, 0.38, 0.62, 0.85]
h1_labels = ['H(Tx1)', 'H(Tx2)', 'H(Tx3)', 'H(Tx4)']
h1_colors = [MLGREEN, MLGREEN, MLORANGE, MLGREEN]

for x, label, color in zip(h1_positions, h1_labels, h1_colors):
    circle = Circle((x, h1_y), 0.055, facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, h1_y, label.replace('H(', '').replace(')', ''), ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    # Arrow from tx to hash
    tx_idx = h1_positions.index(x)
    ax.annotate('', xy=(x, h1_y - 0.055), xytext=(tx_positions[tx_idx], tx_y + 0.06),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

# Level 2: Paired hashes
h2_positions = [0.265, 0.735]
h2_labels = ['H12', 'H34']
h2_colors = [MLGREEN, MLORANGE]

for i, (x, label, color) in enumerate(zip(h2_positions, h2_labels, h2_colors)):
    circle = Circle((x, h2_y), 0.06, facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, h2_y, label, ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Arrows from level 1
    if i == 0:
        sources = [0.15, 0.38]
    else:
        sources = [0.62, 0.85]
    for src_x in sources:
        ax.annotate('', xy=(x, h2_y - 0.06), xytext=(src_x, h1_y + 0.055),
                    arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

# Root
root_x = 0.5
circle = Circle((root_x, root_y), 0.07, facecolor=MLPURPLE, edgecolor='black', linewidth=2)
ax.add_patch(circle)
ax.text(root_x, root_y, 'ROOT', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Arrows to root
for x in h2_positions:
    ax.annotate('', xy=(root_x, root_y - 0.07), xytext=(x, h2_y + 0.06),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

# Level labels
ax.text(0.02, tx_y, 'Level 0\nData', ha='center', va='center', fontsize=14, color='#666')
ax.text(0.02, h1_y, 'Level 1\nLeaf Hashes', ha='center', va='center', fontsize=14, color='#666')
ax.text(0.02, h2_y, 'Level 2\nInternal', ha='center', va='center', fontsize=14, color='#666')
ax.text(0.02, root_y, 'Level 3\nMerkle Root', ha='center', va='center', fontsize=14, color='#666')

# Merkle proof annotation
proof_text = 'Merkle Proof for Tx3:\n1. H(Tx4) - sibling\n2. H12 - aunt\nVerify: H(H12 || H(H(Tx3)||H(Tx4))) = Root'
props = dict(boxstyle='round,pad=0.3', facecolor='#FFF5E6', edgecolor=MLORANGE, alpha=0.95)
ax.text(0.98, 0.25, proof_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right', bbox=props, color='#333')

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Merkle Tree: Hierarchical Hash Structure', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
