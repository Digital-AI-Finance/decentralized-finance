"""
Real-World Transaction Costs
Bar chart showing typical transaction costs
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Real World Costs',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/05_real_world_costs'
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

# Transaction types and their gas usage
tx_types = ['ETH Transfer', 'ERC-20\nTransfer', 'Uniswap\nSwap', 'NFT Mint',
            'OpenSea\nPurchase', 'Contract\nDeploy']
gas_used = [21000, 55000, 150000, 120000, 250000, 400000]

# Calculate USD costs at 30 Gwei and $2000/ETH
gwei_price = 32  # 30 base + 2 tip
eth_price = 2000
usd_costs = [(gas * gwei_price * 1e-9 * eth_price) for gas in gas_used]

# Colors
colors = [MLGREEN, MLGREEN, MLBLUE, MLORANGE, MLORANGE, MLRED]

bars = ax.bar(tx_types, usd_costs, color=colors, edgecolor='black', linewidth=0.5)

# Add cost labels
for bar, cost, gas in zip(bars, usd_costs, gas_used):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
            f'${cost:.2f}', ha='center', fontsize=14, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, height/2,
            f'{gas/1000:.0f}K gas', ha='center', fontsize=14, color='white')

# Reference line
ax.axhline(y=5, color=MLRED, linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(5.5, 5.5, 'Typical "reasonable" threshold', fontsize=14, color=MLRED)

ax.set_ylabel('Cost (USD) at 32 Gwei, $2000/ETH', fontsize=15)
ax.set_ylim(0, 30)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLGREEN, edgecolor='black', label='Simple'),
    Patch(facecolor=MLBLUE, edgecolor='black', label='DeFi'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='NFT'),
    Patch(facecolor=MLRED, edgecolor='black', label='Complex'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=14)

ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Real-World Ethereum Transaction Costs', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
