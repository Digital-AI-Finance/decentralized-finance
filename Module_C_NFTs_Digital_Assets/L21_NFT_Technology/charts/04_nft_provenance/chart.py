"""NFT Provenance Chain"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.text(5, 6.5, 'NFT Provenance: Ownership Chain', fontsize=16, ha='center', fontweight='bold')
ax.plot([1, 9], [3.5, 3.5], color='#333333', lw=3, zorder=1)

events = [(1.5, 'Mint', 'Creator', '#3333B2', 'Jan 2022'),
          (3.5, 'Transfer', 'Collector A', '#0066CC', 'Mar 2022'),
          (5.5, 'Transfer', 'Gallery', '#2CA02C', 'Jun 2022'),
          (7.5, 'Transfer', 'Collector B', '#FF7F0E', 'Nov 2023')]

for x, event, name, color, date in events:
    circle = plt.Circle((x, 3.5), 0.2, color=color, zorder=2)
    ax.add_patch(circle)
    box = mpatches.FancyBboxPatch((x-0.7, 4.2), 1.4, 1.6, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', alpha=0.9)
    ax.add_patch(box)
    ax.text(x, 5.4, event, fontsize=14, ha='center', color='white', fontweight='bold')
    ax.text(x, 4.7, name, fontsize=14, ha='center', color='white')
    ax.text(x, 2.8, date, fontsize=14, ha='center', color='#666666')

ax.text(5, 1.5, 'Each Transfer event is permanently recorded on blockchain', fontsize=15, ha='center', style='italic', color='#666666', bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#CCCCCC'))
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
