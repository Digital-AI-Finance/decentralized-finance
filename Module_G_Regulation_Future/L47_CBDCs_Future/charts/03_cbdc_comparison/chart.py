"""
CBDC vs Stablecoin vs Cryptocurrency Comparison
Grouped bar chart showing characteristics
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Digital Currency Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L47_CBDCs_Future/charts/03_cbdc_comparison'
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

# Characteristics (1-10 scale)
characteristics = ['Stability', 'Privacy', 'Decentralization', 'Legal Status', 'Programmability']
cbdc = [10, 4, 1, 10, 6]
stablecoin = [8, 3, 3, 4, 9]
crypto = [2, 8, 10, 2, 9]

x = np.arange(len(characteristics))
width = 0.25

bars1 = ax.bar(x - width, cbdc, width, label='CBDC', color=MLGREEN, edgecolor='black')
bars2 = ax.bar(x, stablecoin, width, label='Stablecoin', color=MLBLUE, edgecolor='black')
bars3 = ax.bar(x + width, crypto, width, label='Cryptocurrency', color=MLORANGE, edgecolor='black')

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(characteristics, fontsize=10)
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 2), textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)

ax.set_title('Digital Currency Comparison: CBDC vs Stablecoin vs Crypto', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
