"""
Course Module Overview
Treemap showing 7 modules and lesson distribution
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Course Modules',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L48_Course_Synthesis/charts/01_course_modules'
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
MLCYAN = '#17BECF'
MLPINK = '#E377C2'

fig, ax = plt.subplots(figsize=(10, 6))

# Module data
modules = ['A: Blockchain\nFoundations', 'B: Ethereum &\nSmart Contracts',
           'C: NFTs &\nDigital Assets', 'D: Tokenomics',
           'E: DeFi\nEcosystem', 'F: Advanced\nTopics', 'G: Regulation\n& Future']
lessons = [12, 8, 8, 4, 8, 4, 4]
colors = [MLBLUE, MLPURPLE, MLORANGE, MLGREEN, MLRED, MLCYAN, MLPINK]

# Create horizontal bar chart
y_pos = np.arange(len(modules))
bars = ax.barh(y_pos, lessons, color=colors, edgecolor='black', linewidth=1.5, height=0.7)

# Add value labels
for bar, val in zip(bars, lessons):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{val} lessons', ha='left', va='center', fontsize=14, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(modules, fontsize=14)
ax.set_xlabel('Number of Lessons', fontsize=15)
ax.set_xlim(0, 15)
ax.invert_yaxis()

ax.grid(True, alpha=0.3, axis='x')

# Add total annotation
ax.text(0.98, 0.02, f'Total: {sum(lessons)} lessons\n12 weeks',
        transform=ax.transAxes, fontsize=14, ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Course Structure: 7 Modules, 48 Lessons', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
