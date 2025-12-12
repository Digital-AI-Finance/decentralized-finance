"""
Gas Costs by Operation
Bar chart showing EVM operation costs
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Gas Costs Operations',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/04_gas_costs_operations'
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

# Operations and their gas costs
operations = ['ADD/SUB', 'MUL', 'DIV', 'SHA3', 'SLOAD\n(warm)', 'SLOAD\n(cold)',
              'SSTORE\n(update)', 'SSTORE\n(new)', 'CALL', 'CREATE']
costs = [3, 5, 5, 30, 100, 2100, 5000, 20000, 700, 32000]

# Color by category
colors = [MLGREEN, MLGREEN, MLGREEN, MLBLUE, MLORANGE, MLRED, MLRED, MLRED, MLORANGE, MLRED]

bars = ax.barh(operations, costs, color=colors, edgecolor='black', linewidth=0.5)

# Log scale for better visualization
ax.set_xscale('log')
ax.set_xlim(1, 50000)

# Add cost labels
for bar, cost in zip(bars, costs):
    width = bar.get_width()
    ax.text(width * 1.3, bar.get_y() + bar.get_height()/2,
            f'{cost:,}', va='center', fontsize=10, fontweight='bold')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLGREEN, edgecolor='black', label='Arithmetic (cheap)'),
    Patch(facecolor=MLBLUE, edgecolor='black', label='Hashing'),
    Patch(facecolor=MLORANGE, edgecolor='black', label='Memory/Calls'),
    Patch(facecolor=MLRED, edgecolor='black', label='Storage (expensive!)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

ax.set_xlabel('Gas Cost (log scale)', fontsize=13)
ax.set_title('EVM Operation Gas Costs', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
