"""
EVM Architecture
Stack-based virtual machine structure
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'EVM Architecture',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/01_evm_architecture'
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

# Main EVM box
evm_box = FancyBboxPatch((0.1, 0.15), 0.8, 0.75,
                          boxstyle="round,pad=0.02", facecolor='#F8F8F8',
                          edgecolor=MLBLUE, linewidth=3)
ax.add_patch(evm_box)
ax.text(0.5, 0.85, 'Ethereum Virtual Machine (EVM)', ha='center',
        fontsize=14, fontweight='bold', color=MLBLUE)

# Stack (left)
stack_box = FancyBboxPatch((0.15, 0.25), 0.18, 0.45,
                            boxstyle="round,pad=0.01", facecolor=MLORANGE,
                            edgecolor='black', linewidth=1.5)
ax.add_patch(stack_box)
ax.text(0.24, 0.65, 'STACK', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.24, 0.55, '256-bit', ha='center', fontsize=14, color='white')
ax.text(0.24, 0.48, 'words', ha='center', fontsize=14, color='white')
ax.text(0.24, 0.38, 'Max 1024', ha='center', fontsize=14, color='white')
ax.text(0.24, 0.30, 'items', ha='center', fontsize=14, color='white')

# Memory (center-left)
mem_box = FancyBboxPatch((0.37, 0.25), 0.18, 0.45,
                          boxstyle="round,pad=0.01", facecolor=MLGREEN,
                          edgecolor='black', linewidth=1.5)
ax.add_patch(mem_box)
ax.text(0.46, 0.65, 'MEMORY', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.46, 0.50, 'Byte array', ha='center', fontsize=14, color='white')
ax.text(0.46, 0.40, 'Volatile', ha='center', fontsize=14, color='white')
ax.text(0.46, 0.30, '(per call)', ha='center', fontsize=14, color='white')

# Storage (center-right)
storage_box = FancyBboxPatch((0.59, 0.25), 0.18, 0.45,
                              boxstyle="round,pad=0.01", facecolor=MLPURPLE,
                              edgecolor='black', linewidth=1.5)
ax.add_patch(storage_box)
ax.text(0.68, 0.65, 'STORAGE', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.68, 0.50, 'Key-Value', ha='center', fontsize=14, color='white')
ax.text(0.68, 0.40, 'Persistent', ha='center', fontsize=14, color='white')
ax.text(0.68, 0.30, '(on-chain)', ha='center', fontsize=14, color='white')

# Program Counter (right)
pc_box = FancyBboxPatch((0.81, 0.45), 0.08, 0.25,
                         boxstyle="round,pad=0.01", facecolor=MLRED,
                         edgecolor='black', linewidth=1.5)
ax.add_patch(pc_box)
ax.text(0.85, 0.60, 'PC', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.85, 0.50, 'Code', ha='center', fontsize=14, color='white')

# Gas meter
ax.text(0.85, 0.38, 'GAS', ha='center', fontsize=14, fontweight='bold', color=MLRED)
ax.text(0.85, 0.30, 'Meter', ha='center', fontsize=14, color='#555')

# Bytecode at bottom
ax.text(0.5, 0.20, 'Bytecode: PUSH1 0x60 PUSH1 0x40 MSTORE CALLVALUE DUP1 ...',
        ha='center', fontsize=14, family='monospace', color='#555')

# Properties at bottom
props = dict(boxstyle='round,pad=0.3', facecolor='#E8E8E8', edgecolor='#888')
ax.text(0.5, 0.05, 'Deterministic | Isolated | Gas-metered | 256-bit word size',
        ha='center', fontsize=14, bbox=props)

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('EVM: Stack-Based Virtual Machine', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
