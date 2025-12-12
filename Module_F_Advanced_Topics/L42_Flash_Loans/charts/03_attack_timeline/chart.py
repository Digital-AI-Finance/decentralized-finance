"""
Flash Loan Attack Timeline
Major attacks and losses
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Flash Loan Attacks',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L42_Flash_Loans/charts/03_attack_timeline'
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

# Major flash loan attacks
attacks = ['BZx\n(Feb 2020)', 'Harvest\n(Oct 2020)', 'Cream\n(Oct 2021)', 'Beanstalk\n(Apr 2022)',
           'Mango\n(Oct 2022)', 'Euler\n(Mar 2023)']
losses = [0.35, 34, 130, 182, 110, 200]  # Millions USD
attack_types = ['Oracle', 'Oracle', 'Reentrancy', 'Governance', 'Oracle', 'Donation']
colors = [MLRED, MLRED, MLORANGE, MLPURPLE, MLRED, MLBLUE]

y_pos = np.arange(len(attacks))

bars = ax.barh(y_pos, losses, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, val, atype in zip(bars, losses, attack_types):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'${val}M ({atype})', va='center', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(attacks, fontsize=14)
ax.set_xlabel('Losses (Million USD)', fontsize=15)
ax.set_xlim(0, 260)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Total annotation
total_loss = sum(losses)
ax.text(0.5, -0.15, f'Total flash loan-related losses: ~${total_loss:.0f}M (2020-2023)',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Major Flash Loan Attacks by Loss Amount', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
