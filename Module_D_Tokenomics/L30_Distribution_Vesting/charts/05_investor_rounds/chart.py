"""
Investment Rounds Comparison
Grouped bar chart comparing allocation, price, and vesting by round
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Investor Rounds',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L30_Distribution_Vesting/charts/05_investor_rounds'
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

# Investment rounds
rounds = ['Seed', 'Series A', 'Series B', 'Public Sale']

# Metrics (normalized to 0-10 scale)
allocation = [8, 7, 6, 5]  # % of supply (scaled)
price_discount = [10, 7, 4, 1]  # Discount from public price
vesting_length = [10, 7, 5, 2]  # Length of vesting (years * 3)
risk = [10, 8, 5, 3]  # Investment risk

x = np.arange(len(rounds))
width = 0.2

bars1 = ax.bar(x - 1.5*width, allocation, width, label='Allocation (%)', color=MLBLUE, edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x - 0.5*width, price_discount, width, label='Price Discount', color=MLGREEN, edgecolor='black', linewidth=0.5)
bars3 = ax.bar(x + 0.5*width, vesting_length, width, label='Vesting Length', color=MLORANGE, edgecolor='black', linewidth=0.5)
bars4 = ax.bar(x + 1.5*width, risk, width, label='Investment Risk', color=MLRED, edgecolor='black', linewidth=0.5)

ax.set_ylabel('Score (Normalized)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(rounds, fontsize=11, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.text(0.5, -0.12, 'Earlier rounds: Lower price, longer vesting, higher risk/reward',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Investment Round Characteristics', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
