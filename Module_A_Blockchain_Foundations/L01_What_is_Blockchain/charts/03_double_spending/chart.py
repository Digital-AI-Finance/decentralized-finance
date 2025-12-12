"""
Double Spending Problem Visualization
Shows the attack scenario and blockchain solution
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Double Spending Problem Visualization',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/03_double_spending'
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

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Left panel: The Problem (Digital copy attack)
ax1 = axes[0]
ax1.set_title('The Problem: Digital Copy Attack', fontweight='bold', fontsize=14, color=MLRED)

# Alice (attacker)
alice_box = FancyBboxPatch((0.15, 0.6), 0.2, 0.25, boxstyle="round,pad=0.02",
                            facecolor='#FFE4E1', edgecolor=MLRED, linewidth=2)
ax1.add_patch(alice_box)
ax1.text(0.25, 0.72, 'Alice\n(Attacker)', ha='center', va='center', fontsize=14, fontweight='bold')
ax1.text(0.25, 0.63, '1 BTC', ha='center', va='center', fontsize=14, color=MLORANGE)

# Bob
bob_box = FancyBboxPatch((0.65, 0.7), 0.2, 0.2, boxstyle="round,pad=0.02",
                          facecolor='#E6F3FF', edgecolor=MLBLUE, linewidth=2)
ax1.add_patch(bob_box)
ax1.text(0.75, 0.8, 'Bob', ha='center', va='center', fontsize=14, fontweight='bold')

# Charlie
charlie_box = FancyBboxPatch((0.65, 0.2), 0.2, 0.2, boxstyle="round,pad=0.02",
                              facecolor='#E6F3FF', edgecolor=MLBLUE, linewidth=2)
ax1.add_patch(charlie_box)
ax1.text(0.75, 0.3, 'Charlie', ha='center', va='center', fontsize=14, fontweight='bold')

# Arrows showing double spend
ax1.annotate('', xy=(0.65, 0.8), xytext=(0.35, 0.72),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax1.text(0.5, 0.82, 'Send 1 BTC', fontsize=14, ha='center', color=MLRED)

ax1.annotate('', xy=(0.65, 0.3), xytext=(0.35, 0.65),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax1.text(0.5, 0.4, 'Send same 1 BTC!', fontsize=14, ha='center', color=MLRED, fontweight='bold')

# Problem explanation
ax1.text(0.5, 0.05, 'Digital files can be copied infinitely\nNo inherent scarcity in bits',
         ha='center', fontsize=14, style='italic', color='gray')

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')

# Right panel: The Solution (Blockchain ordering)
ax2 = axes[1]
ax2.set_title('The Solution: Blockchain Ordering', fontweight='bold', fontsize=14, color=MLGREEN)

# Timeline with blocks
blocks_y = 0.5
for i, (bx, label, color) in enumerate([
    (0.15, 'Block N\n(history)', '#E8E8E8'),
    (0.4, 'Block N+1\nAlice->Bob\n1 BTC', '#90EE90'),
    (0.65, 'Block N+2\nAlice->Charlie\nREJECTED', '#FFB6C1'),
]):
    box = FancyBboxPatch((bx, 0.35), 0.2, 0.3, boxstyle="round,pad=0.02",
                          facecolor=color, edgecolor='black', linewidth=1.5)
    ax2.add_patch(box)
    ax2.text(bx + 0.1, 0.5, label, ha='center', va='center', fontsize=14)

# Chain arrows
ax2.annotate('', xy=(0.4, 0.5), xytext=(0.35, 0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax2.annotate('', xy=(0.65, 0.5), xytext=(0.6, 0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

# Explanation
ax2.text(0.45, 0.8, 'First valid transaction wins', fontsize=14, ha='center',
         fontweight='bold', color=MLGREEN)
ax2.text(0.45, 0.72, 'Network consensus determines order', fontsize=14, ha='center', style='italic')

# Rejection note
ax2.text(0.75, 0.25, 'Insufficient\nbalance!', fontsize=14, ha='center',
         color=MLRED, fontweight='bold')

ax2.text(0.5, 0.05, 'Immutable ordering prevents double-spend\nConsensus = single source of truth',
         ha='center', fontsize=14, style='italic', color='gray')

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')

plt.suptitle('The Double-Spending Problem and Its Solution', fontweight='bold', fontsize=15, y=0.98)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
