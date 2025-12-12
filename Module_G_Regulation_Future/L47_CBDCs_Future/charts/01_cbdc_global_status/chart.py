"""
Global CBDC Development Status (2024)
Horizontal bar chart showing country status
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'CBDC Global Status',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L47_CBDCs_Future/charts/01_cbdc_global_status'
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

# CBDC development stages
stages = ['Research', 'Development', 'Pilot', 'Launched']
counts = [68, 33, 18, 11]  # Number of countries (2024 estimates)
colors = ['#CCCCCC', MLBLUE, MLORANGE, MLGREEN]

bars = ax.bar(stages, counts, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}', ha='center', va='bottom', fontsize=15, fontweight='bold')

ax.set_ylabel('Number of Countries', fontsize=15)
ax.set_ylim(0, 85)
ax.grid(True, alpha=0.3, axis='y')

# Add examples
examples = ['US, Germany\nJapan', 'EU, UK\nIndia', 'China, Brazil\nRussia', 'Bahamas\nNigeria, Jamaica']
for i, (bar, ex) in enumerate(zip(bars, examples)):
    ax.text(bar.get_x() + bar.get_width()/2, 5, ex, ha='center', va='bottom', fontsize=14, color='white')

# Total annotation
total = sum(counts)
ax.text(3.5, 75, f'Total: {total}+\ncountries\nexploring', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Global CBDC Development Status (Late 2024)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
