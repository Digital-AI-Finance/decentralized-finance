"""
51% Attack Visualization
Shows attack mechanism and cost
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': '51% Attack',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/06_attack_51percent'
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

# Title
ax.text(0.50, 0.95, 'Double-Spend Attack Timeline', ha='center', fontsize=14,
        fontweight='bold', color=MLPURPLE)

# Main chain (honest)
y_honest = 0.70
blocks_honest = [
    (0.08, 'B1', MLBLUE),
    (0.22, 'B2', MLBLUE),
    (0.36, 'B3', MLBLUE),
    (0.50, 'B4', MLBLUE),
]

for x, label, color in blocks_honest:
    box = FancyBboxPatch((x - 0.05, y_honest - 0.08), 0.10, 0.16,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y_honest, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

# Arrows between honest blocks
for i in range(len(blocks_honest) - 1):
    ax.annotate('', xy=(blocks_honest[i+1][0] - 0.06, y_honest),
                xytext=(blocks_honest[i][0] + 0.06, y_honest),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

ax.text(0.02, y_honest, 'Honest\nChain', ha='center', va='center',
        fontsize=10, fontweight='bold', color=MLBLUE)

# Attack chain (secret)
y_attack = 0.40
blocks_attack = [
    (0.36, 'B3*', MLRED),
    (0.50, 'B4*', MLRED),
    (0.64, 'B5*', MLRED),
    (0.78, 'B6*', MLRED),
]

for x, label, color in blocks_attack:
    box = FancyBboxPatch((x - 0.05, y_attack - 0.08), 0.10, 0.16,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y_attack, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

# Arrows between attack blocks
for i in range(len(blocks_attack) - 1):
    ax.annotate('', xy=(blocks_attack[i+1][0] - 0.06, y_attack),
                xytext=(blocks_attack[i][0] + 0.06, y_attack),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Fork from B2
ax.annotate('', xy=(0.31, y_attack + 0.08), xytext=(0.27, y_honest - 0.08),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2,
                           connectionstyle="arc3,rad=-0.2"))

ax.text(0.02, y_attack, 'Attacker\nChain', ha='center', va='center',
        fontsize=10, fontweight='bold', color=MLRED)

# Transaction annotation
ax.text(0.50, y_honest + 0.18, 'TX: Pay merchant', ha='center', fontsize=10,
        color=MLBLUE, style='italic')
ax.text(0.50, y_attack - 0.18, 'TX*: Pay self (no merchant)', ha='center', fontsize=10,
        color=MLRED, style='italic')

# Longer chain wins
ax.annotate('', xy=(0.85, 0.55), xytext=(0.85, y_attack + 0.08),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(0.88, 0.52, 'Attacker\nbroadcasts\nlonger chain', ha='left', fontsize=9,
        fontweight='bold', color=MLGREEN)

# Cost box
cost_box = FancyBboxPatch((0.05, 0.05), 0.40, 0.18,
                           boxstyle="round,pad=0.02", facecolor='#FFE0E0',
                           edgecolor=MLRED, linewidth=2)
ax.add_patch(cost_box)
ax.text(0.25, 0.18, 'Bitcoin 51% Attack Cost:', ha='center', fontsize=11,
        fontweight='bold', color=MLRED)
ax.text(0.25, 0.10, '~$7 billion (hardware + electricity)', ha='center', fontsize=10,
        color='#333')

# Defense box
defense_box = FancyBboxPatch((0.55, 0.05), 0.40, 0.18,
                              boxstyle="round,pad=0.02", facecolor='#E0FFE0',
                              edgecolor=MLGREEN, linewidth=2)
ax.add_patch(defense_box)
ax.text(0.75, 0.18, 'Defense:', ha='center', fontsize=11,
        fontweight='bold', color=MLGREEN)
ax.text(0.75, 0.10, 'Wait for 6+ confirmations', ha='center', fontsize=10,
        color='#333')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('51% Attack: Double-Spend Mechanism', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
