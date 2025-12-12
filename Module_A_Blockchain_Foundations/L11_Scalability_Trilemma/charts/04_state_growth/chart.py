"""
State Growth Over Time
Shows blockchain size growth for Bitcoin and Ethereum
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'State Growth',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/04_state_growth'
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

# Years
years = np.arange(2015, 2025)

# Bitcoin blockchain size (approximate, GB)
bitcoin_size = [50, 80, 130, 180, 220, 280, 350, 420, 480, 550]

# Ethereum archive node size (approximate, GB)
ethereum_size = [0, 10, 60, 200, 350, 500, 700, 900, 1100, 1300]

# Solana size (started 2020)
solana_years = np.arange(2020, 2025)
solana_size = [0, 50, 200, 400, 700]

ax.plot(years, bitcoin_size, 'o-', linewidth=2.5, color=MLORANGE,
        label='Bitcoin (Full Node)', markersize=8)
ax.plot(years, ethereum_size, 's-', linewidth=2.5, color=MLBLUE,
        label='Ethereum (Archive Node)', markersize=8)
ax.plot(solana_years, solana_size, '^-', linewidth=2.5, color=MLGREEN,
        label='Solana (Full History)', markersize=8)

# Current values annotation
ax.annotate(f'{bitcoin_size[-1]} GB', xy=(2024, bitcoin_size[-1]),
            xytext=(2024.3, bitcoin_size[-1] + 100), fontsize=10,
            fontweight='bold', color=MLORANGE)
ax.annotate(f'{ethereum_size[-1]} GB', xy=(2024, ethereum_size[-1]),
            xytext=(2024.3, ethereum_size[-1] - 150), fontsize=10,
            fontweight='bold', color=MLBLUE)

# Storage cost reference
ax.axhline(y=1000, color=MLRED, linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(2015.5, 1050, '1 TB threshold', fontsize=10, color=MLRED)

# Problem annotation
props = dict(boxstyle='round,pad=0.3', facecolor='#FFE0E0', edgecolor=MLRED)
ax.text(2017, 1200, 'Running full nodes becomes\nprohibitively expensive',
        fontsize=10, bbox=props, color=MLRED, ha='center')

ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Blockchain Size (GB)', fontsize=13)
ax.set_xlim(2014.5, 2025.5)
ax.set_ylim(0, 1500)

ax.legend(loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3)

ax.set_title('Blockchain State Growth: A Centralization Pressure', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
