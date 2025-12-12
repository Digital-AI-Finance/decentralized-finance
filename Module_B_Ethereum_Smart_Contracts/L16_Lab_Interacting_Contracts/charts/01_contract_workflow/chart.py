"""Contract Interaction Lab Workflow"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16, 'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 12, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))
exercises = ['Setup\nRemix', 'Ex 1: Deploy\nContract', 'Ex 2: Read\nFunctions', 'Ex 3: Write\nFunctions', 'Ex 4: Events\n& Logs', 'Report']
durations = [10, 25, 20, 25, 15, 5]
colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE]
positions = np.cumsum([0] + durations[:-1])

for exercise, duration, pos, color in zip(exercises, durations, positions, colors):
    ax.barh(0, duration, left=pos, height=0.5, color=color, edgecolor='black', linewidth=1.5)
    ax.text(pos + duration/2, 0, f'{exercise}\n({duration} min)', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

for t in [0, 30, 60, 100]:
    ax.axvline(x=t, color='gray', linestyle='--', alpha=0.5)
    ax.text(t, -0.4, f'{t} min', ha='center', va='top', fontsize=14)

ax.set_xlim(-2, 105)
ax.set_ylim(-0.6, 0.6)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_title('Contract Interaction Lab: 100 Minutes', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
print(f"Chart saved")
