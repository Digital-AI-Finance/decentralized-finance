"""
Solana Token Distribution
Horizontal bar chart showing SOL allocation
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Solana Distribution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L30_Distribution_Vesting/charts/03_solana_distribution'
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

# Solana allocation breakdown
categories = ['Community & Ecosystem', 'Seed Sale', 'Team', 'Foundation',
              'Founding Sale', 'Validator Sale', 'Strategic', 'Public']
percentages = [38.9, 15.9, 12.5, 10.5, 5.1, 5.1, 1.8, 2.9]

# Colors: green for community, orange/red for insiders
colors = [MLGREEN, MLRED, MLORANGE, MLGRAY, MLRED, MLBLUE, MLRED, MLPURPLE]

y_pos = np.arange(len(categories))

bars = ax.barh(y_pos, percentages, color=colors, edgecolor='black', linewidth=0.5, height=0.6)

# Add value labels
for bar, val in zip(bars, percentages):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', ha='left', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=14)
ax.set_xlabel('Allocation (%)', fontsize=15)
ax.set_xlim(0, 45)

# Add insider annotation
ax.text(0.95, 0.95, 'Insiders: ~35%\nCommunity: ~65%', transform=ax.transAxes,
        ha='right', va='top', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.grid(True, alpha=0.3, axis='x')
ax.invert_yaxis()

ax.set_title('Solana (SOL) Token Distribution (2020)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
