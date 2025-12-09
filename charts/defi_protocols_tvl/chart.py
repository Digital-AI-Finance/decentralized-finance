"""
DeFi Protocols by TVL (Total Value Locked)
Shows market share of major DeFi protocols
[SYNTHETIC DATA - Representative of Dec 2024 landscape]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'DeFi Protocols by Total Value Locked (TVL)',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/defi_protocols_tvl'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9
})

# Synthetic data representing DeFi landscape
protocols = ['Lido', 'AAVE', 'MakerDAO', 'Uniswap', 'Eigenlayer', 'Rocket Pool', 'Compound', 'Curve', 'Others']
tvl_billions = [28.5, 12.3, 8.1, 6.2, 5.8, 4.2, 3.1, 2.8, 15.0]
categories = ['Liquid Staking', 'Lending', 'CDP', 'DEX', 'Restaking', 'Liquid Staking', 'Lending', 'DEX', 'Various']

# Sort by TVL
sorted_indices = np.argsort(tvl_billions)[::-1]
protocols = [protocols[i] for i in sorted_indices]
tvl_billions = [tvl_billions[i] for i in sorted_indices]
categories = [categories[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# Grayscale gradient
colors = plt.cm.Greys(np.linspace(0.3, 0.8, len(protocols)))

bars = ax.barh(protocols, tvl_billions, color=colors, edgecolor='black', linewidth=0.5)

ax.set_xlabel('Total Value Locked ($ Billions)')
ax.set_title('DeFi Protocols by TVL (Synthetic Data - Dec 2024)', fontweight='bold')
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

# Add value labels
for bar, tvl, cat in zip(bars, tvl_billions, categories):
    width = bar.get_width()
    ax.text(width + 0.3, bar.get_y() + bar.get_height()/2,
            f'${tvl:.1f}B ({cat})', ha='left', va='center', fontsize=8)

ax.set_xlim(0, max(tvl_billions) + 12)

# Add total
total_tvl = sum(tvl_billions)
ax.text(0.98, 0.02, f'Total DeFi TVL: ${total_tvl:.1f}B', transform=ax.transAxes,
        ha='right', va='bottom', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC]', ha='right', va='bottom', fontsize=8, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
