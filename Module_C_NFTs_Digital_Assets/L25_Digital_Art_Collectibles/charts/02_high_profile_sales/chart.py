"""
High-Profile NFT Art Sales
Horizontal bar chart of major sales
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'High-Profile NFT Sales',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles/charts/02_high_profile_sales'
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

# Major NFT sales (in millions USD)
sales = [
    ('Beeple "Everydays"\n(2021)', 69.3, MLBLUE),
    ('Beeple "Human One"\n(2021)', 28.9, MLBLUE),
    ('CryptoPunk #5822\n(2022)', 23.7, MLPURPLE),
    ('CryptoPunk #7523\n(2021)', 11.8, MLPURPLE),
    ('Art Blocks Ringers #879\n(2021)', 7.1, MLORANGE),
]

labels = [s[0] for s in sales]
values = [s[1] for s in sales]
colors = [s[2] for s in sales]

y_pos = np.arange(len(labels))

bars = ax.barh(y_pos, values, color=colors, edgecolor='black', linewidth=0.5, height=0.6)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'${val}M', va='center', ha='left', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=14, fontweight='bold')
ax.set_xlabel('Sale Price (Millions USD)', fontsize=15)
ax.set_xlim(0, 80)
ax.grid(True, alpha=0.3, axis='x')

# Legend for categories
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, label='Beeple (1/1 Art)'),
    Patch(facecolor=MLPURPLE, label='CryptoPunks (PFP)'),
    Patch(facecolor=MLORANGE, label='Art Blocks (Generative)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=14)

ax.set_title('Top NFT Art Sales (All Time)', fontweight='bold', fontsize=15, pad=10)
ax.invert_yaxis()
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
