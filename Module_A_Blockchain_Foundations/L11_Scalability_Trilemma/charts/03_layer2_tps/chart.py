"""
Layer 2 Throughput Comparison
Shows L2 solutions vs L1 throughput
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Layer 2 TPS',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/03_layer2_tps'
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

# Data: solution, TPS, type
solutions = [
    ('Ethereum L1', 30, 'L1', MLBLUE),
    ('Arbitrum', 4000, 'Optimistic', MLGREEN),
    ('Optimism', 2000, 'Optimistic', MLGREEN),
    ('zkSync', 2000, 'ZK Rollup', MLORANGE),
    ('StarkNet', 10000, 'ZK Rollup', MLORANGE),
    ('Polygon PoS', 7000, 'Sidechain', MLPURPLE),
    ('Lightning', 1000000, 'Channels', MLRED),
]

names = [s[0] for s in solutions]
tps = [s[1] for s in solutions]
colors = [s[3] for s in solutions]

bars = ax.barh(names, tps, color=colors, edgecolor='black', linewidth=0.5)

ax.set_xscale('log')
ax.set_xlim(10, 2000000)

# Add TPS labels
for bar, t in zip(bars, tps):
    width = bar.get_width()
    label = f'{t:,}' if t < 1000000 else '1M+'
    ax.text(width * 1.5, bar.get_y() + bar.get_height()/2,
            f'{label} TPS', va='center', fontsize=14, fontweight='bold')

# Improvement annotation
ax.annotate('', xy=(4000, 1), xytext=(30, 1),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(100, 0.5, '100x+', fontsize=14, fontweight='bold', color=MLGREEN)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, edgecolor='black', label='Layer 1'),
    Patch(facecolor=MLGREEN, edgecolor='black', label='Optimistic Rollup'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='ZK Rollup'),
    Patch(facecolor=MLPURPLE, edgecolor='black', label='Sidechain'),
    Patch(facecolor=MLRED, edgecolor='black', label='Payment Channels'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=14)

ax.set_xlabel('Transactions Per Second (log scale)', fontsize=16)
ax.set_title('Layer 2 Scaling: 100-10,000x Improvement over L1', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
