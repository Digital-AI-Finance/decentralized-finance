"""Testnet Swap Lab Workflow"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))
exercises = ['Setup\nMetaMask', 'Get Test\nETH', 'First\nSwap', 'Analyze\nSlippage', 'Provide\nLiquidity', 'Monitor\n& Remove']
durations = [10, 10, 15, 15, 20, 20]
colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE]
positions = np.cumsum([0] + durations[:-1])

for i, (pos, dur, ex, col) in enumerate(zip(positions, durations, exercises, colors)):
    ax.barh(0, dur, left=pos, height=0.5, color=col, edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.text(pos + dur/2, 0, ex, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax.text(pos + dur/2, -0.4, f'{dur} min', ha='center', va='center', fontsize=14)

ax.set_xlim(-2, 95)
ax.set_ylim(-0.8, 0.8)
ax.set_xlabel('Time (minutes)', fontsize=15)
ax.set_title('Testnet Swap Lab: 90-Minute Session', fontweight='bold', fontsize=14)
ax.set_yticks([])
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
