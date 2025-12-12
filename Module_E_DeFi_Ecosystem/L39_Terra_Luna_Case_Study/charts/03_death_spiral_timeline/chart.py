"""
Terra/Luna Death Spiral Timeline (May 7-12, 2022)
Shows UST price and LUNA supply over time
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Death Spiral Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L39_Terra_Luna_Case_Study/charts/03_death_spiral_timeline'
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

fig, ax1 = plt.subplots(figsize=(10, 6))

# Timeline data (May 7-12, 2022)
dates = ['May 7', 'May 8', 'May 9', 'May 10', 'May 11', 'May 12']
ust_price = [1.00, 0.98, 0.92, 0.60, 0.30, 0.10]  # USD
luna_supply = [350, 400, 1000, 5000, 500000, 6500000]  # Millions of tokens

x = np.arange(len(dates))

# UST Price on left axis
color1 = MLBLUE
ax1.set_xlabel('Date (2022)', fontsize=15)
ax1.set_ylabel('UST Price (USD)', color=color1, fontsize=15)
line1 = ax1.plot(x, ust_price, color=color1, marker='o', linewidth=3, markersize=10, label='UST Price')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, 1.1)
ax1.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='$1 Peg')

# LUNA Supply on right axis (log scale)
ax2 = ax1.twinx()
color2 = MLORANGE
ax2.set_ylabel('LUNA Supply (Millions)', color=color2, fontsize=15)
line2 = ax2.plot(x, luna_supply, color=color2, marker='s', linewidth=3, markersize=10, label='LUNA Supply')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_yscale('log')
ax2.set_ylim(100, 10000000)

ax1.set_xticks(x)
ax1.set_xticklabels(dates, fontsize=14)

# Add event annotations
ax1.annotate('Initial\nDepeg', xy=(1, 0.98), xytext=(1, 0.7),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))
ax1.annotate('Panic\nBegins', xy=(2, 0.92), xytext=(2.3, 0.5),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))
ax1.annotate('Death\nSpiral', xy=(3, 0.60), xytext=(3.3, 0.3),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color=MLRED))

ax1.grid(True, alpha=0.3)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=14)

ax1.set_title('Terra/Luna Death Spiral (May 7-12, 2022)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
