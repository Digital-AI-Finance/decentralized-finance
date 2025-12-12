"""
Terra Ecosystem Size at Peak (April 2022)
Bar chart showing market caps and ecosystem value
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Terra Ecosystem Size',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L39_Terra_Luna_Case_Study/charts/01_terra_ecosystem_size'
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

# Terra ecosystem components at peak (April 2022)
categories = ['LUNA\nMarket Cap', 'UST\nMarket Cap', 'Anchor\nTVL', 'Other\nProtocols']
values = [40, 18, 14, 5]  # Billions USD
colors = [MLORANGE, MLBLUE, MLGREEN, '#CCCCCC']

bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'${val}B', ha='center', va='bottom', fontsize=13, fontweight='bold')

# Add total annotation
ax.axhline(y=60, color=MLRED, linestyle='--', linewidth=2, alpha=0.7)
ax.text(3.5, 62, 'Total Ecosystem: ~$60B', ha='right', fontsize=11, color=MLRED, fontweight='bold')

ax.set_ylabel('Value (Billion USD)', fontsize=12)
ax.set_ylim(0, 70)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Terra Ecosystem at Peak (April 2022)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
