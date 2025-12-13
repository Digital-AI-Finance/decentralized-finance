"""NFT Rendering Pipeline"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.text(5, 6.5, 'NFT Rendering Pipeline', fontsize=16, ha='center', fontweight='bold')

steps = [(1, 4.5, '#3333B2', 'Smart\nContract'), (3.5, 4.5, '#0066CC', 'Metadata\nURI'),
         (6, 4.5, '#2CA02C', 'JSON\nMetadata'), (8.5, 4.5, '#FF7F0E', 'Media\nAsset')]

for x, y, color, title in steps:
    box = mpatches.FancyBboxPatch((x-0.7, y-0.8), 1.4, 1.6, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, title, fontsize=11, ha='center', va='center', color='white', fontweight='bold')

for x1, x2 in [(1.7, 2.6), (4.2, 5.1), (6.7, 7.6)]:
    ax.annotate('', xy=(x2, 4.5), xytext=(x1, 4.5), arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

failures = [(2.15, 3.2, 'Gateway\ndown?'), (4.65, 3.2, 'IPFS\nfailed?'), (7.15, 3.2, 'Server\noffline?')]
for x, y, text in failures:
    ax.text(x, y, text, fontsize=10, ha='center', color='#D62728', bbox=dict(boxstyle='round', facecolor='#FFE5E5', edgecolor='#D62728', alpha=0.8))

display = mpatches.FancyBboxPatch((3.5, 0.8), 3, 1.2, boxstyle="round,pad=0.1", facecolor='#1a1a2e', edgecolor='#333333', alpha=0.9)
ax.add_patch(display)
ax.text(5, 1.4, 'Displayed in Wallet', fontsize=12, ha='center', color='white')
ax.annotate('', xy=(5, 2.0), xytext=(8.5, 3.7), arrowprops=dict(arrowstyle='->', color='#333333', lw=2, connectionstyle='arc3,rad=-0.3'))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
