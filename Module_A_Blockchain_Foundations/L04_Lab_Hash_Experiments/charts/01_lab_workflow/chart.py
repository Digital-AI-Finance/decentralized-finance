"""
Lab Session Workflow
Timeline showing 90-minute lab structure
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Lab Workflow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L04_Lab_Hash_Experiments/charts/01_lab_workflow'
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

# Lab exercises and durations
exercises = ['Setup', 'Ex 1: Basic\nHashing', 'Ex 2: Avalanche\nEffect',
             'Ex 3: PoW\nMining', 'Ex 4: Chain\nVerification', 'Wrap-up']
durations = [5, 15, 20, 30, 20, 10]
colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]

# Calculate cumulative positions
positions = np.cumsum([0] + durations[:-1])

# Create horizontal bars (Gantt-like)
for i, (exercise, duration, pos, color) in enumerate(zip(exercises, durations, positions, colors)):
    ax.barh(0, duration, left=pos, height=0.5, color=color, edgecolor='black', linewidth=1.5)
    # Label inside bar
    ax.text(pos + duration/2, 0, f'{exercise}\n({duration} min)',
            ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Add time markers
for t in [0, 30, 60, 90]:
    ax.axvline(x=t, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(t, -0.4, f'{t} min', ha='center', va='top', fontsize=10)

ax.set_xlim(-2, 95)
ax.set_ylim(-0.6, 0.6)
ax.set_xlabel('Time (minutes)', fontsize=12)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_title('Lab Session Structure: 90 Minutes Total', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
