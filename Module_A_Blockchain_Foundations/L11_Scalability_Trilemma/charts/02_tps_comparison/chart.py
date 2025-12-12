"""
TPS Comparison Across Blockchains
Bar chart showing throughput
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'TPS Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/02_tps_comparison'
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

# Data
blockchains = ['Bitcoin', 'Ethereum\nL1', 'Cardano', 'Polkadot', 'EOS', 'Avalanche', 'Solana', 'Visa']
tps = [7, 30, 250, 1000, 4000, 4500, 65000, 24000]
nodes = ['15K nodes', '7K nodes', '3K nodes', '1K nodes', '21 BPs', '1.3K nodes', '2K nodes', 'Centralized']

# Colors based on decentralization
colors = [MLBLUE, MLBLUE, MLGREEN, MLGREEN, MLORANGE, MLORANGE, MLRED, MLLAVENDER]

bars = ax.bar(blockchains, tps, color=colors, edgecolor='black', linewidth=0.5)

# Log scale
ax.set_yscale('log')
ax.set_ylim(1, 100000)

# Add TPS labels on bars
for bar, t, n in zip(bars, tps, nodes):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height * 1.2,
            f'{t:,}', ha='center', fontsize=14, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, height * 0.4,
            n, ha='center', fontsize=14, color='white', rotation=90)

# Reference lines
ax.axhline(y=24000, color=MLLAVENDER, linestyle='--', alpha=0.7, linewidth=1.5)
ax.text(7.5, 28000, 'Visa avg.', ha='right', fontsize=14, color='#666')

ax.set_ylabel('Transactions Per Second (log scale)', fontsize=16)
ax.set_title('Layer 1 Throughput: TPS vs Decentralization Trade-off', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='y')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, edgecolor='black', label='High Decentralization'),
    Patch(facecolor=MLGREEN, edgecolor='black', label='Medium Decentralization'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='Low Decentralization'),
    Patch(facecolor=MLRED, edgecolor='black', label='Vertical Scaling'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=14)

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
