"""
Block Structure: Anatomy of a Blockchain Block
Shows header fields, Merkle root, and hash linking
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Anatomy of a Blockchain Block',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/04_block_structure'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Main block container
main_block = FancyBboxPatch((0.25, 0.1), 0.5, 0.8, boxstyle="round,pad=0.02",
                             facecolor='white', edgecolor=MLPURPLE, linewidth=3)
ax.add_patch(main_block)

# Block Header section
header_box = Rectangle((0.28, 0.55), 0.44, 0.32, facecolor=MLLAVENDER, edgecolor=MLPURPLE, linewidth=2)
ax.add_patch(header_box)
ax.text(0.5, 0.84, 'BLOCK HEADER', ha='center', va='center', fontsize=14, fontweight='bold', color=MLPURPLE)

# Header fields
header_fields = [
    ('Version', '4 bytes'),
    ('Previous Block Hash', '32 bytes'),
    ('Merkle Root', '32 bytes'),
    ('Timestamp', '4 bytes'),
    ('Difficulty Target', '4 bytes'),
    ('Nonce', '4 bytes'),
]

y_pos = 0.78
for field, size in header_fields:
    ax.text(0.32, y_pos, f'{field}:', fontsize=15, fontweight='bold', va='center')
    ax.text(0.62, y_pos, size, fontsize=14, va='center', color='gray')
    y_pos -= 0.042

# Transaction section
tx_box = Rectangle((0.28, 0.13), 0.44, 0.38, facecolor='#F0F0F0', edgecolor=MLBLUE, linewidth=2)
ax.add_patch(tx_box)
ax.text(0.5, 0.485, 'TRANSACTIONS', ha='center', va='center', fontsize=14, fontweight='bold', color=MLBLUE)

# Individual transactions
for i, y in enumerate([0.42, 0.34, 0.26, 0.18]):
    tx_color = MLGREEN if i == 0 else '#E8E8E8'
    tx = Rectangle((0.32, y), 0.36, 0.06, facecolor=tx_color, edgecolor='black', linewidth=1)
    ax.add_patch(tx)
    if i == 0:
        ax.text(0.5, y + 0.03, 'Coinbase (Block Reward)', ha='center', va='center', fontsize=14, fontweight='bold')
    else:
        ax.text(0.5, y + 0.03, f'Transaction {i}', ha='center', va='center', fontsize=14)

# Left side: Previous block
prev_block = FancyBboxPatch((0.02, 0.35), 0.15, 0.3, boxstyle="round,pad=0.02",
                             facecolor='#E8E8E8', edgecolor='gray', linewidth=2)
ax.add_patch(prev_block)
ax.text(0.095, 0.5, 'Block\nN-1', ha='center', va='center', fontsize=14, fontweight='bold', color='gray')

# Right side: Next block
next_block = FancyBboxPatch((0.83, 0.35), 0.15, 0.3, boxstyle="round,pad=0.02",
                             facecolor='#E8E8E8', edgecolor='gray', linewidth=2)
ax.add_patch(next_block)
ax.text(0.905, 0.5, 'Block\nN+1', ha='center', va='center', fontsize=14, fontweight='bold', color='gray')

# Chain arrows with labels below the side blocks
ax.annotate('', xy=(0.25, 0.5), xytext=(0.17, 0.5),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2.5))
ax.text(0.095, 0.30, 'Hash', ha='center', fontsize=14, color=MLORANGE, fontweight='bold')

ax.annotate('', xy=(0.83, 0.5), xytext=(0.75, 0.5),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2.5))
ax.text(0.905, 0.30, 'Hash', ha='center', fontsize=14, color=MLORANGE, fontweight='bold')

# Block label
ax.text(0.5, 0.92, 'Block N', ha='center', va='center', fontsize=14, fontweight='bold', color=MLPURPLE)

# Size annotation
ax.text(0.5, 0.02, 'Average Bitcoin block: ~1-2 MB | ~2000-3000 transactions',
        ha='center', fontsize=14, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Anatomy of a Blockchain Block', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
