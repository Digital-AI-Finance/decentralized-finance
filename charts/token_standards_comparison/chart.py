"""
Token Standards Comparison (ERC-20, ERC-721, ERC-1155)
Compares features and use cases of Ethereum token standards
[SYNTHETIC DATA]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Ethereum Token Standards Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/token_standards_comparison'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12
})

fig, ax = plt.subplots(figsize=(10, 6))

# Standards
standards = ['ERC-20', 'ERC-721', 'ERC-1155']

# Feature scores (1-10)
features = {
    'Fungibility': [10, 1, 8],
    'Gas Efficiency': [7, 5, 9],
    'Batch Transfers': [3, 2, 10],
    'Metadata Support': [2, 9, 9],
    'Composability': [8, 7, 9],
}

x = np.arange(len(standards))
width = 0.15
multiplier = 0

# Grayscale colors
colors = ['#1a1a1a', '#404040', '#666666', '#8c8c8c', '#b3b3b3']

for i, (attribute, values) in enumerate(features.items()):
    offset = width * multiplier
    bars = ax.bar(x + offset, values, width, label=attribute, color=colors[i])
    multiplier += 1

ax.set_ylabel('Score (1-10)')
ax.set_title('Ethereum Token Standards: Feature Comparison', fontweight='bold')
ax.set_xticks(x + width * 2)
ax.set_xticklabels(standards, fontsize=14, fontweight='bold')
ax.legend(loc='upper left', fontsize=14)
ax.set_ylim(0, 12)
ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

# Add use case annotations
use_cases = {
    'ERC-20': 'Cryptocurrencies,\nUtility Tokens, DeFi',
    'ERC-721': 'NFTs, Digital Art,\nCollectibles',
    'ERC-1155': 'Gaming Items,\nMulti-Token Systems'
}

for i, (std, use) in enumerate(use_cases.items()):
    ax.text(i + width * 2, 11.2, use, ha='center', va='bottom', fontsize=14,
            style='italic', alpha=0.8)

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC]', ha='right', va='bottom', fontsize=14, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
