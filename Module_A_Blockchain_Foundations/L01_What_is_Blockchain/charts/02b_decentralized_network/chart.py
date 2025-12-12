"""
Decentralized Network Topology
ONE figure only - shows federated hub structure
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Decentralized Network Topology',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/02b_decentralized_network'
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

# Three hub positions
hubs = [(0.25, 0.5), (0.5, 0.7), (0.75, 0.5)]

# Draw connections between hubs
for i, (hx1, hy1) in enumerate(hubs):
    for j, (hx2, hy2) in enumerate(hubs):
        if i < j:
            ax.plot([hx1, hx2], [hy1, hy2], color=MLORANGE, linewidth=3, zorder=1)

# Draw hubs and their clients
for hi, (hx, hy) in enumerate(hubs):
    # Hub node
    hub = plt.Circle((hx, hy), 0.08, color=MLORANGE, ec='black', linewidth=2, zorder=3)
    ax.add_patch(hub)
    ax.text(hx, hy, f'Hub{hi+1}', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Client nodes around each hub
    n_clients = 4
    angles = np.linspace(0, 2*np.pi, n_clients, endpoint=False) + (hi * 0.3)
    client_radius = 0.15

    for ci, angle in enumerate(angles):
        cx = hx + client_radius * np.cos(angle)
        cy = hy + client_radius * np.sin(angle)

        # Skip if outside bounds
        if 0.05 < cx < 0.95 and 0.15 < cy < 0.85:
            # Connection to hub
            ax.plot([hx, cx], [hy, cy], color='gray', linewidth=1.5, zorder=1)

            # Client node
            client = plt.Circle((cx, cy), 0.035, color=MLBLUE, ec='black', linewidth=1, zorder=2)
            ax.add_patch(client)

# Title
ax.text(0.5, 0.95, 'DECENTRALIZED', ha='center', fontsize=16, fontweight='bold', color=MLORANGE)

# Properties
ax.text(0.5, 0.05, 'Multiple hubs | Federation trust | ~10³ TPS | ~1s latency',
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
