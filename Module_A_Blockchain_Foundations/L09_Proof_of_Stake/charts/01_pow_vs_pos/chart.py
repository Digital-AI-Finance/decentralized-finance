"""
Proof of Work vs Proof of Stake Comparison
Side-by-side comparison of key properties
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'PoW vs PoS Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/01_pow_vs_pos'
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

# Categories and values
categories = ['Energy Use', 'Hardware Need', 'Entry Barrier', 'Finality Speed', 'Decentralization']
pow_scores = [95, 85, 70, 30, 60]  # Higher = more (for PoW)
pos_scores = [5, 15, 80, 85, 50]   # Higher = more (for PoS)

y_positions = np.arange(len(categories))
bar_height = 0.35

# Create horizontal bars
bars_pow = ax.barh(y_positions - bar_height/2, pow_scores, bar_height,
                   label='Proof of Work', color=MLORANGE, edgecolor='black', linewidth=1)
bars_pos = ax.barh(y_positions + bar_height/2, pos_scores, bar_height,
                   label='Proof of Stake', color=MLGREEN, edgecolor='black', linewidth=1)

# Labels
ax.set_yticks(y_positions)
ax.set_yticklabels(categories)
ax.set_xlabel('Relative Score', fontsize=16)
ax.set_xlim(0, 110)

# Add value labels
for bar, score in zip(bars_pow, pow_scores):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            f'{score}', va='center', fontsize=14)

for bar, score in zip(bars_pos, pos_scores):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            f'{score}', va='center', fontsize=14)

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F4E8', edgecolor=MLGREEN)
ax.text(55, 4.5, 'PoS: ~99.95% less energy', fontsize=14, fontweight='bold',
        bbox=props, color='#333')

ax.legend(loc='upper right', fontsize=14)

ax.set_title('Proof of Work vs Proof of Stake: Key Metrics', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
