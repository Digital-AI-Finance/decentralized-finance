"""
Dencun Upgrade Impact on L2 Fees
Before/After comparison
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Dencun Impact',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L41_Layer2_Scaling/charts/05_dencun_impact'
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

# L2 fee comparison before/after Dencun (March 2024)
l2s = ['Arbitrum', 'Base', 'Optimism', 'zkSync']
before_dencun = [0.50, 0.60, 0.55, 0.40]  # Average transaction cost in USD
after_dencun = [0.02, 0.01, 0.02, 0.03]   # After EIP-4844

x = np.arange(len(l2s))
width = 0.35

bars1 = ax.bar(x - width/2, before_dencun, width, label='Before Dencun (Feb 2024)',
               color=MLRED, edgecolor='black', alpha=0.8)
bars2 = ax.bar(x + width/2, after_dencun, width, label='After Dencun (Apr 2024)',
               color=MLGREEN, edgecolor='black', alpha=0.8)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'${height:.2f}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'${height:.2f}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Average Transaction Cost (USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(l2s, fontsize=12)
ax.set_ylim(0, 0.8)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Reduction annotation
ax.text(0.5, -0.15, 'EIP-4844 (Blobs) reduced L2 transaction costs by 90-95%',
        transform=ax.transAxes, ha='center', fontsize=11,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Dencun Upgrade Impact on L2 Transaction Costs', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
