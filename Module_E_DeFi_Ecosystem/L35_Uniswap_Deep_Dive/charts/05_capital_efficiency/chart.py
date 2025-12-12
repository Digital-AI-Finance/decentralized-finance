"""
Capital Efficiency by Range Width
Shows how concentrated liquidity increases efficiency
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Capital Efficiency',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive/charts/05_capital_efficiency'
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

# Range widths and corresponding efficiency
range_widths = ['Full Range\n(V2 style)', 'Wide\n(+/- 50%)', 'Medium\n(+/- 20%)', 'Narrow\n(+/- 5%)', 'Very Narrow\n(+/- 1%)']
efficiency = [1, 3, 10, 50, 200]  # x times more capital efficient
risk_level = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
colors = [MLGREEN, '#81C784', MLORANGE, '#FFB74D', MLRED]

x_pos = np.arange(len(range_widths))

bars = ax.bar(x_pos, efficiency, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add efficiency labels
for bar, eff, risk in zip(bars, efficiency, risk_level):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            f'{eff}x', ha='center', fontsize=11, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, 5,
            f'Risk:\n{risk}', ha='center', fontsize=8, color='white', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(range_widths, fontsize=10)
ax.set_ylabel('Capital Efficiency (vs V2)', fontsize=12)
ax.set_ylim(0, 250)

ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.text(0.5, -0.15, 'Narrower ranges = higher returns when price stays in range, but requires active management',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Uniswap V3: Capital Efficiency by Range Width', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
