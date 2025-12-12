"""
SHA-256 High-Level Process Flow
Shows the main steps of the SHA-256 algorithm
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'SHA-256 Process Flow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/04_sha256_process'
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

# Process steps (x position, y position, label, description, color)
steps = [
    (0.08, 0.5, 'INPUT', 'Any length\nmessage', MLBLUE),
    (0.25, 0.5, 'PADDING', '+1 bit\n+zeros\n+64-bit len', MLORANGE),
    (0.42, 0.5, 'PARSING', '512-bit\nblocks', MLGREEN),
    (0.59, 0.5, 'COMPRESSION', '64 rounds\nper block', MLPURPLE),
    (0.76, 0.5, 'FINALIZE', 'Concatenate\n8 words', MLRED),
    (0.93, 0.5, 'OUTPUT', '256-bit\nhash', MLBLUE),
]

box_width = 0.12
box_height = 0.35

for i, (x, y, label, desc, color) in enumerate(steps):
    # Main box
    box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=2, alpha=0.85)
    ax.add_patch(box)

    # Label (bold)
    ax.text(x, y + 0.08, label, ha='center', va='center', fontsize=14,
            fontweight='bold', color='white')

    # Description
    ax.text(x, y - 0.05, desc, ha='center', va='center', fontsize=14,
            color='white')

    # Arrow to next step
    if i < len(steps) - 1:
        next_x = steps[i + 1][0]
        ax.annotate('', xy=(next_x - box_width/2 - 0.01, y),
                    xytext=(x + box_width/2 + 0.01, y),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Add details below
details = [
    (0.25, 0.12, 'Ensure length\n= 448 mod 512'),
    (0.42, 0.12, 'Split into\nn blocks'),
    (0.59, 0.12, 'AND, XOR,\nrotate, add'),
]

for x, y, text in details:
    ax.text(x, y, text, ha='center', va='center', fontsize=14,
            color='#555', style='italic')
    # Dotted line up
    ax.plot([x, x], [y + 0.05, 0.5 - box_height/2 - 0.02],
            color='#999', linestyle=':', linewidth=1)

# Initial hash values annotation
ax.annotate('Initialize with\n8 constants\n(prime roots)', xy=(0.59, 0.7),
            xytext=(0.59, 0.88), ha='center', fontsize=14, color=MLPURPLE,
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=1.5))

# Example sizes
ax.text(0.08, 0.18, '"abc"\n(3 bytes)', ha='center', va='center', fontsize=14, color=MLBLUE)
ax.text(0.93, 0.18, '64 hex\ncharacters', ha='center', va='center', fontsize=14, color=MLBLUE)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('SHA-256 Algorithm: High-Level Process Flow', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
