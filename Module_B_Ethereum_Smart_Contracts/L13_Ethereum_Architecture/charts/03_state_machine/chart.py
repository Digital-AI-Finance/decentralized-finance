"""
Ethereum State Machine
State transition via transactions
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'State Machine',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/03_state_machine'
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

# State boxes
state_t = FancyBboxPatch((0.05, 0.30), 0.25, 0.40,
                          boxstyle="round,pad=0.02", facecolor=MLBLUE,
                          edgecolor='black', linewidth=2)
ax.add_patch(state_t)
ax.text(0.175, 0.60, 'State $S_t$', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.175, 0.45, 'Block N', ha='center', fontsize=10, color='white')

state_t1 = FancyBboxPatch((0.70, 0.30), 0.25, 0.40,
                           boxstyle="round,pad=0.02", facecolor=MLGREEN,
                           edgecolor='black', linewidth=2)
ax.add_patch(state_t1)
ax.text(0.825, 0.60, 'State $S_{t+1}$', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.825, 0.45, 'Block N+1', ha='center', fontsize=10, color='white')

# Transaction arrow
ax.annotate('', xy=(0.68, 0.50), xytext=(0.32, 0.50),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=3))

# Transaction box
tx_box = FancyBboxPatch((0.38, 0.55), 0.24, 0.15,
                         boxstyle="round,pad=0.01", facecolor=MLORANGE,
                         edgecolor='black', linewidth=1.5)
ax.add_patch(tx_box)
ax.text(0.50, 0.62, 'Transaction T', ha='center', fontsize=11, fontweight='bold', color='white')

# Formula
ax.text(0.50, 0.78, '$S_{t+1} = Y(S_t, T)$', ha='center', fontsize=16,
        fontweight='bold', color='#333')
ax.text(0.50, 0.88, 'State Transition Function', ha='center', fontsize=12,
        color='#555')

# State components (simplified)
ax.text(0.175, 0.35, 'Balances', ha='center', fontsize=9, color='white')
ax.text(0.175, 0.32, 'Nonces, Code', ha='center', fontsize=8, color='white')

ax.text(0.825, 0.35, 'Updated', ha='center', fontsize=9, color='white')
ax.text(0.825, 0.32, 'Balances, etc.', ha='center', fontsize=8, color='white')

# Execution steps at bottom
steps = ['Validate', 'Deduct Gas', 'Execute', 'Update State', 'Refund']
step_x = np.linspace(0.12, 0.88, len(steps))
for x, step in zip(step_x, steps):
    props = dict(boxstyle='round,pad=0.2', facecolor='#E8E8E8', edgecolor='#888')
    ax.text(x, 0.12, step, ha='center', fontsize=9, bbox=props)

# Arrows between steps
for i in range(len(steps) - 1):
    ax.annotate('', xy=(step_x[i+1] - 0.08, 0.12), xytext=(step_x[i] + 0.08, 0.12),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1))

ax.text(0.50, 0.03, 'Transaction Execution Flow', ha='center', fontsize=10,
        fontweight='bold', color='#555')

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('Ethereum: Deterministic State Machine', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
