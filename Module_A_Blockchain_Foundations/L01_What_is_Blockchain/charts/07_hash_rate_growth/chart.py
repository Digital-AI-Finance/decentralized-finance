"""
Bitcoin Hash Rate Growth (Log Scale)
Demonstrates the massive computational security backing the network
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Hash Rate Growth',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/07_hash_rate_growth'
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

# Historical hash rate data (EH/s = ExaHash per second)
# Source: blockchain.com hash rate data
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
# Hash rate in EH/s (exponential growth)
hash_rate_ehs = np.array([
    0.00001,      # 2010: ~10 MH/s
    0.00001,      # 2011: ~10 MH/s (GPU era)
    0.00002,      # 2012: ~20 TH/s (FPGA)
    0.01,         # 2013: 10 PH/s (early ASICs)
    0.3,          # 2014: 300 PH/s
    0.4,          # 2015: 400 PH/s
    2,            # 2016: 2 EH/s
    15,           # 2017: 15 EH/s
    40,           # 2018: 40 EH/s
    100,          # 2019: 100 EH/s
    150,          # 2020: 150 EH/s
    180,          # 2021: 180 EH/s
    250,          # 2022: 250 EH/s
    500,          # 2023: 500 EH/s
    750,          # 2024: 750 EH/s (Dec 2024)
])

fig, ax = plt.subplots(figsize=(10, 6))

# Log scale plot
ax.semilogy(years, hash_rate_ehs, color=MLGREEN, linewidth=3, marker='s', markersize=8)
ax.fill_between(years, 0.000001, hash_rate_ehs, alpha=0.2, color=MLGREEN)

# Mining era annotations
eras = [
    (2010, 0.00001, 'CPU/GPU'),
    (2013, 0.01, 'ASICs'),
    (2020, 150, 'Industrial'),
    (2024, 750, '750 EH/s'),
]

for year, val, label in eras:
    ax.annotate(label, xy=(year, val), fontsize=14, fontweight='bold',
                xytext=(5, 5), textcoords='offset points', color=MLPURPLE)

ax.set_xlabel('Year', fontsize=15, fontweight='bold')
ax.set_ylabel('Hash Rate (EH/s, log scale)', fontsize=15, fontweight='bold')
ax.set_title('Bitcoin Network Security: Hash Rate Growth', fontsize=14, fontweight='bold', color=MLPURPLE)

ax.set_xlim(2009.5, 2025)
ax.set_ylim(0.000001, 1000)
ax.grid(True, alpha=0.3, linestyle='--', which='both')

# Add context
ax.text(0.98, 0.02, '750 EH/s = 750,000,000,000,000,000,000 hashes/second',
        transform=ax.transAxes, fontsize=14, ha='right', va='bottom', color='gray', style='italic')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
