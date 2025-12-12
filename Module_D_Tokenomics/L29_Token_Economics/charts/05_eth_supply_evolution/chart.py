"""
ETH Supply Evolution
Timeline showing ETH issuance changes through major upgrades
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'ETH Supply Evolution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/05_eth_supply_evolution'
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

# Time periods and issuance rates
periods = ['Pre-EIP-1559\n(Before Aug 2021)', 'Post-EIP-1559\n(Aug 2021-Sep 2022)', 'Post-Merge\n(After Sep 2022)']
issuance = [4.5, 3.0, 0.5]  # % annual issuance
burn_rate = [0, 1.5, 1.0]  # % annual burn
net_change = [4.5, 1.5, -0.5]  # Net supply change

x = np.arange(len(periods))
width = 0.25

bars1 = ax.bar(x - width, issuance, width, label='New ETH Issued', color=MLRED, edgecolor='black', linewidth=1)
bars2 = ax.bar(x, burn_rate, width, label='ETH Burned (EIP-1559)', color=MLORANGE, edgecolor='black', linewidth=1)
bars3 = ax.bar(x + width, [abs(n) for n in net_change], width, label='Net Supply Change',
               color=[MLRED if n > 0 else MLGREEN for n in net_change], edgecolor='black', linewidth=1, alpha=0.7)

# Add value labels
for bars, vals in [(bars1, issuance), (bars2, burn_rate), (bars3, net_change)]:
    for bar, val in zip(bars, vals):
        sign = '+' if val > 0 else ''
        ax.annotate(f'{sign}{val}%',
                    xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=14, fontweight='bold')

# Add milestone annotations
ax.annotate('EIP-1559:\nFee Burns Begin', xy=(1, 3.5), xytext=(0.3, 4.5),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))
ax.annotate('The Merge:\n90% Issuance Cut', xy=(2, 1.5), xytext=(2.7, 3),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))

ax.set_ylabel('Annual Rate (%)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(periods, fontsize=14, fontweight='bold')
ax.set_ylim(0, 5.5)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Ethereum Supply Evolution: From Inflationary to Deflationary', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
