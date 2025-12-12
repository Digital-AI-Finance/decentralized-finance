"""
MiCA Implementation Timeline
Horizontal timeline showing key milestones
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'MiCA Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L45_Global_Regulation/charts/05_mica_timeline'
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

# MiCA milestones
dates = [2020, 2022, 2023, 2024.5, 2025]
events = ['Proposal', 'Parliament\nApproval', 'Published\nin OJ', 'Stablecoin\nRules Active', 'Full\nImplementation']
colors = [MLBLUE, MLBLUE, MLGREEN, MLGREEN, MLGREEN]

# Draw timeline
ax.plot([2019.5, 2025.5], [0.5, 0.5], 'k-', linewidth=3, alpha=0.3)

# Plot milestones
for i, (date, event, color) in enumerate(zip(dates, events, colors)):
    ax.scatter(date, 0.5, s=200, c=color, edgecolors='black', linewidth=2, zorder=5)

    # Alternate label positions
    if i % 2 == 0:
        ax.text(date, 0.65, event, ha='center', va='bottom', fontsize=10, fontweight='bold')
        ax.plot([date, date], [0.5, 0.62], 'k-', linewidth=1)
    else:
        ax.text(date, 0.35, event, ha='center', va='top', fontsize=10, fontweight='bold')
        ax.plot([date, date], [0.5, 0.38], 'k-', linewidth=1)

# Add year labels
for date in dates:
    if date == 2024.5:
        ax.text(date, 0.48, 'Jun 2024', ha='center', va='top', fontsize=9, color='gray')
    elif date == 2025:
        ax.text(date, 0.52, 'Dec 2024', ha='center', va='bottom', fontsize=9, color='gray')
    else:
        ax.text(date, 0.48, str(int(date)), ha='center', va='top', fontsize=9, color='gray')

# Annotations
ax.annotate('Single framework\nfor 27 EU countries', xy=(2025, 0.5), xytext=(2024.2, 0.2),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_xlim(2019.5, 2025.8)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('EU MiCA Regulation Timeline', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
