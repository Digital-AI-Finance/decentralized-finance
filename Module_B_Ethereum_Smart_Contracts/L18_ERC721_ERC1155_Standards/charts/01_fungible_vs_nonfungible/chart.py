"""
Fungible vs Non-Fungible Tokens
Visual comparison of token types
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
from pathlib import Path

CHART_METADATA = {
    'title': 'Fungible vs Non-Fungible',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_Standards/charts/01_fungible_vs_nonfungible'
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

# Left side: Fungible (identical coins)
ax.text(0.25, 0.92, 'Fungible (ERC-20)', fontsize=14, fontweight='bold',
        ha='center', color=MLBLUE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

# Draw identical coins
for i in range(4):
    for j in range(2):
        circle = Circle((0.12 + i * 0.09, 0.68 - j * 0.12), 0.035,
                        facecolor=MLBLUE, edgecolor='black', linewidth=1)
        ax.add_patch(circle)
        ax.text(0.12 + i * 0.09, 0.68 - j * 0.12, '$', ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

ax.text(0.25, 0.42, '1 USDC = 1 USDC', ha='center', fontsize=11,
        fontweight='bold', family='monospace')
ax.text(0.25, 0.32, 'Interchangeable\nDivisible\nUniform value', ha='center', fontsize=10)

# Right side: Non-Fungible (unique items)
ax.text(0.75, 0.92, 'Non-Fungible (ERC-721)', fontsize=14, fontweight='bold',
        ha='center', color=MLORANGE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

# Draw unique items with different shapes/colors
shapes = [
    {'x': 0.58, 'y': 0.68, 'color': MLORANGE, 'id': '#1'},
    {'x': 0.70, 'y': 0.68, 'color': MLGREEN, 'id': '#2'},
    {'x': 0.82, 'y': 0.68, 'color': MLPURPLE, 'id': '#3'},
    {'x': 0.92, 'y': 0.68, 'color': MLRED, 'id': '#4'},
]

for shape in shapes:
    box = FancyBboxPatch((shape['x'] - 0.035, shape['y'] - 0.06), 0.07, 0.12,
                          boxstyle="round,pad=0.02", facecolor=shape['color'],
                          edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(shape['x'], shape['y'], shape['id'], ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

ax.text(0.75, 0.42, 'Token #1 != Token #2', ha='center', fontsize=11,
        fontweight='bold', family='monospace')
ax.text(0.75, 0.32, 'Unique ownership\nIndivisible\nIndividual value', ha='center', fontsize=10)

# Dividing line
ax.axvline(x=0.50, color='#888', linestyle='--', linewidth=1.5, alpha=0.5)

# Examples at bottom
ax.text(0.25, 0.10, 'Examples: USDC, DAI, UNI', ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))
ax.text(0.75, 0.10, 'Examples: BAYC, CryptoPunks, ENS', ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Fungible vs Non-Fungible Tokens', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
