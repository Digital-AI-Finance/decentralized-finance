"""
SegWit vs Legacy Transaction Comparison
Shows structure differences and benefits
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'SegWit vs Legacy Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/06_segwit_comparison'
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# Left: Legacy transaction structure
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')
ax1.set_title('Legacy Transaction', fontsize=14, fontweight='bold', color=MLRED, pad=10)

# Legacy structure
legacy_parts = [
    (0.50, 0.85, 'Version', 0.08, '#CCCCCC'),
    (0.50, 0.72, 'Inputs', 0.15, '#FFE0E0'),
    (0.50, 0.52, 'ScriptSig\n(Signature)', 0.15, MLRED),
    (0.50, 0.32, 'Outputs', 0.12, '#E0FFE0'),
    (0.50, 0.15, 'Locktime', 0.08, '#CCCCCC'),
]

for x, y, label, height, color in legacy_parts:
    box = FancyBboxPatch((0.15, y - height/2), 0.70, height,
                          boxstyle="round,pad=0.01", facecolor=color,
                          edgecolor='black', linewidth=1.5)
    ax1.add_patch(box)
    ax1.text(x, y, label, ha='center', va='center', fontsize=10,
             fontweight='bold', color='#333' if color != MLRED else 'white')

# Bracket showing TX ID includes signature
ax1.annotate('', xy=(0.88, 0.90), xytext=(0.88, 0.10),
             arrowprops=dict(arrowstyle='-[', color=MLRED, lw=2))
ax1.text(0.92, 0.50, 'TX ID\nincludes\nSignature', ha='left', fontsize=9,
         color=MLRED, fontweight='bold')

# Problem annotation
ax1.text(0.50, 0.02, 'Malleability: Sig changes -> TX ID changes',
         ha='center', fontsize=9, color=MLRED, style='italic')

# Right: SegWit transaction structure
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_title('SegWit Transaction', fontsize=14, fontweight='bold', color=MLGREEN, pad=10)

# SegWit structure - main transaction
segwit_main = [
    (0.35, 0.85, 'Version', 0.08, '#CCCCCC'),
    (0.35, 0.72, 'Marker + Flag', 0.06, MLBLUE),
    (0.35, 0.60, 'Inputs', 0.12, '#FFE0E0'),
    (0.35, 0.45, 'Outputs', 0.12, '#E0FFE0'),
    (0.35, 0.30, 'Locktime', 0.08, '#CCCCCC'),
]

for x, y, label, height, color in segwit_main:
    box = FancyBboxPatch((0.05, y - height/2), 0.60, height,
                          boxstyle="round,pad=0.01", facecolor=color,
                          edgecolor='black', linewidth=1.5)
    ax2.add_patch(box)
    ax2.text(x, y, label, ha='center', va='center', fontsize=10,
             fontweight='bold', color='white' if color == MLBLUE else '#333')

# Witness data (separate)
witness_box = FancyBboxPatch((0.70, 0.40), 0.25, 0.35,
                              boxstyle="round,pad=0.01", facecolor=MLGREEN,
                              edgecolor='black', linewidth=2)
ax2.add_patch(witness_box)
ax2.text(0.825, 0.65, 'Witness', ha='center', fontsize=11, fontweight='bold', color='white')
ax2.text(0.825, 0.55, '(Signatures)', ha='center', fontsize=10, color='white')
ax2.text(0.825, 0.45, 'Segregated!', ha='center', fontsize=10,
         color='white', style='italic')

# Bracket showing TX ID excludes witness
ax2.annotate('', xy=(0.02, 0.90), xytext=(0.02, 0.25),
             arrowprops=dict(arrowstyle='-[', color=MLPURPLE, lw=2))
ax2.text(0.00, 0.57, 'TX ID', ha='right', fontsize=9, color=MLPURPLE, fontweight='bold')

# Benefits
ax2.text(0.50, 0.12, 'No malleability', ha='center', fontsize=10,
         color=MLGREEN, fontweight='bold')
ax2.text(0.50, 0.05, '~40% smaller effective size', ha='center', fontsize=10,
         color=MLGREEN)

plt.suptitle('Segregated Witness: Separating Signatures', fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
