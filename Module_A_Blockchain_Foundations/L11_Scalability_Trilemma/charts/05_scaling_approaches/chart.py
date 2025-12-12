"""
Vertical vs Horizontal Scaling
Comparison diagram
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Scaling Approaches',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/05_scaling_approaches'
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

# Left side: Vertical Scaling
ax.text(0.25, 0.95, 'VERTICAL SCALING', ha='center', fontsize=14,
        fontweight='bold', color=MLORANGE)
ax.text(0.25, 0.88, '(Scale Up)', ha='center', fontsize=14, color='#666')

# Draw big server
big_server = FancyBboxPatch((0.15, 0.35), 0.20, 0.45,
                             boxstyle="round,pad=0.02", facecolor=MLORANGE,
                             edgecolor='black', linewidth=2)
ax.add_patch(big_server)
ax.text(0.25, 0.57, 'POWERFUL\nNODE', ha='center', va='center',
        fontsize=14, fontweight='bold', color='white')

# Characteristics
ax.text(0.25, 0.28, 'Bigger blocks', ha='center', fontsize=14)
ax.text(0.25, 0.22, 'Faster processing', ha='center', fontsize=14)
ax.text(0.25, 0.16, 'Higher hardware req.', ha='center', fontsize=14)
ax.text(0.25, 0.08, 'Examples: Solana, EOS', ha='center', fontsize=14,
        fontweight='bold', color=MLORANGE)

# Right side: Horizontal Scaling
ax.text(0.75, 0.95, 'HORIZONTAL SCALING', ha='center', fontsize=14,
        fontweight='bold', color=MLGREEN)
ax.text(0.75, 0.88, '(Scale Out)', ha='center', fontsize=14, color='#666')

# Draw multiple small servers (shards)
shard_positions = [(0.58, 0.55), (0.70, 0.55), (0.82, 0.55),
                   (0.64, 0.38), (0.76, 0.38)]

for i, (x, y) in enumerate(shard_positions):
    shard = FancyBboxPatch((x, y), 0.10, 0.18,
                            boxstyle="round,pad=0.01", facecolor=MLGREEN,
                            edgecolor='black', linewidth=1.5)
    ax.add_patch(shard)
    ax.text(x + 0.05, y + 0.09, f'S{i+1}', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')

# Characteristics
ax.text(0.75, 0.28, 'Parallel processing', ha='center', fontsize=14)
ax.text(0.75, 0.22, 'Preserved decentralization', ha='center', fontsize=14)
ax.text(0.75, 0.16, 'Complex coordination', ha='center', fontsize=14)
ax.text(0.75, 0.08, 'Examples: Sharding, L2', ha='center', fontsize=14,
        fontweight='bold', color=MLGREEN)

# Dividing line
ax.axvline(x=0.5, color='#888', linestyle='--', linewidth=2, alpha=0.5)

# Trade-off indicators
props_bad = dict(boxstyle='round,pad=0.2', facecolor='#FFE0E0', edgecolor=MLRED)
props_good = dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN)

ax.text(0.25, 0.02, 'Centralization risk', ha='center', fontsize=14,
        bbox=props_bad, color=MLRED)
ax.text(0.75, 0.02, 'Preserves decentralization', ha='center', fontsize=14,
        bbox=props_good, color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Scaling Approaches: Trade-offs in Design', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
