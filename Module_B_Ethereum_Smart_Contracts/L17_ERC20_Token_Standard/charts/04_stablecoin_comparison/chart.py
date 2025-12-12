"""
Stablecoin Comparison
Compares USDC, DAI, USDT characteristics
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Stablecoin Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard/charts/04_stablecoin_comparison'
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

# Stablecoins
coins = ['USDC', 'DAI', 'USDT']

# Characteristics (scale 1-10)
characteristics = {
    'Decentralization': [3, 9, 2],
    'Transparency': [8, 9, 4],
    'Censorship\nResistance': [3, 9, 2],
    'DeFi\nIntegration': [9, 10, 7],
}

x = np.arange(len(coins))
width = 0.2
colors = [MLBLUE, MLGREEN, MLORANGE, MLPURPLE]

# Create grouped bar chart
for i, (char_name, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=char_name,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.8)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(coins, fontsize=12, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add backing type annotations
backing = ['Fiat (USD)', 'Crypto (ETH, etc.)', 'Fiat + Commercial Paper']
for i, (coin, back) in enumerate(zip(coins, backing)):
    ax.text(i, -1.5, f'Backed by: {back}', ha='center', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Stablecoin Characteristics Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
