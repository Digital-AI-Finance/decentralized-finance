"""
Multi-Signature Wallet Schemes
Shows different M-of-N configurations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Multi-Signature Schemes',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/06_multisig_schemes'
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

fig, axes = plt.subplots(1, 3, figsize=(10, 6))

def draw_multisig(ax, m, n, title, use_case, color):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title
    ax.set_title(f'{m}-of-{n}', fontsize=16, fontweight='bold', color=color, pad=10)

    # Draw key circles
    positions = []
    if n == 2:
        positions = [(0.3, 0.65), (0.7, 0.65)]
    elif n == 3:
        positions = [(0.2, 0.65), (0.5, 0.65), (0.8, 0.65)]
    elif n == 5:
        positions = [(0.15, 0.65), (0.35, 0.65), (0.5, 0.65), (0.65, 0.65), (0.85, 0.65)]

    for i, (x, y) in enumerate(positions):
        # Color: green if needed, gray if spare
        if i < m:
            key_color = MLGREEN
        else:
            key_color = '#CCCCCC'

        circle = Circle((x, y), 0.08, facecolor=key_color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, f'K{i+1}', ha='center', va='center', fontsize=12,
                fontweight='bold', color='white')

    # Required vs total
    ax.text(0.5, 0.45, f'{m} signatures required', ha='center', va='center',
            fontsize=11, color=color, fontweight='bold')
    ax.text(0.5, 0.38, f'out of {n} total keys', ha='center', va='center',
            fontsize=10, color='#666')

    # Use case box
    use_box = FancyBboxPatch((0.1, 0.08), 0.8, 0.18,
                              boxstyle="round,pad=0.02", facecolor='white',
                              edgecolor=color, linewidth=2)
    ax.add_patch(use_box)
    ax.text(0.5, 0.17, use_case, ha='center', va='center', fontsize=10,
            color='#333', style='italic')

# 2-of-3 (most common)
draw_multisig(axes[0], 2, 3, '2-of-3', 'Personal backup\nEscrow services', MLBLUE)

# 3-of-5 (corporate)
draw_multisig(axes[1], 3, 5, '3-of-5', 'Corporate treasury\nDAO governance', MLPURPLE)

# 2-of-2 (joint)
draw_multisig(axes[2], 2, 2, '2-of-2', 'Joint accounts\nBuyer + Seller', MLORANGE)

# Add legend at bottom
fig.text(0.5, 0.02, 'Green = Required for signing | Gray = Spare/backup key',
         ha='center', fontsize=11, color='#555')

plt.suptitle('Multi-Signature (M-of-N) Wallet Configurations', fontsize=15,
             fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
