"""
Howey Test Criteria Applied to Token Types
Horizontal grouped bar showing which tokens pass each criterion
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Howey Test Criteria',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L31_Token_Classification/charts/01_howey_test_criteria'
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

# Howey Test Criteria
criteria = ['Investment\nof Money', 'Common\nEnterprise', 'Expectation\nof Profits', 'Efforts\nof Others']

# Token types and their scores (1=Yes, 0=No, 0.5=Maybe)
token_types = {
    'ICO Token': [1, 1, 1, 1],  # All yes = Security
    'XRP (Institutional)': [1, 1, 1, 1],  # Security
    'BTC': [1, 0.5, 0.5, 0],  # Decentralized, no effort of others
    'ETH (2024)': [1, 0.5, 0.5, 0.3],  # Mostly decentralized
    'Pure Utility (FIL)': [1, 0.5, 0.3, 0.2],  # Low speculation
}

x = np.arange(len(criteria))
width = 0.15
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN, MLPURPLE]

for i, (token, scores) in enumerate(token_types.items()):
    bars = ax.bar(x + i * width - 0.3, scores, width, label=token,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Meets Criterion (0=No, 1=Yes)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(criteria, fontsize=14, fontweight='bold')
ax.set_ylim(0, 1.2)

ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
ax.text(3.7, 0.52, 'Gray Area', fontsize=14, va='bottom', color='gray')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Howey Test Applied to Different Token Types', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
