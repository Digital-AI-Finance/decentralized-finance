"""
Stablecoin Market Share Distribution
Shows dominance of major stablecoins in the crypto ecosystem
[SYNTHETIC DATA - Approximate 2024 distribution]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Stablecoin Market Share Distribution 2024',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/stablecoin_market_share'
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

# Stablecoin market share (approximate 2024 data)
stablecoins = ['USDT\n(Tether)', 'USDC\n(Circle)', 'DAI\n(MakerDAO)',
               'FDUSD', 'USDE', 'Others']
market_share = [65.5, 21.0, 4.5, 3.2, 2.8, 3.0]  # Percentages

# Create grayscale colors
colors = ['#1a1a1a', '#4d4d4d', '#808080', '#999999', '#b3b3b3', '#cccccc']

# Create the chart
fig, ax = plt.subplots(figsize=(8, 8))

# Create pie chart
wedges, texts, autotexts = ax.pie(market_share,
                                    labels=stablecoins,
                                    autopct='%1.1f%%',
                                    startangle=90,
                                    colors=colors,
                                    wedgeprops=dict(edgecolor='white', linewidth=2))

# Enhance text readability
for text in texts:
    text.set_fontsize(10)
    text.set_weight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)
    autotext.set_weight('bold')

ax.set_title('Stablecoin Market Share Distribution (2024)', pad=20)

# Add legend with stablecoin types
legend_labels = [
    'USDT - Centralized (Fiat-backed)',
    'USDC - Centralized (Fiat-backed)',
    'DAI - Decentralized (Crypto-backed)',
    'FDUSD - Centralized (Fiat-backed)',
    'USDE - Decentralized (Synthetic)',
    'Others - Various types'
]

ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1),
          framealpha=0.9, fontsize=8)

# Add total market cap note
total_cap = "$180B"  # Approximate 2024 total
fig.text(0.5, 0.05, f'Total Stablecoin Market Cap: ~{total_cap}',
         ha='center', fontsize=9, style='italic', alpha=0.7)

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC - Approximate 2024 data]',
         ha='right', va='bottom', fontsize=8, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
