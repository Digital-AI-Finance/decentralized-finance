"""Liquidity Provider Workflow"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

steps = ['Deposit\nTokens', 'Select\nFee Tier', 'Set Price\nRange (V3)', 'Earn\nFees', 'Monitor\nIL', 'Withdraw']
y_pos = [0.7, 0.7, 0.7, 0.3, 0.3, 0.3]
x_pos = [0.15, 0.4, 0.65, 0.15, 0.4, 0.65]
colors = [MLBLUE, MLORANGE, MLGREEN, MLGREEN, MLRED, MLPURPLE]

for x, y, step, col in zip(x_pos, y_pos, steps, colors):
    rect = mpatches.FancyBboxPatch((x-0.1, y-0.12), 0.2, 0.24, boxstyle="round,pad=0.02", facecolor=col, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, step, ha='center', va='center', fontsize=14, fontweight='bold', color='white')

ax.annotate('', xy=(0.3, 0.7), xytext=(0.25, 0.7), arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
ax.annotate('', xy=(0.55, 0.7), xytext=(0.5, 0.7), arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
ax.annotate('', xy=(0.65, 0.5), xytext=(0.65, 0.58), arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
ax.annotate('', xy=(0.5, 0.3), xytext=(0.55, 0.3), arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
ax.annotate('', xy=(0.25, 0.3), xytext=(0.3, 0.3), arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

ax.text(0.4, 0.9, 'SETUP PHASE', ha='center', va='center', fontsize=15, fontweight='bold', color='gray')
ax.text(0.4, 0.1, 'MONITORING PHASE', ha='center', va='center', fontsize=15, fontweight='bold', color='gray')

ax.set_xlim(0, 0.8)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Liquidity Provider Lifecycle', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
