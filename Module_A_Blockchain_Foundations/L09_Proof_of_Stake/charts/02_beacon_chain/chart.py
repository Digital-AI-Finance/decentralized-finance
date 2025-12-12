"""
Ethereum Beacon Chain Architecture
Shows two-layer design after The Merge
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Beacon Chain Architecture',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/02_beacon_chain'
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

# Consensus Layer (top)
cl_box = FancyBboxPatch((0.10, 0.55), 0.80, 0.35,
                         boxstyle="round,pad=0.02", facecolor=MLGREEN,
                         edgecolor='black', linewidth=2)
ax.add_patch(cl_box)
ax.text(0.50, 0.85, 'Consensus Layer (Beacon Chain)', ha='center',
        fontsize=14, fontweight='bold', color='white')

# CL components
cl_components = [
    (0.20, 0.70, 'Validator\nSelection'),
    (0.40, 0.70, 'Block\nProposal'),
    (0.60, 0.70, 'Attestations'),
    (0.80, 0.70, 'Finality'),
]

for x, y, text in cl_components:
    box = FancyBboxPatch((x - 0.07, y - 0.06), 0.14, 0.12,
                          boxstyle="round,pad=0.01", facecolor='white',
                          edgecolor='black', linewidth=1)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#333')

# Engine API (connection)
api_box = FancyBboxPatch((0.35, 0.45), 0.30, 0.08,
                          boxstyle="round,pad=0.01", facecolor=MLORANGE,
                          edgecolor='black', linewidth=2)
ax.add_patch(api_box)
ax.text(0.50, 0.49, 'Engine API', ha='center', fontsize=11,
        fontweight='bold', color='white')

# Arrows
ax.annotate('', xy=(0.50, 0.53), xytext=(0.50, 0.55),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=2))

# Execution Layer (bottom)
el_box = FancyBboxPatch((0.10, 0.10), 0.80, 0.33,
                         boxstyle="round,pad=0.02", facecolor=MLBLUE,
                         edgecolor='black', linewidth=2)
ax.add_patch(el_box)
ax.text(0.50, 0.38, 'Execution Layer', ha='center',
        fontsize=14, fontweight='bold', color='white')

# EL components
el_components = [
    (0.20, 0.23, 'Transactions'),
    (0.40, 0.23, 'EVM'),
    (0.60, 0.23, 'State'),
    (0.80, 0.23, 'Smart\nContracts'),
]

for x, y, text in el_components:
    box = FancyBboxPatch((x - 0.07, y - 0.06), 0.14, 0.12,
                          boxstyle="round,pad=0.01", facecolor='white',
                          edgecolor='black', linewidth=1)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#333')

# Client labels on sides
ax.text(0.02, 0.72, 'CL Clients:\nPrysm\nLighthouse\nTeku\nNimbus', ha='left',
        fontsize=9, color='#555', va='center')
ax.text(0.02, 0.23, 'EL Clients:\nGeth\nNethermind\nErigon\nBesu', ha='left',
        fontsize=9, color='#555', va='center')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Ethereum Post-Merge: Two-Layer Architecture', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
