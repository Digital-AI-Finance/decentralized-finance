"""
Energy Consumption Comparison
Bar chart comparing energy usage across consensus mechanisms
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Energy Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/04_energy_comparison'
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

# Data: blockchain, energy (TWh/year)
blockchains = ['Bitcoin (PoW)', 'Eth pre-Merge (PoW)', 'Litecoin (PoW)',
               'Eth post-Merge (PoS)', 'Cardano (PoS)', 'Polkadot (PoS)', 'All PoS combined']
energy = [150, 94, 0.5, 0.01, 0.006, 0.007, 0.1]
colors = [MLBLUE, MLBLUE, MLBLUE, MLGREEN, MLGREEN, MLGREEN, MLGREEN]

# Use log scale
bars = ax.barh(blockchains, energy, color=colors, edgecolor='black', linewidth=0.5)

ax.set_xscale('log')
ax.set_xlim(0.001, 500)

# Add values as labels
for bar, e in zip(bars, energy):
    width = bar.get_width()
    if e >= 1:
        label = f'{e:.0f} TWh'
    else:
        label = f'{e:.3f} TWh'
    label_x = width * 1.5
    ax.text(label_x, bar.get_y() + bar.get_height()/2, label,
            va='center', fontsize=10, fontweight='bold')

# Add comparison annotations
ax.axvline(x=150, color=MLRED, linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(150, 7.2, 'Argentina\n(~150 TWh/yr)', ha='center', fontsize=9, color=MLRED)

# Key insight box
props = dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(0.003, 1.5, 'PoS: 99.95%\nenergy reduction\nvs PoW',
        fontsize=10, fontweight='bold', bbox=props, color=MLGREEN, ha='left')

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLBLUE, edgecolor='black', label='Proof of Work'),
    Patch(facecolor=MLGREEN, edgecolor='black', label='Proof of Stake'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=11)

ax.set_xlabel('Annual Energy Consumption (TWh, log scale)', fontsize=13)
ax.set_title('Blockchain Energy Consumption by Consensus Type', fontweight='bold', fontsize=15, pad=10)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
