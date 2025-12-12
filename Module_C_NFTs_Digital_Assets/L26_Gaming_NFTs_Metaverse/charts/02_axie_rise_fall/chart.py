"""
Axie Infinity Rise and Fall
Dual-axis chart showing users and SLP price
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Axie Rise and Fall',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse/charts/02_axie_rise_fall'
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

fig, ax1 = plt.subplots(figsize=(10, 6))

# Timeline data
months = ['Jan\n2021', 'Apr', 'Jul', 'Oct', 'Jan\n2022', 'Apr', 'Jul', 'Jan\n2023', 'Jan\n2024']
x = np.arange(len(months))

# Daily Active Users (millions)
dau = [0.05, 0.3, 2.8, 2.5, 1.5, 0.8, 0.5, 0.1, 0.01]

# SLP Price (USD)
slp_price = [0.05, 0.15, 0.30, 0.10, 0.02, 0.01, 0.008, 0.004, 0.003]

# Plot DAU on left axis
color1 = MLBLUE
ax1.fill_between(x, dau, alpha=0.3, color=color1)
ax1.plot(x, dau, color=color1, linewidth=2.5, marker='o', markersize=6, label='Daily Active Users')
ax1.set_ylabel('Daily Active Users (Millions)', color=color1, fontsize=12)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, 3.5)

# Plot SLP price on right axis
ax2 = ax1.twinx()
color2 = MLORANGE
ax2.plot(x, slp_price, color=color2, linewidth=2.5, marker='s', markersize=6, label='SLP Price')
ax2.set_ylabel('SLP Price (USD)', color=color2, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(0, 0.4)

# Annotations
ax1.annotate('Peak: 2.8M DAU', xy=(2, 2.8), xytext=(3, 3.2),
             fontsize=9, fontweight='bold', color=MLBLUE,
             arrowprops=dict(arrowstyle='->', color=MLBLUE))

ax1.annotate('Ronin\nHack', xy=(5, 0.8), xytext=(5, 1.5),
             fontsize=8, color=MLRED, ha='center',
             arrowprops=dict(arrowstyle='->', color=MLRED))

ax2.annotate('SLP: -99%', xy=(8, 0.003), xytext=(7, 0.1),
             fontsize=9, fontweight='bold', color=MLORANGE,
             arrowprops=dict(arrowstyle='->', color=MLORANGE))

ax1.set_xticks(x)
ax1.set_xticklabels(months, fontsize=9)
ax1.grid(True, alpha=0.3, axis='y')

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=10)

ax1.set_title('Axie Infinity: Rise and Fall (2021-2024)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
