"""
Market Cap vs Fully Diluted Valuation
Grouped bar showing dilution risk for various tokens
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Market Cap vs FDV',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L31_Token_Classification/charts/05_mcap_vs_fdv'
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

# Tokens and their Market Cap vs FDV (billions USD, illustrative)
tokens = ['BTC', 'ETH', 'SOL', 'New\nProject A', 'New\nProject B']
market_cap = [800, 300, 40, 1, 0.5]  # Current market cap
fdv = [840, 315, 60, 10, 5]  # Fully diluted valuation

x = np.arange(len(tokens))
width = 0.35

bars1 = ax.bar(x - width/2, market_cap, width, label='Market Cap', color=MLBLUE, edgecolor='black', linewidth=1)
bars2 = ax.bar(x + width/2, fdv, width, label='FDV', color=MLORANGE, edgecolor='black', linewidth=1)

# Add ratio labels
for i, (mc, fv) in enumerate(zip(market_cap, fdv)):
    ratio = fv / mc
    color = MLGREEN if ratio < 1.5 else (MLORANGE if ratio < 3 else MLRED)
    ax.annotate(f'{ratio:.1f}x',
                xy=(x[i], max(mc, fv) + 20),
                ha='center', fontsize=10, fontweight='bold', color=color)

ax.set_ylabel('Value (Billions USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(tokens, fontsize=10, fontweight='bold')
ax.set_ylim(0, 900)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Add warning annotation
ax.text(0.5, -0.12, 'High FDV/MC ratio (>3x) indicates significant future dilution risk',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Market Cap vs Fully Diluted Valuation (FDV)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
