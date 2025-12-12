"""
US Crypto Regulatory Agencies
Stacked bar showing jurisdiction overlap
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'US Regulators',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L45_Global_Regulation/charts/02_us_regulators'
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

# Asset types and regulator jurisdiction (relative authority 0-10)
asset_types = ['Bitcoin', 'ETH', 'Utility\nTokens', 'Security\nTokens', 'Stablecoins', 'NFTs', 'DeFi']
sec = [2, 4, 5, 9, 3, 3, 6]
cftc = [8, 5, 2, 1, 2, 1, 3]
fincen = [3, 3, 3, 3, 4, 2, 5]
states = [2, 2, 2, 2, 3, 2, 2]

x = np.arange(len(asset_types))
width = 0.2

bars1 = ax.bar(x - 1.5*width, sec, width, label='SEC', color=MLBLUE, edgecolor='black')
bars2 = ax.bar(x - 0.5*width, cftc, width, label='CFTC', color=MLORANGE, edgecolor='black')
bars3 = ax.bar(x + 0.5*width, fincen, width, label='FinCEN', color=MLGREEN, edgecolor='black')
bars4 = ax.bar(x + 1.5*width, states, width, label='States', color=MLPURPLE, edgecolor='black')

ax.set_ylabel('Regulatory Authority (Relative)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(asset_types, fontsize=14)
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Annotation
ax.annotate('Jurisdiction\nOverlap', xy=(3, 9), xytext=(4.5, 9.5),
            fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('US Crypto Regulatory Jurisdiction (Fragmented)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
