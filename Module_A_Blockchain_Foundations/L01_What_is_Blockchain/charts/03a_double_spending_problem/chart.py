"""
Double Spending Problem - The Attack Scenario
ONE figure only - shows why digital money can be copied
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Double Spending Problem - Attack Scenario',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/03a_double_spending_problem'
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

# Alice (attacker) - center left
alice_box = FancyBboxPatch((0.1, 0.35), 0.2, 0.3, boxstyle="round,pad=0.02",
                            facecolor='#FFE4E1', edgecolor=MLRED, linewidth=3)
ax.add_patch(alice_box)
ax.text(0.2, 0.55, 'Alice', ha='center', va='center', fontsize=14, fontweight='bold')
ax.text(0.2, 0.42, '1 BTC', ha='center', va='center', fontsize=15, color=MLORANGE, fontweight='bold')

# Bob - top right
bob_box = FancyBboxPatch((0.65, 0.6), 0.2, 0.25, boxstyle="round,pad=0.02",
                          facecolor='#E6F3FF', edgecolor=MLBLUE, linewidth=3)
ax.add_patch(bob_box)
ax.text(0.75, 0.72, 'Bob', ha='center', va='center', fontsize=14, fontweight='bold')

# Charlie - bottom right
charlie_box = FancyBboxPatch((0.65, 0.15), 0.2, 0.25, boxstyle="round,pad=0.02",
                              facecolor='#E6F3FF', edgecolor=MLBLUE, linewidth=3)
ax.add_patch(charlie_box)
ax.text(0.75, 0.27, 'Charlie', ha='center', va='center', fontsize=14, fontweight='bold')

# Arrow to Bob
ax.annotate('', xy=(0.65, 0.72), xytext=(0.3, 0.55),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=3))
ax.text(0.48, 0.72, 'Send 1 BTC', fontsize=15, ha='center', color=MLRED, fontweight='bold')

# Arrow to Charlie (same BTC!)
ax.annotate('', xy=(0.65, 0.27), xytext=(0.3, 0.42),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=3))
ax.text(0.48, 0.25, 'Send same 1 BTC!', fontsize=15, ha='center', color=MLRED, fontweight='bold')

# Problem statement
ax.text(0.5, 0.92, 'THE PROBLEM: Digital files can be copied',
        ha='center', fontsize=14, fontweight='bold', color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
