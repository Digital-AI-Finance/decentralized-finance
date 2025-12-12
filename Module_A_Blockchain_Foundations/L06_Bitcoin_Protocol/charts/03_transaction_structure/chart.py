"""
Bitcoin Transaction Structure
Shows anatomy of a Bitcoin transaction
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Bitcoin Transaction Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/03_transaction_structure'
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

# Main transaction box
main_box = FancyBboxPatch((0.15, 0.15), 0.70, 0.75,
                           boxstyle="round,pad=0.02", facecolor='#F8F8F8',
                           edgecolor='black', linewidth=2)
ax.add_patch(main_box)

ax.text(0.50, 0.86, 'Bitcoin Transaction', ha='center', fontsize=14,
        fontweight='bold', color=MLPURPLE)

# Header section
header_box = FancyBboxPatch((0.18, 0.73), 0.64, 0.10,
                             boxstyle="round,pad=0.01", facecolor=MLLAVENDER,
                             edgecolor='black', linewidth=1.5)
ax.add_patch(header_box)
ax.text(0.50, 0.78, 'Header: Version (4 bytes) | Input Count | Output Count | Locktime (4 bytes)',
        ha='center', fontsize=10, color='#333')

# Inputs section
input_box = FancyBboxPatch((0.18, 0.42), 0.30, 0.28,
                            boxstyle="round,pad=0.01", facecolor='#FFE0E0',
                            edgecolor=MLRED, linewidth=2)
ax.add_patch(input_box)
ax.text(0.33, 0.66, 'INPUTS', ha='center', fontsize=12, fontweight='bold', color=MLRED)

input_fields = [
    ('Previous TX Hash', '32 bytes'),
    ('Output Index', '4 bytes'),
    ('ScriptSig', 'variable'),
    ('Sequence', '4 bytes'),
]

for i, (field, size) in enumerate(input_fields):
    y = 0.58 - i * 0.055
    ax.text(0.20, y, f'{field}:', ha='left', fontsize=9, color='#333')
    ax.text(0.46, y, size, ha='right', fontsize=9, color='#666', style='italic')

# Outputs section
output_box = FancyBboxPatch((0.52, 0.42), 0.30, 0.28,
                             boxstyle="round,pad=0.01", facecolor='#E0FFE0',
                             edgecolor=MLGREEN, linewidth=2)
ax.add_patch(output_box)
ax.text(0.67, 0.66, 'OUTPUTS', ha='center', fontsize=12, fontweight='bold', color=MLGREEN)

output_fields = [
    ('Value', '8 bytes (satoshis)'),
    ('ScriptPubKey', 'variable'),
    ('Length', '1-9 bytes'),
]

for i, (field, size) in enumerate(output_fields):
    y = 0.58 - i * 0.055
    ax.text(0.54, y, f'{field}:', ha='left', fontsize=9, color='#333')
    ax.text(0.80, y, size, ha='right', fontsize=9, color='#666', style='italic')

# Arrow showing flow
ax.annotate('', xy=(0.52, 0.55), xytext=(0.48, 0.55),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Fee calculation
fee_box = FancyBboxPatch((0.25, 0.18), 0.50, 0.12,
                          boxstyle="round,pad=0.01", facecolor='#FFF8E0',
                          edgecolor=MLORANGE, linewidth=1.5)
ax.add_patch(fee_box)
ax.text(0.50, 0.26, 'Fee = Sum(Inputs) - Sum(Outputs)', ha='center', fontsize=11,
        fontweight='bold', color=MLORANGE)
ax.text(0.50, 0.20, 'Implicit fee (not a field)', ha='center', fontsize=10, color='#666')

# Annotations
ax.text(0.92, 0.60, 'References\nprevious\nUTXOs', ha='center', fontsize=9,
        color=MLRED, style='italic')
ax.annotate('', xy=(0.85, 0.55), xytext=(0.88, 0.55),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5))

ax.text(0.08, 0.55, 'Creates\nnew\nUTXOs', ha='center', fontsize=9,
        color=MLGREEN, style='italic')
ax.annotate('', xy=(0.15, 0.55), xytext=(0.12, 0.55),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=1.5))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Bitcoin Transaction Anatomy', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
