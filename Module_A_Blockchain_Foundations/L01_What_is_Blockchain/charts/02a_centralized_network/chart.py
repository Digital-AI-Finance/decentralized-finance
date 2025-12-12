"""
Centralized Network Topology
ONE figure only - shows single point of failure architecture
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Centralized Network Topology',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/02a_centralized_network'
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

# Central node (server)
central = plt.Circle((0.5, 0.5), 0.12, color=MLRED, ec='black', linewidth=2)
ax.add_patch(central)
ax.text(0.5, 0.5, 'Central\nServer', ha='center', va='center', fontsize=15, fontweight='bold', color='white')

# Outer nodes (clients)
n_nodes = 8
angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
radius = 0.35

for i, angle in enumerate(angles):
    x = 0.5 + radius * np.cos(angle)
    y = 0.5 + radius * np.sin(angle)

    # Draw connection line
    ax.plot([0.5, x], [0.5, y], color='gray', linewidth=2, zorder=1)

    # Draw node
    node = plt.Circle((x, y), 0.05, color=MLBLUE, ec='black', linewidth=1.5, zorder=2)
    ax.add_patch(node)
    ax.text(x, y, f'C{i+1}', ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# Title
ax.text(0.5, 0.95, 'CENTRALIZED', ha='center', fontsize=16, fontweight='bold', color=MLRED)

# Properties
ax.text(0.5, 0.05, 'Single point of failure | High throughput (~10⁶ TPS) | <10ms latency',
        ha='center', fontsize=14, style='italic', color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
