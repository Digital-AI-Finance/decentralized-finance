"""
NFT Market Timeline
Evolution of NFT technology and market
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Market Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/05_nft_market_timeline'
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

# Timeline events
events = [
    {'year': 2017, 'event': 'CryptoPunks\nERC-721 Proposed', 'color': MLPURPLE},
    {'year': 2018, 'event': 'ERC-721\nFinalized', 'color': MLBLUE},
    {'year': 2019, 'event': 'ERC-1155\nMulti-Token', 'color': MLGREEN},
    {'year': 2021, 'event': 'NFT Boom\nBeeple $69M', 'color': MLORANGE},
    {'year': 2023, 'event': 'Bitcoin\nOrdinals', 'color': MLRED},
    {'year': 2024, 'event': 'NFT-Fi\nIntegration', 'color': '#666'},
]

# Market volume data (synthetic, billions USD)
years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
volumes = [0.01, 0.03, 0.1, 0.3, 25, 15, 8, 10]

# Plot volume as area
ax.fill_between(years, volumes, alpha=0.3, color=MLBLUE)
ax.plot(years, volumes, color=MLBLUE, lw=2, marker='o', markersize=6)

# Add event markers
for evt in events:
    # Find y value at event year
    if evt['year'] in years:
        y_val = volumes[years.index(evt['year'])]
    else:
        y_val = 0.1

    ax.axvline(x=evt['year'], color=evt['color'], linestyle='--', alpha=0.5)
    ax.annotate(evt['event'], xy=(evt['year'], min(y_val + 2, 20)),
               ha='center', fontsize=8, fontweight='bold', color=evt['color'],
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=evt['color'], alpha=0.9))

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Volume ($ Billions)', fontsize=12)
ax.set_xlim(2016.5, 2024.5)
ax.set_ylim(0, 30)

ax.grid(True, alpha=0.3)

# Peak annotation
ax.annotate('Peak: $25B\n(2021)', xy=(2021, 25), xytext=(2022, 27),
           arrowprops=dict(arrowstyle='->', color='black'),
           fontsize=9, ha='center')

ax.set_title('NFT Market Evolution and Key Milestones', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
