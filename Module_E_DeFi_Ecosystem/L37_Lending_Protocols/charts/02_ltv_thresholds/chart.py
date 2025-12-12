"""
LTV and Liquidation Thresholds by Asset
Grouped bar showing LTV limits for different assets
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'LTV Thresholds',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L37_Lending_Protocols/charts/02_ltv_thresholds'
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

# Asset data
assets = ['USDC', 'ETH', 'WBTC', 'LINK', 'UNI', 'Low-cap\nToken']
max_ltv = [85, 80, 75, 70, 65, 45]
liq_threshold = [88, 83, 78, 75, 70, 55]

x = np.arange(len(assets))
width = 0.35

bars1 = ax.bar(x - width/2, max_ltv, width, label='Max LTV (Borrow Limit)',
               color=MLBLUE, edgecolor='black', linewidth=1)
bars2 = ax.bar(x + width/2, liq_threshold, width, label='Liquidation Threshold',
               color=MLRED, edgecolor='black', linewidth=1)

# Add buffer zone annotation
for i, (ltv, liq) in enumerate(zip(max_ltv, liq_threshold)):
    buffer = liq - ltv
    ax.annotate(f'+{buffer}%\nbuffer',
                xy=(x[i] + width/4, (ltv + liq)/2),
                fontsize=14, ha='center', color='gray')

ax.set_ylabel('Percentage (%)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(assets, fontsize=14, fontweight='bold')
ax.set_ylim(0, 100)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.text(0.5, -0.12, 'Lower risk assets (stablecoins) have higher LTV; volatile assets have lower LTV',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('Aave LTV and Liquidation Thresholds by Asset', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
