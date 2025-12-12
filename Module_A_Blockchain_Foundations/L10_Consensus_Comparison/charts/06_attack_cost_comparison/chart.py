"""
Attack Cost Comparison
Shows the cost to attack different consensus mechanisms
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Attack Cost Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/06_attack_cost_comparison'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Attack scenarios and estimated costs (in billions USD)
attacks = [
    ('Bitcoin 51%\n(PoW)', 20, MLBLUE, 'Hardware + electricity\nfor 51% hash rate'),
    ('Ethereum 33%\n(PoS)', 40, MLGREEN, '33% of staked ETH\n~$40B at current prices'),
    ('Ethereum 67%\n(PoS - safety)', 80, MLGREEN, '67% stake to finalize\nconflicting blocks'),
    ('EOS Cartel\n(DPoS)', 0.5, MLORANGE, 'Bribe/compromise\n11 of 21 BPs'),
    ('Hyperledger\n(PBFT)', 0.01, MLPURPLE, 'Compromise 1/3 of\nknown validators'),
]

names = [a[0] for a in attacks]
costs = [a[1] for a in attacks]
colors = [a[2] for a in attacks]
descriptions = [a[3] for a in attacks]

# Horizontal bar chart with log scale
bars = ax.barh(names, costs, color=colors, edgecolor='black', linewidth=1)

ax.set_xscale('log')
ax.set_xlim(0.001, 200)

# Add cost labels
for bar, cost, desc in zip(bars, costs, descriptions):
    width = bar.get_width()
    if cost >= 1:
        label = f'${cost:.0f}B'
    else:
        label = f'${cost*1000:.0f}M'

    # Cost on the bar
    ax.text(width * 0.5, bar.get_y() + bar.get_height()/2, label,
            va='center', ha='center', fontsize=11, fontweight='bold', color='white')

    # Description on the right
    ax.text(width * 1.5, bar.get_y() + bar.get_height()/2, desc,
            va='center', fontsize=9, color='#555')

# Security insight annotation
props = dict(boxstyle='round,pad=0.3', facecolor='#FFE0E0', edgecolor=MLRED)
ax.text(0.005, -0.8, 'Lower cost = Higher vulnerability',
        fontsize=11, fontweight='bold', bbox=props, color=MLRED)

ax.set_xlabel('Estimated Attack Cost (USD, log scale)', fontsize=13)
ax.set_title('Cost to Attack Different Consensus Mechanisms', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
