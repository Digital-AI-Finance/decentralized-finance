"""
Bitcoin Block Header Structure
Shows the 80-byte header components
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Block Header Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/02_block_header'
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

# Header components (proportional to byte size)
components = [
    ('Version', 4, MLLAVENDER, '4 bytes'),
    ('Previous Block Hash', 32, MLBLUE, '32 bytes'),
    ('Merkle Root', 32, MLGREEN, '32 bytes'),
    ('Timestamp', 4, MLORANGE, '4 bytes'),
    ('Difficulty Target', 4, MLPURPLE, '4 bytes'),
    ('Nonce', 4, MLRED, '4 bytes'),
]

total_bytes = 80
y_start = 0.75
bar_height = 0.35
x_pos = 0.05

for name, bytes_size, color, size_label in components:
    width = (bytes_size / total_bytes) * 0.90

    box = FancyBboxPatch((x_pos, y_start - bar_height/2), width, bar_height,
                          boxstyle="round,pad=0.01", facecolor=color,
                          edgecolor='black', linewidth=1.5)
    ax.add_patch(box)

    # Label inside or outside based on width
    if width > 0.15:
        ax.text(x_pos + width/2, y_start + 0.05, name, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')
        ax.text(x_pos + width/2, y_start - 0.08, size_label, ha='center', va='center',
                fontsize=14, color='white')
    else:
        ax.text(x_pos + width/2, y_start + 0.25, name, ha='center', va='bottom',
                fontsize=14, fontweight='bold', color=color, rotation=45)
        ax.text(x_pos + width/2, y_start - 0.22, size_label, ha='center', va='top',
                fontsize=14, color='#555')

    x_pos += width

# Total size annotation
ax.text(0.50, 0.32, 'Total: 80 bytes', ha='center', fontsize=16, fontweight='bold', color='#333')

# Mining process description
process_text = [
    ('1. Construct header', 0.15, 0.15),
    ('2. Hash (SHA-256 twice)', 0.45, 0.15),
    ('3. Check if < Target', 0.75, 0.15),
]

for text, x, y in process_text:
    ax.text(x, y, text, ha='center', fontsize=14, color='#444')

# Nonce highlight
highlight = FancyBboxPatch((0.88, 0.08), 0.10, 0.10,
                            boxstyle="round,pad=0.02", facecolor='#FFE0E0',
                            edgecolor=MLRED, linewidth=2)
ax.add_patch(highlight)
ax.text(0.93, 0.13, 'Nonce:\nThe only field\nminers change', ha='center', fontsize=14,
        color=MLRED, fontweight='bold')

# Arrow showing nonce is modified
ax.annotate('', xy=(0.90, 0.57), xytext=(0.90, 0.22),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Bitcoin Block Header (80 bytes)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
