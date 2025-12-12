"""
Anchor Protocol Math: Revenue vs Expenses
Horizontal bar showing the unsustainable deficit
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Anchor Protocol Math',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L39_Terra_Luna_Case_Study/charts/02_anchor_math'
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

# Anchor Protocol annual economics
categories = ['Interest Paid to\nDepositors (20% APY)', 'Interest Received\nfrom Borrowers (~12%)', 'Annual\nDeficit']
values = [2800, 480, -2320]  # Millions USD
colors = [MLRED, MLGREEN, '#FF6666']

y_pos = np.arange(len(categories))

# Plot bars (absolute values for deficit)
bar_values = [2800, 480, 2320]
bars = ax.barh(y_pos, bar_values, color=colors, edgecolor='black', linewidth=1.5, height=0.5)

# Add value labels
labels = ['$2.8B OUT', '$0.48B IN', '$2.32B GAP']
for i, (bar, label) in enumerate(zip(bars, labels)):
    ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2,
            label, va='center', fontsize=12, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=11)
ax.set_xlabel('Annual Amount (Million USD)', fontsize=12)
ax.set_xlim(0, 3500)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Add annotation
ax.text(0.5, -0.15, 'Anchor needed $2.3B/year in subsidies to maintain 20% APY - unsustainable!',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Anchor Protocol: Why 20% APY Was Unsustainable', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
