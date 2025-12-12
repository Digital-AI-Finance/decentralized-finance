"""
China e-CNY Adoption Growth
Line chart showing wallet adoption
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'e-CNY Adoption',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L47_CBDCs_Future/charts/02_ecny_adoption'
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

# e-CNY adoption data
periods = ['Q4\n2020', 'Q2\n2021', 'Q4\n2021', 'Q2\n2022', 'Q4\n2022', 'Q2\n2023', 'Q4\n2023', 'Q4\n2024']
wallets = [4, 21, 87, 140, 180, 210, 240, 260]  # Millions
transactions = [0.1, 0.5, 1.5, 3.0, 4.5, 5.5, 6.5, 7.0]  # Trillions CNY

x = np.arange(len(periods))

# Primary axis - wallets
color1 = MLBLUE
ax1.set_xlabel('Period', fontsize=15)
ax1.set_ylabel('Wallets (Millions)', fontsize=15, color=color1)
line1 = ax1.plot(x, wallets, 'o-', color=color1, linewidth=2.5, markersize=8, label='Wallets')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_xticks(x)
ax1.set_xticklabels(periods, fontsize=14)
ax1.set_ylim(0, 300)

# Secondary axis - transactions
ax2 = ax1.twinx()
color2 = MLORANGE
ax2.set_ylabel('Cumulative Transactions (Trillion CNY)', fontsize=15, color=color2)
line2 = ax2.plot(x, transactions, 's--', color=color2, linewidth=2.5, markersize=8, label='Transactions')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(0, 8)

# Annotation
ax1.annotate('Olympic Games\nPilot', xy=(2, 87), xytext=(1, 150),
            fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax1.annotate('Nationwide\nExpansion', xy=(6, 240), xytext=(5, 280),
            fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

# Legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=14)

ax1.grid(True, alpha=0.3)
ax1.set_title('China e-CNY Adoption (2020-2024)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
