"""
Real World Asset (RWA) Tokenization Market
Bar chart showing projected growth
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'RWA Market',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L47_CBDCs_Future/charts/05_rwa_market'
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

# RWA tokenization market size
years = ['2021', '2022', '2023', '2024', '2025*', '2027*', '2030*']
market_size = [0.1, 0.3, 0.8, 2.0, 4.0, 8.0, 16.0]  # Trillions USD

colors = [MLBLUE if i < 4 else MLGREEN for i in range(len(years))]

bars = ax.bar(years, market_size, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, market_size):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'${val}T', ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Market Size (Trillion USD)', fontsize=15)
ax.set_xlabel('Year (* = projected)', fontsize=15)
ax.set_ylim(0, 20)
ax.grid(True, alpha=0.3, axis='y')

# Add growth annotation
ax.annotate('BCG Estimate:\n$16T by 2030', xy=(6, 16), xytext=(5, 18),
            fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN))

# Asset class breakdown annotation
ax.text(0.02, 0.98, 'Includes:\nReal Estate, Bonds,\nPrivate Equity, Art',
        transform=ax.transAxes, fontsize=14, va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Real World Asset (RWA) Tokenization Market', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
