"""
Top Smart Contract Vulnerabilities
Horizontal bar showing most common vulnerability types
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Top Vulnerabilities',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L43_Smart_Contract_Security/charts/01_top_vulnerabilities'
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

# Top vulnerabilities by frequency in exploits
vulnerabilities = ['Access\nControl', 'Reentrancy', 'Oracle\nManipulation', 'Flash Loan\nAttacks',
                   'Bridge\nExploits', 'Integer\nOverflow']
frequency = [30, 20, 18, 15, 12, 5]  # Percentage of total exploits
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN, MLPURPLE, '#CCCCCC']

y_pos = np.arange(len(vulnerabilities))

bars = ax.barh(y_pos, frequency, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, pct in zip(bars, frequency):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct}%', va='center', fontsize=11, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(vulnerabilities, fontsize=10)
ax.set_xlabel('Percentage of Total Exploits', fontsize=12)
ax.set_xlim(0, 40)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Annotation
ax.text(0.5, -0.12, 'Access control failures are now the leading cause of DeFi exploits',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Smart Contract Vulnerability Types by Frequency', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
