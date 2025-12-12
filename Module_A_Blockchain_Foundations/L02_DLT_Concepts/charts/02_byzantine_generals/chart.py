"""
Byzantine Generals Problem Visualization
Shows the communication challenge with a traitor sending conflicting messages
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Byzantine Generals Problem',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/02_byzantine_generals'
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

# General positions (square arrangement)
positions = {
    'A': (0.25, 0.75),  # Commander - top left
    'B': (0.75, 0.75),  # Loyal - top right
    'C': (0.25, 0.25),  # Loyal - bottom left
    'D': (0.75, 0.25),  # Traitor - bottom right
}

# Draw generals
general_radius = 0.08
for gen, (x, y) in positions.items():
    if gen == 'D':  # Traitor
        color = MLRED
        label = f'General {gen}\n(Traitor)'
    elif gen == 'A':  # Commander
        color = MLBLUE
        label = f'Commander {gen}\n(Loyal)'
    else:  # Loyal generals
        color = MLGREEN
        label = f'General {gen}\n(Loyal)'

    circle = Circle((x, y), general_radius, facecolor=color, edgecolor='black',
                    linewidth=2, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, y, gen, ha='center', va='center', fontsize=18, fontweight='bold', color='white')

    # Label below
    label_y = y - 0.14 if y > 0.5 else y + 0.14
    ax.text(x, label_y, label, ha='center', va='center', fontsize=14, color='#333')

# Draw arrows with messages
# Commander A sends "ATTACK" to all
arrows = [
    ('A', 'B', 'ATTACK', MLGREEN, 0.02),
    ('A', 'C', 'ATTACK', MLGREEN, 0.02),
    ('A', 'D', 'ATTACK', MLGREEN, -0.02),
]

for src, dst, msg, color, offset in arrows:
    x1, y1 = positions[src]
    x2, y2 = positions[dst]

    # Adjust for circle radius
    dx, dy = x2 - x1, y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    dx, dy = dx/dist, dy/dist

    x1 += dx * general_radius
    y1 += dy * general_radius
    x2 -= dx * general_radius
    y2 -= dy * general_radius

    ax.annotate('', xy=(x2, y2 + offset), xytext=(x1, y1 + offset),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5))

    mid_x, mid_y = (x1 + x2) / 2 + offset, (y1 + y2) / 2 + 0.04
    ax.text(mid_x, mid_y, f'"{msg}"', ha='center', va='center',
            fontsize=15, color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.9))

# Traitor D sends conflicting messages
traitor_arrows = [
    ('D', 'B', '"A said RETREAT"', MLRED, 0.03),
    ('D', 'C', '"A said ATTACK"', MLORANGE, -0.03),
]

for src, dst, msg, color, offset in traitor_arrows:
    x1, y1 = positions[src]
    x2, y2 = positions[dst]

    dx, dy = x2 - x1, y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    dx, dy = dx/dist, dy/dist

    x1 += dx * general_radius
    y1 += dy * general_radius
    x2 -= dx * general_radius
    y2 -= dy * general_radius

    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2, linestyle='--'))

    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2 + offset
    ax.text(mid_x, mid_y, msg, ha='center', va='center',
            fontsize=14, color=color, fontweight='bold', style='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF0F0', edgecolor=color, alpha=0.9))

# Legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLBLUE, markersize=12, label='Commander'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLGREEN, markersize=12, label='Loyal General'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=MLRED, markersize=12, label='Traitor'),
]
ax.legend(handles=legend_elements, loc='upper center', ncol=3, fontsize=14,
          framealpha=0.9, bbox_to_anchor=(0.5, 1.02))

# Problem statement
ax.text(0.5, 0.02, 'Problem: How can loyal generals reach consensus when traitors send conflicting messages?',
        ha='center', va='center', fontsize=15, style='italic', color=MLPURPLE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLPURPLE))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('The Byzantine Generals Problem', fontweight='bold', fontsize=16, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
