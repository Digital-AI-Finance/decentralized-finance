"""
IPFS Pinning Services Comparison
Comparing different pinning service options
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'IPFS Pinning Services',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS/charts/02_pinning_services'
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

# Pinning services
services = ['Pinata\n(Commercial)', 'NFT.Storage\n(Free)', 'Infura\n(Enterprise)', 'Self-Hosted\n(Node)']

# Characteristics (scale 1-10)
characteristics = {
    'Reliability': [9, 8, 9, 6],
    'Cost Efficiency': [5, 10, 4, 7],
    'Features': [8, 7, 9, 5],
    'Decentralization': [6, 7, 5, 10],
}

x = np.arange(len(services))
width = 0.2
colors = [MLGREEN, MLBLUE, MLORANGE, MLPURPLE]

for i, (char, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=char,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(services, fontsize=10, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Pricing info
pricing = ['$0.15/GB/mo', 'Free (Filecoin)', '$0.08/GB/mo', 'Server costs']
for i, price in enumerate(pricing):
    ax.text(i, -1.5, price, ha='center', fontsize=8,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('IPFS Pinning Services Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
