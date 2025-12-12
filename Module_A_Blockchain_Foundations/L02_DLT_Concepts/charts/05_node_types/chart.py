"""
Node Types Comparison
Bar chart comparing storage, validation, and use cases for different node types
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Node Types Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/05_node_types'
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

# Node types
node_types = ['Full Node', 'Light/SPV', 'Miner (PoW)', 'Validator (PoS)', 'Archive Node']

# Storage requirements (in GB, log scale visualization)
storage = [500, 0.1, 500, 100, 12000]  # GB

# Normalize for visualization (bar heights)
storage_normalized = [np.log10(s + 1) * 25 for s in storage]

# Colors
colors = [MLBLUE, MLGREEN, MLORANGE, MLPURPLE, MLRED]

# Create bars
x = np.arange(len(node_types))
bars = ax.bar(x, storage_normalized, color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)

# Add storage labels on bars
storage_labels = ['~500 GB', '<100 MB', '~500 GB+', '~100 GB', '>12 TB']
for bar, label in zip(bars, storage_labels):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            label, ha='center', va='bottom', fontsize=15, fontweight='bold')

# Trust level indicators (circles at bottom)
trust_levels = ['Trustless', 'Trust others', 'Trustless', 'Trustless', 'Trustless']
for i, (trust, color) in enumerate(zip(trust_levels, colors)):
    if trust == 'Trustless':
        marker_color = MLGREEN
    else:
        marker_color = MLORANGE
    ax.scatter(i, -8, s=200, c=marker_color, marker='s', zorder=5, edgecolor='black', linewidth=1)
    ax.text(i, -15, trust, ha='center', va='top', fontsize=14, color='#444')

# Use cases
use_cases = ['Personal\nsovereignty', 'Mobile\nwallets', 'Mining\nrevenue', 'Staking\nrewards', 'Block\nexplorers']
for i, use in enumerate(use_cases):
    ax.text(i, -28, use, ha='center', va='top', fontsize=14, color='#666', style='italic')

# Customize axes
ax.set_xticks(x)
ax.set_xticklabels(node_types, fontsize=15)
ax.set_ylabel('Relative Storage Requirement', fontsize=16)
ax.set_ylim(-35, 120)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add section labels
ax.text(-0.7, 95, 'Storage:', fontsize=14, fontweight='bold', color='#444')
ax.text(-0.7, -8, 'Trust:', fontsize=14, fontweight='bold', color='#444')
ax.text(-0.7, -28, 'Use Case:', fontsize=14, fontweight='bold', color='#444')

# Add horizontal line separating sections
ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
ax.axhline(y=-20, color='gray', linestyle=':', linewidth=0.5)

plt.title('Blockchain Node Types: Storage & Trust Requirements', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
