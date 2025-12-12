"""
Token Minting Strategies
Shows different approaches to token minting
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Minting Strategies',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard/charts/05_minting_strategies'
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

# Minting strategies
strategies = [
    {
        'name': 'Fixed Supply',
        'color': MLBLUE,
        'examples': 'BTC, LINK',
        'desc': 'All tokens minted at launch\nNo future minting possible',
        'trust': 'None needed',
        'x': 0.08
    },
    {
        'name': 'Owner Controlled',
        'color': MLORANGE,
        'examples': 'USDC, USDT',
        'desc': 'Authorized addresses mint\nCentralized control',
        'trust': 'High (issuer)',
        'x': 0.38
    },
    {
        'name': 'Algorithmic',
        'color': MLGREEN,
        'examples': 'DAI, UNI rewards',
        'desc': 'Smart contract logic\nNo human discretion',
        'trust': 'Code only',
        'x': 0.68
    },
]

box_w = 0.26
box_h = 0.55
y_start = 0.35

for strat in strategies:
    # Main box
    box = FancyBboxPatch((strat['x'], y_start), box_w, box_h,
                          boxstyle="round,pad=0.02", facecolor=strat['color'],
                          edgecolor='black', linewidth=2, alpha=0.15)
    ax.add_patch(box)

    # Header
    header_box = FancyBboxPatch((strat['x'], y_start + box_h - 0.12), box_w, 0.12,
                                 boxstyle="round,pad=0.02", facecolor=strat['color'],
                                 edgecolor='black', linewidth=1, alpha=0.85)
    ax.add_patch(header_box)
    ax.text(strat['x'] + box_w/2, y_start + box_h - 0.06, strat['name'],
            ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Content
    ax.text(strat['x'] + box_w/2, y_start + box_h - 0.22, f"Examples: {strat['examples']}",
            ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(strat['x'] + box_w/2, y_start + box_h/2 - 0.05, strat['desc'],
            ha='center', va='center', fontsize=14)
    ax.text(strat['x'] + box_w/2, y_start + 0.08, f"Trust: {strat['trust']}",
            ha='center', va='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#888'))

# Add spectrum arrow at bottom
ax.annotate('', xy=(0.92, 0.15), xytext=(0.08, 0.15),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax.text(0.08, 0.08, 'More Decentralized', fontsize=14, ha='left', fontweight='bold', color=MLGREEN)
ax.text(0.92, 0.08, 'More Centralized', fontsize=14, ha='right', fontweight='bold', color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Token Minting Strategies', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
