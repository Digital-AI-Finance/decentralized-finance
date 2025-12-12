"""
Solidity Visibility Modifiers Comparison
Shows what can access functions with different visibility
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Visibility Modifiers',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals/charts/03_visibility_modifiers'
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

# Visibility modifiers and their accessibility
modifiers = ['public', 'external', 'internal', 'private']
callers = ['External\n(EOA/Contract)', 'Same\nContract', 'Derived\nContract']

# Access matrix: 1 = accessible, 0 = not accessible
access_matrix = np.array([
    [1, 1, 1],  # public: all can access
    [1, 0, 0],  # external: only external calls
    [0, 1, 1],  # internal: same + derived
    [0, 1, 0],  # private: only same
])

# Create heatmap
colors = np.where(access_matrix == 1, MLGREEN, MLRED)

for i, mod in enumerate(modifiers):
    for j, caller in enumerate(callers):
        rect = plt.Rectangle((j, len(modifiers) - 1 - i), 1, 1,
                              facecolor=colors[i, j], alpha=0.7,
                              edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        symbol = 'Y' if access_matrix[i, j] == 1 else 'N'
        color = 'white'
        ax.text(j + 0.5, len(modifiers) - 1 - i + 0.5, symbol,
                ha='center', va='center', fontsize=14, fontweight='bold', color=color)

# Labels
ax.set_xticks([0.5, 1.5, 2.5])
ax.set_xticklabels(callers, fontsize=14)
ax.set_yticks([0.5, 1.5, 2.5, 3.5])
ax.set_yticklabels(reversed(modifiers), fontsize=14, fontweight='bold')

ax.set_xlim(0, 3)
ax.set_ylim(0, 4)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=MLGREEN, alpha=0.7, label='Can Access'),
    Patch(facecolor=MLRED, alpha=0.7, label='Cannot Access'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=14,
          bbox_to_anchor=(1.0, 1.15))

# Key insight
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN)
ax.text(1.5, -0.4, 'Tip: Use external for gas efficiency when only called from outside',
        ha='center', fontsize=14, bbox=props, color=MLGREEN)

ax.set_title('Solidity Function Visibility Access', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
