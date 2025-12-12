"""
Key to Address Derivation Flow
Shows how private key becomes a blockchain address
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Key to Address Derivation',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/03_key_derivation'
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

# Flow: Private Key -> Public Key -> Hash -> Address
steps = [
    (0.08, 0.5, 'Private Key', '256-bit random\nnumber', MLRED),
    (0.30, 0.5, 'Public Key', 'Q = k * G\n(x, y coordinates)', MLBLUE),
    (0.52, 0.5, 'Hash', 'SHA-256 +\nRIPEMD-160', MLORANGE),
    (0.74, 0.5, 'Checksum', 'Double SHA-256\n(first 4 bytes)', MLGREEN),
    (0.92, 0.5, 'Address', 'Base58\nencoded', MLPURPLE),
]

box_width = 0.14
box_height = 0.28

for i, (x, y, label, desc, color) in enumerate(steps):
    # Box
    box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=2, alpha=0.85)
    ax.add_patch(box)

    # Label
    ax.text(x, y + 0.06, label, ha='center', va='center', fontsize=14,
            fontweight='bold', color='white')

    # Description
    ax.text(x, y - 0.04, desc, ha='center', va='center', fontsize=14,
            color='white')

    # Arrow
    if i < len(steps) - 1:
        next_x = steps[i + 1][0]
        ax.annotate('', xy=(next_x - box_width/2 - 0.01, y),
                    xytext=(x + box_width/2 + 0.01, y),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=2.5))

# Example values below
examples = [
    (0.08, 0.15, '256 bits\n(secret!)'),
    (0.30, 0.15, '33 or 65 bytes\n(public)'),
    (0.52, 0.15, '20 bytes\n(160 bits)'),
    (0.74, 0.15, '4 bytes'),
    (0.92, 0.15, '25-34 chars\n1A1zP1...'),
]

for x, y, text in examples:
    ax.text(x, y, text, ha='center', va='center', fontsize=14,
            color='#555', style='italic')

# One-way arrows annotation
ax.annotate('One-way function', xy=(0.19, 0.68), fontsize=14, color=MLRED,
            ha='center')
ax.annotate('', xy=(0.26, 0.65), xytext=(0.12, 0.65),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5))

# Key insight
insight_text = 'Cannot reverse: Address -> Private Key'
props = dict(boxstyle='round,pad=0.3', facecolor='#FFE0E0', edgecolor=MLRED, alpha=0.95)
ax.text(0.5, 0.88, insight_text, ha='center', va='center', fontsize=15,
        fontweight='bold', bbox=props, color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Bitcoin Address Derivation: From Private Key to Address', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
