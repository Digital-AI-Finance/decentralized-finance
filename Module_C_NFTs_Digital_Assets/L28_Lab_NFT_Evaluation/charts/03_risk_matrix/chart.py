"""NFT Investment Risk Matrix"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

risks = ['Liquidity\nRisk', 'Smart Contract\nRisk', 'Market\nVolatility', 'Rug Pull\nRisk', 'Platform\nRisk']
scores = [8, 7, 9, 6, 5]
colors = [MLRED if s >= 7 else MLORANGE if s >= 5 else MLGREEN for s in scores]

bars = ax.barh(risks, scores, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

for bar, val in zip(bars, scores):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{val}/10', ha='left', va='center', fontsize=14, fontweight='bold')

ax.axvline(x=7, color=MLRED, linestyle='--', alpha=0.5, linewidth=2)
ax.text(7.1, 4.5, 'High Risk', fontsize=14, color=MLRED)

ax.set_xlabel('Risk Level (1-10)', fontsize=15)
ax.set_xlim(0, 11)
ax.grid(True, alpha=0.3, axis='x')
ax.set_title('NFT Investment Risk Assessment', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
