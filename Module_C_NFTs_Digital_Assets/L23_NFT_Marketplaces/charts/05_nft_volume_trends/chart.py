"""
NFT Trading Volume Trends (2021-2024)
Line chart showing volume decline from peak
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Volume Trends',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces/charts/05_nft_volume_trends'
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

# Monthly NFT volume data (billions USD, synthetic based on market trends)
months = ['Jan\n2021', 'Jul\n2021', 'Jan\n2022', 'Jul\n2022',
          'Jan\n2023', 'Jul\n2023', 'Jan\n2024', 'Jul\n2024']
x = np.arange(len(months))

# Total market volume (estimated)
volume = [0.5, 2.5, 5.0, 1.2, 0.9, 0.4, 0.5, 0.3]  # Billions USD

# OpenSea vs Blur share (rough estimates)
opensea_share = [0.48, 2.4, 4.8, 1.0, 0.5, 0.15, 0.15, 0.08]
blur_share = [0, 0, 0, 0, 0.35, 0.2, 0.3, 0.18]

# Plot stacked area
ax.fill_between(x, 0, opensea_share, alpha=0.7, color=MLBLUE, label='OpenSea')
ax.fill_between(x, opensea_share, np.array(opensea_share) + np.array(blur_share),
                alpha=0.7, color=MLORANGE, label='Blur')
ax.fill_between(x, np.array(opensea_share) + np.array(blur_share), volume,
                alpha=0.7, color='#888888', label='Others')

# Total volume line
ax.plot(x, volume, color='black', linewidth=2.5, marker='o', markersize=6, label='Total Volume')

# Annotate peak
peak_idx = volume.index(max(volume))
ax.annotate(f'Peak: ${max(volume)}B', xy=(peak_idx, max(volume)),
            xytext=(peak_idx + 0.5, max(volume) + 0.5),
            fontsize=14, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='black'))

# Annotate current
ax.annotate(f'${volume[-1]}B\n(-94% from peak)', xy=(len(volume)-1, volume[-1]),
            xytext=(len(volume)-1.5, volume[-1] + 1),
            fontsize=14, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=MLRED))

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=14)
ax.set_ylabel('Monthly Volume (Billions USD)', fontsize=15)
ax.set_ylim(0, 6)
ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('NFT Marketplace Trading Volume (2021-2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
