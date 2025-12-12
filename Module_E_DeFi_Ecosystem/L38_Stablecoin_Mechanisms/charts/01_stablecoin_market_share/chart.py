"""
Stablecoin Market Share
Pie chart showing major stablecoins by market cap
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Stablecoin Market Share',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms/charts/01_stablecoin_market_share'
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

fig, ax = plt.subplots(figsize=(10, 6))

# Stablecoin market share (Dec 2024)
stablecoins = ['USDT', 'USDC', 'DAI', 'FDUSD', 'USDE', 'Other']
market_caps = [90, 35, 5, 4, 3, 3]  # Billions USD
colors = ['#26A17B', '#2775CA', '#F5AC37', '#F0B90B', '#000000', '#CCCCCC']

explode = (0.03, 0, 0, 0, 0, 0)

wedges, texts, autotexts = ax.pie(market_caps, labels=stablecoins, colors=colors,
                                   autopct='%1.0f%%', startangle=90, explode=explode,
                                   pctdistance=0.7, labeldistance=1.1)

for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
    autotext.set_color('white')

# Add total
ax.text(0, 0, f'Total\n$140B', ha='center', va='center', fontsize=15, fontweight='bold')

# Add legend with type
legend_labels = ['USDT - Fiat-backed', 'USDC - Fiat-backed', 'DAI - Crypto-backed',
                 'FDUSD - Fiat-backed', 'USDE - Hybrid', 'Other']
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=14)

ax.set_title('Stablecoin Market Share (Dec 2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
