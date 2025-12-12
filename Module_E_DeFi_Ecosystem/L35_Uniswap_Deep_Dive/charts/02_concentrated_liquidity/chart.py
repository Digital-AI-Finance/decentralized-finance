"""
Concentrated Liquidity V2 vs V3 Comparison
Shows how liquidity is distributed in each version
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Concentrated Liquidity',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive/charts/02_concentrated_liquidity'
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Price range
prices = np.linspace(500, 5000, 200)
current_price = 2000

# V2: Liquidity spread across entire range (constant)
v2_liquidity = np.ones_like(prices) * 0.3

# V3: Concentrated liquidity in narrow range
v3_liquidity = np.where((prices > 1800) & (prices < 2200),
                         1.5, 0.05)

# V2 Chart
ax1.fill_between(prices, v2_liquidity, alpha=0.5, color=MLBLUE)
ax1.plot(prices, v2_liquidity, color=MLBLUE, linewidth=2)
ax1.axvline(x=current_price, color='black', linestyle='--', linewidth=1.5)
ax1.text(current_price + 100, 0.5, 'Current\nPrice', fontsize=9)
ax1.set_xlabel('ETH Price (USD)', fontsize=11)
ax1.set_ylabel('Liquidity Depth', fontsize=11)
ax1.set_title('Uniswap V2: Full Range', fontweight='bold', fontsize=12)
ax1.set_xlim(500, 5000)
ax1.set_ylim(0, 2)
ax1.fill_between(prices, v2_liquidity, alpha=0.3, color=MLBLUE, label='Liquidity spread thin')

# V3 Chart
ax2.fill_between(prices, v3_liquidity, alpha=0.5, color=MLGREEN)
ax2.plot(prices, v3_liquidity, color=MLGREEN, linewidth=2)
ax2.axvline(x=current_price, color='black', linestyle='--', linewidth=1.5)
ax2.axvline(x=1800, color=MLRED, linestyle=':', linewidth=1.5, alpha=0.7)
ax2.axvline(x=2200, color=MLRED, linestyle=':', linewidth=1.5, alpha=0.7)
ax2.text(current_price + 100, 1.7, 'Current\nPrice', fontsize=9)
ax2.annotate('Range\nbounds', xy=(1800, 1.5), xytext=(1400, 1.3),
             fontsize=9, color=MLRED, arrowprops=dict(arrowstyle='->', color=MLRED))
ax2.set_xlabel('ETH Price (USD)', fontsize=11)
ax2.set_title('Uniswap V3: Concentrated', fontweight='bold', fontsize=12)
ax2.set_xlim(500, 5000)
ax2.set_ylim(0, 2)

# Add efficiency comparison
ax1.text(0.5, -0.18, 'Capital Efficiency: 1x', transform=ax1.transAxes, ha='center',
         fontsize=10, fontweight='bold', color=MLBLUE)
ax2.text(0.5, -0.18, 'Capital Efficiency: ~5x (in range)', transform=ax2.transAxes, ha='center',
         fontsize=10, fontweight='bold', color=MLGREEN)

plt.suptitle('V2 vs V3: Liquidity Distribution', fontweight='bold', fontsize=14, y=1.02)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
