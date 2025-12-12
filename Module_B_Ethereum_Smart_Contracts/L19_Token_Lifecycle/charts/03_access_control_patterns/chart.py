"""
Access Control Patterns
Comparing Ownable, AccessControl, and Multi-sig
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Access Control Patterns',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle/charts/03_access_control_patterns'
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

# Access control patterns
patterns = ['Ownable\n(Single Admin)', 'AccessControl\n(Role-Based)', 'Multi-Sig\n(3-of-5)', 'Governance\n(Token Voting)']

# Characteristics
characteristics = {
    'Security': [3, 6, 8, 9],
    'Simplicity': [10, 6, 5, 3],
    'Speed': [10, 8, 4, 2],
    'Decentralization': [1, 4, 6, 10],
}

x = np.arange(len(patterns))
width = 0.2
colors = [MLRED, MLBLUE, MLGREEN, MLORANGE]

for i, (char, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=char,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(patterns, fontsize=10, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Add examples
examples = ['Small projects\nMVPs', 'Aave, Compound\nEnterprise', 'Uniswap\nTreasury', 'MakerDAO\nGovernor']
for i, ex in enumerate(examples):
    ax.text(i, -2.0, f'Ex: {ex}', ha='center', fontsize=8, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Access Control Patterns Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
