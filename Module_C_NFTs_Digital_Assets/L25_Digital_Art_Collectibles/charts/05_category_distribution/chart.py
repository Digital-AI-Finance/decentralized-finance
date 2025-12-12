"""
NFT Art Category Distribution (2024)
Pie chart showing market breakdown
"""

import matplotlib.pyplot as plt
from pathlib import Path

CHART_METADATA = {
    'title': 'Category Distribution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles/charts/05_category_distribution'
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

# Category breakdown (2024 estimates)
labels = ['PFP\nCollections', 'Generative\nArt', '1/1 Art', 'Gaming\nNFTs', 'Other']
sizes = [50, 20, 15, 10, 5]
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, '#888888']
explode = (0.05, 0, 0, 0, 0)  # Slightly separate PFP (largest)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 11, 'fontweight': 'bold'},
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

# Make percentage text white for dark wedges
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)

# Add legend with examples
legend_labels = [
    'PFP (50%) - BAYC, CryptoPunks, Azuki',
    'Generative (20%) - Art Blocks, fx(hash)',
    '1/1 Art (15%) - SuperRare, Foundation',
    'Gaming (10%) - Play-to-earn assets',
    'Other (5%) - Music, photography'
]

ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=14, frameon=True, facecolor='white', edgecolor='#888')

ax.set_title('NFT Art Market Category Distribution (2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
