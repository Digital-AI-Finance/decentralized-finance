"""
MEV Extraction Methods
Pie chart showing MEV types
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'MEV Extraction',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L42_Flash_Loans/charts/04_mev_extraction'
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

# MEV extraction methods (approximate 2023 breakdown)
methods = ['DEX Arbitrage', 'Liquidations', 'Sandwich\nAttacks', 'Other']
percentages = [45, 30, 20, 5]
colors = [MLGREEN, MLBLUE, MLRED, '#CCCCCC']

explode = (0.05, 0, 0.05, 0)  # Highlight arbitrage and sandwich

wedges, texts, autotexts = ax.pie(percentages, labels=methods, colors=colors,
                                   autopct='%1.0f%%', startangle=90, explode=explode,
                                   pctdistance=0.75, labeldistance=1.15)

for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Annotations
ax.text(1.3, 0.5, 'Profitable\n(legitimate)', fontsize=9, ha='left', color=MLGREEN,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN))
ax.text(1.3, -0.5, 'Harmful\n(front-running)', fontsize=9, ha='left', color=MLRED,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('MEV Extraction Methods (2023)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
