"""
Token Decimals Comparison
Shows how decimals affect token display
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Decimals',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard/charts/03_token_decimals'
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

# Token data
tokens = ['USDC', 'USDT', 'DAI', 'LINK', 'UNI']
decimals = [6, 6, 18, 18, 18]
raw_for_one = ['1,000,000', '1,000,000', '1e18', '1e18', '1e18']
colors = [MLBLUE, MLGREEN, MLORANGE, MLPURPLE, MLRED]

x = np.arange(len(tokens))
bars = ax.bar(x, decimals, color=colors, edgecolor='black', linewidth=0.5, alpha=0.8)

# Add decimal values on bars
for bar, dec in zip(bars, decimals):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
            str(dec), ha='center', fontsize=15, fontweight='bold')

ax.set_ylabel('Decimals', fontsize=15)
ax.set_xlabel('Token', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(tokens, fontsize=14, fontweight='bold')
ax.set_ylim(0, 22)

ax.grid(True, alpha=0.3, axis='y')

# Add raw value annotations
for i, (tok, raw) in enumerate(zip(tokens, raw_for_one)):
    ax.text(i, -2.5, f'1 {tok} = {raw} units', ha='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8E8E8', edgecolor='#888')
ax.text(0.50, 0.95, 'Convention: 18 decimals (like ETH) unless stablecoin (6 decimals)',
        transform=ax.transAxes, ha='center', fontsize=14, bbox=props)

ax.set_title('ERC-20 Token Decimals Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
