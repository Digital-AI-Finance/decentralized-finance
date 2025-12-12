"""
Bitcoin Energy Consumption Comparison
Compares to countries and other systems
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Energy Consumption',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/07_energy_comparison'
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

# Energy consumption data (TWh/year)
entities = ['Bitcoin\nMining', 'Argentina', 'Netherlands', 'Norway', 'Traditional\nBanking*']
consumption = [150, 130, 120, 140, 260]
colors = [MLORANGE, MLBLUE, MLBLUE, MLBLUE, MLLAVENDER]

bars = ax.barh(entities, consumption, color=colors, edgecolor='black', linewidth=1.5)

# Add value labels
for bar, val in zip(bars, consumption):
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2.,
            f'{val} TWh', ha='left', va='center', fontsize=14, fontweight='bold')

ax.set_xlabel('Annual Energy Consumption (TWh)', fontsize=16)
ax.set_xlim(0, 320)

# Energy source annotation
ax.text(0.98, 0.95, 'Bitcoin Mining Energy Sources:', transform=ax.transAxes,
        ha='right', fontsize=14, fontweight='bold', color='#333')
ax.text(0.98, 0.88, 'Renewable: ~50-60%', transform=ax.transAxes,
        ha='right', fontsize=14, color=MLGREEN)
ax.text(0.98, 0.81, 'Fossil Fuels: ~35-45%', transform=ax.transAxes,
        ha='right', fontsize=14, color=MLRED)
ax.text(0.98, 0.74, 'Nuclear: ~5%', transform=ax.transAxes,
        ha='right', fontsize=14, color=MLPURPLE)

# Footnote
ax.text(0.5, -0.12, '*Traditional banking includes data centers, branches, ATMs, card networks',
        transform=ax.transAxes, ha='center', fontsize=14, color='#666', style='italic')

ax.set_title('Bitcoin Energy Consumption in Context (2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
