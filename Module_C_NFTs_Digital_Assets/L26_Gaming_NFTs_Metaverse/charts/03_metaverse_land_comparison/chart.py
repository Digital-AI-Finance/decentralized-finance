"""
Metaverse Virtual Land Comparison
Comparing major metaverse platforms
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Metaverse Land Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse/charts/03_metaverse_land_comparison'
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

# Platforms and metrics (normalized 1-10)
platforms = ['Decentraland', 'The Sandbox', 'Otherside\n(Yuga)', 'Somnium\nSpace']
metrics = {
    'Land Supply': [3, 5, 4, 2],           # Lower = more scarce
    'User Activity': [2, 3, 5, 1],          # Daily active users
    'Brand Partners': [7, 9, 8, 3],         # Major brand presence
    'Floor Price': [2, 3, 7, 2],            # Current value retention
}

x = np.arange(len(platforms))
width = 0.2
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=metric,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(platforms, fontsize=14, fontweight='bold')
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=14, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Platform details
details = ['90K parcels\n<1K DAU', '166K parcels\nPolygon', '100K parcels\nIn Dev', 'VR Focus\nNiche']
for i, detail in enumerate(details):
    ax.text(i, -1.2, detail, ha='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('Metaverse Virtual Land Platform Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
