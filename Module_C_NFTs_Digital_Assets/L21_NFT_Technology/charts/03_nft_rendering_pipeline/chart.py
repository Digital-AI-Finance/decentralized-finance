"""
NFT Rendering Pipeline
Shows how NFTs are displayed from contract to screen
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Rendering Pipeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/03_nft_rendering_pipeline'
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

# Pipeline steps
steps = [
    {'name': 'Wallet/DApp', 'desc': 'User requests\nNFT display', 'x': 0.10, 'color': '#E8E8E8'},
    {'name': 'Smart Contract', 'desc': 'tokenURI(id)\nreturns URI', 'x': 0.30, 'color': MLBLUE},
    {'name': 'IPFS/Server', 'desc': 'Fetch JSON\nmetadata', 'x': 0.50, 'color': MLORANGE},
    {'name': 'Image Storage', 'desc': 'Fetch image\nfrom URI', 'x': 0.70, 'color': MLGREEN},
    {'name': 'Display', 'desc': 'Render NFT\nwith traits', 'x': 0.90, 'color': MLPURPLE},
]

box_width = 0.14
box_height = 0.30

for i, step in enumerate(steps):
    # Main box
    box = FancyBboxPatch((step['x'] - box_width/2, 0.45), box_width, box_height,
                          boxstyle="round,pad=0.02", facecolor=step['color'],
                          edgecolor='black', linewidth=2, alpha=0.9)
    ax.add_patch(box)

    # Step number
    ax.text(step['x'], 0.72, f'{i+1}', ha='center', va='center',
            fontsize=16, fontweight='bold', color='white' if step['color'] not in ['#E8E8E8'] else 'black')

    # Step name
    ax.text(step['x'], 0.60, step['name'], ha='center', va='center',
            fontsize=9, fontweight='bold', color='white' if step['color'] not in ['#E8E8E8'] else 'black')

    # Description
    ax.text(step['x'], 0.50, step['desc'], ha='center', va='center',
            fontsize=8, color='white' if step['color'] not in ['#E8E8E8'] else 'black')

    # Arrow to next step
    if i < len(steps) - 1:
        ax.annotate('', xy=(steps[i+1]['x'] - box_width/2 - 0.02, 0.60),
                   xytext=(step['x'] + box_width/2 + 0.02, 0.60),
                   arrowprops=dict(arrowstyle='->', color='#444', lw=2))

# Data flow labels
flow_labels = ['Call', 'URI', 'JSON', 'Image']
for i, label in enumerate(flow_labels):
    ax.text(0.20 + i * 0.20, 0.82, label, ha='center', fontsize=9,
            color='#666', fontweight='bold')

# Key insight at bottom
ax.text(0.50, 0.20, 'Critical: If any step fails (server down, IPFS unpinned), NFT becomes unrenderable',
        ha='center', fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_xlim(0, 1)
ax.set_ylim(0.1, 0.95)
ax.axis('off')

ax.set_title('NFT Rendering Pipeline', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
