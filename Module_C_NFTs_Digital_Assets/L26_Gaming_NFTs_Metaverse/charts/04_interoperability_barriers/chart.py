"""
Interoperability Barriers
Horizontal bar chart showing challenges to cross-game assets
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Interoperability Barriers',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse/charts/04_interoperability_barriers'
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

# Barriers and their severity (1-10)
barriers = [
    ('3D Model\nCompatibility', 9, 'Technical'),
    ('Game\nBalance', 8, 'Game Design'),
    ('Art Style\nCoherence', 7, 'Aesthetic'),
    ('Revenue\nCannibalization', 9, 'Economic'),
    ('Legal/IP\nIssues', 6, 'Legal'),
]

labels = [b[0] for b in barriers]
severity = [b[1] for b in barriers]
categories = [b[2] for b in barriers]

# Color by category
color_map = {'Technical': MLBLUE, 'Game Design': MLORANGE,
             'Aesthetic': MLGREEN, 'Economic': MLRED, 'Legal': MLPURPLE}
colors = [color_map[c] for c in categories]

y_pos = np.arange(len(labels))

bars = ax.barh(y_pos, severity, color=colors, edgecolor='black', linewidth=0.5, height=0.6)

# Add value labels
for i, (bar, sev) in enumerate(zip(bars, severity)):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{sev}/10', va='center', ha='left', fontsize=11, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10, fontweight='bold')
ax.set_xlabel('Severity (1-10)', fontsize=12)
ax.set_xlim(0, 11)
ax.grid(True, alpha=0.3, axis='x')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, label='Technical'),
    Patch(facecolor=MLORANGE, label='Game Design'),
    Patch(facecolor=MLRED, label='Economic'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

# Note
ax.text(0.5, -0.12, 'Result: Very limited cross-game interoperability exists today',
        transform=ax.transAxes, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Barriers to Cross-Game Asset Interoperability', fontweight='bold', fontsize=15, pad=10)
ax.invert_yaxis()
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
