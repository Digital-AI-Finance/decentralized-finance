"""
Network Topologies Comparison
Shows centralized, decentralized, and distributed network architectures side-by-side
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Network Topologies Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/03_network_topologies'
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

def draw_centralized(ax):
    """Draw centralized network - hub and spoke"""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Central hub
    hub = Circle((0.5, 0.5), 0.12, facecolor=MLRED, edgecolor='black', linewidth=2)
    ax.add_patch(hub)
    ax.text(0.5, 0.5, 'Hub', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Outer nodes
    n_nodes = 8
    radius = 0.32
    for i in range(n_nodes):
        angle = 2 * np.pi * i / n_nodes - np.pi/2
        x = 0.5 + radius * np.cos(angle)
        y = 0.5 + radius * np.sin(angle)

        # Connection to hub
        ax.plot([0.5, x], [0.5, y], color='gray', linewidth=1.5, zorder=1)

        # Node
        node = Circle((x, y), 0.05, facecolor=MLBLUE, edgecolor='black', linewidth=1.5, zorder=2)
        ax.add_patch(node)

    ax.set_title('CENTRALIZED', fontsize=14, fontweight='bold', color=MLRED, pad=10)
    ax.text(0.5, 0.08, 'Single point of failure', ha='center', fontsize=14, color='gray', style='italic')

def draw_decentralized(ax):
    """Draw decentralized network - multiple hubs"""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Three hub positions
    hubs = [(0.25, 0.65), (0.75, 0.65), (0.5, 0.3)]

    # Draw connections between hubs
    for i, (x1, y1) in enumerate(hubs):
        for x2, y2 in hubs[i+1:]:
            ax.plot([x1, x2], [y1, y2], color=MLORANGE, linewidth=2.5, zorder=1)

    # Draw each hub cluster
    for hx, hy in hubs:
        # Hub node
        hub = Circle((hx, hy), 0.08, facecolor=MLORANGE, edgecolor='black', linewidth=2, zorder=3)
        ax.add_patch(hub)

        # Satellite nodes
        n_satellites = 3
        sat_radius = 0.15
        start_angle = np.random.uniform(0, np.pi/3)
        for i in range(n_satellites):
            angle = start_angle + 2 * np.pi * i / n_satellites
            x = hx + sat_radius * np.cos(angle)
            y = hy + sat_radius * np.sin(angle)

            # Clamp to boundaries
            x = max(0.08, min(0.92, x))
            y = max(0.15, min(0.92, y))

            ax.plot([hx, x], [hy, y], color='gray', linewidth=1, zorder=1)
            node = Circle((x, y), 0.04, facecolor=MLBLUE, edgecolor='black', linewidth=1, zorder=2)
            ax.add_patch(node)

    ax.set_title('DECENTRALIZED', fontsize=14, fontweight='bold', color=MLORANGE, pad=10)
    ax.text(0.5, 0.08, 'Multiple hubs, federated', ha='center', fontsize=14, color='gray', style='italic')

def draw_distributed(ax):
    """Draw distributed network - P2P mesh"""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Random but reproducible node positions
    np.random.seed(42)
    n_nodes = 12
    nodes = []
    for _ in range(n_nodes):
        x = 0.15 + 0.7 * np.random.random()
        y = 0.15 + 0.7 * np.random.random()
        nodes.append((x, y))

    # Draw connections (each node connects to nearby nodes)
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes[i+1:], i+1):
            dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            if dist < 0.35:  # Only connect nearby nodes
                ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1, alpha=0.6, zorder=1)

    # Draw nodes
    for x, y in nodes:
        node = Circle((x, y), 0.04, facecolor=MLGREEN, edgecolor='black', linewidth=1.5, zorder=2)
        ax.add_patch(node)

    ax.set_title('DISTRIBUTED', fontsize=14, fontweight='bold', color=MLGREEN, pad=10)
    ax.text(0.5, 0.08, 'P2P, no central authority', ha='center', fontsize=14, color='gray', style='italic')

# Draw all three topologies
draw_centralized(axes[0])
draw_decentralized(axes[1])
draw_distributed(axes[2])

plt.suptitle('Network Topologies', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
