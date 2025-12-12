"""
Solidity Data Locations Comparison
Shows storage vs memory vs calldata
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Data Locations',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals/charts/04_data_locations'
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

# Data locations
locations = ['storage', 'memory', 'calldata']

# Characteristics (scale 1-10, higher = more expensive/persistent/modifiable)
characteristics = {
    'Gas Cost': [10, 5, 2],
    'Persistence': [10, 2, 2],
    'Modifiable': [10, 10, 0],
}

x = np.arange(len(locations))
width = 0.25
colors = [MLRED, MLORANGE, MLGREEN]

# Create grouped bar chart
for i, (char_name, values) in enumerate(characteristics.items()):
    bars = ax.bar(x + i * width, values, width, label=char_name,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.8)

    # Add value labels
    for bar, val in zip(bars, values):
        height = bar.get_height()
        label = 'High' if val >= 8 else ('Med' if val >= 4 else 'Low')
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
                label, ha='center', fontsize=14, fontweight='bold')

ax.set_ylabel('Level (0-10)', fontsize=15)
ax.set_xlabel('Data Location', fontsize=15)
ax.set_xticks(x + width)
ax.set_xticklabels(locations, fontsize=15, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Add use case annotations
use_cases = [
    ('storage', 'State variables\nPersists across calls'),
    ('memory', 'Temporary data\nFunction scope'),
    ('calldata', 'External inputs\nRead-only, cheapest'),
]

for i, (loc, desc) in enumerate(use_cases):
    ax.text(i + width, -1.8, desc, ha='center', fontsize=14, va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Solidity Data Locations: Cost vs Capability', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
