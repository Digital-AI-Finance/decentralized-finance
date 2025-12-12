"""NFT Evaluation Lab Workflow"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))
exercises = ['Setup', 'Ex 1: Project\nResearch', 'Ex 2: On-chain\nAnalysis', 'Ex 3: Risk\nAssessment', 'Report']
durations = [5, 30, 30, 25, 10]
colors = [MLPURPLE, MLBLUE, MLORANGE, MLRED, MLPURPLE]
positions = np.cumsum([0] + durations[:-1])

for exercise, duration, pos, color in zip(exercises, durations, positions, colors):
    ax.barh(0, duration, left=pos, height=0.5, color=color, edgecolor='black', linewidth=1.5)
    ax.text(pos + duration/2, 0, f'{exercise}\n({duration} min)', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

ax.set_xlim(-2, 105)
ax.set_ylim(-0.6, 0.6)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_title('NFT Evaluation Lab: 100 Minutes', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
