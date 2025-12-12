"""
Play-to-Earn Economic Model
Flow diagram showing capital flows in P2E games
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'P2E Economics',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse/charts/01_p2e_economics'
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

# Create boxes representing P2E flow
boxes = [
    (0.1, 0.7, 'New Players', MLBLUE, 'Buy NFTs\n(Capital Inflow)'),
    (0.4, 0.7, 'Game\nEconomy', MLPURPLE, 'Token\nMinting'),
    (0.7, 0.7, 'Existing\nPlayers', MLORANGE, 'Sell Tokens\n(Capital Outflow)'),
    (0.4, 0.2, 'Sustainability\nRequirement', MLRED, 'Inflow > Outflow'),
]

# Draw boxes
for x, y, label, color, sublabel in boxes:
    rect = mpatches.FancyBboxPatch((x-0.1, y-0.1), 0.2, 0.2,
                                    boxstyle="round,pad=0.01,rounding_size=0.02",
                                    facecolor=color, edgecolor='black',
                                    linewidth=2, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x, y+0.02, label, ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')
    ax.text(x, y-0.06, sublabel, ha='center', va='center',
            fontsize=14, color='white', style='italic')

# Draw arrows
arrow_props = dict(arrowstyle='->', color='black', lw=2)

# New players -> Game economy
ax.annotate('', xy=(0.3, 0.7), xytext=(0.2, 0.7), arrowprops=arrow_props)
ax.text(0.25, 0.78, 'NFT\nPurchases', ha='center', fontsize=14, fontweight='bold')

# Game economy -> Existing players
ax.annotate('', xy=(0.6, 0.7), xytext=(0.5, 0.7), arrowprops=arrow_props)
ax.text(0.55, 0.78, 'Token\nRewards', ha='center', fontsize=14, fontweight='bold')

# Down arrow to sustainability
ax.annotate('', xy=(0.4, 0.4), xytext=(0.4, 0.55), arrowprops=arrow_props)

# Feedback loop (dashed)
ax.annotate('', xy=(0.65, 0.6), xytext=(0.15, 0.6),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, linestyle='dashed'))
ax.text(0.4, 0.52, 'Some players become sellers', ha='center', fontsize=14, color='gray')

# Warning box
warning_rect = mpatches.FancyBboxPatch((0.65, 0.15), 0.3, 0.15,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#FFEBEE', edgecolor=MLRED,
                                        linewidth=2)
ax.add_patch(warning_rect)
ax.text(0.8, 0.225, 'Warning: Ponzi Risk', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLRED)
ax.text(0.8, 0.175, 'If new players decline,\neconomy collapses', ha='center', va='center',
        fontsize=14, color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()

ax.set_title('Play-to-Earn Economic Flow', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
