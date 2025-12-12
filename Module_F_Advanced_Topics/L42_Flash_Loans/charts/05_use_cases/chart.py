"""
Flash Loan Legitimate Use Cases
Horizontal bar showing use case frequency
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Flash Loan Use Cases',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L42_Flash_Loans/charts/05_use_cases'
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

# Use cases and estimated transaction share
use_cases = ['DEX Arbitrage', 'Liquidations', 'Collateral\nSwap', 'Self-\nLiquidation', 'Debt\nRefinancing']
percentage = [50, 25, 12, 8, 5]
colors = [MLGREEN, MLBLUE, MLORANGE, MLPURPLE, '#9C27B0']
capital_required = ['$0', '$0', '$0', '$0', '$0']

y_pos = np.arange(len(use_cases))

bars = ax.barh(y_pos, percentage, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, pct in zip(bars, percentage):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{pct}%', va='center', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(use_cases, fontsize=14)
ax.set_xlabel('Share of Flash Loan Transactions (%)', fontsize=15)
ax.set_xlim(0, 65)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Annotation
ax.text(0.5, -0.15, 'All use cases require $0 upfront capital (only gas fees)',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Legitimate Flash Loan Use Cases', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
