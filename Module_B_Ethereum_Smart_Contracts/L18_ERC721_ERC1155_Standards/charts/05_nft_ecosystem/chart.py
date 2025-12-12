"""
NFT Ecosystem Overview
Major projects and their characteristics
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'NFT Ecosystem',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_Standards/charts/05_nft_ecosystem'
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

# Projects and their launch year (x) vs total value (y, log scale proxy)
projects = [
    {'name': 'CryptoPunks', 'year': 2017, 'value': 2.0, 'color': MLPURPLE, 'type': 'PFP'},
    {'name': 'CryptoKitties', 'year': 2017, 'value': 0.5, 'color': MLBLUE, 'type': 'Gaming'},
    {'name': 'ENS Domains', 'year': 2017, 'value': 1.2, 'color': MLGREEN, 'type': 'Utility'},
    {'name': 'BAYC', 'year': 2021, 'value': 1.8, 'color': MLORANGE, 'type': 'PFP'},
    {'name': 'Art Blocks', 'year': 2020, 'value': 1.0, 'color': MLRED, 'type': 'Generative'},
    {'name': 'Axie Infinity', 'year': 2018, 'value': 1.5, 'color': '#666', 'type': 'Gaming'},
]

for proj in projects:
    ax.scatter(proj['year'], proj['value'], s=300, c=proj['color'],
               edgecolor='black', linewidth=1.5, alpha=0.8, zorder=3)
    ax.annotate(proj['name'], (proj['year'], proj['value']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=14, fontweight='bold')

# Categories legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLPURPLE, edgecolor='black', label='PFP Collections'),
    Patch(facecolor=MLBLUE, edgecolor='black', label='Gaming NFTs'),
    Patch(facecolor=MLGREEN, edgecolor='black', label='Utility NFTs'),
    Patch(facecolor=MLRED, edgecolor='black', label='Generative Art'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=14)

ax.set_xlabel('Launch Year', fontsize=15)
ax.set_ylabel('Market Significance (relative)', fontsize=15)
ax.set_xlim(2016.5, 2022)
ax.set_ylim(0, 2.5)

ax.grid(True, alpha=0.3)

# Timeline annotations
ax.axvline(x=2017, color='#888', linestyle='--', alpha=0.3)
ax.text(2017, 2.3, 'ERC-721\nStandard', ha='center', fontsize=14, color='#666')

ax.axvline(x=2021, color='#888', linestyle='--', alpha=0.3)
ax.text(2021, 2.3, 'NFT\nBoom', ha='center', fontsize=14, color='#666')

ax.set_title('NFT Ecosystem: Major Projects Timeline', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
