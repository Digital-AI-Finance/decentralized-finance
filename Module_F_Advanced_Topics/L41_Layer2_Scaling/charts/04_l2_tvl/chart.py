"""
Layer 2 TVL Distribution (Q4 2024)
Horizontal bar chart
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'L2 TVL Distribution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L41_Layer2_Scaling/charts/04_l2_tvl'
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

# L2 TVL data (Q4 2024 approximate)
l2s = ['Arbitrum One', 'Base', 'OP Mainnet', 'zkSync Era', 'Polygon zkEVM', 'Scroll', 'Other']
tvl = [15, 8, 6, 4, 1.5, 1, 4.5]  # Billions USD
colors = ['#28A0F0', '#0052FF', '#FF0420', '#8B5CF6', '#7B3FE4', '#F0B90B', '#CCCCCC']
rollup_type = ['Optimistic', 'Optimistic', 'Optimistic', 'ZK', 'ZK', 'ZK', 'Mixed']

y_pos = np.arange(len(l2s))

bars = ax.barh(y_pos, tvl, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels and type annotations
for bar, val, rtype in zip(bars, tvl, rollup_type):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            f'${val}B ({rtype})', va='center', fontsize=10, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(l2s, fontsize=11)
ax.set_xlabel('Total Value Locked (Billion USD)', fontsize=12)
ax.set_xlim(0, 22)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Total annotation
total_tvl = sum(tvl)
ax.text(0.5, -0.12, f'Total L2 TVL: ~${total_tvl:.0f}B (up from $10B in early 2024)',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Ethereum L2 TVL Distribution (Q4 2024)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
