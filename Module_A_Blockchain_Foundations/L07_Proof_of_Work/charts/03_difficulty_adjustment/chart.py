"""
Bitcoin Difficulty Adjustment
Shows how difficulty adapts to hash rate changes
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Difficulty Adjustment',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/03_difficulty_adjustment'
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

# Simulated data for difficulty and block time
np.random.seed(42)
periods = np.arange(0, 20)  # Adjustment periods

# Difficulty increases over time with some variation
difficulty = np.array([1.0])
for i in range(19):
    change = np.random.uniform(-0.1, 0.3)
    difficulty = np.append(difficulty, difficulty[-1] * (1 + change))

# Block time fluctuates around 10 minutes
block_time = np.zeros(20)
for i in range(20):
    if i == 0:
        block_time[i] = 10
    else:
        # Block time depends on previous hash rate vs difficulty
        deviation = np.random.uniform(-3, 3)
        block_time[i] = 10 + deviation

# Plot difficulty
ax1.plot(periods, difficulty, 'o-', color=MLBLUE, linewidth=2, markersize=6, label='Difficulty')
ax1.fill_between(periods, difficulty, alpha=0.2, color=MLBLUE)
ax1.set_xlabel('Adjustment Period (every 2016 blocks)', fontsize=13)
ax1.set_ylabel('Relative Difficulty', fontsize=13, color=MLBLUE)
ax1.tick_params(axis='y', labelcolor=MLBLUE)

# Plot block time on secondary axis
ax2 = ax1.twinx()
ax2.bar(periods, block_time, alpha=0.5, color=MLORANGE, width=0.6, label='Avg Block Time')
ax2.axhline(y=10, color=MLGREEN, linestyle='--', linewidth=2, label='Target: 10 min')
ax2.set_ylabel('Average Block Time (minutes)', fontsize=13, color=MLORANGE)
ax2.tick_params(axis='y', labelcolor=MLORANGE)
ax2.set_ylim(0, 20)

# Adjustment formula annotation
formula = r'New Difficulty = Old Difficulty $\times$ $\frac{\text{Actual Time}}{\text{Expected Time}}$'
props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLPURPLE, alpha=0.95)
ax1.text(10, max(difficulty) * 0.95, formula, ha='center', fontsize=11,
         bbox=props, color='#333')

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

ax1.set_title('Bitcoin Difficulty Adjustment Mechanism', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
