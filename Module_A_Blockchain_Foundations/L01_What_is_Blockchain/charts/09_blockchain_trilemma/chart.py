"""
Blockchain Trilemma Visualization
Shows the trade-off between decentralization, security, and scalability
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Blockchain Trilemma',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/09_blockchain_trilemma'
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
angles = np.array([90, 210, 330]) * np.pi / 180
r = 0.35
vertices = [(0.5 + r * np.cos(a), 0.5 + r * np.sin(a)) for a in angles]

# Draw triangle
triangle = plt.Polygon(vertices, fill=False, edgecolor=MLPURPLE, linewidth=3)
ax.add_patch(triangle)

# Fill triangle
triangle_fill = plt.Polygon(vertices, fill=True, facecolor='#E8E8FF', alpha=0.5)
ax.add_patch(triangle_fill)

# Labels at vertices
labels = ['DECENTRALIZATION', 'SECURITY', 'SCALABILITY']
label_offsets = [(0, 0.08), (-0.12, -0.05), (0.12, -0.05)]

for (x, y), label, (ox, oy) in zip(vertices, labels, label_offsets):
    ax.text(x + ox, y + oy, label, ha='center', va='center',
            fontsize=15, fontweight='bold', color=MLPURPLE)

# Position various blockchains
blockchains = [
    ('Bitcoin', 0.5, 0.68, MLORANGE, '~7 TPS'),
    ('Visa', 0.70, 0.32, 'gray', '~65K TPS'),
    ('Solana', 0.55, 0.38, MLGREEN, '~65K TPS'),
    ('Ethereum L2', 0.42, 0.45, MLBLUE, '~4K TPS'),
]

for name, x, y, color, desc in blockchains:
    ax.scatter(x, y, s=250, color=color, edgecolor='black', linewidth=2, zorder=5)
    ax.text(x, y - 0.07, f'{name}', ha='center', va='top', fontsize=15, fontweight='bold')
    ax.text(x, y - 0.12, desc, ha='center', va='top', fontsize=14, color='gray')

# Title
ax.text(0.5, 0.95, 'The Blockchain Trilemma', ha='center', fontsize=14, fontweight='bold', color=MLPURPLE)
ax.text(0.5, 0.90, 'Pick any two (traditionally)', ha='center', fontsize=14, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
