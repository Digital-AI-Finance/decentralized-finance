"""
P2PKH Script Execution
Shows stack-based execution of Pay-to-Public-Key-Hash
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'P2PKH Script Execution',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/04_script_execution'
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

# Script components at top
ax.text(0.50, 0.95, 'P2PKH: Pay-to-Public-Key-Hash', ha='center', fontsize=14,
        fontweight='bold', color=MLPURPLE)

# ScriptSig (unlocking)
sig_box = FancyBboxPatch((0.05, 0.78), 0.40, 0.10,
                          boxstyle="round,pad=0.01", facecolor='#FFE0E0',
                          edgecolor=MLRED, linewidth=2)
ax.add_patch(sig_box)
ax.text(0.25, 0.85, 'ScriptSig (Unlocking)', ha='center', fontsize=14,
        fontweight='bold', color=MLRED)
ax.text(0.25, 0.80, '<sig> <pubKey>', ha='center', fontsize=14,
        family='monospace', color='#333')

# ScriptPubKey (locking)
pubkey_box = FancyBboxPatch((0.55, 0.78), 0.40, 0.10,
                             boxstyle="round,pad=0.01", facecolor='#E0FFE0',
                             edgecolor=MLGREEN, linewidth=2)
ax.add_patch(pubkey_box)
ax.text(0.75, 0.85, 'ScriptPubKey (Locking)', ha='center', fontsize=14,
        fontweight='bold', color=MLGREEN)
ax.text(0.75, 0.80, 'OP_DUP OP_HASH160 <hash> OP_EQUALVERIFY OP_CHECKSIG',
        ha='center', fontsize=14, family='monospace', color='#333')

# Execution steps
steps = [
    (0.08, 'Push <sig>', ['sig']),
    (0.22, 'Push <pubKey>', ['pubKey', 'sig']),
    (0.36, 'OP_DUP', ['pubKey', 'pubKey', 'sig']),
    (0.50, 'OP_HASH160', ['hash160', 'pubKey', 'sig']),
    (0.64, 'Push <hash>', ['hash', 'hash160', 'pubKey', 'sig']),
    (0.78, 'OP_EQUALVERIFY', ['pubKey', 'sig']),
    (0.92, 'OP_CHECKSIG', ['TRUE']),
]

# Draw execution flow
base_y = 0.65
for i, (x, op, stack) in enumerate(steps):
    # Operation label
    ax.text(x, base_y + 0.03, f'{i+1}. {op}', ha='center', fontsize=14,
            fontweight='bold', color=MLBLUE, rotation=45)

    # Stack visualization
    stack_height = len(stack) * 0.08
    for j, item in enumerate(stack):
        y = base_y - 0.15 - j * 0.08
        color = MLGREEN if item == 'TRUE' else MLORANGE if j == 0 else MLLAVENDER
        box = FancyBboxPatch((x - 0.05, y - 0.03), 0.10, 0.06,
                              boxstyle="round,pad=0.01", facecolor=color,
                              edgecolor='#333', linewidth=1)
        ax.add_patch(box)
        # Truncate long items
        display = item[:6] + '..' if len(item) > 6 else item
        ax.text(x, y, display, ha='center', va='center', fontsize=14,
                color='white' if item == 'TRUE' else '#333')

# Result annotation
result_box = FancyBboxPatch((0.35, 0.03), 0.30, 0.10,
                             boxstyle="round,pad=0.02", facecolor=MLGREEN,
                             edgecolor='black', linewidth=2)
ax.add_patch(result_box)
ax.text(0.50, 0.08, 'Stack = TRUE -> Valid!', ha='center', fontsize=15,
        fontweight='bold', color='white')

# Legend
ax.text(0.85, 0.15, 'Stack grows\ndownward', ha='center', fontsize=14,
        color='#555', style='italic')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Bitcoin Script Stack Execution', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
