"""
Merkle Tree Structure Visualization
Shows how transaction hashes are combined into a Merkle root
[SYNTHETIC DATA]
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Merkle Tree Structure - Transaction Hash Aggregation',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/merkle_tree'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9
})

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title('Merkle Tree: Efficient Transaction Verification', fontsize=12, fontweight='bold')

# Colors (grayscale-friendly)
root_color = '#2d2d2d'
branch_color = '#5a5a5a'
leaf_color = '#8a8a8a'
tx_color = '#b0b0b0'

def draw_node(x, y, text, color, width=1.2, height=0.5):
    rect = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                    boxstyle="round,pad=0.05", facecolor=color,
                                    edgecolor='black', linewidth=1)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=8, color='white', fontweight='bold')

def draw_line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1, alpha=0.6)

# Level 0: Merkle Root
draw_node(5, 6, 'Merkle Root', root_color, width=1.8)

# Level 1: Branch hashes
draw_node(2.5, 4.5, 'H(AB)', branch_color, width=1.4)
draw_node(7.5, 4.5, 'H(CD)', branch_color, width=1.4)
draw_line(5, 5.75, 2.5, 4.75)
draw_line(5, 5.75, 7.5, 4.75)

# Level 2: Leaf hashes
draw_node(1.25, 3, 'H(A)', leaf_color)
draw_node(3.75, 3, 'H(B)', leaf_color)
draw_node(6.25, 3, 'H(C)', leaf_color)
draw_node(8.75, 3, 'H(D)', leaf_color)
draw_line(2.5, 4.25, 1.25, 3.25)
draw_line(2.5, 4.25, 3.75, 3.25)
draw_line(7.5, 4.25, 6.25, 3.25)
draw_line(7.5, 4.25, 8.75, 3.25)

# Level 3: Transactions
draw_node(1.25, 1.5, 'Tx A', tx_color)
draw_node(3.75, 1.5, 'Tx B', tx_color)
draw_node(6.25, 1.5, 'Tx C', tx_color)
draw_node(8.75, 1.5, 'Tx D', tx_color)
draw_line(1.25, 2.75, 1.25, 1.75)
draw_line(3.75, 2.75, 3.75, 1.75)
draw_line(6.25, 2.75, 6.25, 1.75)
draw_line(8.75, 2.75, 8.75, 1.75)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=root_color, edgecolor='black', label='Merkle Root (in block header)'),
    mpatches.Patch(facecolor=branch_color, edgecolor='black', label='Branch Hashes'),
    mpatches.Patch(facecolor=leaf_color, edgecolor='black', label='Leaf Hashes'),
    mpatches.Patch(facecolor=tx_color, edgecolor='black', label='Transactions'),
]
ax.legend(handles=legend_elements, loc='lower center', ncol=2, fontsize=8, framealpha=0.9)

# Add explanation
ax.text(5, 0.3, 'Verification: To prove Tx B is in the tree, only need H(A), H(CD), and Root',
        ha='center', va='center', fontsize=9, style='italic', alpha=0.7)

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC]', ha='right', va='bottom', fontsize=8, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
