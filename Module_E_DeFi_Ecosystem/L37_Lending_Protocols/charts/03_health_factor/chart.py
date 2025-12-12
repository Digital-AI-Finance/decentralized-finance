"""
Health Factor Visualization
Shows health factor changes with collateral price
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Health Factor',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L37_Lending_Protocols/charts/03_health_factor'
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

# Scenario: 10 ETH collateral, $12k borrowed, 83% liquidation threshold
# Initial ETH price: $2000
borrowed = 12000
liq_threshold = 0.83

# ETH prices from $1200 to $3000
eth_prices = np.linspace(1200, 3000, 100)
collateral_values = 10 * eth_prices
health_factors = (collateral_values * liq_threshold) / borrowed

ax.plot(eth_prices, health_factors, '-', color=MLBLUE, linewidth=2.5)

# Zones
ax.fill_between(eth_prices, 0, health_factors, where=(health_factors < 1),
                color=MLRED, alpha=0.3, label='Liquidation Zone (HF < 1)')
ax.fill_between(eth_prices, 0, health_factors, where=(health_factors >= 1) & (health_factors < 1.5),
                color=MLORANGE, alpha=0.3, label='Warning Zone (1 < HF < 1.5)')
ax.fill_between(eth_prices, 0, health_factors, where=(health_factors >= 1.5),
                color=MLGREEN, alpha=0.3, label='Safe Zone (HF > 1.5)')

# Liquidation line
ax.axhline(y=1, color=MLRED, linestyle='--', linewidth=2, label='Liquidation Threshold')

# Mark key points
# Liquidation price
liq_price = borrowed / (10 * liq_threshold)
ax.axvline(x=liq_price, color=MLRED, linestyle=':', linewidth=1.5, alpha=0.7)
ax.annotate(f'Liquidation\n${liq_price:.0f}', xy=(liq_price, 1), xytext=(liq_price-150, 1.5),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color=MLRED))

# Initial price
ax.axvline(x=2000, color=MLGREEN, linestyle=':', linewidth=1.5, alpha=0.7)
hf_initial = (10 * 2000 * 0.83) / 12000
ax.plot(2000, hf_initial, 'o', color=MLGREEN, markersize=10, zorder=5)
ax.annotate(f'Initial\nHF={hf_initial:.2f}', xy=(2000, hf_initial), xytext=(2150, hf_initial-0.3),
            fontsize=14, ha='left', arrowprops=dict(arrowstyle='->', color=MLGREEN))

ax.set_xlabel('ETH Price (USD)', fontsize=15)
ax.set_ylabel('Health Factor', fontsize=15)
ax.set_xlim(1200, 3000)
ax.set_ylim(0, 2.5)

ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3)

ax.set_title('Health Factor vs Collateral Price (10 ETH, $12k Borrowed)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
