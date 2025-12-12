"""
Ethereum Staking Rewards APR Curve
Shows how APR decreases with total stake
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Staking Rewards APR',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/05_staking_rewards'
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

# APR formula: APR = 64 * sqrt(N) / N where N is total ETH staked in millions
# Simplified: APR% = 64 / sqrt(N)

total_staked = np.linspace(1, 50, 100)  # Million ETH
apr = 64 / np.sqrt(total_staked)

ax.plot(total_staked, apr, color=MLBLUE, linewidth=3, label='Base APR')
ax.fill_between(total_staked, apr, alpha=0.2, color=MLBLUE)

# MEV boost addition
apr_with_mev = apr * 1.3  # ~30% boost from MEV
ax.plot(total_staked, apr_with_mev, color=MLGREEN, linewidth=2, linestyle='--',
        label='APR + MEV Boost (~30%)')

# Current marker (34M ETH)
current_stake = 34
current_apr = 64 / np.sqrt(current_stake)
ax.plot(current_stake, current_apr, 'o', markersize=12, color=MLRED, zorder=5)
ax.annotate(f'Current (2024)\n{current_stake}M ETH\n{current_apr:.1f}% APR',
            xy=(current_stake, current_apr), xytext=(40, 5),
            fontsize=14, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

ax.set_xlabel('Total ETH Staked (Millions)', fontsize=16)
ax.set_ylabel('Annual Percentage Rate (%)', fontsize=16)
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)

# Formula annotation
formula = r'$APR \approx \frac{64}{\sqrt{N}}$ where N = total ETH staked (millions)'
props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLPURPLE)
ax.text(30, 18, formula, fontsize=14, bbox=props, color='#333')

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3)

ax.set_title('Ethereum Staking Rewards: APR vs Total Stake', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
