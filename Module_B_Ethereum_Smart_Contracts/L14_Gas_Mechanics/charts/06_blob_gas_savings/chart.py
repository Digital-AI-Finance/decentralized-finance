"""
EIP-4844 Blob Gas Savings
Shows cost reduction for L2 data posting
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Blob Gas Savings',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/06_blob_gas_savings'
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

# Data sizes
data_sizes = ['10 KB', '50 KB', '100 KB', '128 KB\n(1 blob)']
data_bytes = [10000, 50000, 100000, 128000]

# Pre-Dencun: calldata at 16 gas/byte
pre_dencun_gas = [b * 16 for b in data_bytes]
# At 30 Gwei, $2000/ETH
pre_dencun_cost = [(g * 30 * 1e-9 * 2000) for g in pre_dencun_gas]

# Post-Dencun: blob gas much cheaper (~0.001 Gwei equivalent)
# Roughly $0.01 per blob
post_dencun_cost = [0.01, 0.05, 0.08, 0.10]

x = np.arange(len(data_sizes))
width = 0.35

bars_pre = ax.bar(x - width/2, pre_dencun_cost, width, label='Pre-Dencun (Calldata)',
                   color=MLRED, edgecolor='black', linewidth=0.5)
bars_post = ax.bar(x + width/2, post_dencun_cost, width, label='Post-Dencun (Blobs)',
                    color=MLGREEN, edgecolor='black', linewidth=0.5)

# Add cost labels
for bar, cost in zip(bars_pre, pre_dencun_cost):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'${cost:.2f}', ha='center', fontsize=14)

for bar, cost in zip(bars_post, post_dencun_cost):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'${cost:.2f}', ha='center', fontsize=14, fontweight='bold', color=MLGREEN)

# Savings annotation
for i, (pre, post) in enumerate(zip(pre_dencun_cost, post_dencun_cost)):
    savings = (1 - post/pre) * 100
    ax.text(i, 25, f'-{savings:.0f}%', ha='center', fontsize=14,
            fontweight='bold', color=MLGREEN)

ax.set_xlabel('L2 Data Size Posted to Ethereum', fontsize=16)
ax.set_ylabel('Cost (USD)', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(data_sizes, fontsize=14)
ax.set_ylim(0, 35)

ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.98, 0.95, 'EIP-4844 (March 2024):\n90-99% L2 cost reduction',
        transform=ax.transAxes, ha='right', va='top',
        fontsize=14, fontweight='bold', bbox=props, color=MLGREEN)

ax.set_title('EIP-4844: Blob Gas vs Calldata Costs', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
