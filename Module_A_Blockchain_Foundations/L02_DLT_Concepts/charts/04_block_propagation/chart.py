"""
Block Propagation via Gossip Protocol
Shows how a new block spreads through the network
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Block Propagation via Gossip Protocol',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/04_block_propagation'
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

# Timeline stages
stages = ['t=0\nMiner finds block', 't=1\nDirect peers', 't=2\nPeers of peers', 't=3\nFull network']
stage_x = [0.12, 0.35, 0.60, 0.88]

# Draw timeline
ax.plot([0.05, 0.95], [0.92, 0.92], color='gray', linewidth=2, zorder=1)
for i, (x, label) in enumerate(zip(stage_x, stages)):
    ax.plot(x, 0.92, 'o', markersize=12, color=MLPURPLE, zorder=2)
    ax.text(x, 0.97, label, ha='center', va='bottom', fontsize=14, color=MLPURPLE)

# Stage 0: Miner finds block
ax.add_patch(Circle((0.12, 0.6), 0.06, facecolor=MLGREEN, edgecolor='black', linewidth=2))
ax.text(0.12, 0.6, 'M', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.12, 0.48, 'Miner', ha='center', fontsize=14, color='#444')

# Stage 1: Direct peers (3 nodes)
peers1_y = [0.7, 0.6, 0.5]
for i, y in enumerate(peers1_y):
    ax.add_patch(Circle((0.35, y), 0.04, facecolor=MLORANGE, edgecolor='black', linewidth=1.5))
    ax.annotate('', xy=(0.31, y), xytext=(0.18, 0.6),
                arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5))

# Stage 2: Peers of peers (6 nodes)
peers2_positions = [(0.60, 0.78), (0.60, 0.68), (0.60, 0.58), (0.60, 0.48), (0.60, 0.38)]
for x, y in peers2_positions:
    ax.add_patch(Circle((x, y), 0.035, facecolor=MLBLUE, edgecolor='black', linewidth=1.5))

# Draw arrows from stage 1 to stage 2
for i, src_y in enumerate(peers1_y):
    for j, (dx, dy) in enumerate(peers2_positions):
        if abs(src_y - dy) < 0.15:
            ax.annotate('', xy=(0.565, dy), xytext=(0.39, src_y),
                        arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=1, alpha=0.6))

# Stage 3: Full network (many nodes)
np.random.seed(123)
n_final = 12
for i in range(n_final):
    angle = 2 * np.pi * i / n_final
    r = 0.12 + 0.05 * np.random.random()
    x = 0.88 + r * np.cos(angle) * 0.4
    y = 0.58 + r * np.sin(angle) * 0.8
    x = max(0.76, min(0.98, x))
    y = max(0.25, min(0.85, y))
    ax.add_patch(Circle((x, y), 0.025, facecolor=MLLAVENDER, edgecolor=MLPURPLE, linewidth=1))

# Arrows from stage 2 to stage 3
ax.annotate('', xy=(0.76, 0.58), xytext=(0.64, 0.58),
            arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=2))

# Legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLGREEN, markersize=10, label='Miner (source)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLORANGE, markersize=10, label='Direct peers'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLBLUE, markersize=10, label='2nd hop peers'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLLAVENDER, markersize=10, label='Full network'),
]
ax.legend(handles=legend_elements, loc='lower center', ncol=4, fontsize=14,
          framealpha=0.9, bbox_to_anchor=(0.5, -0.02))

# Stats box
stats_text = 'Bitcoin: ~6-12 sec to reach 95% of network\nEthereum: ~2-6 sec propagation time'
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=MLPURPLE, alpha=0.9)
ax.text(0.5, 0.18, stats_text, ha='center', va='center', fontsize=14,
        bbox=props, color='#333')

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 1.02)
ax.axis('off')

plt.title('Block Propagation: Gossip Protocol', fontweight='bold', fontsize=16, pad=5)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
