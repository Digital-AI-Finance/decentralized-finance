"""NFT Valuation Factors - Key factors influencing NFT value"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

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

# Valuation factors with importance scores
factors = [
    'Rarity\n(Traits)',
    'Team\nCredibility',
    'Community\nSize',
    'Utility\nValue',
    'Trading\nVolume',
    'Floor Price\nTrend',
    'Holder\nDistribution',
    'Roadmap\nDelivery'
]

importance = [9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5]
colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE, MLBLUE, MLGREEN]

# Create spider/radar chart
angles = np.linspace(0, 2 * np.pi, len(factors), endpoint=False).tolist()
importance_plot = importance + [importance[0]]
angles += angles[:1]

ax = plt.subplot(111, projection='polar')
ax.plot(angles, importance_plot, 'o-', linewidth=2, color=MLPURPLE, markersize=8)
ax.fill(angles, importance_plot, alpha=0.25, color=MLPURPLE)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(factors, fontsize=12)
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10, color='gray')
ax.set_title('NFT Valuation Factors\n(Importance Score 1-10)', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
