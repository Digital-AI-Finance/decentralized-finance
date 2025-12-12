"""
Utilization-Based Interest Rate Model
Shows how rates increase with utilization
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Interest Rate Model',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L37_Lending_Protocols/charts/04_interest_rate_model'
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

# Utilization from 0% to 100%
utilization = np.linspace(0, 100, 200)

# Aave-style interest rate model
# Below optimal (80%): linear increase
# Above optimal: steep increase
optimal_util = 80
base_rate = 1
slope1 = 4  # slope below optimal
slope2 = 100  # slope above optimal (steep)

borrow_rate = []
for u in utilization:
    if u <= optimal_util:
        rate = base_rate + (slope1 * u / optimal_util)
    else:
        rate = base_rate + slope1 + (slope2 * (u - optimal_util) / (100 - optimal_util))
    borrow_rate.append(rate)

borrow_rate = np.array(borrow_rate)

# Supply rate = borrow rate * utilization * (1 - reserve factor)
reserve_factor = 0.1
supply_rate = borrow_rate * (utilization / 100) * (1 - reserve_factor)

ax.plot(utilization, borrow_rate, '-', color=MLRED, linewidth=2.5, label='Borrow APY')
ax.plot(utilization, supply_rate, '-', color=MLGREEN, linewidth=2.5, label='Supply APY')

# Mark optimal utilization
ax.axvline(x=optimal_util, color='gray', linestyle='--', linewidth=1.5)
ax.annotate('Optimal\nUtilization', xy=(optimal_util, 60), fontsize=14, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray'))

# Mark current zones
ax.fill_between(utilization, 0, 5, where=(utilization <= 60), color=MLGREEN, alpha=0.1)
ax.fill_between(utilization, 0, 5, where=(utilization > 60) & (utilization <= 90), color=MLORANGE, alpha=0.1)
ax.fill_between(utilization, 0, 5, where=(utilization > 90), color=MLRED, alpha=0.1)

ax.text(30, 2, 'Low Rates\n(Encourage\nBorrowing)', fontsize=14, ha='center', color=MLGREEN)
ax.text(97, 50, 'High Rates\n(Discourage\nBorrowing)', fontsize=14, ha='center', color=MLRED)

ax.set_xlabel('Utilization Rate (%)', fontsize=15)
ax.set_ylabel('Interest Rate (APY %)', fontsize=15)
ax.set_xlim(0, 100)
ax.set_ylim(0, 110)

ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3)

ax.set_title('Aave Interest Rate Model (USDC)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
