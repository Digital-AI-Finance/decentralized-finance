"""NFT Risk Assessment Matrix - Risk categories and levels"""
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

# Risk categories
categories = ['Liquidity\nRisk', 'Smart Contract\nRisk', 'Market\nRisk',
              'Rug Pull\nRisk', 'Platform\nRisk']

# Example risk scores for three NFT projects
project_a = [3, 2, 5, 2, 3]  # Low risk blue-chip
project_b = [6, 5, 7, 5, 6]  # Medium risk
project_c = [9, 8, 8, 9, 7]  # High risk

x = np.arange(len(categories))
width = 0.25

bars1 = ax.bar(x - width, project_a, width, label='Blue-Chip Project (Low Risk)',
               color=MLGREEN, alpha=0.8)
bars2 = ax.bar(x, project_b, width, label='Emerging Project (Medium Risk)',
               color=MLORANGE, alpha=0.8)
bars3 = ax.bar(x + width, project_c, width, label='New Project (High Risk)',
               color=MLRED, alpha=0.8)

# Risk zones
ax.axhspan(0, 4, alpha=0.1, color=MLGREEN, label='Low Risk Zone')
ax.axhspan(4, 7, alpha=0.1, color=MLORANGE, label='Medium Risk Zone')
ax.axhspan(7, 10, alpha=0.1, color=MLRED, label='High Risk Zone')

ax.set_xlabel('Risk Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Risk Score (1-10)', fontsize=14, fontweight='bold')
ax.set_title('NFT Investment Risk Assessment Matrix', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=15)
ax.set_ylim(0, 10)
ax.legend(loc='upper left', fontsize=14)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
