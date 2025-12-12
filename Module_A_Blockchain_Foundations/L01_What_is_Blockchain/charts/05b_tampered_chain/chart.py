"""
Tampered Blockchain: Hash Mismatch Detection
ONE figure only - shows how modification breaks the chain
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Tampered Blockchain Detection',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/05b_tampered_chain'
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

# Title
ax.text(0.5, 0.92, 'TAMPERED BLOCKCHAIN: Hash Mismatch Detected!',
        ha='center', fontsize=14, fontweight='bold', color=MLRED)

blocks = [
    ('Block 100', '0x7a3f...', '0x8b4e...', False),
    ('Block 101\n(MODIFIED!)', '0x8b4e...', '0xXXXX...', True),
    ('Block 102', '0xXXXX...', '0x9c5d...', True),
    ('Block 103', '0x9c5d...', '0xad6e...', True),
]

for i, (name, prev_hash, curr_hash, broken) in enumerate(blocks):
    x = 0.05 + i * 0.24

    # Block box - red for broken, green for valid
    facecolor = '#FFE8E8' if broken else '#E8FFE8'
    edgecolor = MLRED if broken else MLGREEN
    block = FancyBboxPatch((x, 0.25), 0.20, 0.55, boxstyle="round,pad=0.02",
                            facecolor=facecolor, edgecolor=edgecolor, linewidth=3)
    ax.add_patch(block)

    # Block name
    text_color = MLRED if broken else 'black'
    ax.text(x + 0.10, 0.70, name, ha='center', va='center', fontsize=14, fontweight='bold', color=text_color)

    # Previous hash - red if mismatch
    prev_color = MLRED if (i > 0 and blocks[i-1][3]) else 'gray'
    ax.text(x + 0.10, 0.50, f'Prev: {prev_hash}', ha='center', va='center', fontsize=14, color=prev_color)

    # Current hash
    hash_color = MLRED if broken else MLPURPLE
    ax.text(x + 0.10, 0.35, f'Hash: {curr_hash}', ha='center', va='center', fontsize=14, color=hash_color, fontweight='bold')

    # Chain arrow and status indicator
    if i < len(blocks) - 1:
        arrow_color = MLRED if i >= 1 else MLGREEN
        ax.annotate('', xy=(x + 0.29, 0.5), xytext=(x + 0.20, 0.5),
                    arrowprops=dict(arrowstyle='->', color=arrow_color, lw=3))

        if i >= 1:
            ax.text(x + 0.245, 0.15, 'BROKEN!', ha='center', fontsize=14, color=MLRED, fontweight='bold')
        else:
            ax.text(x + 0.245, 0.15, 'Match', ha='center', fontsize=14, color=MLGREEN, fontweight='bold')

# Warning symbol on modified block
ax.text(0.05 + 1 * 0.24 + 0.10, 0.85, '!', ha='center', va='center', fontsize=20, fontweight='bold', color=MLRED)

# Bottom note
ax.text(0.5, 0.05, 'Modifying any block invalidates ALL subsequent blocks',
        ha='center', fontsize=14, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
