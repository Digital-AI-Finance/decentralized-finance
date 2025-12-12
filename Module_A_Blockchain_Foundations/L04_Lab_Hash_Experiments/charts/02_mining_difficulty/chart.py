"""
Mining Difficulty vs Computation Time
Exponential growth visualization
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Mining Difficulty',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L04_Lab_Hash_Experiments/charts/02_mining_difficulty'
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

# Difficulty levels and expected attempts
difficulty = [1, 2, 3, 4, 5]
avg_attempts = [16, 256, 4096, 65536, 1048576]
time_estimate = ['< 1 sec', '< 1 sec', '1-5 sec', '10-60 sec', '5-20 min']

bars = ax.bar(difficulty, avg_attempts, color=MLBLUE, edgecolor='black', linewidth=1.5, width=0.6)

# Color gradient based on difficulty
for i, bar in enumerate(bars):
    if i <= 1:
        bar.set_color(MLGREEN)
    elif i == 2:
        bar.set_color(MLORANGE)
    else:
        bar.set_color(MLRED)

# Add time labels
for i, (bar, time) in enumerate(zip(bars, time_estimate)):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.1,
            time, ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_yscale('log')
ax.set_xlabel('Difficulty (Leading Zeros)', fontsize=12)
ax.set_ylabel('Average Attempts (log scale)', fontsize=12)
ax.set_xticks(difficulty)
ax.set_xticklabels(['1 zero', '2 zeros', '3 zeros', '4 zeros', '5 zeros'], fontsize=10)

ax.grid(True, alpha=0.3, axis='y')

# Add formula annotation
ax.text(0.98, 0.02, 'Expected attempts = 16^difficulty',
        transform=ax.transAxes, fontsize=10, ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Mining Difficulty: Exponential Growth in Computation', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
