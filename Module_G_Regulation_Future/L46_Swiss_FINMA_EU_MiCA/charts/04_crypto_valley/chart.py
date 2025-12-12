"""
Swiss Crypto Valley Growth
Bar chart showing ecosystem growth
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Crypto Valley',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA/charts/04_crypto_valley'
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

# Crypto Valley company growth
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
companies = [350, 450, 600, 750, 900, 960, 1050, 1100]

colors = [MLBLUE if c < 800 else MLGREEN for c in companies]

bars = ax.bar(years, companies, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, companies):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
            f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Number of Blockchain Companies', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylim(0, 1300)
ax.grid(True, alpha=0.3, axis='y')

# Add notable foundations
ax.annotate('Ethereum Foundation\nTezos, Cardano', xy=(0, 350), xytext=(1.5, 100),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor=MLBLUE))

# Highlight 1000+ milestone
ax.axhline(y=1000, color=MLGREEN, linestyle='--', alpha=0.5, linewidth=2)
ax.text(7.5, 1020, '1,000+ companies', fontsize=9, color=MLGREEN, ha='right')

ax.set_title('Crypto Valley (Zug) Ecosystem Growth', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
