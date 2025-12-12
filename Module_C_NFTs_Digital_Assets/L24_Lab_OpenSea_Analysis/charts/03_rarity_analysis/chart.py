"""NFT Rarity Factors"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

factors = ['Trait Rarity', 'Statistical\nRarity', '1/1 Art', 'Provenance', 'Utility']
weights = [30, 25, 20, 15, 10]
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]

bars = ax.bar(factors, weights, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

for bar, val in zip(bars, weights):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{val}%', ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Weight in Rarity Score (%)', fontsize=15)
ax.set_ylim(0, 40)
ax.grid(True, alpha=0.3, axis='y')
ax.set_title('NFT Rarity Score Components', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
