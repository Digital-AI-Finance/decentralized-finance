"""
Tokenized Treasury Market Leaders
Horizontal bar chart showing AUM by platform
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Tokenized Treasury Market',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/02_tokenized_treasury_market'
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

# Platforms and AUM (millions USD)
platforms = ['BlackRock\nBUILD', 'Franklin\nTempleton', 'Ondo\nFinance', 'Backed\nFinance', 'MatrixDock']
aum = [500, 400, 200, 100, 80]  # Millions USD
colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, '#888888']

y_pos = np.arange(len(platforms))

bars = ax.barh(y_pos, aum, color=colors, edgecolor='black', linewidth=0.5, height=0.6)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, aum)):
    ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
            f'${val}M', va='center', ha='left', fontsize=11, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(platforms, fontsize=10, fontweight='bold')
ax.set_xlabel('Assets Under Management (Millions USD)', fontsize=12)
ax.set_xlim(0, 600)
ax.grid(True, alpha=0.3, axis='x')

# Total market annotation
total = sum(aum)
ax.text(0.95, 0.05, f'Total: ${total/1000:.1f}B+', transform=ax.transAxes,
        ha='right', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Tokenized US Treasury Market Leaders (2024)', fontweight='bold', fontsize=15, pad=10)
ax.invert_yaxis()
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
