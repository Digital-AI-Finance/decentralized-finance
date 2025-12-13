"""NFT Market Evolution"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16, 'xtick.labelsize': 12, 'ytick.labelsize': 12, 'figure.figsize': (10, 6), 'figure.dpi': 150})
fig, ax = plt.subplots(figsize=(10, 6))

years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
volume = [0.03, 0.04, 0.06, 0.34, 24.9, 11.0, 4.1, 5.8]
colors = ['#3333B2', '#3333B2', '#3333B2', '#0066CC', '#2CA02C', '#FF7F0E', '#D62728', '#0066CC']

bars = ax.bar(years, volume, color=colors, edgecolor='black', alpha=0.85)
ax.set_ylabel('Trading Volume (Billion USD)')
ax.set_xlabel('Year')
ax.set_title('NFT Market Trading Volume Evolution')

for bar, val in zip(bars, volume):
    label = f'${val:.1f}B' if val >= 1 else f'${val*1000:.0f}M'
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, label, ha='center', fontsize=14, fontweight='bold')

ax.annotate('CryptoKitties', xy=(0, 0.03), xytext=(0.5, 5), fontsize=14, ha='center', color='#666666', arrowprops=dict(arrowstyle='->', color='#666666', lw=1))
ax.annotate('Beeple 9M', xy=(4, 24.9), xytext=(3, 20), fontsize=14, ha='center', color='#2CA02C', arrowprops=dict(arrowstyle='->', color='#2CA02C', lw=1))
ax.set_ylim(0, 28)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
