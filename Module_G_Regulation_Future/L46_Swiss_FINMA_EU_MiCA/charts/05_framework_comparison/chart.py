"""
Swiss FINMA vs EU MiCA Framework Comparison
Radar/spider chart showing different dimensions
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Framework Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA/charts/05_framework_comparison'
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

# Comparison dimensions
dimensions = ['Regulatory\nClarity', 'Flexibility', 'Market\nAccess', 'Stablecoin\nRules',
              'DeFi\nCoverage', 'Compliance\nCost']

# Scores (1-10)
finma_scores = [9, 8, 4, 7, 5, 6]  # Higher = better (except compliance cost where lower is better)
mica_scores = [8, 5, 9, 9, 3, 4]

x = np.arange(len(dimensions))
width = 0.35

bars1 = ax.bar(x - width/2, finma_scores, width, label='Swiss FINMA', color=MLRED, edgecolor='black')
bars2 = ax.bar(x + width/2, mica_scores, width, label='EU MiCA', color=MLBLUE, edgecolor='black')

# Add value labels
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Score (1-10, higher = better)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(dimensions, fontsize=10)
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Annotation
ax.text(0.02, 0.98, 'MiCA: EU-wide passport\nFINMA: Swiss market only',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Swiss FINMA vs EU MiCA: Framework Comparison', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
