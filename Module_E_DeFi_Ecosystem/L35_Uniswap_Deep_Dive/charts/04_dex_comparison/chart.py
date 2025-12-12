"""
DEX TVL Comparison
Bar chart showing major DEXs by TVL
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DEX Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive/charts/04_dex_comparison'
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

# DEX data (Dec 2024 approximate)
dexs = ['Uniswap', 'Curve', 'PancakeSwap', 'Balancer', 'SushiSwap', 'Raydium']
tvl = [5.0, 2.0, 1.8, 1.0, 0.4, 0.8]  # Billions USD
colors = ['#FF007A', '#FFCD00', '#D1884F', '#1E1E1E', '#FA52A0', '#9945FF']

y_pos = np.arange(len(dexs))

bars = ax.barh(y_pos, tvl, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, val in zip(bars, tvl):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            f'${val}B', va='center', fontsize=11, fontweight='bold')

# Highlight Uniswap
ax.axhline(y=-0.3, xmin=0, xmax=5/6, color=MLRED, linewidth=0, alpha=0)

ax.set_yticks(y_pos)
ax.set_yticklabels(dexs, fontsize=11, fontweight='bold')
ax.set_xlabel('Total Value Locked (Billion USD)', fontsize=12)
ax.set_xlim(0, 6.5)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Add annotation
ax.text(0.5, -0.12, 'Uniswap leads with ~45% of total DEX TVL across all chains',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE0E6', edgecolor='#FF007A'))

ax.set_title('Top DEXs by Total Value Locked (Dec 2024)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
