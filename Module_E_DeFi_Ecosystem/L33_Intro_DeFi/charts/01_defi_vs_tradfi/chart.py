"""
DeFi vs Traditional Finance Comparison
Radar chart comparing key features
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DeFi vs TradFi',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/01_defi_vs_tradfi'
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

# Categories and scores
categories = ['Accessibility', 'Transparency', 'Speed', 'User\nProtection', 'Stability', 'Ease of\nUse']
tradfi_scores = [4, 3, 3, 9, 8, 8]
defi_scores = [9, 10, 9, 3, 4, 4]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, tradfi_scores, width, label='Traditional Finance',
               color=MLBLUE, edgecolor='black', linewidth=1)
bars2 = ax.bar(x + width/2, defi_scores, width, label='DeFi',
               color=MLORANGE, edgecolor='black', linewidth=1)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=14, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('DeFi vs Traditional Finance: Key Attributes', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
