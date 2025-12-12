"""
Permissioned vs Permissionless Blockchain Comparison
Matrix showing key differences between public and private blockchains
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Permissioned vs Permissionless Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/06_permissioned_comparison'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Categories for comparison
categories = ['Access', 'Speed', 'Decentralization', 'Privacy', 'Trust Model']
permissionless = [5, 2, 5, 2, 5]  # Scale 1-5
permissioned = [2, 5, 2, 5, 2]

# Bar positions
x = np.arange(len(categories))
width = 0.35

# Create bars
bars1 = ax.barh(x - width/2, permissionless, width, label='Permissionless (Public)',
                color=MLGREEN, edgecolor='black', linewidth=1.5, alpha=0.8)
bars2 = ax.barh(x + width/2, permissioned, width, label='Permissioned (Private)',
                color=MLORANGE, edgecolor='black', linewidth=1.5, alpha=0.8)

# Add value labels
for bar in bars1:
    width_val = bar.get_width()
    ax.text(width_val + 0.1, bar.get_y() + bar.get_height()/2.,
            f'{int(width_val)}', va='center', fontsize=12, fontweight='bold', color=MLGREEN)

for bar in bars2:
    width_val = bar.get_width()
    ax.text(width_val + 0.1, bar.get_y() + bar.get_height()/2.,
            f'{int(width_val)}', va='center', fontsize=12, fontweight='bold', color=MLORANGE)

# Labels and formatting
ax.set_yticks(x)
ax.set_yticklabels(categories, fontsize=13)
ax.set_xlabel('Score (1=Low, 5=High)', fontsize=13)
ax.set_xlim(0, 6)

# Add examples as annotations
examples_permissionless = 'Bitcoin, Ethereum'
examples_permissioned = 'Hyperledger, R3 Corda'

ax.text(3, -1.2, f'Examples: {examples_permissionless}', ha='center', fontsize=11,
        color=MLGREEN, fontweight='bold')
ax.text(3, -1.6, f'Examples: {examples_permissioned}', ha='center', fontsize=11,
        color=MLORANGE, fontweight='bold')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)

plt.title('Permissionless vs Permissioned Blockchains', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
