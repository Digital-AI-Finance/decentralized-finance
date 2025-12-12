"""
Casper FFG Finality Mechanism
Shows justification and finalization process
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Casper FFG Finality',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/04_casper_ffg'
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

# Epochs as checkpoints
epochs = [
    (0.10, 'Epoch N-2', MLGREEN, 'FINALIZED'),
    (0.35, 'Epoch N-1', MLGREEN, 'FINALIZED'),
    (0.60, 'Epoch N', MLORANGE, 'JUSTIFIED'),
    (0.85, 'Epoch N+1', MLLAVENDER, 'PENDING'),
]

y = 0.50

for x, label, color, status in epochs:
    box = FancyBboxPatch((x - 0.10, y - 0.15), 0.20, 0.30,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.05, label, ha='center', va='center',
            fontsize=11, fontweight='bold',
            color='white' if color in [MLGREEN, MLORANGE] else '#333')
    ax.text(x, y - 0.05, status, ha='center', va='center',
            fontsize=10, color='white' if color in [MLGREEN, MLORANGE] else '#555')

# Arrows between epochs
for i in range(len(epochs) - 1):
    x1 = epochs[i][0] + 0.10
    x2 = epochs[i + 1][0] - 0.10
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Voting arrows (curved) from validators to checkpoints
ax.text(0.50, 0.20, '67%+ validators vote on (source, target) pairs',
        ha='center', fontsize=11, color='#333', fontweight='bold')

# Justification and Finalization explanation
ax.text(0.10, 0.85, 'Justified: 67%+ attestations', ha='center',
        fontsize=10, color=MLORANGE, fontweight='bold')
ax.text(0.35, 0.85, 'Finalized: Justified + next justified', ha='center',
        fontsize=10, color=MLGREEN, fontweight='bold')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#FFE0E0', edgecolor=MLRED)
ax.text(0.50, 0.08, 'Reverting finalized block requires 33%+ stake to be slashed',
        ha='center', fontsize=11, fontweight='bold', bbox=props, color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Casper FFG: Justification and Finalization', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
