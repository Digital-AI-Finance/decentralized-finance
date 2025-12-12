"""
DeFi Lending Protocol TVL Comparison
Bar chart showing major lending protocols
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Lending Protocol TVL',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L37_Lending_Protocols/charts/05_lending_protocol_tvl'
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

# Lending protocol data (Dec 2024 approximate)
protocols = ['Aave', 'Spark', 'Compound', 'MakerDAO', 'Venus', 'Morpho']
tvl = [12.0, 5.0, 2.5, 8.0, 1.5, 1.2]  # Billions USD
chains = ['Multi-chain', 'Ethereum', 'Multi-chain', 'Ethereum', 'BNB Chain', 'Ethereum']
colors = ['#B6509E', '#F7A600', '#00D395', '#4F8A61', '#F9B500', '#2B4C9B']

y_pos = np.arange(len(protocols))

bars = ax.barh(y_pos, tvl, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels and chain info
for bar, val, chain in zip(bars, tvl, chains):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'${val}B', va='center', fontsize=11, fontweight='bold')
    ax.text(0.2, bar.get_y() + bar.get_height()/2,
            chain, va='center', fontsize=9, color='white')

ax.set_yticks(y_pos)
ax.set_yticklabels(protocols, fontsize=11, fontweight='bold')
ax.set_xlabel('Total Value Locked (Billion USD)', fontsize=12)
ax.set_xlim(0, 15)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Add annotation
ax.text(0.5, -0.12, 'Aave dominates multi-chain lending; MakerDAO TVL includes DAI collateral',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3E5F5', edgecolor='#B6509E'))

ax.set_title('DeFi Lending Protocols by TVL (Dec 2024)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
