"""
Ethereum's Four MPT Tries
Block references four trie roots
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Four Tries',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/05_four_tries'
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

# Block header box at top
block_header = FancyBboxPatch((0.30, 0.72), 0.40, 0.18,
                               boxstyle="round,pad=0.02", facecolor='#E8E8E8',
                               edgecolor='#333', linewidth=2)
ax.add_patch(block_header)
ax.text(0.50, 0.85, 'Block Header', ha='center', fontsize=13, fontweight='bold')
ax.text(0.50, 0.77, 'stateRoot | txRoot | receiptsRoot', ha='center', fontsize=9,
        family='monospace')

# Four tries
tries = [
    (0.05, 'State Trie', MLBLUE, 'Global', 'Address -> Account'),
    (0.30, 'Storage Trie', MLGREEN, 'Per Contract', 'Key -> Value'),
    (0.55, 'Transaction Trie', MLORANGE, 'Per Block', 'Index -> TX'),
    (0.80, 'Receipt Trie', MLPURPLE, 'Per Block', 'Index -> Receipt'),
]

for x, name, color, scope, mapping in tries:
    # Trie box
    trie = FancyBboxPatch((x, 0.25), 0.18, 0.35,
                           boxstyle="round,pad=0.01", facecolor=color,
                           edgecolor='black', linewidth=1.5)
    ax.add_patch(trie)

    ax.text(x + 0.09, 0.52, name.split()[0], ha='center', fontsize=10,
            fontweight='bold', color='white')
    ax.text(x + 0.09, 0.46, name.split()[1] if len(name.split()) > 1 else '',
            ha='center', fontsize=10, fontweight='bold', color='white')
    ax.text(x + 0.09, 0.38, scope, ha='center', fontsize=9, color='white')
    ax.text(x + 0.09, 0.30, mapping, ha='center', fontsize=8, color='white')

    # Connection to block header
    ax.plot([x + 0.09, 0.50], [0.60, 0.72], 'k-', linewidth=1, alpha=0.5)

# Properties at bottom
props_text = [
    'Merkle proof: O(log n)',
    'Deterministic root hash',
    'Efficient updates',
]
for i, txt in enumerate(props_text):
    ax.text(0.15 + i * 0.30, 0.12, txt, ha='center', fontsize=10, color='#555')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE)
ax.text(0.50, 0.05, 'Root hashes in block header enable light client verification',
        ha='center', fontsize=10, bbox=props, color=MLBLUE)

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('Ethereum Block: Four Merkle Patricia Tries', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
