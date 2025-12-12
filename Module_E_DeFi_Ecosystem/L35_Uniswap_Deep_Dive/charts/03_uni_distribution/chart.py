"""
UNI Token Distribution
Pie chart showing allocation breakdown
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'UNI Distribution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive/charts/03_uni_distribution'
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

# UNI token distribution
categories = ['Community Treasury', 'Team', 'Investors', 'Advisors', 'Community Airdrop']
percentages = [43, 21.5, 17.8, 0.7, 15]
colors = [MLGREEN, MLBLUE, MLORANGE, MLPURPLE, '#81C784']

explode = (0.02, 0, 0, 0, 0.05)

wedges, texts, autotexts = ax.pie(percentages, labels=categories, colors=colors,
                                   autopct='%1.1f%%', startangle=90, explode=explode,
                                   pctdistance=0.6, labeldistance=1.15)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

# Add detail annotations
ax.text(1.4, 0.3, 'Team/Investors:\n4-year vesting', fontsize=9, ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))
ax.text(1.4, -0.3, 'Airdrop:\n400 UNI per user', fontsize=9, ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('UNI Token Distribution (1 Billion Total)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
