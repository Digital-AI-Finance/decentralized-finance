"""
RWA Asset Class Breakdown (2024)
Pie chart showing current tokenized asset distribution
"""

import matplotlib.pyplot as plt
from pathlib import Path

CHART_METADATA = {
    'title': 'RWA Asset Breakdown',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/06_rwa_asset_breakdown'
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

# Asset class breakdown (current 2024, billions USD)
labels = ['Stablecoins\n(USD-backed)', 'Tokenized\nTreasuries', 'Commodities\n(Gold)', 'Real\nEstate', 'Private\nCredit']
sizes = [45, 2, 1, 0.5, 0.5]  # Billions USD
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLRED]
explode = (0.05, 0.02, 0, 0, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct=lambda p: f'{p*sum(sizes)/100:.1f}B' if p > 3 else '',
                                   startangle=90,
                                   textprops={'fontsize': 10, 'fontweight': 'bold'},
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

# Make text readable
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

# Legend with percentages
legend_labels = [
    f'Stablecoins: ${sizes[0]}B ({sizes[0]/sum(sizes)*100:.0f}%)',
    f'Treasuries: ${sizes[1]}B ({sizes[1]/sum(sizes)*100:.0f}%)',
    f'Gold: ${sizes[2]}B ({sizes[2]/sum(sizes)*100:.1f}%)',
    f'Real Estate: ${sizes[3]}B ({sizes[3]/sum(sizes)*100:.1f}%)',
    f'Private Credit: ${sizes[4]}B ({sizes[4]/sum(sizes)*100:.1f}%)',
]

ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=9, frameon=True, facecolor='white', edgecolor='#888')

# Total annotation
ax.text(0.5, -0.05, f'Total: ${sum(sizes):.0f}B+ On-Chain (2024)',
        transform=ax.transAxes, ha='center', fontsize=11, fontweight='bold')

ax.set_title('Tokenized Real-World Assets by Category', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
