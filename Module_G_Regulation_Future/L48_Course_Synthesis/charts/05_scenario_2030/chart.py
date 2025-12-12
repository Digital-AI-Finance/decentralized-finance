"""
Realistic 2030 Scenario
Projected metrics for blockchain industry
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': '2030 Scenario',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L48_Course_Synthesis/charts/05_scenario_2030'
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

# 2024 vs 2030 projections
categories = ['Crypto Users\n(Billions)', 'DeFi TVL\n($T)', 'RWA Tokenized\n($T)',
              'CBDC Countries\n(Live)', 'Stablecoin\nMarket Cap ($B)']
values_2024 = [0.5, 0.1, 2, 10, 200]
values_2030 = [2.0, 0.8, 16, 50, 1000]

# Normalize for visualization (different scales)
max_vals = [2.5, 1.0, 20, 60, 1200]
norm_2024 = [v/m*100 for v, m in zip(values_2024, max_vals)]
norm_2030 = [v/m*100 for v, m in zip(values_2030, max_vals)]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, norm_2024, width, label='2024', color=MLBLUE, edgecolor='black')
bars2 = ax.bar(x + width/2, norm_2030, width, label='2030 Projected', color=MLGREEN, edgecolor='black')

# Add actual value labels
for bar, val in zip(bars1, values_2024):
    label = f'{val}B' if val >= 100 else str(val)
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=MLBLUE)

for bar, val in zip(bars2, values_2030):
    label = f'{val}B' if val >= 100 else str(val)
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            label, ha='center', va='bottom', fontsize=9, fontweight='bold', color=MLGREEN)

ax.set_ylabel('Relative Scale (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 120)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Add growth annotation
ax.text(0.98, 0.98, 'Average Growth:\n4-8x across metrics',
        transform=ax.transAxes, fontsize=9, ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Blockchain Industry: 2024 vs 2030 Projections', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
