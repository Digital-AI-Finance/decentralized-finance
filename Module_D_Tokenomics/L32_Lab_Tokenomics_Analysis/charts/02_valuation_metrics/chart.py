"""Key Tokenomics Valuation Metrics"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

metrics = ['Market Cap', 'FDV', 'FDV/MC\nRatio', 'NVT\nRatio', 'Inflation\nRate']
importance = [95, 90, 85, 75, 70]
colors = [MLBLUE, MLBLUE, MLORANGE, MLGREEN, MLRED]

bars = ax.barh(metrics, importance, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

for bar, val in zip(bars, importance):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{val}%', ha='left', va='center', fontsize=11, fontweight='bold')

ax.axvline(x=80, color='gray', linestyle='--', alpha=0.5)
ax.text(81, 4.5, 'Essential', fontsize=9, color='gray')

ax.set_xlabel('Importance in Analysis (%)', fontsize=12)
ax.set_xlim(0, 105)
ax.grid(True, alpha=0.3, axis='x')
ax.set_title('Key Tokenomics Metrics to Calculate', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
