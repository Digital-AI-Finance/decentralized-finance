"""
Top DeFi Protocols by TVL
Horizontal bar chart showing major protocols
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Protocol TVL',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/04_protocol_tvl'
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

# Top protocols by TVL (Dec 2024 approximate)
protocols = ['Lido', 'EigenLayer', 'Aave', 'MakerDAO', 'Spark', 'Uniswap', 'Ethena', 'Rocket Pool']
tvl = [25, 15, 12, 8, 5, 5, 4, 3]  # Billions USD
categories = ['Liquid Staking', 'Restaking', 'Lending', 'Stablecoin', 'Lending', 'DEX', 'Stablecoin', 'Liquid Staking']

# Color by category
category_colors = {
    'Liquid Staking': MLBLUE,
    'Restaking': MLPURPLE,
    'Lending': MLGREEN,
    'Stablecoin': MLORANGE,
    'DEX': MLRED
}

colors = [category_colors[cat] for cat in categories]

y_pos = np.arange(len(protocols))
bars = ax.barh(y_pos, tvl, color=colors, edgecolor='black', linewidth=1)

# Add value labels
for bar, val, cat in zip(bars, tvl, categories):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            f'${val}B', va='center', fontsize=14, fontweight='bold')
    ax.text(bar.get_width() - 0.3, bar.get_y() + bar.get_height()/2,
            cat, va='center', ha='right', fontsize=14, color='white')

ax.set_yticks(y_pos)
ax.set_yticklabels(protocols, fontsize=14, fontweight='bold')
ax.set_xlabel('Total Value Locked (Billion USD)', fontsize=15)
ax.set_xlim(0, 30)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

ax.set_title('Top DeFi Protocols by TVL (December 2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
