"""
DAI Collateral Composition
Pie chart showing DAI backing assets
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DAI Collateral',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms/charts/04_dai_collateral'
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

# DAI collateral composition (Dec 2024 approximate)
collateral_types = ['USDC (PSM)', 'RWA\n(T-bills)', 'ETH', 'stETH', 'WBTC', 'Other']
percentages = [35, 25, 20, 10, 5, 5]
colors = ['#2775CA', '#4CAF50', '#627EEA', '#00A3FF', '#F7931A', '#CCCCCC']

explode = (0, 0.05, 0, 0, 0, 0)  # Highlight RWA growth

wedges, texts, autotexts = ax.pie(percentages, labels=collateral_types, colors=colors,
                                   autopct='%1.0f%%', startangle=90, explode=explode,
                                   pctdistance=0.75, labeldistance=1.1)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

# Add annotations
ax.text(1.3, 0.5, 'Centralized\ncollateral\n(60%)', fontsize=9, ha='left', color='gray',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor='gray'))
ax.text(1.3, -0.5, 'Crypto\ncollateral\n(40%)', fontsize=9, ha='left', color='gray',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor='gray'))

ax.set_title('DAI Collateral Composition (Dec 2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
