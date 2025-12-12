"""
Scalability Trilemma Triangle
Shows the three competing properties
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Trilemma Triangle',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/01_trilemma_triangle'
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
top = (0.5, 0.9)
left = (0.1, 0.15)
right = (0.9, 0.15)

# Draw triangle
triangle = Polygon([top, left, right], closed=True, fill=False,
                   edgecolor='#333', linewidth=3)
ax.add_patch(triangle)

# Fill with gradient-like pattern
inner_triangle = Polygon([top, left, right], closed=True,
                        facecolor='#F0F8FF', edgecolor='none', alpha=0.5)
ax.add_patch(inner_triangle)

# Vertex labels with boxes
vertices = [
    (top[0], top[1] + 0.08, 'DECENTRALIZATION', MLGREEN,
     'No single point of control\nCensorship resistant'),
    (left[0] - 0.05, left[1] - 0.02, 'SECURITY', MLBLUE,
     'Attack resistant\nImmutable data'),
    (right[0] + 0.05, right[1] - 0.02, 'SCALABILITY', MLORANGE,
     'High throughput\nLow latency'),
]

for x, y, label, color, desc in vertices:
    props = dict(boxstyle='round,pad=0.4', facecolor=color, edgecolor='black', alpha=0.9)
    ax.text(x, y, label, ha='center', va='center', fontsize=16,
            fontweight='bold', color='white', bbox=props)

# Descriptions below/beside labels
ax.text(0.5, 0.78, 'No single point of control\nCensorship resistant',
        ha='center', fontsize=14, color='#555')
ax.text(0.02, 0.25, 'Attack resistant\nImmutable data',
        ha='left', fontsize=14, color='#555')
ax.text(0.98, 0.25, 'High throughput\nLow latency',
        ha='right', fontsize=14, color='#555')

# Edge labels
ax.text(0.26, 0.55, 'Bitcoin', ha='center', fontsize=14, fontweight='bold',
        rotation=58, color=MLBLUE)
ax.text(0.74, 0.55, 'EOS', ha='center', fontsize=14, fontweight='bold',
        rotation=-58, color=MLORANGE)
ax.text(0.50, 0.12, 'Centralized DB', ha='center', fontsize=14, fontweight='bold',
        color=MLPURPLE)

# Central question mark
ax.text(0.5, 0.42, '?', ha='center', va='center', fontsize=50,
        fontweight='bold', color='#888', alpha=0.5)
ax.text(0.5, 0.30, 'Can we have all three?', ha='center', fontsize=14,
        color='#555', style='italic')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('The Blockchain Scalability Trilemma', fontweight='bold', fontsize=16, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
