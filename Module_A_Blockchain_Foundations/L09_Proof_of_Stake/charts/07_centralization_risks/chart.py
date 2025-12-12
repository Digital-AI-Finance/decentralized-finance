"""
Ethereum Staking Centralization
Shows stake distribution among entities
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Staking Centralization',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/07_centralization_risks'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Staking distribution (approximate 2024)
entities = ['Lido', 'Coinbase', 'Binance', 'Kraken', 'Rocket Pool', 'Others']
percentages = [28, 13, 5, 4, 3, 47]
colors = [MLORANGE, MLBLUE, MLLAVENDER, MLPURPLE, MLGREEN, '#CCCCCC']

# Create pie chart
wedges, texts, autotexts = ax.pie(percentages, labels=entities, autopct='%1.0f%%',
                                   colors=colors, startangle=90,
                                   textprops={'fontsize': 11})

# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontweight('bold')

# Add danger zone annotation
ax.text(0, -1.35, 'Top 5 entities: ~53% of staked ETH', ha='center',
        fontsize=15, fontweight='bold', color=MLRED)
ax.text(0, -1.50, '33% threshold = finality blocking power', ha='center',
        fontsize=14, color='#555', style='italic')

# Decentralization trends
ax.text(1.2, 0.6, 'Trends:', ha='left', fontsize=14, fontweight='bold')
ax.text(1.2, 0.45, '- Lido share declining', ha='left', fontsize=14, color=MLGREEN)
ax.text(1.2, 0.30, '- Solo stakers growing', ha='left', fontsize=14, color=MLGREEN)
ax.text(1.2, 0.15, '- DVT adoption rising', ha='left', fontsize=14, color=MLGREEN)

ax.set_title('Ethereum Staking Concentration (2024)', fontweight='bold', fontsize=15, pad=20)

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
