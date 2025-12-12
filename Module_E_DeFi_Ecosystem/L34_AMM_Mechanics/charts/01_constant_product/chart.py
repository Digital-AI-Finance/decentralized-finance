"""
Constant Product AMM Curve (x * y = k)
Shows how price changes along the curve
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Constant Product Curve',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L34_AMM_Mechanics/charts/01_constant_product'
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

# Constant product k = 20,000,000 (100 ETH * 200,000 USDC)
k = 20_000_000

# ETH reserves from 50 to 200
x = np.linspace(50, 200, 200)
y = k / x  # USDC reserves

ax.plot(x, y, '-', color=MLBLUE, linewidth=2.5, label='x * y = k')

# Mark initial point
ax.plot(100, 200000, 'o', color=MLGREEN, markersize=12, zorder=5)
ax.annotate('Initial\n100 ETH\n200k USDC', xy=(100, 200000), xytext=(115, 220000),
            fontsize=10, ha='left',
            arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Mark after buying 10 ETH
ax.plot(90, k/90, 'o', color=MLORANGE, markersize=12, zorder=5)
ax.annotate('After buying 10 ETH\n90 ETH, 222k USDC', xy=(90, k/90), xytext=(55, 260000),
            fontsize=10, ha='left',
            arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Mark extreme point
ax.plot(150, k/150, 'o', color=MLRED, markersize=10, zorder=5)
ax.annotate('After selling ETH\n150 ETH, 133k USDC', xy=(150, k/150), xytext=(155, 160000),
            fontsize=10, ha='left',
            arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Add arrow showing trade direction
ax.annotate('', xy=(90, 250000), xytext=(100, 200000),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(85, 225000, 'Buy\nETH', fontsize=9, ha='center', color=MLGREEN)

ax.set_xlabel('ETH in Pool', fontsize=12)
ax.set_ylabel('USDC in Pool', fontsize=12)
ax.set_xlim(40, 210)
ax.set_ylim(80000, 420000)

# Format y-axis with K
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}k'))

ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=11)

ax.set_title('Constant Product AMM: x * y = k', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
