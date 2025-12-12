"""
Block Explorer Comparison
Features across different explorers
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Explorer Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L12_Lab_Block_Explorer/charts/03_explorer_comparison'
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

explorers = ['Etherscan', 'Blockchair', 'Blockchain.com', 'Mempool.space']
features = ['UI/UX', 'Multi-chain', 'API Access', 'Analytics', 'Contract Tools']

# Scores (1-10)
scores = np.array([
    [9, 7, 9, 8, 9],   # Etherscan
    [7, 10, 8, 9, 6],  # Blockchair
    [8, 6, 7, 6, 4],   # Blockchain.com
    [8, 3, 6, 7, 3],   # Mempool.space
])

x = np.arange(len(features))
width = 0.2
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

for i, (explorer, color) in enumerate(zip(explorers, colors)):
    offset = (i - 1.5) * width
    bars = ax.bar(x + offset, scores[i], width, label=explorer, color=color, edgecolor='black')

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(features, fontsize=14)
ax.set_ylim(0, 12)
ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Block Explorer Comparison by Feature', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
