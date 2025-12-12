"""
Layer 2 Throughput and Cost Comparison
Horizontal bar chart
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'L2 Throughput Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L41_Layer2_Scaling/charts/02_l2_throughput_comparison'
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

# Layer solutions and their TPS
solutions = ['Ethereum L1', 'Optimistic\nRollups', 'ZK-Rollups', 'Sidechains', 'Lightning\nNetwork']
tps = [15, 2000, 5000, 10000, 1000000]  # Log scale better
colors = [MLRED, MLORANGE, MLGREEN, MLBLUE, '#F7931A']

y_pos = np.arange(len(solutions))

bars = ax.barh(y_pos, tps, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

# Add value labels
for bar, val in zip(bars, tps):
    if val >= 1000000:
        label = f'{val/1000000:.0f}M TPS'
    elif val >= 1000:
        label = f'{val/1000:.0f}K TPS'
    else:
        label = f'{val} TPS'
    ax.text(bar.get_width() * 1.05, bar.get_y() + bar.get_height()/2,
            label, va='center', fontsize=10, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(solutions, fontsize=10)
ax.set_xlabel('Transactions Per Second (TPS)', fontsize=12)
ax.set_xscale('log')
ax.set_xlim(10, 2000000)

ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')

# Visa comparison line
ax.axvline(x=65000, color='gray', linestyle='--', linewidth=2, alpha=0.7)
ax.text(65000, -0.5, 'Visa (65K TPS)', fontsize=9, ha='center', color='gray')

ax.set_title('Blockchain Throughput Comparison (Log Scale)', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
