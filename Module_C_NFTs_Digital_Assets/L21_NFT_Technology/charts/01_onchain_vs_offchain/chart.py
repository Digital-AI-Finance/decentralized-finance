"""On-Chain vs Off-Chain NFT Data Comparison"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 12,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Storage Cost', 'Permanence', 'Speed', 'Flexibility', 'Decentralization']
on_chain = [2, 10, 3, 4, 10]
off_chain = [9, 4, 9, 9, 3]
x = np.arange(len(categories))
width = 0.35

bars1 = ax.barh(x - width/2, on_chain, width, label='On-Chain', color='#3333B2')
bars2 = ax.barh(x + width/2, off_chain, width, label='Off-Chain', color='#FF7F0E')
ax.set_xlabel('Score (1-10)')
ax.set_title('On-Chain vs Off-Chain NFT Data Storage')
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.legend(loc='lower right')
ax.set_xlim(0, 11)

for bar in bars1:
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', va='center', fontsize=11)
for bar in bars2:
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', va='center', fontsize=11)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
