"""
Blockchain Scalability Trilemma
Radar chart showing tradeoffs
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Scalability Trilemma',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L41_Layer2_Scaling/charts/01_scalability_trilemma'
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

# Trilemma properties
categories = ['Decentralization', 'Security', 'Scalability']

# Different solutions (scores 1-10)
solutions = {
    'Bitcoin/Ethereum L1': [9, 10, 2],
    'Optimistic Rollups': [7, 8, 7],
    'ZK-Rollups': [7, 9, 8],
    'Sidechains': [5, 5, 9],
}

x = np.arange(len(categories))
width = 0.18
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED]

for i, (solution, values) in enumerate(solutions.items()):
    offset = width * (i - 1.5)
    bars = ax.bar(x + offset, values, width, label=solution, color=colors[i], edgecolor='black', alpha=0.8)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.text(0.5, -0.15, 'Layer 2 solutions balance the trilemma better than pure L1 or sidechains',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('Blockchain Scalability Trilemma: Solution Comparison', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
