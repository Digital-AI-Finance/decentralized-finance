"""Remix IDE Interface Components"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

# Main areas
areas = [
    (0.02, 0.2, 0.15, 0.7, 'File\nExplorer', MLBLUE),
    (0.18, 0.2, 0.45, 0.7, 'Code\nEditor', MLGREEN),
    (0.64, 0.2, 0.34, 0.7, 'Deploy &\nInteract', MLORANGE),
    (0.02, 0.02, 0.96, 0.15, 'Terminal / Console', MLPURPLE),
]

for x, y, w, h, label, color in areas:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", facecolor=color, edgecolor='black', linewidth=2, alpha=0.8)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=14, fontweight='bold', color='white')

ax.text(0.5, 0.95, 'Remix IDE Layout', ha='center', va='center', fontsize=14, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
print(f"Chart saved")
