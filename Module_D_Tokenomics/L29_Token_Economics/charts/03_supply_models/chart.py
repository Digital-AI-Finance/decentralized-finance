"""
Supply Models Comparison
Comparing fixed, inflationary, and deflationary supply models
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Supply Models Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/03_supply_models'
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

# Years projection
years = np.arange(2020, 2031)

# Bitcoin fixed supply model (approaching 21M)
btc_supply = 18.5 + 0.4 * np.log1p(years - 2020)  # Millions
btc_supply = np.minimum(btc_supply, 21)

# Inflationary model (constant growth)
inflationary = 100 * (1.02 ** (years - 2020))  # 2% annual inflation

# Deflationary model (BNB-like burns)
deflationary = 200 - 5.5 * (years - 2020)  # Burns toward 100M target
deflationary = np.maximum(deflationary, 100)

# ETH post-merge (near-zero to slightly deflationary)
eth_supply = 120 - 0.3 * (years - 2022)  # Millions, slight deflation
eth_supply[:2] = [115, 117]  # Pre-merge

ax.plot(years, btc_supply, 'o-', color=MLORANGE, linewidth=2.5, markersize=6, label='Fixed (BTC): 21M cap')
ax.plot(years, inflationary, 's-', color=MLRED, linewidth=2.5, markersize=6, label='Inflationary: 2%/year')
ax.plot(years, deflationary, '^-', color=MLGREEN, linewidth=2.5, markersize=6, label='Deflationary (BNB): burn to 100M')
ax.plot(years, eth_supply, 'd-', color=MLBLUE, linewidth=2.5, markersize=6, label='ETH: slight deflation post-merge')

# Add annotations
ax.axhline(y=21, color=MLORANGE, linestyle='--', alpha=0.5)
ax.text(2030.2, 21, '21M cap', fontsize=9, va='center', color=MLORANGE)

ax.axhline(y=100, color=MLGREEN, linestyle='--', alpha=0.5)
ax.text(2030.2, 100, '100M target', fontsize=9, va='center', color=MLGREEN)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Token Supply (Millions)', fontsize=12)
ax.set_xlim(2019.5, 2032)
ax.set_ylim(0, 140)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

ax.set_title('Token Supply Model Projections', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
