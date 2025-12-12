"""
Distributed Network Topology (Blockchain)
ONE figure only - shows peer-to-peer mesh network
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Distributed Network Topology',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/02c_distributed_network'
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

# Generate node positions in a distributed pattern
np.random.seed(42)
n_nodes = 12

# Use a combination of random and structured placement
positions = []
for i in range(n_nodes):
    angle = 2 * np.pi * i / n_nodes
    r = 0.25 + 0.1 * np.random.random()
    x = 0.5 + r * np.cos(angle)
    y = 0.5 + r * np.sin(angle)
    positions.append((x, y))

# Draw connections (partial mesh - each node connects to 3-4 nearest neighbors)
for i, (x1, y1) in enumerate(positions):
    distances = []
    for j, (x2, y2) in enumerate(positions):
        if i != j:
            dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            distances.append((dist, j))
    distances.sort()

    # Connect to 3-4 nearest neighbors
    for dist, j in distances[:4]:
        x2, y2 = positions[j]
        ax.plot([x1, x2], [y1, y2], color=MLGREEN, linewidth=1.5, alpha=0.6, zorder=1)

# Draw nodes (all equal - no hierarchy)
for i, (x, y) in enumerate(positions):
    node = plt.Circle((x, y), 0.045, color=MLGREEN, ec='black', linewidth=1.5, zorder=2)
    ax.add_patch(node)
    ax.text(x, y, f'N{i+1}', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Title
ax.text(0.5, 0.95, 'DISTRIBUTED (Blockchain)', ha='center', fontsize=16, fontweight='bold', color=MLGREEN)

# Properties
ax.text(0.5, 0.05, 'No single point of failure | Cryptographic trust | ~10 TPS | ~10 min finality',
        ha='center', fontsize=14, style='italic', color='gray')

# Highlight key property
ax.text(0.5, 0.12, 'All nodes are equal peers', ha='center', fontsize=14, fontweight='bold', color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
