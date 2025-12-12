"""Tokenomics Lab Workflow"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))
exercises = ['Choose\nProject', 'Gather\nBasic Info', 'Analyze\nDistribution', 'Calculate\nMetrics', 'Develop\nThesis', 'Write\nReport']
durations = [5, 15, 20, 20, 20, 10]
colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE]
positions = np.cumsum([0] + durations[:-1])

for i, (pos, dur, ex, col) in enumerate(zip(positions, durations, exercises, colors)):
    ax.barh(0, dur, left=pos, height=0.5, color=col, edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.text(pos + dur/2, 0, ex, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(pos + dur/2, -0.4, f'{dur} min', ha='center', va='center', fontsize=9)

ax.set_xlim(-2, 95)
ax.set_ylim(-0.8, 0.8)
ax.set_xlabel('Time (minutes)', fontsize=12)
ax.set_title('Tokenomics Analysis Lab: 90-Minute Session', fontweight='bold', fontsize=14)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.1)
ax.set_yticks([])
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
