"""
Token Sinks vs Faucets
Waterfall-style chart showing token inflows and outflows
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Sinks vs Faucets',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/04_token_sinks_faucets'
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

# Token flows (positive = faucet, negative = sink)
categories = ['Block\nRewards', 'Liquidity\nMining', 'Airdrops', 'Fee\nBurns', 'Staking\nLocks', 'Slashing', 'Net\nChange']
values = [100, 50, 30, -40, -80, -20, 40]  # Thousands of tokens
colors = []

for val in values[:-1]:
    colors.append(MLGREEN if val > 0 else MLRED)
colors.append(MLBLUE)  # Net change

x = np.arange(len(categories))

bars = ax.bar(x, [abs(v) for v in values], color=colors, edgecolor='black', linewidth=1)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    sign = '+' if val > 0 else ''
    va = 'bottom' if val > 0 else 'top'
    offset = 3 if val > 0 else -3
    ax.annotate(f'{sign}{val}K',
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, offset), textcoords='offset points',
                ha='center', va=va, fontsize=11, fontweight='bold')

# Add category labels
ax.text(1, 120, 'FAUCETS\n(Token Creation)', ha='center', fontsize=11, fontweight='bold', color=MLGREEN)
ax.text(4, 120, 'SINKS\n(Token Removal)', ha='center', fontsize=11, fontweight='bold', color=MLRED)

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.set_ylabel('Token Volume (Thousands)', fontsize=12)
ax.set_ylim(0, 130)

ax.axvline(x=2.5, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Token Sinks vs. Faucets: Supply Dynamics', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
