"""
Terra Contagion Cascade
Shows how Terra collapse caused broader failures
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Contagion Cascade',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L39_Terra_Luna_Case_Study/charts/05_contagion_cascade'
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

# Timeline of collapses following Terra
events = ['Terra/Luna\nCollapse', '3AC\nBankruptcy', 'Celsius\nHalt', 'Voyager\nBankruptcy',
          'BlockFi\nLiquidity', 'FTX\nCollapse']
dates = ['May 2022', 'Jun 2022', 'Jun 2022', 'Jul 2022', 'Jul 2022', 'Nov 2022']
losses = [60, 10, 4.7, 5, 1, 8]  # Billions USD

x = np.arange(len(events))
colors = [MLRED, MLORANGE, MLORANGE, MLORANGE, MLORANGE, MLRED]

bars = ax.bar(x, losses, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val, date in zip(bars, losses, dates):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'${val}B', ha='center', va='bottom', fontsize=14, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, -3,
            date, ha='center', va='top', fontsize=14, color='gray')

# Add arrow showing cascade
ax.annotate('', xy=(4.5, 7), xytext=(0.5, 58),
            arrowprops=dict(arrowstyle='->', color='gray', lw=2, ls='--'))
ax.text(2.5, 35, 'Contagion\nCascade', ha='center', fontsize=14, color='gray', style='italic')

ax.set_ylabel('Estimated Losses (Billion USD)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(events, fontsize=14)
ax.set_ylim(0, 70)

ax.grid(True, alpha=0.3, axis='y')

# Legend annotation
ax.text(0.02, 0.98, 'Terra collapse triggered $200B+ total crypto market crash',
        transform=ax.transAxes, ha='left', va='top', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Crypto Contagion: Terra as First Domino (2022)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
