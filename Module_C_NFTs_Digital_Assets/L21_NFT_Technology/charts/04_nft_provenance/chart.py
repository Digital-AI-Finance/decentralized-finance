"""
NFT Provenance Chain
Shows ownership history tracking
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Provenance Chain',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/04_nft_provenance'
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

# Provenance chain events
events = [
    {'event': 'Mint', 'from': '0x0...0', 'to': 'Artist', 'block': '14,500,000', 'date': 'Jan 2022', 'color': MLGREEN},
    {'event': 'Transfer', 'from': 'Artist', 'to': 'Collector A', 'block': '14,600,000', 'date': 'Feb 2022', 'color': MLBLUE},
    {'event': 'Transfer', 'from': 'Collector A', 'to': 'Collector B', 'block': '15,200,000', 'date': 'Aug 2022', 'color': MLBLUE},
    {'event': 'Transfer', 'from': 'Collector B', 'to': 'Current', 'block': '17,500,000', 'date': 'Jun 2023', 'color': MLORANGE},
]

y_start = 0.75
y_step = 0.15

for i, evt in enumerate(events):
    y = y_start - i * y_step

    # Event box
    box = FancyBboxPatch((0.15, y - 0.05), 0.70, 0.10,
                          boxstyle="round,pad=0.02", facecolor=evt['color'],
                          edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)

    # Event type
    ax.text(0.22, y, evt['event'], ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')

    # From -> To
    ax.text(0.43, y, f"{evt['from']} -> {evt['to']}", ha='center', va='center',
            fontsize=14, color='white')

    # Block and date
    ax.text(0.70, y, f"Block {evt['block']}", ha='center', va='center',
            fontsize=14, color='white')
    ax.text(0.82, y, evt['date'], ha='center', va='center',
            fontsize=14, color='white')

    # Chain connector
    if i < len(events) - 1:
        ax.plot([0.50, 0.50], [y - 0.05, y - y_step + 0.05], color='#666', lw=2, linestyle='--')

# Headers
ax.text(0.22, 0.87, 'Event', ha='center', fontsize=14, fontweight='bold')
ax.text(0.43, 0.87, 'From -> To', ha='center', fontsize=14, fontweight='bold')
ax.text(0.70, 0.87, 'Block', ha='center', fontsize=14, fontweight='bold')
ax.text(0.82, 0.87, 'Date', ha='center', fontsize=14, fontweight='bold')

# Key insight
ax.text(0.50, 0.12, 'Provenance: Immutable record of ownership history from mint to present',
        ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 0.95)
ax.axis('off')

ax.set_title('NFT Provenance: On-Chain Ownership History', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
