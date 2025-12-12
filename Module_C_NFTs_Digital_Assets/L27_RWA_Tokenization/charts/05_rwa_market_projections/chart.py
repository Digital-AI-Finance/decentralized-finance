"""
RWA Market Projections
Bar chart showing growth projections
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'RWA Market Projections',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/05_rwa_market_projections'
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

# Market projections (trillions USD)
years = ['2024\n(Current)', '2027\n(BCG)', '2030\n(Citi)', '2030\n(BCG)']
values = [0.05, 2, 5, 16]  # Trillions USD
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

x = np.arange(len(years))

bars = ax.bar(x, values, color=colors, edgecolor='black', linewidth=1, alpha=0.85)

# Add value labels
for bar, val in zip(bars, values):
    height = bar.get_height()
    if val < 1:
        label = f'${val*1000:.0f}B'
    else:
        label = f'${val:.0f}T'
    ax.annotate(label,
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5), textcoords="offset points",
                ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_ylabel('Market Size (Trillions USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=10, fontweight='bold')
ax.set_ylim(0, 20)

ax.grid(True, alpha=0.3, axis='y')

# Growth annotation
ax.annotate('320x Growth\n(2024-2030)', xy=(3, 16), xytext=(2, 18),
            fontsize=10, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='black'))

ax.set_title('Tokenized RWA Market Projections', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
