"""
Content Addressing vs Location Addressing
Shows how IPFS differs from traditional web
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Content vs Location Addressing',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS/charts/01_content_addressing'
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

# Left side - Location Addressing (HTTP)
ax.text(0.25, 0.92, 'Location Addressing (HTTP)', ha='center', fontsize=12,
        fontweight='bold', color=MLRED,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

# URL -> Server -> File
loc_boxes = [
    {'name': 'URL', 'desc': 'server.com/file.jpg', 'x': 0.08, 'y': 0.65},
    {'name': 'Server', 'desc': 'Central Host', 'x': 0.25, 'y': 0.65},
    {'name': 'File', 'desc': 'Image.jpg', 'x': 0.42, 'y': 0.65},
]

for b in loc_boxes:
    box = FancyBboxPatch((b['x'] - 0.06, b['y'] - 0.08), 0.12, 0.16,
                          boxstyle="round,pad=0.02", facecolor=MLRED,
                          edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(box)
    ax.text(b['x'], b['y'] + 0.02, b['name'], ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(b['x'], b['y'] - 0.04, b['desc'], ha='center', va='center',
            fontsize=7, color='white')

# Arrows
ax.annotate('', xy=(0.19, 0.65), xytext=(0.14, 0.65),
           arrowprops=dict(arrowstyle='->', color='#666', lw=2))
ax.annotate('', xy=(0.36, 0.65), xytext=(0.31, 0.65),
           arrowprops=dict(arrowstyle='->', color='#666', lw=2))

# Problem: Server down = 404
ax.text(0.25, 0.45, 'Server down = 404 Error', ha='center', fontsize=10,
        color=MLRED, fontweight='bold')

# Right side - Content Addressing (IPFS)
ax.text(0.75, 0.92, 'Content Addressing (IPFS)', ha='center', fontsize=12,
        fontweight='bold', color=MLGREEN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

# CID -> Any Node -> File
cont_boxes = [
    {'name': 'CID', 'desc': 'QmXyZ123...', 'x': 0.58, 'y': 0.65},
    {'name': 'Network', 'desc': 'P2P Nodes', 'x': 0.75, 'y': 0.65},
    {'name': 'File', 'desc': 'Image.jpg', 'x': 0.92, 'y': 0.65},
]

for b in cont_boxes:
    box = FancyBboxPatch((b['x'] - 0.06, b['y'] - 0.08), 0.12, 0.16,
                          boxstyle="round,pad=0.02", facecolor=MLGREEN,
                          edgecolor='black', linewidth=1.5, alpha=0.8)
    ax.add_patch(box)
    ax.text(b['x'], b['y'] + 0.02, b['name'], ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(b['x'], b['y'] - 0.04, b['desc'], ha='center', va='center',
            fontsize=7, color='white')

# Arrows
ax.annotate('', xy=(0.69, 0.65), xytext=(0.64, 0.65),
           arrowprops=dict(arrowstyle='->', color='#666', lw=2))
ax.annotate('', xy=(0.86, 0.65), xytext=(0.81, 0.65),
           arrowprops=dict(arrowstyle='->', color='#666', lw=2))

# Advantage: Multiple sources
ax.text(0.75, 0.45, 'Any node can serve file', ha='center', fontsize=10,
        color=MLGREEN, fontweight='bold')

# Key differences at bottom
differences = [
    ('Content can change at URL', 'Same content = Same CID'),
    ('Single point of failure', 'Distributed retrieval'),
    ('No integrity guarantee', 'Cryptographic verification'),
]

for i, (loc, cont) in enumerate(differences):
    y = 0.30 - i * 0.08
    ax.text(0.25, y, loc, ha='center', fontsize=9, color=MLRED)
    ax.text(0.75, y, cont, ha='center', fontsize=9, color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 1)
ax.axis('off')

ax.set_title('Content Addressing vs Location Addressing', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
