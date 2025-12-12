"""
Token Types Comparison
Comparing characteristics of utility, security, governance, and SoV tokens
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Types Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/01_token_types_comparison'
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

# Token types and attributes (1-10 scale)
token_types = ['Utility\n(BNB, LINK)', 'Security\n(tStocks)', 'Governance\n(UNI, MKR)', 'Store of Value\n(BTC)']
attributes = ['Regulatory Burden', 'Platform Access', 'Voting Rights', 'Value Storage', 'Yield Potential']

# Scores for each token type across attributes
scores = np.array([
    [3, 9, 2, 3, 5],   # Utility
    [9, 2, 3, 7, 8],   # Security
    [4, 5, 10, 4, 6],  # Governance
    [2, 1, 1, 10, 3],  # Store of Value
])

x = np.arange(len(token_types))
width = 0.15
colors = [MLRED, MLBLUE, MLGREEN, MLORANGE, MLPURPLE]

for i, (attr, color) in enumerate(zip(attributes, colors)):
    bars = ax.bar(x + i * width - 0.3, scores[:, i], width, label=attr,
                  color=color, edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(token_types, fontsize=10, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Token Type Characteristics Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
