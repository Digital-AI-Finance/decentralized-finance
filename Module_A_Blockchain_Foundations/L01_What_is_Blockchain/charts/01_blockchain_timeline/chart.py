"""
Blockchain Timeline: Key Events 1991-2025
Real historical data for MSc-level course
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Blockchain Technology Timeline 1991-2025',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L01_What_is_Blockchain/charts/01_blockchain_timeline'
}

# Set font sizes (MANDATORY)
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

# Color palette
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Real historical events with verified dates
events = [
    (1991, "Haber & Stornetta\nTimestamping", "research"),
    (1992, "Merkle Trees\nIntegrated", "research"),
    (1998, "Nick Szabo\nBit Gold", "research"),
    (2004, "Hal Finney\nRPOW", "research"),
    (2008, "Bitcoin\nWhitepaper", "bitcoin"),
    (2009, "Genesis\nBlock", "bitcoin"),
    (2010, "10K BTC\nPizza", "bitcoin"),
    (2013, "BTC > $1000", "market"),
    (2014, "Ethereum\nWhitepaper", "ethereum"),
    (2015, "Ethereum\nMainnet", "ethereum"),
    (2017, "ICO Boom\n$5.6B", "market"),
    (2020, "DeFi Summer\n$15B TVL", "defi"),
    (2021, "NFT Boom\n$25B", "market"),
    (2022, "ETH Merge\nPoS", "ethereum"),
    (2024, "Bitcoin ETF\nApproved", "institutional"),
    (2025, "MiCA\nEnforced", "regulation"),
]

# Color mapping for event types
colors = {
    "research": MLPURPLE,
    "bitcoin": MLORANGE,
    "ethereum": MLBLUE,
    "market": MLGREEN,
    "defi": MLRED,
    "institutional": '#8B4513',
    "regulation": '#4B0082'
}

fig, ax = plt.subplots(figsize=(10, 6))

# Draw timeline axis
years = [e[0] for e in events]
ax.axhline(y=0, color='black', linewidth=2, zorder=1)
ax.scatter(years, [0]*len(years), s=100, c='black', zorder=2)

# Alternate labels above and below
for i, (year, label, etype) in enumerate(events):
    y_offset = 0.4 if i % 2 == 0 else -0.4
    va = 'bottom' if i % 2 == 0 else 'top'

    # Draw vertical connector
    ax.plot([year, year], [0, y_offset * 0.8], color=colors[etype], linewidth=1.5, zorder=1)

    # Draw label
    ax.annotate(label, xy=(year, y_offset), fontsize=14, ha='center', va=va,
                color=colors[etype], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=colors[etype], alpha=0.9))

# Configure axes
ax.set_xlim(1989, 2027)
ax.set_ylim(-0.8, 0.8)
ax.set_xlabel('Year')
ax.set_title('Evolution of Blockchain Technology: 1991-2025', fontweight='bold', fontsize=15)

# Remove y-axis
ax.yaxis.set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add legend
legend_elements = [
    mpatches.Patch(facecolor=MLPURPLE, label='Research'),
    mpatches.Patch(facecolor=MLORANGE, label='Bitcoin'),
    mpatches.Patch(facecolor=MLBLUE, label='Ethereum'),
    mpatches.Patch(facecolor=MLGREEN, label='Market'),
    mpatches.Patch(facecolor=MLRED, label='DeFi'),
]
ax.legend(handles=legend_elements, loc='upper left', ncol=5, fontsize=14)

# Add x-axis ticks
ax.set_xticks([1991, 1995, 2000, 2005, 2010, 2015, 2020, 2025])

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
