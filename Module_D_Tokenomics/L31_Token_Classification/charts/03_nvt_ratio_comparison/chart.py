"""
NVT Ratio Comparison Across Tokens
Bar chart showing NVT ratios for major cryptocurrencies
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NVT Ratio Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L31_Token_Classification/charts/03_nvt_ratio_comparison'
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
MLGRAY = '#888888'

fig, ax = plt.subplots(figsize=(10, 6))

# Tokens and their NVT ratios (approximate 2024 values)
tokens = ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'ADA']
nvt_ratios = [75, 30, 25, 20, 15, 40]  # Higher = store of value, Lower = payment/DeFi

# Color based on interpretation
colors = []
for nvt in nvt_ratios:
    if nvt > 50:
        colors.append(MLORANGE)  # Store of value
    elif nvt > 30:
        colors.append(MLBLUE)  # Moderate
    else:
        colors.append(MLGREEN)  # High utility

bars = ax.bar(tokens, nvt_ratios, color=colors, edgecolor='black', linewidth=1)

# Add value labels
for bar, val in zip(bars, nvt_ratios):
    ax.annotate(f'{val}',
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 5), textcoords='offset points',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add interpretation zones
ax.axhline(y=50, color=MLORANGE, linestyle='--', alpha=0.5)
ax.text(5.6, 52, 'Store of Value\n(NVT > 50)', fontsize=9, va='bottom', color=MLORANGE)

ax.axhline(y=20, color=MLGREEN, linestyle='--', alpha=0.5)
ax.text(5.6, 12, 'High Utility\n(NVT < 20)', fontsize=9, va='bottom', color=MLGREEN)

ax.set_ylabel('NVT Ratio (Market Cap / Daily Tx Volume)', fontsize=11)
ax.set_ylim(0, 90)

ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Network Value to Transactions (NVT) Ratio Comparison', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
