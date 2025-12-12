"""
Total Cryptocurrency Market Capitalization (2013-2024)
Shows the growth of the entire crypto ecosystem
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Cryptocurrency Market Cap Growth',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/08_crypto_market_cap'
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

# Market cap data (in billions USD, end of year)
# Source: CoinGecko, CoinMarketCap historical data
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
total_mcap_b = np.array([15, 6, 7, 18, 600, 130, 190, 770, 2200, 800, 1700, 3500])
btc_mcap_b = np.array([10, 4, 5, 12, 230, 67, 130, 540, 900, 320, 850, 2000])
eth_mcap_b = np.array([0, 0, 0, 0.7, 70, 14, 14, 85, 500, 140, 280, 450])

fig, ax = plt.subplots(figsize=(10, 6))

# Stacked area chart
ax.fill_between(years, 0, btc_mcap_b, alpha=0.8, color=MLORANGE, label='Bitcoin')
ax.fill_between(years, btc_mcap_b, btc_mcap_b + eth_mcap_b, alpha=0.8, color=MLBLUE, label='Ethereum')
ax.fill_between(years, btc_mcap_b + eth_mcap_b, total_mcap_b, alpha=0.8, color=MLGREEN, label='Altcoins')

# Add line for total
ax.plot(years, total_mcap_b, color='black', linewidth=2, linestyle='--', label='Total')

# Key events
events = [
    (2017, 600, 'ICO Bubble'),
    (2021, 2200, 'NFT/DeFi Peak\n$3T ATH'),
    (2024, 3500, 'ETF Era\n$3.5T'),
]

for year, val, label in events:
    ax.annotate(label, xy=(year, val), xytext=(year, val + 300),
                fontsize=14, ha='center', va='bottom',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.set_xlabel('Year', fontsize=15, fontweight='bold')
ax.set_ylabel('Market Cap (Billion USD)', fontsize=15, fontweight='bold')
ax.set_title('Cryptocurrency Market Capitalization Growth', fontsize=14, fontweight='bold', color=MLPURPLE)

ax.set_xlim(2012.5, 2025)
ax.set_ylim(0, 4200)
ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3, linestyle='--', axis='y')

# Format y-axis
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.1f}T' if x >= 1000 else f'${x:.0f}B'))

ax.text(0.98, 0.02, 'Data: CoinGecko (Dec 2024)', transform=ax.transAxes,
        fontsize=14, ha='right', va='bottom', color='gray', style='italic')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
