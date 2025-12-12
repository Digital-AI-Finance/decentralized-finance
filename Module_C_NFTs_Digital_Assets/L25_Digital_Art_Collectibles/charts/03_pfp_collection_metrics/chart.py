"""
Blue-Chip PFP Collection Metrics
Comparing major PFP collections
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'PFP Collection Metrics',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles/charts/03_pfp_collection_metrics'
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

# PFP collections and metrics (normalized scores 1-10)
collections = ['CryptoPunks\n(2017)', 'BAYC\n(2021)', 'Azuki\n(2022)', 'Doodles\n(2021)']
metrics = {
    'Floor Price': [10, 7, 4, 3],       # Relative floor
    'Community': [8, 10, 7, 6],          # Discord/engagement
    'Brand Value': [9, 10, 6, 5],        # Recognition
    'Utility': [3, 9, 7, 5],             # IP rights, airdrops
}

x = np.arange(len(collections))
width = 0.2
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width - 0.3, values, width, label=metric,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(collections, fontsize=14, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=14, ncol=2)
ax.grid(True, alpha=0.3, axis='y')

# Note about floor prices
ax.text(0.5, -0.12, 'Floor prices (2024): CryptoPunks ~50 ETH, BAYC ~25 ETH, Azuki ~3 ETH, Doodles ~2 ETH',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('Blue-Chip PFP Collection Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
