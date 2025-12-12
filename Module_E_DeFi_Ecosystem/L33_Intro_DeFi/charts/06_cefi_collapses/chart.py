"""
CeFi Collapses vs DeFi Resilience (2022)
Timeline showing major CeFi failures
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'CeFi Collapses 2022',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/06_cefi_collapses'
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

# CeFi collapse events with estimated losses
events = [
    ('May 2022', 'Terra/Luna', 40, 'Algorithmic stablecoin death spiral'),
    ('Jun 2022', 'Celsius', 12, 'Lending platform insolvency'),
    ('Jul 2022', 'Voyager', 1.3, 'Crypto broker bankruptcy'),
    ('Jul 2022', '3AC', 10, 'Hedge fund liquidation'),
    ('Nov 2022', 'FTX', 8, 'Exchange fraud/bankruptcy'),
    ('Nov 2022', 'BlockFi', 0.7, 'Lending platform bankruptcy'),
]

months = [e[0] for e in events]
names = [e[1] for e in events]
losses = [e[2] for e in events]
descriptions = [e[3] for e in events]

y_pos = np.arange(len(events))

bars = ax.barh(y_pos, losses, color=MLRED, edgecolor='black', linewidth=1, alpha=0.8)

# Add labels
for i, (bar, name, loss, desc) in enumerate(zip(bars, names, losses, descriptions)):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'${loss}B - {desc}', va='center', fontsize=9)

ax.set_yticks(y_pos)
ax.set_yticklabels([f'{m}\n{n}' for m, n in zip(months, names)], fontsize=10, fontweight='bold')
ax.set_xlabel('Estimated Losses (Billion USD)', fontsize=12)
ax.set_xlim(0, 55)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Add summary
total_loss = sum(losses)
ax.text(0.5, -0.12, f'Total CeFi losses in 2022: ~${total_loss:.0f}B | Major DeFi protocols (Aave, Uniswap, MakerDAO) survived',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('2022 CeFi Collapses: The Case for Non-Custodial Finance', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
