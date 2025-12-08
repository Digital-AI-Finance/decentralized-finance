"""
Bitcoin Block Reward Halving Schedule
Shows the step-down of mining rewards over time
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Bitcoin Block Reward Halving Schedule',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/bitcoin_halving'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9
})

# Bitcoin halving schedule (real data)
halvings = [
    ('2009-01', 0, 50.0),      # Genesis
    ('2012-11', 210000, 25.0),  # First halving
    ('2016-07', 420000, 12.5),  # Second halving
    ('2020-05', 630000, 6.25),  # Third halving
    ('2024-04', 840000, 3.125), # Fourth halving
    ('2028-01', 1050000, 1.5625), # Fifth halving (projected)
    ('2032-01', 1260000, 0.78125) # Sixth halving (projected)
]

# Prepare data for step plot
dates = [datetime.strptime(d, '%Y-%m') for d, _, _ in halvings]
blocks = [b for _, b, _ in halvings]
rewards = [r for _, _, r in halvings]

# Create the chart
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

# Top plot: Block reward over time
ax1.step(dates, rewards, where='post', color='black', linewidth=2)
ax1.fill_between(dates, rewards, step='post', alpha=0.2, color='gray')

# Mark halving events
for i, (date_obj, date_str, block, reward) in enumerate([(dates[j], halvings[j][0], halvings[j][1], halvings[j][2]) for j in range(len(halvings)-2)]):
    ax1.plot(date_obj, reward, 'o', color='black', markersize=6)
    if i < 5:  # Add labels for first few halvings
        label_text = f'{reward} BTC'
        ax1.text(date_obj, reward + 2, label_text, ha='center', fontsize=8)

# Mark projected halvings differently
for i in [-2, -1]:
    ax1.plot(dates[i], halvings[i][2], 'o', color='gray', markersize=6)
    ax1.text(dates[i], halvings[i][2] + 1, f'{halvings[i][2]} BTC', ha='center', fontsize=8, color='gray')

ax1.set_ylabel('Block Reward (BTC)')
ax1.set_title('Bitcoin Block Reward Halving Schedule')
ax1.set_ylim(0, 55)
ax1.grid(alpha=0.3, linestyle=':', linewidth=0.5)
ax1.axvline(x=dates[4], color='gray',
            linestyle='--', linewidth=0.8, alpha=0.5)
ax1.text(dates[4], 50, 'Current',
         ha='center', fontsize=8, style='italic', alpha=0.7)

# Bottom plot: Cumulative BTC mined
cumulative_btc = []
total = 0
for i in range(len(halvings)):
    if i == 0:
        blocks_in_period = halvings[i][1]
    else:
        blocks_in_period = halvings[i][1] - halvings[i-1][1]

    if i > 0:
        total += blocks_in_period * halvings[i-1][2]
    cumulative_btc.append(total / 1_000_000)  # Convert to millions

ax2.plot(dates, cumulative_btc, color='black', linewidth=2)
ax2.fill_between(dates, cumulative_btc, alpha=0.2, color='gray')

# Add 21M limit line
ax2.axhline(y=21, color='black', linestyle='--', linewidth=1, label='21M Limit')
ax2.text(dates[-1], 21.5, '21 Million Cap', ha='right', fontsize=8, style='italic')

ax2.set_xlabel('Year')
ax2.set_ylabel('Cumulative BTC Mined (Millions)')
ax2.set_ylim(0, 22)
ax2.grid(alpha=0.3, linestyle=':', linewidth=0.5)

# Rotate x-axis labels
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Add note about projected data
fig.text(0.99, 0.01, 'Halvings after 2024 are projected',
         ha='right', va='bottom', fontsize=8, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
