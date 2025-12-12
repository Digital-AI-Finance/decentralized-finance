"""
2024-2025 Crypto Milestones
Timeline of major events
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': '2024 Milestones',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L48_Course_Synthesis/charts/04_2024_milestones'
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

# Timeline events
events = [
    (1, 'Jan 2024', 'Bitcoin ETF\nApproved', MLGREEN, 'top'),
    (3, 'Mar 2024', 'Dencun\nUpgrade', MLPURPLE, 'bottom'),
    (4, 'Apr 2024', 'Bitcoin\nHalving', MLORANGE, 'top'),
    (7, 'Jul 2024', 'Ethereum\nETF Launch', MLBLUE, 'bottom'),
    (12, 'Dec 2024', 'MiCA\nFull Force', MLRED, 'top'),
    (14, '2025', 'Digital Euro\nDecision', MLGREEN, 'bottom'),
]

# Draw timeline
ax.axhline(y=0.5, color='gray', linewidth=2, zorder=1)

# Add events
for x, date, label, color, pos in events:
    y_offset = 0.7 if pos == 'top' else 0.3
    y_text = 0.85 if pos == 'top' else 0.15

    # Vertical line
    ax.plot([x, x], [0.5, y_offset], color=color, linewidth=2, zorder=2)

    # Circle marker
    ax.scatter([x], [y_offset], s=150, c=color, edgecolors='black', linewidth=1.5, zorder=3)

    # Date label
    ax.text(x, 0.5 + (0.05 if pos == 'top' else -0.05), date,
            ha='center', va='bottom' if pos == 'top' else 'top',
            fontsize=14, fontweight='bold')

    # Event label
    ax.text(x, y_text, label, ha='center', va='center',
            fontsize=14, color=color,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.9))

# Add BTC price annotation
ax.annotate('BTC: $100K+', xy=(13, 0.5), xytext=(13, 0.75),
            fontsize=14, ha='center', fontweight='bold', color=MLORANGE,
            arrowprops=dict(arrowstyle='->', color=MLORANGE))

ax.set_xlim(0, 16)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('2024-2025 Crypto Industry Milestones', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
