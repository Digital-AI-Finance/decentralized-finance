"""NFT Valuation Factors"""
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

factors = ['Rarity/Scarcity', 'Artist/Brand', 'Community', 'Utility', 'Historical Sales']
weights = [25, 20, 20, 20, 15]
colors = [MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE]

wedges, texts, autotexts = ax.pie(weights, labels=factors, colors=colors, autopct='%1.0f%%', startangle=90, textprops={'fontsize': 10})
ax.set_title('NFT Valuation Factors', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
