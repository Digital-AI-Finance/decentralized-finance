"""
Wash Trading Detection Red Flags
Horizontal bar chart showing detection indicators
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Wash Trading Detection',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces/charts/04_wash_trading_detection'
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

# Red flags with reliability scores (how indicative of wash trading)
red_flags = [
    'Same wallet\nfunding source',
    'Back-and-forth\ntrades (same NFT)',
    'Unprofitable\ntrades',
    'Volume spike\nduring rewards',
    'Low unique\nbuyer count',
]

reliability = [95, 90, 85, 75, 70]  # Reliability as indicator (%)
colors = [MLRED if r >= 85 else MLORANGE for r in reliability]

y_pos = np.arange(len(red_flags))

bars = ax.barh(y_pos, reliability, color=colors, edgecolor='black', linewidth=0.5, height=0.6)

# Add percentage labels
for i, (bar, rel) in enumerate(zip(bars, reliability)):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{rel}%', va='center', ha='left', fontsize=11, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(red_flags, fontsize=10, fontweight='bold')
ax.set_xlabel('Reliability as Wash Trading Indicator (%)', fontsize=12)
ax.set_xlim(0, 105)
ax.grid(True, alpha=0.3, axis='x')

# Threshold line
ax.axvline(x=80, color='#333', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(81, 4.5, 'High\nconfidence\nthreshold', fontsize=8, va='center')

# Detection tools note
ax.text(0.5, -0.12, 'Tools: Nansen wallet analysis, Dune Analytics SQL queries, Chainalysis forensics',
        transform=ax.transAxes, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_title('Wash Trading Detection Indicators', fontweight='bold', fontsize=15, pad=10)
ax.invert_yaxis()
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
