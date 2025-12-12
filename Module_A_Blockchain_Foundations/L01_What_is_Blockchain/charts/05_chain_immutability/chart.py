"""
Chain Immutability: How Changing One Block Breaks the Chain
Visual demonstration of hash chain integrity
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Blockchain Immutability Demonstration',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/05_chain_immutability'
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

fig, axes = plt.subplots(2, 1, figsize=(10, 6))

# Top panel: Valid chain
ax1 = axes[0]
ax1.set_title('Valid Blockchain: All Hashes Match', fontweight='bold', fontsize=14, color=MLGREEN)

blocks_valid = [
    ('Block 100', '0x7a3f...', '0x8b4e...', MLGREEN),
    ('Block 101', '0x8b4e...', '0x9c5d...', MLGREEN),
    ('Block 102', '0x9c5d...', '0xad6e...', MLGREEN),
    ('Block 103', '0xad6e...', '0xbe7f...', MLGREEN),
]

for i, (name, prev_hash, curr_hash, color) in enumerate(blocks_valid):
    x = 0.1 + i * 0.22
    # Block
    block = FancyBboxPatch((x, 0.25), 0.18, 0.5, boxstyle="round,pad=0.02",
                            facecolor='#E8FFE8', edgecolor=color, linewidth=2)
    ax1.add_patch(block)
    ax1.text(x + 0.09, 0.68, name, ha='center', va='center', fontsize=14, fontweight='bold')
    ax1.text(x + 0.09, 0.52, f'Prev: {prev_hash}', ha='center', va='center', fontsize=14, color='gray')
    ax1.text(x + 0.09, 0.38, f'Hash: {curr_hash}', ha='center', va='center', fontsize=14, color=MLPURPLE)

    # Chain arrow
    if i < len(blocks_valid) - 1:
        ax1.annotate('', xy=(x + 0.22, 0.5), xytext=(x + 0.18, 0.5),
                    arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
        ax1.text(x + 0.20, 0.15, 'Match!', ha='center', fontsize=14, color=MLGREEN, fontweight='bold')

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')

# Bottom panel: Tampered chain
ax2 = axes[1]
ax2.set_title('Tampered Blockchain: Hash Mismatch Detected', fontweight='bold', fontsize=14, color=MLRED)

blocks_tampered = [
    ('Block 100', '0x7a3f...', '0x8b4e...', MLGREEN, False),
    ('Block 101\n(MODIFIED)', '0x8b4e...', '0xXXXX...', MLRED, True),
    ('Block 102', '0xXXXX...', '0x9c5d...', MLRED, True),
    ('Block 103', '0x9c5d...', '0xad6e...', MLRED, True),
]

for i, (name, prev_hash, curr_hash, color, broken) in enumerate(blocks_tampered):
    x = 0.1 + i * 0.22
    # Block
    facecolor = '#FFE8E8' if broken else '#E8FFE8'
    block = FancyBboxPatch((x, 0.25), 0.18, 0.5, boxstyle="round,pad=0.02",
                            facecolor=facecolor, edgecolor=color, linewidth=2)
    ax2.add_patch(block)
    ax2.text(x + 0.09, 0.68, name, ha='center', va='center', fontsize=14, fontweight='bold',
             color=MLRED if broken else 'black')
    ax2.text(x + 0.09, 0.52, f'Prev: {prev_hash}', ha='center', va='center', fontsize=14,
             color=MLRED if i > 0 and blocks_tampered[i-1][4] else 'gray')
    ax2.text(x + 0.09, 0.38, f'Hash: {curr_hash}', ha='center', va='center', fontsize=14,
             color=MLRED if broken else MLPURPLE)

    # Chain arrow
    if i < len(blocks_tampered) - 1:
        arrow_color = MLRED if i >= 1 else MLGREEN
        ax2.annotate('', xy=(x + 0.22, 0.5), xytext=(x + 0.18, 0.5),
                    arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))
        if i >= 1:
            ax2.text(x + 0.20, 0.15, 'BROKEN!', ha='center', fontsize=14, color=MLRED, fontweight='bold')
        else:
            ax2.text(x + 0.20, 0.15, 'Match', ha='center', fontsize=14, color=MLGREEN)

# Warning symbol on modified block
ax2.text(0.32 + 0.09, 0.85, '!', ha='center', va='center', fontsize=16, fontweight='bold', color=MLRED)

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')

plt.suptitle('Immutability Through Hash Chaining', fontweight='bold', fontsize=15, y=0.98)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
