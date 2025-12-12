"""
Flash Loan Providers Comparison
Bar chart showing fees and liquidity
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Flash Loan Providers',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L42_Flash_Loans/charts/02_providers_comparison'
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

# Provider data
providers = ['Aave', 'dYdX', 'Uniswap V3', 'Balancer']
liquidity = [12, 0.5, 5, 2]  # Billions USD
fees = [0.09, 0.00, 0.05, 0.05]  # Percentage

x = np.arange(len(providers))
width = 0.35

# Two y-axes
ax2 = ax.twinx()

bars1 = ax.bar(x - width/2, liquidity, width, label='Liquidity ($B)', color=MLBLUE, edgecolor='black')
bars2 = ax2.bar(x + width/2, fees, width, label='Fee (%)', color=MLORANGE, edgecolor='black')

# Add value labels
for bar, val in zip(bars1, liquidity):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'${val}B', ha='center', va='bottom', fontsize=14, fontweight='bold')
for bar, val in zip(bars2, fees):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
            f'{val}%', ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Liquidity (Billion USD)', fontsize=15, color=MLBLUE)
ax2.set_ylabel('Fee (%)', fontsize=15, color=MLORANGE)
ax.set_xticks(x)
ax.set_xticklabels(providers, fontsize=14)
ax.set_ylim(0, 15)
ax2.set_ylim(0, 0.12)

ax.tick_params(axis='y', labelcolor=MLBLUE)
ax2.tick_params(axis='y', labelcolor=MLORANGE)

# Combined legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=14)

ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Flash Loan Providers: Liquidity vs Fees', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
