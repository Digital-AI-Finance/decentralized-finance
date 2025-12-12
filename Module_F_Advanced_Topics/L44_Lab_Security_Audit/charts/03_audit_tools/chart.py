"""Security Audit Tools Comparison"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN = '#0066CC', '#FF7F0E', '#2CA02C'

fig, ax = plt.subplots(figsize=(10, 6))

tools = ['Manual\nReview', 'Slither', 'Mythril']
categories = ['Speed', 'Deep Analysis', 'Coverage', 'False Positive Rate']
data = {
    'Manual\nReview': [2, 10, 8, 2],
    'Slither': [10, 5, 7, 4],
    'Mythril': [4, 9, 6, 5]
}
colors = [MLBLUE, MLORANGE, MLGREEN]

x = np.arange(len(categories))
width = 0.25

for i, (tool, color) in enumerate(zip(tools, colors)):
    offset = (i - 1) * width
    bars = ax.bar(x + offset, data[tool], width, label=tool, color=color, edgecolor='black', linewidth=1)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 12)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.set_title('Security Audit Tools Comparison', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
