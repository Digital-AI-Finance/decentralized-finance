"""
NFT On-Chain vs Off-Chain Data
Shows what data is stored where
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT On-Chain vs Off-Chain',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L21_NFT_Technology/charts/01_onchain_vs_offchain'
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

# On-chain box (blockchain)
onchain_box = FancyBboxPatch((0.05, 0.35), 0.40, 0.50,
                               boxstyle="round,pad=0.02", facecolor='#E3F2FD',
                               edgecolor=MLBLUE, linewidth=3)
ax.add_patch(onchain_box)
ax.text(0.25, 0.80, 'ON-CHAIN', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLBLUE)
ax.text(0.25, 0.72, '(Blockchain)', ha='center', fontsize=14, color='#666')

# On-chain data items
onchain_items = [
    'Token ID: uint256',
    'Owner: address',
    'Approvals: mapping',
    'Token URI: string',
    'Contract Logic'
]
for i, item in enumerate(onchain_items):
    ax.text(0.25, 0.60 - i * 0.07, item, ha='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=MLBLUE))

# Off-chain box (external storage)
offchain_box = FancyBboxPatch((0.55, 0.35), 0.40, 0.50,
                                boxstyle="round,pad=0.02", facecolor='#FFF3E0',
                                edgecolor=MLORANGE, linewidth=3)
ax.add_patch(offchain_box)
ax.text(0.75, 0.80, 'OFF-CHAIN', ha='center', va='center',
        fontsize=14, fontweight='bold', color=MLORANGE)
ax.text(0.75, 0.72, '(IPFS/Server)', ha='center', fontsize=14, color='#666')

# Off-chain data items
offchain_items = [
    'Image/Media',
    'Metadata JSON',
    'Attributes/Traits',
    'Description',
    'Animation URL'
]
for i, item in enumerate(offchain_items):
    ax.text(0.75, 0.60 - i * 0.07, item, ha='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=MLORANGE))

# Arrow connecting them
ax.annotate('', xy=(0.55, 0.55), xytext=(0.45, 0.55),
           arrowprops=dict(arrowstyle='->', color='#666', lw=2))
ax.text(0.50, 0.60, 'tokenURI()', ha='center', fontsize=14, fontweight='bold')

# Cost comparison at bottom
ax.text(0.25, 0.20, 'Cost: HIGH', ha='center', fontsize=14,
        fontweight='bold', color=MLRED)
ax.text(0.25, 0.13, '~20,000 gas per 32 bytes', ha='center', fontsize=14, color='#666')

ax.text(0.75, 0.20, 'Cost: LOW', ha='center', fontsize=14,
        fontweight='bold', color=MLGREEN)
ax.text(0.75, 0.13, '~$0.01 per MB (IPFS)', ha='center', fontsize=14, color='#666')

ax.set_xlim(0, 1)
ax.set_ylim(0.05, 0.95)
ax.axis('off')

ax.set_title('NFT Data Storage: On-Chain vs Off-Chain', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
