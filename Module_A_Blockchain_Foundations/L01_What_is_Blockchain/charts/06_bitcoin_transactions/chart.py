"""
Bitcoin Daily Transactions (2010-2024)
Real-world data visualization showing blockchain adoption growth
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Daily Transactions Growth',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/06_bitcoin_transactions'
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

# Historical Bitcoin transaction data (approximated from blockchain.com data)
# Values represent average daily transactions in thousands
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
# Source: blockchain.com historical data (December average of each year)
transactions_k = np.array([0.5, 2, 15, 50, 70, 100, 200, 300, 250, 300, 330, 280, 250, 400, 550])

fig, ax = plt.subplots(figsize=(10, 6))

# Plot as area chart
ax.fill_between(years, transactions_k, alpha=0.3, color=MLORANGE)
ax.plot(years, transactions_k, color=MLORANGE, linewidth=3, marker='o', markersize=8)

# Key annotations
key_events = [
    (2013, 50, 'Silk Road\nshutdown'),
    (2017, 300, 'ICO boom\n~350K/day peak'),
    (2021, 280, 'Institutional\nadoption'),
    (2024, 550, 'ETF era\n~600K/day'),
]

for year, val, label in key_events:
    ax.annotate(label, xy=(year, val), xytext=(year, val + 80),
                fontsize=14, ha='center', va='bottom',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.set_xlabel('Year', fontsize=15, fontweight='bold')
ax.set_ylabel('Daily Transactions (thousands)', fontsize=15, fontweight='bold')
ax.set_title('Bitcoin Network Transaction Growth', fontsize=14, fontweight='bold', color=MLPURPLE)

ax.set_xlim(2009.5, 2025)
ax.set_ylim(0, 700)
ax.grid(True, alpha=0.3, linestyle='--')

# Add data source note
ax.text(0.98, 0.02, 'Data: blockchain.com (Dec 2024)', transform=ax.transAxes,
        fontsize=14, ha='right', va='bottom', color='gray', style='italic')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
