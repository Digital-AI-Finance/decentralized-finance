"""
Uniswap Fee Tiers and Use Cases
Bar chart showing fee tiers and their applications
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Fee Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L34_AMM_Mechanics/charts/05_fee_structure'
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

# Fee tiers
tiers = ['0.01%', '0.05%', '0.30%', '1.00%']
fee_values = [0.01, 0.05, 0.30, 1.00]
use_cases = [
    'Stablecoins\n(USDC/DAI)',
    'Correlated\n(ETH/stETH)',
    'Standard\n(ETH/USDC)',
    'Exotic\n(High volatility)'
]
colors = [MLGREEN, MLBLUE, MLORANGE, MLRED]

y_pos = np.arange(len(tiers))

bars = ax.barh(y_pos, fee_values, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add labels
for bar, tier, use_case in zip(bars, tiers, use_cases):
    ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
            use_case, va='center', fontsize=10)

ax.set_yticks(y_pos)
ax.set_yticklabels(tiers, fontsize=12, fontweight='bold')
ax.set_xlabel('Fee Per Trade (%)', fontsize=12)
ax.set_xlim(0, 1.6)

ax.grid(True, alpha=0.3, axis='x')

# Add annotation
ax.text(0.5, -0.15, 'Lower fees = more competitive for stable pairs; Higher fees = compensation for IL risk',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('Uniswap V3 Fee Tiers', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
