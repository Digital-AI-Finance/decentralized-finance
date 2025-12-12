"""
Bitcoin Fee Market Dynamics
Shows fee estimation and mempool congestion
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Fee Market',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/07_fee_market'
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

# Fee rate categories
categories = ['Economy\n(1+ hours)', 'Standard\n(30-60 min)', 'Priority\n(~10 min)', 'Urgent\n(next block)']
fees = [5, 15, 35, 80]  # sat/vB
colors = [MLGREEN, MLBLUE, MLORANGE, MLRED]

bars = ax.bar(categories, fees, color=colors, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar, fee in zip(bars, fees):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            f'{fee} sat/vB', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add cost estimate for typical transaction (250 vB)
ax.text(0.98, 0.95, 'Typical TX: ~250 vBytes', transform=ax.transAxes,
        ha='right', fontsize=11, color='#555', style='italic')

# Horizontal lines for context
ax.axhline(y=20, color='#888', linestyle='--', linewidth=1, alpha=0.5)
ax.text(3.5, 22, 'Average fee', fontsize=10, color='#555')

ax.set_ylabel('Fee Rate (satoshis/vByte)', fontsize=13)
ax.set_xlabel('Confirmation Speed', fontsize=13)
ax.set_ylim(0, 100)

# Add secondary y-axis for USD (approximate)
ax2 = ax.twinx()
ax2.set_ylim(0, 100 * 250 / 100000000 * 100000)  # Approximate USD at $100k/BTC
ax2.set_ylabel('Est. Fee (USD) @ $100k BTC', fontsize=11, color='#666')
ax2.tick_params(axis='y', labelcolor='#666')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#FFF8E0', edgecolor=MLORANGE, alpha=0.95)
ax.text(0.5, 85, 'Fee = Fee Rate x Transaction Size (vBytes)',
        ha='center', fontsize=12, fontweight='bold', bbox=props, color='#333')

ax.set_title('Bitcoin Fee Market: Pay for Priority', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
