"""
Decentralization Spectrum
Horizontal visualization showing decentralization levels
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Decentralization Spectrum',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/05_decentralization_spectrum'
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

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(1, -1)
ax.imshow(gradient, aspect='auto', cmap='RdYlGn', extent=[0, 100, 0, 1], alpha=0.3)

# Blockchains with their decentralization scores (0-100)
blockchains = [
    ('Bitcoin (PoW)', 85, MLBLUE, '15K+ nodes\n~4 pools control 51%'),
    ('Ethereum (PoS)', 70, MLGREEN, '7K+ nodes\n900K+ validators'),
    ('Cardano (PoS)', 60, MLGREEN, '3K+ pools\nStake concentration'),
    ('Solana (PoH)', 40, MLORANGE, '1.5K validators\nHigh hardware req.'),
    ('EOS (DPoS)', 20, MLORANGE, '21 block producers'),
    ('Hyperledger (PBFT)', 5, MLPURPLE, '10-100 validators\nPermissioned'),
]

y_positions = np.linspace(0.85, 0.15, len(blockchains))

for (name, score, color, detail), y in zip(blockchains, y_positions):
    # Plot marker
    ax.scatter(score, y, s=200, color=color, edgecolor='black', linewidth=2, zorder=5)

    # Name label
    ax.text(score, y + 0.08, name, ha='center', va='bottom', fontsize=14, fontweight='bold')

    # Detail below
    ax.text(score, y - 0.08, detail, ha='center', va='top', fontsize=14, color='#555')

# Arrow and labels for spectrum
ax.annotate('', xy=(95, 0.02), xytext=(5, 0.02),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.text(5, -0.05, 'CENTRALIZED', ha='left', fontsize=14, fontweight='bold', color=MLRED)
ax.text(95, -0.05, 'DECENTRALIZED', ha='right', fontsize=14, fontweight='bold', color=MLGREEN)

# Nakamoto coefficient annotation
props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#333')
ax.text(50, 0.97, 'Nakamoto Coefficient = min. entities to control 51%/33%',
        ha='center', fontsize=14, bbox=props)

ax.set_xlim(0, 100)
ax.set_ylim(-0.15, 1.05)
ax.axis('off')

ax.set_title('Blockchain Decentralization Spectrum', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
