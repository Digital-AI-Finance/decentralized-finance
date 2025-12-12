"""
ERC-1155 Batch Gas Savings
Shows gas efficiency of batch transfers
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Batch Gas Savings',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_Standards/charts/04_batch_gas_savings'
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

# Number of items transferred
items = [1, 2, 5, 10, 20]

# Gas costs (approximate)
erc721_gas = [71000, 142000, 355000, 710000, 1420000]  # 71K per item
erc1155_gas = [35000, 45000, 60500, 100000, 180000]  # Batch efficiency

x = np.arange(len(items))
width = 0.35

bars1 = ax.bar(x - width/2, [g/1000 for g in erc721_gas], width,
               label='ERC-721 (separate)', color=MLRED, edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, [g/1000 for g in erc1155_gas], width,
               label='ERC-1155 (batch)', color=MLGREEN, edgecolor='black', linewidth=0.5)

# Add savings percentage
for i, (e721, e1155) in enumerate(zip(erc721_gas, erc1155_gas)):
    savings = (1 - e1155/e721) * 100
    ax.text(i, max(e721, e1155)/1000 + 50, f'-{savings:.0f}%',
            ha='center', fontsize=10, fontweight='bold', color=MLGREEN)

ax.set_xlabel('Number of Items Transferred', fontsize=12)
ax.set_ylabel('Gas Used (thousands)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(items, fontsize=11)

ax.legend(loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.98, 0.98, 'ERC-1155 batch transfers\nsave 50-87% gas',
        transform=ax.transAxes, ha='right', va='top',
        fontsize=11, fontweight='bold', bbox=props, color=MLGREEN)

ax.set_title('Gas Costs: ERC-721 vs ERC-1155 Batch Transfers', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
