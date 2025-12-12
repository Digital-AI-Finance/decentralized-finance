"""
NFT Art Categories Comparison
Comparing 1/1 art, editions, and generative art
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Art Categories',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles/charts/01_nft_art_categories'
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

# Categories and their characteristics (scores 1-10)
categories = ['1/1 Art', 'Editions', 'Generative']
characteristics = {
    'Scarcity': [10, 5, 7],
    'Price Range': [10, 4, 6],
    'Accessibility': [2, 8, 7],
    'Collector\nParticipation': [3, 4, 9],
}

x = np.arange(len(categories))
width = 0.2
colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN]

for i, (char, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=char,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add category descriptions
descriptions = [
    'SuperRare, Foundation\nUnique pieces',
    'Manifold, Zora\nLimited copies',
    'Art Blocks, fx(hash)\nAlgorithmic'
]
for i, desc in enumerate(descriptions):
    ax.text(i, -1.8, desc, ha='center', fontsize=8, style='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('NFT Art Categories Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
