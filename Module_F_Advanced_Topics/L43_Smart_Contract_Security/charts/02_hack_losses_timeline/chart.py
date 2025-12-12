"""
DeFi Hack Losses by Year
Bar chart showing annual losses
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Hack Losses Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L43_Smart_Contract_Security/charts/02_hack_losses_timeline'
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

# Annual DeFi hack losses
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
losses = [0.06, 0.3, 0.2, 0.3, 0.5, 1.3, 3.1, 1.8, 1.7]  # Billions USD
colors = [MLBLUE if l < 1 else (MLORANGE if l < 2 else MLRED) for l in losses]

bars = ax.bar(years, losses, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, losses):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
            f'${val}B', ha='center', va='bottom', fontsize=14, fontweight='bold')

# Highlight The DAO (2016) and peak (2022)
ax.annotate('The DAO\n($60M)', xy=(0, 0.06), xytext=(0.5, 1.0),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))
ax.annotate('Peak Year', xy=(6, 3.1), xytext=(6, 3.6),
            fontsize=14, ha='center', arrowprops=dict(arrowstyle='->', color=MLRED))

ax.set_ylabel('Losses (Billion USD)', fontsize=15)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylim(0, 4.0)

ax.grid(True, alpha=0.3, axis='y')

ax.set_title('DeFi/Crypto Hack Losses by Year', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
