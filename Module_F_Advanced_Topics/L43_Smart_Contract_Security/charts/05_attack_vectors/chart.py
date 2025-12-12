"""
Attack Vectors by Loss Amount (2020-2024)
Pie chart showing attack categories
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Attack Vectors',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L43_Smart_Contract_Security/charts/05_attack_vectors'
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

# Attack vectors by total losses (2020-2024)
vectors = ['Bridge\nExploits', 'Access\nControl', 'Flash Loan\n/Oracle', 'Reentrancy', 'Other']
percentages = [35, 25, 20, 10, 10]
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN, '#CCCCCC']

explode = (0.05, 0, 0, 0, 0)  # Highlight bridges

wedges, texts, autotexts = ax.pie(percentages, labels=vectors, colors=colors,
                                   autopct='%1.0f%%', startangle=90, explode=explode,
                                   pctdistance=0.75, labeldistance=1.15)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Annotations
ax.text(1.3, 0.3, 'Bridge exploits\nare largest\ncategory (~$2.5B)', fontsize=14, ha='left', color=MLRED,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('DeFi Attack Vectors by Total Losses (2020-2024)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
