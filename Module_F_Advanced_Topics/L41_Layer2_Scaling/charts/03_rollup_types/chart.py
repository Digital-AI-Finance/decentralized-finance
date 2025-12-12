"""
Optimistic vs ZK-Rollups Comparison
Grouped bar chart
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Rollup Types Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L41_Layer2_Scaling/charts/03_rollup_types'
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

# Comparison metrics (scores 1-10)
metrics = ['Security', 'Finality\nSpeed', 'EVM\nCompatibility', 'Gas\nCost', 'Prover\nComplexity']
optimistic = [7, 3, 9, 6, 2]  # 7-day withdrawal = slow finality
zk_rollup = [9, 8, 7, 8, 9]   # Fast finality, high prover complexity

x = np.arange(len(metrics))
width = 0.35

bars1 = ax.bar(x - width/2, optimistic, width, label='Optimistic Rollups', color=MLORANGE, edgecolor='black')
bars2 = ax.bar(x + width/2, zk_rollup, width, label='ZK-Rollups', color=MLGREEN, edgecolor='black')

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords='offset points',
                ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Score (1-10, higher = better)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=10)
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Optimistic vs ZK-Rollups: Feature Comparison', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
