"""
Throughput Comparison
Bar chart showing TPS by blockchain/consensus type
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Throughput Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/02_throughput_comparison'
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

# Data: blockchain, TPS, consensus type
blockchains = ['Bitcoin', 'Litecoin', 'Ethereum', 'Cardano', 'EOS', 'Solana', 'Hyperledger', 'Visa']
tps = [7, 56, 30, 250, 4000, 65000, 10000, 24000]
consensus = ['PoW', 'PoW', 'PoS', 'PoS', 'DPoS', 'PoH+PoS', 'PBFT', 'Centralized']

# Colors based on consensus type
color_map = {
    'PoW': MLBLUE,
    'PoS': MLGREEN,
    'DPoS': MLORANGE,
    'PoH+PoS': MLRED,
    'PBFT': MLPURPLE,
    'Centralized': MLLAVENDER
}
colors = [color_map[c] for c in consensus]

bars = ax.barh(blockchains, tps, color=colors, edgecolor='black', linewidth=0.5)

# Use log scale for x-axis
ax.set_xscale('log')
ax.set_xlim(1, 100000)

# Add TPS values as labels
for bar, t in zip(bars, tps):
    width = bar.get_width()
    label_x = width * 1.2 if width < 50000 else width * 0.3
    ax.text(label_x, bar.get_y() + bar.get_height()/2, f'{t:,} TPS',
            va='center', fontsize=14, fontweight='bold')

# Legend for consensus types
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, edgecolor='black', label='Proof of Work'),
    Patch(facecolor=MLGREEN, edgecolor='black', label='Proof of Stake'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='Delegated PoS'),
    Patch(facecolor=MLPURPLE, edgecolor='black', label='PBFT'),
    Patch(facecolor=MLLAVENDER, edgecolor='black', label='Centralized'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=14)

ax.set_xlabel('Transactions Per Second (log scale)', fontsize=16)
ax.set_title('Blockchain Throughput Comparison', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
