"""
AMM Curve Variants Comparison
Shows Uniswap (constant product), Curve (stableswap), and constant sum
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'AMM Variants',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L34_AMM_Mechanics/charts/04_amm_variants'
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

# Normalized reserves (same total)
x = np.linspace(0.1, 1.9, 200)

# Constant product: x * y = 1
y_product = 1 / x

# Constant sum: x + y = 2
y_sum = 2 - x

# Stableswap (hybrid) - simplified approximation
# Flatter near 1:1, curves at extremes
A = 100  # Amplification parameter
y_stable = []
for xi in x:
    # Simplified stableswap approximation
    if 0.5 <= xi <= 1.5:
        yi = 2 - xi + 0.1 * (xi - 1)**2
    else:
        yi = 1 / xi + 0.5
    y_stable.append(max(0.1, min(1.9, yi)))

ax.plot(x, y_product, '-', color=MLBLUE, linewidth=2.5, label='Uniswap (x*y=k)')
ax.plot(x, y_stable, '-', color=MLORANGE, linewidth=2.5, label='Curve (Stableswap)')
ax.plot(x, y_sum, '--', color=MLGREEN, linewidth=2, label='Constant Sum (x+y=k)')

# Mark the 1:1 point
ax.plot(1, 1, 'o', color='black', markersize=10, zorder=5)
ax.annotate('1:1 price', xy=(1, 1), xytext=(1.15, 1.2), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Add annotations for each curve
ax.text(0.3, 1.7, 'High slippage\nat extremes', fontsize=9, color=MLBLUE)
ax.text(1.5, 0.8, 'Flat near 1:1\n(low slippage)', fontsize=9, color=MLORANGE)
ax.text(0.2, 1.2, 'Pool drains\n(dangerous)', fontsize=9, color=MLGREEN, alpha=0.7)

ax.set_xlabel('Token A Reserve', fontsize=12)
ax.set_ylabel('Token B Reserve', fontsize=12)
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)

ax.set_title('AMM Curve Variants', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
