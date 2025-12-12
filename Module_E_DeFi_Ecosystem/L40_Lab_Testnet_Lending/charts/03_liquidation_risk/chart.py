"""Collateral vs Debt and Liquidation Point"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

eth_prices = np.linspace(1000, 2500, 100)
collateral_value = 0.5 * eth_prices
debt = np.full_like(eth_prices, 400)
liquidation_threshold = collateral_value * 0.825

ax.fill_between(eth_prices, 0, debt, alpha=0.3, color=MLRED, label='Borrowed (Debt)')
ax.fill_between(eth_prices, debt, liquidation_threshold, alpha=0.3, color=MLORANGE, where=liquidation_threshold > debt, label='Safety Buffer')
ax.fill_between(eth_prices, liquidation_threshold, collateral_value, alpha=0.3, color=MLGREEN, label='Available Collateral')

ax.plot(eth_prices, collateral_value, color=MLBLUE, linewidth=2.5, label='Collateral Value')
ax.plot(eth_prices, liquidation_threshold, color=MLORANGE, linewidth=2.5, linestyle='--', label='Liquidation Threshold (82.5%)')
ax.axhline(y=400, color=MLRED, linewidth=2.5, linestyle=':', label='Debt ($400)')

liq_price = 400 / (0.5 * 0.825)
ax.axvline(x=liq_price, color=MLRED, linewidth=2, alpha=0.7)
ax.text(liq_price + 20, 450, f'Liquidation\n@ ${liq_price:.0f}', fontsize=9, color=MLRED)

ax.set_xlabel('ETH Price ($)', fontsize=12)
ax.set_ylabel('Value ($)', fontsize=12)
ax.set_title('Collateral Value vs ETH Price (0.5 ETH, $400 Debt)', fontweight='bold', fontsize=14)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(1000, 2500)
ax.set_ylim(0, 1400)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
