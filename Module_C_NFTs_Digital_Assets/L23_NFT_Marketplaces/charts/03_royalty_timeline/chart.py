"""
NFT Royalty Enforcement Timeline
Timeline showing the shift from mandatory to optional royalties
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'Royalty Enforcement Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces/charts/03_royalty_timeline'
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
    (2017, 'OpenSea\nlaunches', 'Mandatory\nroyalties', MLGREEN),
    (2020, 'Rarible\nlaunches', 'Royalties\nstandard', MLBLUE),
    (2022, 'Blur\nlaunches', 'Optional\nroyalties', MLORANGE),
    (2022.5, 'X2Y2\nfollow', 'Zero fee\nmodel', MLORANGE),
    (2023, 'OpenSea\ncapitulates', 'Optional\nroyalties', MLRED),
    (2024, 'Market\nnorm', 'Royalties\noptional', '#888888'),
]

# Draw timeline axis
ax.axhline(y=0.5, color='#333', linewidth=2, linestyle='-')

# Plot events
for i, (year, event, status, color) in enumerate(events):
    # Circle marker
    ax.scatter(year, 0.5, s=200, color=color, edgecolors='black', linewidth=2, zorder=5)

    # Event label (alternating above/below)
    if i % 2 == 0:
        ax.annotate(event, xy=(year, 0.5), xytext=(year, 0.75),
                    ha='center', va='bottom', fontsize=14, fontweight='bold',
                    arrowprops=dict(arrowstyle='-', color=color, lw=1.5))
        ax.text(year, 0.88, status, ha='center', va='bottom', fontsize=14,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.3))
    else:
        ax.annotate(event, xy=(year, 0.5), xytext=(year, 0.25),
                    ha='center', va='top', fontsize=14, fontweight='bold',
                    arrowprops=dict(arrowstyle='-', color=color, lw=1.5))
        ax.text(year, 0.12, status, ha='center', va='top', fontsize=14,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.3))

# Year labels on axis
years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
for year in years:
    ax.text(year, 0.42, str(year), ha='center', va='top', fontsize=14, fontweight='bold')

# Styling
ax.set_xlim(2016.5, 2024.5)
ax.set_ylim(0, 1)
ax.set_axis_off()

# Legend for periods
mandatory = mpatches.Patch(color=MLGREEN, alpha=0.7, label='Mandatory Royalties Era (2017-2022)')
optional = mpatches.Patch(color=MLORANGE, alpha=0.7, label='Optional Royalties Era (2022+)')
ax.legend(handles=[mandatory, optional], loc='upper center', bbox_to_anchor=(0.5, 0.05),
          ncol=2, fontsize=14, frameon=True)

ax.set_title('NFT Creator Royalty Enforcement Timeline', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
