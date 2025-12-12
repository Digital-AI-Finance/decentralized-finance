"""Sample Token Distribution Template"""
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

categories = ['Community/Public', 'Team & Founders', 'Investors (VCs)', 'Ecosystem Fund', 'Treasury', 'Liquidity']
sizes = [30, 20, 15, 15, 12, 8]
colors = [MLBLUE, MLRED, MLORANGE, MLGREEN, MLPURPLE, '#888888']
explode = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=categories, colors=colors,
                                   autopct='%1.0f%%', startangle=90,
                                   pctdistance=0.75, labeldistance=1.15,
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

ax.set_title('Sample Token Distribution (Fill In Your Data)', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
