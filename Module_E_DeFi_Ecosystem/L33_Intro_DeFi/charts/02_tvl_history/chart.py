"""
DeFi Total Value Locked (TVL) Historical Growth
Line chart showing TVL from 2019-2024
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DeFi TVL History',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/02_tvl_history'
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

# Historical TVL data (approximate, in billions USD)
dates = ['Jan\n2019', 'Jul\n2019', 'Jan\n2020', 'Jul\n2020', 'Jan\n2021', 'Jul\n2021',
         'Nov\n2021', 'Jan\n2022', 'Jul\n2022', 'Jan\n2023', 'Jul\n2023', 'Jan\n2024', 'Dec\n2024']
tvl = [0.3, 0.5, 1, 3, 25, 100, 180, 150, 40, 45, 50, 60, 85]

ax.plot(dates, tvl, '-o', color=MLBLUE, linewidth=2.5, markersize=8)
ax.fill_between(dates, tvl, alpha=0.2, color=MLBLUE)

# Key events annotations
ax.annotate('DeFi Summer\n2020', xy=(4, 25), fontsize=14, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))
ax.annotate('ATH: $180B', xy=(6, 180), xytext=(7, 160), fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))
ax.annotate('Terra/Luna\nCollapse', xy=(8, 40), xytext=(9, 70), fontsize=14, ha='center',
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_ylabel('Total Value Locked (Billion USD)', fontsize=15)
ax.set_ylim(0, 200)

ax.grid(True, alpha=0.3)

ax.set_title('DeFi Total Value Locked (TVL): 2019-2024', fontweight='bold', fontsize=15, pad=10)
plt.xticks(rotation=0)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
