"""
NFT Metadata Storage Comparison
On-chain vs IPFS vs Centralized
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Metadata Storage',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_Standards/charts/03_metadata_storage'
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

# Storage options
options = ['On-Chain', 'IPFS', 'Centralized\nServer']

# Characteristics (scale 1-10)
characteristics = {
    'Gas Cost': [10, 3, 1],  # Lower is better, inverted display
    'Permanence': [10, 7, 3],
    'Decentralization': [10, 8, 1],
    'Accessibility': [6, 7, 10],
}

x = np.arange(len(options))
width = 0.2
colors = [MLRED, MLGREEN, MLBLUE, MLORANGE]

for i, (char, values) in enumerate(characteristics.items()):
    if char == 'Gas Cost':
        # Invert for display (high gas = bad = show high bar)
        display_values = values
        label = 'Gas Cost (High=Expensive)'
    else:
        display_values = values
        label = char
    bars = ax.bar(x + i * width - 0.3, display_values, width, label=label,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.8)

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(options, fontsize=14, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Examples
examples = ['Loot, Art Blocks', 'BAYC, CryptoPunks\n(wrapped)', 'Early NFTs,\nsome games']
for i, ex in enumerate(examples):
    ax.text(i, -1.8, f'Ex: {ex}', ha='center', fontsize=14, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('NFT Metadata Storage Options', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
