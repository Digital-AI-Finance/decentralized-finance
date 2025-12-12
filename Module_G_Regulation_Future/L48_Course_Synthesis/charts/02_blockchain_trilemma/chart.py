"""
Blockchain Trilemma Visualization
Triangle showing the tradeoffs
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Blockchain Trilemma',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L48_Course_Synthesis/charts/02_blockchain_trilemma'
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

# Triangle vertices
vertices = np.array([
    [0.5, 0.9],   # Top: Decentralization
    [0.1, 0.15],  # Bottom left: Security
    [0.9, 0.15]   # Bottom right: Scalability
])

# Draw triangle
triangle = plt.Polygon(vertices, fill=True, facecolor='#E3F2FD',
                       edgecolor=MLBLUE, linewidth=3)
ax.add_patch(triangle)

# Add vertex labels
labels = ['DECENTRALIZATION', 'SECURITY', 'SCALABILITY']
label_positions = [
    (0.5, 0.95),
    (0.05, 0.08),
    (0.95, 0.08)
]
for pos, label in zip(label_positions, labels):
    ax.text(pos[0], pos[1], label, ha='center', va='center',
            fontsize=11, fontweight='bold', color=MLBLUE)

# Add blockchain positions
blockchains = {
    'Bitcoin': (0.35, 0.55, MLORANGE),      # High decentralization, high security, low scalability
    'Ethereum': (0.5, 0.45, MLPURPLE),       # Balanced
    'Solana': (0.65, 0.35, MLGREEN),         # Lower decentralization, high scalability
    'Layer 2s': (0.55, 0.30, MLRED),         # Scalability focus with L1 security
}

for name, (x, y, color) in blockchains.items():
    ax.scatter(x, y, s=200, c=color, edgecolors='black', linewidth=1.5, zorder=5)
    ax.annotate(name, (x, y), xytext=(10, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color=color)

# Add explanatory text
ax.text(0.5, 0.02, 'The Trilemma: No blockchain can fully optimize all three properties simultaneously',
        ha='center', va='bottom', fontsize=9, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

ax.set_title('The Blockchain Trilemma', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
