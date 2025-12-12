"""
RWA Tokenization Benefits
Comparing traditional vs tokenized ownership
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'RWA Benefits',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/03_rwa_benefits'
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

# Benefits and comparison scores (1-10)
benefits = ['Fractional\nOwnership', 'Liquidity', 'Settlement\nSpeed', 'Global\nAccess', 'Transparency']

traditional = [2, 2, 3, 3, 4]  # Traditional ownership
tokenized = [9, 8, 9, 9, 10]   # Tokenized ownership

x = np.arange(len(benefits))
width = 0.35

bars1 = ax.bar(x - width/2, traditional, width, label='Traditional',
               color=MLRED, edgecolor='black', linewidth=0.5, alpha=0.85)
bars2 = ax.bar(x + width/2, tokenized, width, label='Tokenized',
               color=MLGREEN, edgecolor='black', linewidth=0.5, alpha=0.85)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=14, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(benefits, fontsize=14, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper left', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

ax.set_title('Traditional vs Tokenized Asset Ownership', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
