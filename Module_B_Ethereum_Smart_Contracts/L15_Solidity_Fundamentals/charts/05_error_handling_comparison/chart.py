"""
Solidity Error Handling Comparison
Shows require vs assert vs revert vs custom errors
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Error Handling Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals/charts/05_error_handling_comparison'
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

# Error handling methods
methods = ['require()', 'assert()', 'revert()', 'Custom\nErrors']

# Characteristics
gas_cost = [100, 80, 100, 50]  # Relative gas cost (lower = better)
error_info = [60, 20, 60, 90]   # Error information quality (higher = better)
use_case_fit = [90, 50, 70, 85]  # General usefulness (higher = better)

x = np.arange(len(methods))
width = 0.25

bars1 = ax.bar(x - width, gas_cost, width, label='Gas Cost (lower=better)',
               color=MLRED, edgecolor='black', linewidth=0.5, alpha=0.8)
bars2 = ax.bar(x, error_info, width, label='Error Info Quality',
               color=MLBLUE, edgecolor='black', linewidth=0.5, alpha=0.8)
bars3 = ax.bar(x + width, use_case_fit, width, label='Overall Usefulness',
               color=MLGREEN, edgecolor='black', linewidth=0.5, alpha=0.8)

ax.set_ylabel('Score', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(methods, fontsize=11, fontweight='bold')
ax.set_ylim(0, 110)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Add use case labels
use_cases = [
    'Input\nvalidation',
    'Invariant\nchecks',
    'Complex\nlogic',
    'Best\npractice'
]

for i, (bar, use) in enumerate(zip(bars1, use_cases)):
    ax.text(i, 105, use, ha='center', fontsize=9, va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

# Add recommendation
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.98, 0.02, 'Recommendation: Use custom errors (0.8.4+)\nfor best gas efficiency and error context',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=10, fontweight='bold', bbox=props, color=MLGREEN)

ax.set_title('Solidity Error Handling Methods', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
