"""Slippage Impact by Trade Size"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLRED = '#0066CC', '#FF7F0E', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

trade_sizes = np.array([0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0])
slippage = np.array([0.05, 0.15, 0.3, 1.2, 2.5, 5.0, 12.5])

colors = [MLBLUE if s < 1 else MLORANGE if s < 5 else MLRED for s in slippage]
bars = ax.bar(range(len(trade_sizes)), slippage, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

for bar, sl in zip(bars, slippage):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{sl}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.axhline(y=1, color=MLORANGE, linestyle='--', alpha=0.5, linewidth=2)
ax.text(6.5, 1.3, 'Caution', fontsize=9, color=MLORANGE)
ax.axhline(y=5, color=MLRED, linestyle='--', alpha=0.5, linewidth=2)
ax.text(6.5, 5.3, 'High Impact', fontsize=9, color=MLRED)

ax.set_xticks(range(len(trade_sizes)))
ax.set_xticklabels([f'{s} ETH' for s in trade_sizes])
ax.set_xlabel('Trade Size', fontsize=12)
ax.set_ylabel('Price Slippage (%)', fontsize=12)
ax.set_title('Slippage Impact Increases Non-Linearly', fontweight='bold', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
