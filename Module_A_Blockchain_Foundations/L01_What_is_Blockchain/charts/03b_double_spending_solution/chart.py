"""
Double Spending Solution - Blockchain Ordering
ONE figure only - shows how blockchain solves double spending
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Double Spending Solution - Blockchain Ordering',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/03b_double_spending_solution'
}

# MANDATORY: Font size 11pt minimum for readability after scaling
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

# Timeline with blocks
blocks = [
    (0.08, 'Block N\n(History)', '#E8E8E8', 'black'),
    (0.38, 'Block N+1\nAlice→Bob\n1 BTC', '#90EE90', MLGREEN),
    (0.68, 'Block N+2\nAlice→Charlie\nREJECTED', '#FFB6C1', MLRED),
]

for bx, label, facecolor, edgecolor in blocks:
    box = FancyBboxPatch((bx, 0.3), 0.22, 0.4, boxstyle="round,pad=0.02",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=3)
    ax.add_patch(box)
    ax.text(bx + 0.11, 0.5, label, ha='center', va='center', fontsize=15, fontweight='bold')

# Chain arrows
ax.annotate('', xy=(0.38, 0.5), xytext=(0.30, 0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=3))
ax.annotate('', xy=(0.68, 0.5), xytext=(0.60, 0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=3))

# Title
ax.text(0.5, 0.88, 'THE SOLUTION: Blockchain Ordering',
        ha='center', fontsize=14, fontweight='bold', color=MLGREEN)

# Explanation
ax.text(0.5, 0.78, 'First valid transaction wins — Network consensus determines order',
        ha='center', fontsize=15, style='italic')

# Rejection note
ax.text(0.79, 0.18, 'Insufficient\nbalance!', ha='center', fontsize=15,
        color=MLRED, fontweight='bold')

# Checkmark on accepted block
ax.text(0.49, 0.18, '✓ Confirmed', ha='center', fontsize=15,
        color=MLGREEN, fontweight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
