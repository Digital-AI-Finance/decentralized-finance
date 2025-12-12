"""
Bitcoin Halving Schedule
Block reward reduction over time
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Halving Schedule',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/08_halving_schedule'
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

fig, ax1 = plt.subplots(figsize=(10, 6))

# Halving events
halvings = [
    (2009, 50, 'Genesis'),
    (2012, 25, 'Halving 1'),
    (2016, 12.5, 'Halving 2'),
    (2020, 6.25, 'Halving 3'),
    (2024, 3.125, 'Halving 4'),
    (2028, 1.5625, 'Halving 5'),
    (2032, 0.78125, 'Halving 6'),
]

years = [h[0] for h in halvings]
rewards = [h[1] for h in halvings]
labels = [h[2] for h in halvings]

# Step plot for block reward
ax1.step(years, rewards, where='post', color=MLORANGE, linewidth=3, label='Block Reward')
ax1.fill_between(years, rewards, step='post', alpha=0.3, color=MLORANGE)

# Mark halving points
for year, reward, label in halvings:
    ax1.plot(year, reward, 'o', markersize=10, color=MLRED if year <= 2024 else '#888')
    if year <= 2024:
        ax1.annotate(label, (year, reward), textcoords="offset points",
                     xytext=(0, 15), ha='center', fontsize=10, fontweight='bold')

# Cumulative supply on secondary axis
ax2 = ax1.twinx()
cum_years = list(range(2009, 2141))
cum_supply = []
supply = 0
reward = 50
block_year = 2009
halving_block = 210000
blocks_per_year = 52560  # ~6 blocks/hour * 24 * 365

for year in cum_years:
    blocks_this_year = blocks_per_year
    # Check for halving
    year_from_start = year - 2009
    halvings_occurred = year_from_start * blocks_per_year // halving_block
    current_reward = 50 / (2 ** halvings_occurred)
    supply += current_reward * blocks_per_year
    if supply > 21000000:
        supply = 21000000
    cum_supply.append(supply / 1000000)

ax2.plot(cum_years, cum_supply, color=MLBLUE, linewidth=2, linestyle='--', label='Total Supply')
ax2.axhline(y=21, color=MLPURPLE, linestyle=':', linewidth=2, alpha=0.7)
ax2.text(2100, 21.3, '21M Cap', fontsize=11, color=MLPURPLE, fontweight='bold')

ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Block Reward (BTC)', fontsize=13, color=MLORANGE)
ax2.set_ylabel('Total Supply (Millions BTC)', fontsize=13, color=MLBLUE)

ax1.tick_params(axis='y', labelcolor=MLORANGE)
ax2.tick_params(axis='y', labelcolor=MLBLUE)

ax1.set_xlim(2008, 2045)
ax1.set_ylim(0, 55)
ax2.set_ylim(0, 22)

# Current marker
ax1.axvline(x=2024, color=MLGREEN, linestyle='-', linewidth=2, alpha=0.7)
ax1.text(2024.5, 45, 'Current\n(2024)', fontsize=10, color=MLGREEN, fontweight='bold')

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=11)

ax1.set_title('Bitcoin Halving: Block Reward Reduction Every 210,000 Blocks',
              fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
