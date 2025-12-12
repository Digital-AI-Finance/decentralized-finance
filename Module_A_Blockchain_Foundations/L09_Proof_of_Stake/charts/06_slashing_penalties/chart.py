"""
Slashing Penalties Structure
Shows correlation penalty and slashable offenses
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Slashing Penalties',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/06_slashing_penalties'
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

# Correlation penalty formula: Penalty = Stake * 3 * slashed_validators / total_validators
# If 33% slashed together: lose ~99%

percent_slashed = np.linspace(0, 35, 100)
penalty_percent = 3 * percent_slashed

# Cap at 100%
penalty_percent = np.minimum(penalty_percent, 100)

ax.plot(percent_slashed, penalty_percent, color=MLRED, linewidth=3, label='Correlation Penalty')
ax.fill_between(percent_slashed, penalty_percent, alpha=0.2, color=MLRED)

# Key thresholds
thresholds = [
    (1, 3, 'Individual offense'),
    (10, 30, 'Small coordinated'),
    (33, 99, 'Catastrophic'),
]

for x, y, label in thresholds:
    ax.plot(x, y, 'o', markersize=10, color=MLORANGE)
    ax.annotate(f'{label}\n({y:.0f}% loss)', xy=(x, y), xytext=(x + 2, y + 10),
                fontsize=14, arrowprops=dict(arrowstyle='->', color='#333'))

# Initial 1 ETH penalty annotation
ax.axhline(y=3.125, color=MLBLUE, linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(35, 5, 'Initial penalty: 1 ETH (~3% of 32 ETH)', fontsize=14,
        ha='right', color=MLBLUE)

ax.set_xlabel('Validators Slashed Together (%)', fontsize=16)
ax.set_ylabel('Stake Lost (%)', fontsize=16)
ax.set_xlim(0, 36)
ax.set_ylim(0, 110)

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#FFE0E0', edgecolor=MLRED)
ax.text(18, 90, 'Coordinated attacks = Catastrophic losses',
        fontsize=15, fontweight='bold', bbox=props, color=MLRED, ha='center')

ax.legend(loc='lower right', fontsize=14)
ax.grid(True, alpha=0.3)

ax.set_title('Ethereum Slashing: Correlation Penalty', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
