"""NFT Collection Metrics"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

metrics = ['Floor Price', 'Volume (24h)', 'Unique\nOwners', 'Listed\nRatio', 'Avg Sale\nPrice']
importance = [9, 8, 7, 6, 8]
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLBLUE]

bars = ax.barh(metrics, importance, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

for bar, val in zip(bars, importance):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{val}/10', ha='left', va='center', fontsize=14, fontweight='bold')

ax.set_xlabel('Importance for Analysis', fontsize=15)
ax.set_xlim(0, 11)
ax.grid(True, alpha=0.3, axis='x')
ax.set_title('Key NFT Collection Metrics', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
