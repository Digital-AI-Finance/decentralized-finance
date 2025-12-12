"""
Typical Token Allocation Breakdown
Pie chart showing healthy project distribution
"""

import matplotlib.pyplot as plt
from pathlib import Path

CHART_METADATA = {
    'title': 'Typical Token Allocation',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L30_Distribution_Vesting/charts/01_typical_allocation'
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
MLGRAY = '#888888'
MLYELLOW = '#BCBD22'

fig, ax = plt.subplots(figsize=(10, 6))

# Allocation categories
labels = ['Ecosystem &\nDevelopment', 'Investors\n(VCs)', 'Team &\nFounders',
          'Community\nSale', 'Foundation/\nTreasury', 'Liquidity', 'Advisors']
sizes = [25, 20, 17, 15, 12, 8, 3]  # Percentages
colors = [MLGREEN, MLORANGE, MLBLUE, MLPURPLE, MLGRAY, MLYELLOW, MLRED]
explode = (0.03, 0, 0, 0, 0, 0, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 9, 'fontweight': 'bold'},
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Add insider vs community breakdown
ax.text(0.5, -0.12, 'Insiders (Team+VCs+Advisors): ~40%  |  Community: ~60%',
        transform=ax.transAxes, ha='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Typical Token Allocation (Healthy Project)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
