"""
Mining Pool Distribution
Shows market share of top pools
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Mining Pool Distribution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/05_mining_pools'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Mining pool data (approximate 2024 distribution)
pools = ['Foundry USA', 'AntPool', 'F2Pool', 'ViaBTC', 'Binance Pool', 'Others']
shares = [30, 20, 15, 12, 8, 15]
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLRED, MLLAVENDER]

# Pie chart with explode for emphasis
explode = (0.05, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(shares, labels=pools, autopct='%1.1f%%',
                                   colors=colors, explode=explode,
                                   shadow=True, startangle=90,
                                   textprops={'fontsize': 11})

# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

# Add centralization warning
ax.text(0, -1.35, 'Top 5 pools control ~85% of hash rate',
        ha='center', fontsize=12, fontweight='bold', color=MLRED)
ax.text(0, -1.50, '(Miners can switch pools - pools do not own hardware)',
        ha='center', fontsize=10, color='#555', style='italic')

ax.set_title('Bitcoin Mining Pool Distribution (2024)', fontweight='bold', fontsize=15, pad=20)

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
