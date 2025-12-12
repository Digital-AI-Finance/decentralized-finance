"""
Hash Function Properties Overview
Visual diagram showing the 6 key properties of cryptographic hash functions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Hash Function Properties',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/01_hash_properties'
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

# Central hash function box
center_x, center_y = 0.5, 0.5
box = FancyBboxPatch((0.38, 0.38), 0.24, 0.24, boxstyle="round,pad=0.02",
                      facecolor=MLPURPLE, edgecolor='black', linewidth=2)
ax.add_patch(box)
ax.text(center_x, center_y, 'H(x)\nHash\nFunction', ha='center', va='center',
        fontsize=14, fontweight='bold', color='white')

# Properties arranged around the center
properties = [
    (0.15, 0.85, 'Deterministic', 'Same input\n= Same output', MLBLUE),
    (0.50, 0.92, 'Fixed Length', '256 bits\n(always)', MLGREEN),
    (0.85, 0.85, 'Avalanche Effect', '1 bit change\n= 50% flip', MLORANGE),
    (0.15, 0.15, 'Preimage\nResistant', 'Cannot reverse\nhash to input', MLRED),
    (0.50, 0.08, 'Second Preimage\nResistant', 'Cannot find\nalternate input', MLPURPLE),
    (0.85, 0.15, 'Collision\nResistant', 'Cannot find\ntwo same hashes', MLBLUE),
]

for x, y, title, desc, color in properties:
    # Property box
    box_width = 0.22
    box_height = 0.18
    prop_box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                               boxstyle="round,pad=0.02", facecolor='white',
                               edgecolor=color, linewidth=2.5)
    ax.add_patch(prop_box)
    ax.text(x, y + 0.03, title, ha='center', va='center', fontsize=11,
            fontweight='bold', color=color)
    ax.text(x, y - 0.05, desc, ha='center', va='center', fontsize=9,
            color='#444')

    # Arrow to center
    if y > 0.5:
        arrow_start = (x, y - box_height/2 - 0.02)
        arrow_end = (center_x + (x - center_x) * 0.3, center_y + 0.15)
    else:
        arrow_start = (x, y + box_height/2 + 0.02)
        arrow_end = (center_x + (x - center_x) * 0.3, center_y - 0.15)

    ax.annotate('', xy=arrow_end, xytext=arrow_start,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5, alpha=0.6))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Six Essential Properties of Cryptographic Hash Functions', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
