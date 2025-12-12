"""
Deflationary Token Mechanisms
Comparing different burn strategies
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Deflationary Token Mechanisms',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle/charts/04_deflationary_mechanisms'
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

# Burn mechanisms
mechanisms = ['Transaction\nFee Burn', 'Buyback\n& Burn', 'Staking\nBurn', 'Voluntary\nBurn']

# Impact metrics (scale 1-10)
metrics = {
    'Supply Reduction': [7, 8, 4, 3],
    'Price Impact': [6, 9, 5, 2],
    'User Participation': [10, 3, 6, 4],
    'Predictability': [9, 5, 7, 2],
}

x = np.arange(len(mechanisms))
width = 0.2
colors = [MLRED, MLGREEN, MLBLUE, MLORANGE]

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=metric,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Impact Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(mechanisms, fontsize=10, fontweight='bold')
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add examples
examples = ['ETH (EIP-1559)\nBNB Chain', 'BNB Quarterly\nSHIB', 'LUNA (pre-crash)\nFrax', 'Proof-of-Burn\nUser choice']
for i, ex in enumerate(examples):
    ax.text(i, -1.8, f'{ex}', ha='center', fontsize=8, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Deflationary Token Mechanisms', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
