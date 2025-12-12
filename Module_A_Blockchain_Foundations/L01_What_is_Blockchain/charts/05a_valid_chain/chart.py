"""
Valid Blockchain: Hash Chain Integrity
ONE figure only - shows how valid hashes link blocks
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Valid Blockchain Hash Chain',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/05a_valid_chain'
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
ax.text(0.5, 0.92, 'VALID BLOCKCHAIN: All Hashes Match',
        ha='center', fontsize=14, fontweight='bold', color=MLGREEN)

blocks = [
    ('Block 100', '0x7a3f...', '0x8b4e...'),
    ('Block 101', '0x8b4e...', '0x9c5d...'),
    ('Block 102', '0x9c5d...', '0xad6e...'),
    ('Block 103', '0xad6e...', '0xbe7f...'),
]

for i, (name, prev_hash, curr_hash) in enumerate(blocks):
    x = 0.05 + i * 0.24

    # Block box
    block = FancyBboxPatch((x, 0.25), 0.20, 0.55, boxstyle="round,pad=0.02",
                            facecolor='#E8FFE8', edgecolor=MLGREEN, linewidth=3)
    ax.add_patch(block)

    # Block name
    ax.text(x + 0.10, 0.72, name, ha='center', va='center', fontsize=15, fontweight='bold')

    # Previous hash
    ax.text(x + 0.10, 0.55, f'Prev: {prev_hash}', ha='center', va='center', fontsize=14, color='gray')

    # Current hash
    ax.text(x + 0.10, 0.38, f'Hash: {curr_hash}', ha='center', va='center', fontsize=14, color=MLPURPLE, fontweight='bold')

    # Chain arrow and match indicator
    if i < len(blocks) - 1:
        ax.annotate('', xy=(x + 0.29, 0.5), xytext=(x + 0.20, 0.5),
                    arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=3))
        ax.text(x + 0.245, 0.15, 'Match!', ha='center', fontsize=14, color=MLGREEN, fontweight='bold')

# Bottom note
ax.text(0.5, 0.05, 'Each block references the hash of the previous block',
        ha='center', fontsize=14, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
