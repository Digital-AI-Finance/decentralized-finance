"""
NFT Art Market Volume Trends (2020-2024)
Line chart showing market evolution
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Art Market Trends',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles/charts/04_art_market_trends'
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

# Yearly NFT art market volume (billions USD)
years = ['2020', '2021', '2022', '2023', '2024']
volume = [0.1, 25, 10, 6, 8]  # Total market volume

# Plot line with area fill
ax.fill_between(years, volume, alpha=0.3, color=MLBLUE)
ax.plot(years, volume, color=MLBLUE, linewidth=3, marker='o', markersize=10)

# Annotate peak
ax.annotate('Peak: $25B\n(NFT Mania)', xy=(1, 25), xytext=(1.5, 28),
            fontsize=10, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='black'))

# Annotate Beeple sale
ax.annotate('Beeple $69M\nSale', xy=(1, 25), xytext=(0.3, 20),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color=MLGREEN))

# Annotate bear market
ax.annotate('Bear Market\nCorrection', xy=(2, 10), xytext=(2, 15),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color=MLRED))

# Add value labels
for i, (year, vol) in enumerate(zip(years, volume)):
    ax.text(i, vol + 1.5, f'${vol}B', ha='center', fontsize=10, fontweight='bold')

ax.set_ylabel('Annual Volume (Billions USD)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylim(0, 32)
ax.grid(True, alpha=0.3)

ax.set_title('NFT Art Market Volume (2020-2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
