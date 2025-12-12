"""
ERC-721 State Structure
Visual diagram of ERC-721 contract state
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

CHART_METADATA = {
    'title': 'ERC-721 State Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/02_erc721_state_structure'
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

# Contract header
contract_box = FancyBboxPatch((0.05, 0.75), 0.90, 0.18,
                               boxstyle="round,pad=0.02", facecolor=MLPURPLE,
                               edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(contract_box)
ax.text(0.50, 0.86, 'ERC-721 Smart Contract', ha='center', va='center',
        fontsize=14, fontweight='bold', color='white')
ax.text(0.50, 0.79, 'contract MyNFT is ERC721 { ... }', ha='center',
        fontsize=14, color='#DDD', family='monospace')

# State variables
mappings = [
    {'name': '_owners', 'desc': 'tokenId => owner', 'example': '1 => 0xAlice', 'color': MLBLUE, 'x': 0.08},
    {'name': '_balances', 'desc': 'owner => count', 'example': '0xAlice => 3', 'color': MLGREEN, 'x': 0.32},
    {'name': '_approvals', 'desc': 'tokenId => spender', 'example': '1 => 0xBob', 'color': MLORANGE, 'x': 0.56},
    {'name': '_operators', 'desc': 'owner => op => bool', 'example': 'Alice=>OpenSea=>true', 'color': MLRED, 'x': 0.80},
]

for m in mappings:
    # Mapping box
    box = FancyBboxPatch((m['x'] - 0.10, 0.25), 0.22, 0.40,
                          boxstyle="round,pad=0.02", facecolor=m['color'],
                          edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(m['x'], 0.58, m['name'], ha='center', va='center',
            fontsize=14, fontweight='bold', color='white', family='monospace')
    ax.text(m['x'], 0.48, m['desc'], ha='center', va='center',
            fontsize=14, color='white')

    # Example box
    ax.text(m['x'], 0.35, m['example'], ha='center', va='center',
            fontsize=14, color='white', family='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=m['color'], alpha=0.3))

# Description at bottom
ax.text(0.50, 0.12, 'Mappings provide O(1) lookup by key - efficient for sparse token IDs',
        ha='center', fontsize=14, style='italic', color='#555')

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 0.98)
ax.axis('off')

ax.set_title('ERC-721 Contract State Variables', fontweight='bold', fontsize=15, pad=5)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
