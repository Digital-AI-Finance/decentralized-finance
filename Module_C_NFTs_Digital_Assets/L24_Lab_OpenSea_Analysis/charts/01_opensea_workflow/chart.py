"""OpenSea Analysis Lab Workflow"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))
exercises = ['Setup &\nIntro', 'Ex 1: Browse\nCollections', 'Ex 2: Analyze\nMetrics', 'Ex 3: Check\nRarity', 'Report']
durations = [10, 20, 30, 25, 15]
colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLPURPLE]
positions = np.cumsum([0] + durations[:-1])

for exercise, duration, pos, color in zip(exercises, durations, positions, colors):
    ax.barh(0, duration, left=pos, height=0.5, color=color, edgecolor='black', linewidth=1.5)
    ax.text(pos + duration/2, 0, f'{exercise}\n({duration} min)', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

ax.set_xlim(-2, 105)
ax.set_ylim(-0.6, 0.6)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_title('OpenSea Analysis Lab: 100 Minutes', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
