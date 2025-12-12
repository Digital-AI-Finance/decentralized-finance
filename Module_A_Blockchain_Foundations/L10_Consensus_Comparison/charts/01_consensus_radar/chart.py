"""
Consensus Mechanism Radar Chart
Compares PoW, PoS, DPoS, PBFT across key metrics
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Consensus Radar',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/01_consensus_radar'
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

# Categories for comparison (0-10 scale)
categories = ['Decentralization', 'Throughput', 'Energy\nEfficiency',
              'Finality\nSpeed', 'Security', 'Permissionless']
N = len(categories)

# Scores for each consensus mechanism (0-10)
pow_scores = [9, 2, 1, 2, 10, 10]  # PoW
pos_scores = [7, 5, 9, 6, 8, 10]   # PoS
dpos_scores = [3, 8, 9, 9, 6, 8]   # DPoS
pbft_scores = [1, 9, 9, 10, 5, 1]  # PBFT

# Compute angle for each category
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Complete the loop

# Add first value to end to close the polygon
pow_scores += pow_scores[:1]
pos_scores += pos_scores[:1]
dpos_scores += dpos_scores[:1]
pbft_scores += pbft_scores[:1]

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))

# Plot each consensus mechanism
ax.plot(angles, pow_scores, 'o-', linewidth=2, color=MLBLUE, label='PoW (Bitcoin)')
ax.fill(angles, pow_scores, alpha=0.1, color=MLBLUE)

ax.plot(angles, pos_scores, 's-', linewidth=2, color=MLGREEN, label='PoS (Ethereum)')
ax.fill(angles, pos_scores, alpha=0.1, color=MLGREEN)

ax.plot(angles, dpos_scores, '^-', linewidth=2, color=MLORANGE, label='DPoS (EOS)')
ax.fill(angles, dpos_scores, alpha=0.1, color=MLORANGE)

ax.plot(angles, pbft_scores, 'd-', linewidth=2, color=MLPURPLE, label='PBFT (Hyperledger)')
ax.fill(angles, pbft_scores, alpha=0.1, color=MLPURPLE)

# Set category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=11)

# Set radial limits
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], size=9)

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.05), fontsize=11)

plt.title('Consensus Mechanism Comparison', fontweight='bold', fontsize=15, pad=20)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
