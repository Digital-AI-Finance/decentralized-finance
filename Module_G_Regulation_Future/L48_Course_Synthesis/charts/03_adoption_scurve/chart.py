"""
Crypto Adoption S-Curve
Technology adoption lifecycle
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Adoption S-Curve',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L48_Course_Synthesis/charts/03_adoption_scurve'
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

# S-curve data (logistic function)
x = np.linspace(0, 12, 100)
y = 100 / (1 + np.exp(-1.2 * (x - 6)))

ax.plot(x, y, 'b-', linewidth=3, color=MLBLUE)
ax.fill_between(x, y, alpha=0.2, color=MLBLUE)

# Add adoption phases
phases = [
    (1.5, 5, 'Innovators\n(2009-2013)', MLPURPLE),
    (3.5, 15, 'Early Adopters\n(2014-2017)', MLORANGE),
    (6, 50, 'Early Majority\n(2018-2024)', MLGREEN),
    (8.5, 85, 'Late Majority\n(2025-2030)', MLBLUE),
    (10.5, 97, 'Laggards\n(2030+)', MLRED),
]

for x_pos, y_pos, label, color in phases:
    ax.axvline(x=x_pos, color=color, linestyle='--', alpha=0.5, linewidth=1)
    ax.text(x_pos, y_pos + 5, label, ha='center', va='bottom', fontsize=9,
            color=color, fontweight='bold')

# Mark current position (2024)
current_x = 5.8
current_y = 100 / (1 + np.exp(-1.2 * (current_x - 6)))
ax.scatter([current_x], [current_y], s=150, c=MLRED, zorder=5, edgecolors='black', linewidth=2)
ax.annotate('We Are Here\n(2024)', (current_x, current_y),
            xytext=(current_x - 1.5, current_y + 15),
            fontsize=10, fontweight='bold', color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))

# Add percentage labels
ax.text(11, 95, 'Global\nAdoption', ha='center', va='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_xlabel('Time (Years)', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.set_xlim(0, 12)
ax.set_ylim(0, 105)
ax.set_xticks([])  # Hide x-axis ticks (years are shown in labels)

ax.grid(True, alpha=0.3)
ax.set_title('Cryptocurrency Adoption S-Curve', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
