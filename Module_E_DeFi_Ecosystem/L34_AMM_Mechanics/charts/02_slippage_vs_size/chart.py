"""
Slippage vs Trade Size in AMM
Shows non-linear increase in slippage with trade size
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Slippage vs Trade Size',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L34_AMM_Mechanics/charts/02_slippage_vs_size'
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

# Pool: 100 ETH, 200,000 USDC, k = 20,000,000
# Initial price: 1 ETH = 2,000 USDC
k = 20_000_000
initial_price = 2000

# Trade sizes (ETH to buy)
trade_sizes = np.linspace(0.1, 30, 100)

# Calculate slippage for each trade size
slippage = []
for trade in trade_sizes:
    new_x = 100 - trade
    new_y = k / new_x
    usdc_cost = new_y - 200000
    avg_price = usdc_cost / trade
    slip = ((avg_price - initial_price) / initial_price) * 100
    slippage.append(slip)

ax.plot(trade_sizes, slippage, '-', color=MLBLUE, linewidth=2.5)

# Highlight key points
key_sizes = [1, 5, 10, 20]
for size in key_sizes:
    idx = np.abs(trade_sizes - size).argmin()
    ax.plot(size, slippage[idx], 'o', color=MLORANGE, markersize=10, zorder=5)
    ax.annotate(f'{size} ETH: {slippage[idx]:.1f}%',
                xy=(size, slippage[idx]), xytext=(size + 1, slippage[idx] + 3),
                fontsize=14, ha='left')

# Add zones
ax.axhspan(0, 1, color=MLGREEN, alpha=0.1)
ax.axhspan(1, 5, color=MLORANGE, alpha=0.1)
ax.axhspan(5, 40, color=MLRED, alpha=0.1)

ax.text(28, 0.5, 'Acceptable\n(<1%)', fontsize=14, ha='right', color=MLGREEN)
ax.text(28, 3, 'Caution\n(1-5%)', fontsize=14, ha='right', color=MLORANGE)
ax.text(28, 15, 'High\n(>5%)', fontsize=14, ha='right', color=MLRED)

ax.set_xlabel('Trade Size (ETH)', fontsize=15)
ax.set_ylabel('Slippage (%)', fontsize=15)
ax.set_xlim(0, 30)
ax.set_ylim(0, 40)

ax.grid(True, alpha=0.3)

ax.set_title('Price Slippage vs Trade Size (100 ETH / 200k USDC Pool)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
