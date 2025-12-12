"""
Ethereum Gas Costs Comparison by Operation Type
Shows relative gas consumption for common EVM operations
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Ethereum Gas Costs by Operation Type',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/gas_costs_comparison'
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

# Gas costs for common operations (based on EIP-2929 and current gas schedule)
operations = [
    'ADD/SUB',
    'MUL',
    'SLOAD (warm)',
    'SLOAD (cold)',
    'SSTORE (update)',
    'SSTORE (new)',
    'CALL (warm)',
    'CALL (cold)',
    'Transfer (ETH)',
    'Contract Deploy\n(simple)'
]

gas_costs = [
    3,      # ADD/SUB
    5,      # MUL
    100,    # SLOAD warm
    2100,   # SLOAD cold
    2900,   # SSTORE update (5000 - 2100 refund)
    20000,  # SSTORE new
    100,    # CALL warm
    2600,   # CALL cold
    21000,  # ETH transfer
    32000   # Contract creation (base)
]

# Create the chart
fig, ax = plt.subplots(figsize=(9, 6))

# Create horizontal bars with grayscale
bars = ax.barh(range(len(operations)), gas_costs, color='#4d4d4d',
               edgecolor='black', linewidth=0.8)

# Highlight expensive operations
for i, cost in enumerate(gas_costs):
    if cost >= 20000:
        bars[i].set_color('#1a1a1a')
    elif cost >= 2000:
        bars[i].set_color('#808080')

ax.set_yticks(range(len(operations)))
ax.set_yticklabels(operations)
ax.set_xlabel('Gas Cost (units)')
ax.set_title('Ethereum Gas Costs by Operation Type')
ax.set_xscale('log')  # Use log scale for better visualization

# Add value labels on bars
for i, (bar, cost) in enumerate(zip(bars, gas_costs)):
    width = bar.get_width()
    label_x_pos = width * 1.2
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2,
            f'{cost:,}',
            ha='left', va='center', fontsize=14)

# Add vertical lines for reference
ax.axvline(x=21000, color='black', linestyle='--', linewidth=0.8,
           alpha=0.3, label='ETH Transfer cost')

ax.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

# Add legend with cost categories
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, fc='#1a1a1a', ec='black', label='Very Expensive (>20k)'),
    plt.Rectangle((0, 0), 1, 1, fc='#808080', ec='black', label='Expensive (2k-20k)'),
    plt.Rectangle((0, 0), 1, 1, fc='#4d4d4d', ec='black', label='Moderate (<2k)')
]
ax.legend(handles=legend_elements, loc='lower right', framealpha=0.9)

# Add note
note_text = "Warm: previously accessed in transaction | Cold: first access"
fig.text(0.15, 0.96, note_text, fontsize=14, style='italic', alpha=0.7)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
