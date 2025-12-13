"""ERC-721 State Structure"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.text(5, 6.5, 'ERC-721 Contract State', fontsize=16, ha='center', fontweight='bold')

boxes = [
    (0.5, 4, '_owners', 'mapping(uint256 => address)', 'tokenId -> owner', '#3333B2'),
    (5.5, 4, '_balances', 'mapping(address => uint256)', 'owner -> count', '#0066CC'),
    (0.5, 1.5, '_tokenApprovals', 'mapping(uint256 => address)', 'tokenId -> approved', '#2CA02C'),
    (5.5, 1.5, '_operatorApprovals', 'mapping(addr => addr => bool)', 'owner -> op -> bool', '#FF7F0E'),
]

for x, y, title, mapping, desc, color in boxes:
    box = mpatches.FancyBboxPatch((x, y), 4, 2, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', alpha=0.8)
    ax.add_patch(box)
    ax.text(x+2, y+1.5, title, fontsize=14, ha='center', color='white', fontweight='bold')
    ax.text(x+2, y+0.8, mapping, fontsize=14, ha='center', color='white')
    ax.text(x+2, y+0.3, desc, fontsize=14, ha='center', color='#CCCCFF')

ax.text(5, 0.5, 'All mappings provide O(1) lookup time', fontsize=15, ha='center', style='italic', color='#666666')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
