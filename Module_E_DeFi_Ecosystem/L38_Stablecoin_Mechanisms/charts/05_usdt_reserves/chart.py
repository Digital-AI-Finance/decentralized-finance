"""
USDT Reserve Composition
Horizontal bar showing Tether reserve breakdown
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'USDT Reserves',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms/charts/05_usdt_reserves'
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

# USDT reserve composition (2024 attestations)
reserve_types = ['US Treasuries', 'Cash & Bank\nDeposits', 'Secured Loans', 'Corporate Bonds', 'Bitcoin', 'Other']
percentages = [80, 8, 5, 4, 2, 1]
colors = [MLGREEN, MLBLUE, MLORANGE, '#9C27B0', '#F7931A', '#CCCCCC']

y_pos = np.arange(len(reserve_types))

bars = ax.barh(y_pos, percentages, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, pct in zip(bars, percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{pct}%', va='center', fontsize=11, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(reserve_types, fontsize=10)
ax.set_xlabel('Percentage of Reserves', fontsize=12)
ax.set_xlim(0, 100)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Add annotation
ax.text(0.5, -0.15, 'Tether has shifted heavily to US Treasuries after 2022 criticism',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('USDT (Tether) Reserve Composition (2024)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
