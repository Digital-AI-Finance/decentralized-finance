"""
Major Crypto Enforcement Actions
Horizontal bar chart of fines/penalties
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Enforcement Fines',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L45_Global_Regulation/charts/03_enforcement_fines'
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

# Major enforcement actions
cases = ['Terraform Labs\n(2024)', 'Binance DOJ\n(2023)', 'FTX Forfeiture\n(2024)',
         'Celsius\n(2024)', 'BitMEX\n(2022)', 'Ripple XRP\n(2024)', 'BlockFi\n(2022)']
fines = [4.5, 4.3, 3.0, 0.8, 0.1, 0.125, 0.1]  # Billions USD

colors = [MLRED if f > 2 else (MLORANGE if f > 0.5 else MLBLUE) for f in fines]

y_pos = np.arange(len(cases))
bars = ax.barh(y_pos, fines, color=colors, edgecolor='black', linewidth=1.2, height=0.6)

ax.set_yticks(y_pos)
ax.set_yticklabels(cases, fontsize=10)
ax.set_xlabel('Penalty Amount (Billion USD)', fontsize=12)
ax.set_xlim(0, 5.5)

# Add value labels
for bar, fine in zip(bars, fines):
    ax.text(fine + 0.1, bar.get_y() + bar.get_height()/2, f'${fine:.1f}B',
            va='center', fontsize=10, fontweight='bold')

ax.grid(True, alpha=0.3, axis='x')

# Total annotation
total = sum(fines)
ax.text(4.5, -0.8, f'Total: ${total:.1f}B+', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Major Crypto Enforcement Actions (2022-2024)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
