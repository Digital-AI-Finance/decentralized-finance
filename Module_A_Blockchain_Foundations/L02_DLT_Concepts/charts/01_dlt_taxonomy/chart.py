"""
DLT Taxonomy: Blockchain vs Other DLT Types
Shows the relationship between DLT, blockchain, DAG, and other ledger technologies
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DLT Taxonomy',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L02_DLT_Concepts/charts/01_dlt_taxonomy'
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

# Large outer ellipse - DLT
dlt_ellipse = Ellipse((0.5, 0.5), 0.9, 0.85, facecolor='#E8E8FF',
                       edgecolor=MLPURPLE, linewidth=3, alpha=0.5)
ax.add_patch(dlt_ellipse)
ax.text(0.5, 0.92, 'Distributed Ledger Technology (DLT)', ha='center', va='center',
        fontsize=16, fontweight='bold', color=MLPURPLE)

# Blockchain ellipse (left)
blockchain_ellipse = Ellipse((0.32, 0.48), 0.38, 0.55, facecolor='#FFE4B5',
                              edgecolor=MLORANGE, linewidth=2.5, alpha=0.6)
ax.add_patch(blockchain_ellipse)
ax.text(0.32, 0.72, 'Blockchain', ha='center', va='center',
        fontsize=15, fontweight='bold', color=MLORANGE)

# Blockchain examples
ax.text(0.32, 0.58, 'Bitcoin', ha='center', va='center', fontsize=12, color='#444')
ax.text(0.32, 0.48, 'Ethereum', ha='center', va='center', fontsize=12, color='#444')
ax.text(0.32, 0.38, 'Cardano', ha='center', va='center', fontsize=12, color='#444')
ax.text(0.32, 0.28, 'Solana', ha='center', va='center', fontsize=12, color='#444')

# DAG ellipse (right)
dag_ellipse = Ellipse((0.68, 0.48), 0.32, 0.45, facecolor='#E0FFE0',
                       edgecolor=MLGREEN, linewidth=2.5, alpha=0.6)
ax.add_patch(dag_ellipse)
ax.text(0.68, 0.68, 'DAG', ha='center', va='center',
        fontsize=15, fontweight='bold', color=MLGREEN)

# DAG examples
ax.text(0.68, 0.52, 'IOTA (Tangle)', ha='center', va='center', fontsize=12, color='#444')
ax.text(0.68, 0.42, 'Hedera', ha='center', va='center', fontsize=12, color='#444')
ax.text(0.68, 0.32, 'Nano', ha='center', va='center', fontsize=12, color='#444')

# Other DLT label
ax.text(0.85, 0.18, 'Other DLTs:', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLBLUE)
ax.text(0.85, 0.10, 'Holochain, Tempo', ha='center', va='center',
        fontsize=11, color='#666', style='italic')

# Key insight box
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=MLPURPLE, alpha=0.9)
ax.text(0.5, 0.03, 'All blockchains are DLTs, but not all DLTs are blockchains',
        ha='center', va='center', fontsize=13, style='italic',
        bbox=props, color=MLPURPLE)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('DLT Taxonomy: Types of Distributed Ledgers', fontweight='bold', fontsize=16, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
