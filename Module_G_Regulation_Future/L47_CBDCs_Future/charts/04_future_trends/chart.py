"""
Blockchain Future Trends (2025+)
Horizontal bar showing trend importance/adoption
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Future Trends',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L47_CBDCs_Future/charts/04_future_trends'
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

# Future trends and their adoption/importance score
trends = ['RWA Tokenization', 'AI + Blockchain', 'DePIN', 'Account\nAbstraction',
          'Modular\nBlockchains', 'ZK Proofs', 'Liquid Staking', 'ReFi/DeSci']
adoption_2024 = [25, 20, 15, 30, 25, 35, 50, 10]  # Current
projected_2027 = [70, 55, 45, 65, 60, 80, 75, 30]  # Projected

y = np.arange(len(trends))
height = 0.35

bars1 = ax.barh(y - height/2, adoption_2024, height, label='2024 Adoption', color=MLBLUE, edgecolor='black')
bars2 = ax.barh(y + height/2, projected_2027, height, label='2027 Projected', color=MLGREEN, edgecolor='black')

ax.set_yticks(y)
ax.set_yticklabels(trends, fontsize=14)
ax.set_xlabel('Adoption/Maturity Level (%)', fontsize=15)
ax.set_xlim(0, 100)

ax.legend(loc='lower right', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')

# Growth annotation
ax.text(85, 5, 'ZK proofs:\n+45%', fontsize=14, color=MLGREEN,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Blockchain Future Trends: Current vs Projected', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
