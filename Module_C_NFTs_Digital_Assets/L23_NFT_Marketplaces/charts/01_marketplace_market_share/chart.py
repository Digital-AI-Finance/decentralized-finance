"""
NFT Marketplace Market Share (2024)
Pie chart showing trading volume distribution
"""

import matplotlib.pyplot as plt
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Marketplace Market Share',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces/charts/01_marketplace_market_share'
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

# Market share by trading volume (2024 estimates)
labels = ['Blur', 'OpenSea', 'Magic Eden', 'LooksRare', 'Others']
sizes = [55, 25, 12, 4, 4]
colors = [MLORANGE, MLBLUE, MLGREEN, MLPURPLE, '#888888']
explode = (0.05, 0, 0, 0, 0)  # Slightly separate Blur (leader)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 12, 'fontweight': 'bold'},
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

# Make percentage text white for dark wedges
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(13)

# Add legend with key facts
legend_labels = [
    'Blur (55%) - Zero fees, pro traders',
    'OpenSea (25%) - Multi-chain, user-friendly',
    'Magic Eden (12%) - Solana + ETH + Ordinals',
    'LooksRare (4%) - LOOKS rewards',
    'Others (4%) - X2Y2, Rarible, etc.'
]

ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=14, frameon=True, facecolor='white', edgecolor='#888')

ax.set_title('NFT Marketplace Trading Volume Share (2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
