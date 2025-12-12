"""
Bitcoin ETF Inflows
Bar chart showing cumulative ETF inflows
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'BTC ETF Inflows',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L45_Global_Regulation/charts/04_btc_etf_inflows'
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

# ETF providers and their AUM
etfs = ['BlackRock\n(IBIT)', 'Fidelity\n(FBTC)', 'Grayscale\n(GBTC)', 'ARK 21Shares\n(ARKB)',
        'Bitwise\n(BITB)', 'VanEck\n(HODL)', 'Others']
aum = [25, 12, 15, 3, 2.5, 1, 1.5]  # Billions USD (approximate)

colors = [MLBLUE, MLGREEN, MLORANGE, MLPURPLE, '#6699CC', '#99CC99', '#CCCCCC']

bars = ax.bar(etfs, aum, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, aum):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'${val}B', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Assets Under Management (Billion USD)', fontsize=12)
ax.set_ylim(0, 30)
ax.grid(True, alpha=0.3, axis='y')

# Total annotation
total = sum(aum)
ax.text(5.5, 25, f'Total AUM:\n${total:.0f}B+', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

# Timeline note
ax.text(0.5, 27, 'Approved: Jan 10, 2024', fontsize=9, color='gray', style='italic')

ax.set_title('US Spot Bitcoin ETF AUM (Q4 2024)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
