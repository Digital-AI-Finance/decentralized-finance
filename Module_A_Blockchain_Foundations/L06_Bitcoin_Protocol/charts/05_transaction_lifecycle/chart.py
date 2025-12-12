"""
Transaction Lifecycle
From creation to confirmation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Transaction Lifecycle',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/05_transaction_lifecycle'
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

# Stages
stages = [
    (0.10, 'Creation', 'Wallet creates\n& signs TX', MLBLUE),
    (0.30, 'Broadcast', 'Sent to\nnetwork nodes', MLORANGE),
    (0.50, 'Mempool', 'Pending in\nmemory pools', MLPURPLE),
    (0.70, 'Mining', 'Included in\ncandidate block', MLRED),
    (0.90, 'Confirmed', 'Block added\nto chain', MLGREEN),
]

y_center = 0.55

for x, title, desc, color in stages:
    # Circle for stage
    circle = Circle((x, y_center), 0.07, facecolor=color, edgecolor='#333', linewidth=2)
    ax.add_patch(circle)

    # Stage number
    idx = stages.index((x, title, desc, color)) + 1
    ax.text(x, y_center, str(idx), ha='center', va='center', fontsize=14,
            fontweight='bold', color='white')

    # Title above
    ax.text(x, y_center + 0.15, title, ha='center', fontsize=12,
            fontweight='bold', color=color)

    # Description below
    ax.text(x, y_center - 0.18, desc, ha='center', fontsize=10, color='#555')

# Arrows between stages
for i in range(len(stages) - 1):
    x1 = stages[i][0] + 0.08
    x2 = stages[i + 1][0] - 0.08
    ax.annotate('', xy=(x2, y_center), xytext=(x1, y_center),
                arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Confirmation timeline at bottom
ax.axhline(y=0.15, xmin=0.05, xmax=0.95, color='#ddd', linestyle='-', linewidth=2)

confirmations = [
    (0.70, '0 conf', 'Unconfirmed'),
    (0.78, '1 conf', '~10 min'),
    (0.86, '3 conf', '~30 min'),
    (0.94, '6 conf', '~1 hour\n(secure)'),
]

for x, label, time in confirmations:
    ax.plot(x, 0.15, 'o', markersize=8, color=MLGREEN if '6' in label else MLORANGE)
    ax.text(x, 0.20, label, ha='center', fontsize=9, fontweight='bold', color='#333')
    ax.text(x, 0.08, time, ha='center', fontsize=9, color='#555')

ax.text(0.50, 0.22, 'Confirmation Timeline', ha='center', fontsize=11,
        fontweight='bold', color='#333')

# Key insight
insight = 'More confirmations = Higher security (6+ for large amounts)'
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F4E8', edgecolor=MLGREEN)
ax.text(0.50, 0.88, insight, ha='center', fontsize=11, fontweight='bold',
        bbox=props, color='#333')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Bitcoin Transaction Lifecycle', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
