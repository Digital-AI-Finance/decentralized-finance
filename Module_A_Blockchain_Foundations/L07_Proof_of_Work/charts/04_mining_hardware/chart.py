"""
Mining Hardware Evolution
Shows progression from CPU to ASIC
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Mining Hardware Evolution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/04_mining_hardware'
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

# Hardware generations
hardware = ['CPU\n(2009-2010)', 'GPU\n(2010-2013)', 'FPGA\n(2011-2013)', 'ASIC\n(2013-Now)']
hash_rates = [10, 500, 800, 200000000]  # MH/s (ASIC in TH/s scaled)
efficiency = [0.1, 1, 5, 50]  # MH/J approximate

# Colors
colors = [MLBLUE, MLGREEN, MLORANGE, MLRED]

# Bar chart for hash rate (log scale)
bars = ax.bar(hardware, hash_rates, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)

# Add value labels
labels_text = ['~10 MH/s', '~500 MH/s', '~1 GH/s', '~200 TH/s']
for bar, label in zip(bars, labels_text):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height * 1.1,
            label, ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_yscale('log')
ax.set_ylabel('Hash Rate (log scale)', fontsize=13)
ax.set_xlabel('Hardware Generation', fontsize=13)
ax.set_ylim(1, 1e10)

# Efficiency annotation
ax.text(0.02, 0.95, 'Efficiency Improvement:', transform=ax.transAxes,
        fontsize=11, fontweight='bold', color='#333')
ax.text(0.02, 0.88, 'ASIC is ~10,000x more efficient than CPU', transform=ax.transAxes,
        fontsize=10, color='#555')

# Timeline annotation
timeline = [('2009', 0), ('2010', 0.75), ('2013', 2.25), ('2024', 3.25)]
for year, x in timeline:
    ax.axvline(x=x, ymin=0, ymax=0.05, color='#888', linewidth=2)

ax.set_title('Bitcoin Mining Hardware Evolution', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
