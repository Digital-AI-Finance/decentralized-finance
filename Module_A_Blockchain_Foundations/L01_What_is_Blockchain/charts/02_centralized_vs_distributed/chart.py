"""
Network Topology Comparison: Centralized vs Decentralized vs Distributed
Visual comparison for MSc-level understanding
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Network Topology Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/02_centralized_vs_distributed'
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

fig, axes = plt.subplots(1, 3, figsize=(10, 5))

def draw_node(ax, x, y, color, size=300, central=False):
    if central:
        ax.scatter(x, y, s=size*1.5, c=color, zorder=3, edgecolors='black', linewidths=2)
    else:
        ax.scatter(x, y, s=size, c=color, zorder=3, edgecolors='black', linewidths=1)

def draw_edge(ax, x1, y1, x2, y2, color='gray', width=1):
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=width, zorder=1)

# 1. Centralized Network
ax1 = axes[0]
ax1.set_title('Centralized', fontweight='bold', fontsize=14)

# Central node
draw_node(ax1, 0.5, 0.5, MLPURPLE, central=True)

# Peripheral nodes
angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
for angle in angles:
    x = 0.5 + 0.35 * np.cos(angle)
    y = 0.5 + 0.35 * np.sin(angle)
    draw_edge(ax1, 0.5, 0.5, x, y, MLPURPLE, 1.5)
    draw_node(ax1, x, y, MLBLUE)

ax1.text(0.5, 0.05, 'Single point of failure\nBank, AWS, Facebook', ha='center', fontsize=14, style='italic')

# 2. Decentralized Network
ax2 = axes[1]
ax2.set_title('Decentralized', fontweight='bold', fontsize=14)

# Multiple hubs
hubs = [(0.3, 0.7), (0.7, 0.7), (0.5, 0.35)]
for hx, hy in hubs:
    draw_node(ax2, hx, hy, MLORANGE, central=True)

# Connect hubs
draw_edge(ax2, 0.3, 0.7, 0.7, 0.7, MLORANGE, 2)
draw_edge(ax2, 0.3, 0.7, 0.5, 0.35, MLORANGE, 2)
draw_edge(ax2, 0.7, 0.7, 0.5, 0.35, MLORANGE, 2)

# Peripheral nodes around each hub
for hx, hy in hubs:
    for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
        x = hx + 0.12 * np.cos(angle)
        y = hy + 0.12 * np.sin(angle)
        if 0.1 < x < 0.9 and 0.15 < y < 0.9:
            draw_edge(ax2, hx, hy, x, y, 'gray', 1)
            draw_node(ax2, x, y, MLBLUE, size=150)

ax2.text(0.5, 0.05, 'Multiple hubs\nFederated systems', ha='center', fontsize=14, style='italic')

# 3. Distributed Network (P2P)
ax3 = axes[2]
ax3.set_title('Distributed (P2P)', fontweight='bold', fontsize=14)

# Random mesh of nodes
np.random.seed(42)
n_nodes = 12
positions = []
for i in range(n_nodes):
    x = 0.15 + 0.7 * np.random.random()
    y = 0.2 + 0.65 * np.random.random()
    positions.append((x, y))

# Draw edges (connect nearby nodes)
for i, (x1, y1) in enumerate(positions):
    for j, (x2, y2) in enumerate(positions):
        if i < j:
            dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            if dist < 0.35:
                draw_edge(ax3, x1, y1, x2, y2, MLGREEN, 1)

# Draw nodes
for x, y in positions:
    draw_node(ax3, x, y, MLGREEN)

ax3.text(0.5, 0.05, 'No central authority\nBitcoin, IPFS, Tor', ha='center', fontsize=14, style='italic')

# Configure all axes
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

plt.suptitle('Network Architecture Comparison', fontweight='bold', fontsize=15, y=0.98)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
