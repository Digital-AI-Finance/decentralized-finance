"""
Security Tools Comparison
Grouped bar comparing tools
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Security Tools',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L43_Smart_Contract_Security/charts/04_security_tools'
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

# Tools and their characteristics (scores 1-10)
tools = ['Slither', 'Mythril', 'Echidna', 'Certora']
speed = [9, 4, 6, 3]
depth = [6, 8, 7, 10]
ease_of_use = [9, 6, 5, 4]

x = np.arange(len(tools))
width = 0.25

bars1 = ax.bar(x - width, speed, width, label='Speed', color=MLBLUE, edgecolor='black')
bars2 = ax.bar(x, depth, width, label='Analysis Depth', color=MLORANGE, edgecolor='black')
bars3 = ax.bar(x + width, ease_of_use, width, label='Ease of Use', color=MLGREEN, edgecolor='black')

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=14)

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(tools, fontsize=14)
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Type annotations
ax.text(0, -1, 'Static', ha='center', fontsize=14, color='gray')
ax.text(1, -1, 'Symbolic', ha='center', fontsize=14, color='gray')
ax.text(2, -1, 'Fuzzing', ha='center', fontsize=14, color='gray')
ax.text(3, -1, 'Formal', ha='center', fontsize=14, color='gray')

ax.set_title('Smart Contract Security Tools Comparison', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
