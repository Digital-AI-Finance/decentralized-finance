"""
Proof of Work Concept
Shows the hash puzzle and nonce searching
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Proof of Work Concept',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L07_Proof_of_Work/charts/01_pow_concept'
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

# Block header input
header_box = FancyBboxPatch((0.05, 0.55), 0.25, 0.35,
                             boxstyle="round,pad=0.02", facecolor=MLLAVENDER,
                             edgecolor='black', linewidth=2)
ax.add_patch(header_box)
ax.text(0.175, 0.85, 'Block Header', ha='center', fontsize=15, fontweight='bold', color=MLPURPLE)
ax.text(0.175, 0.75, 'Prev Hash', ha='center', fontsize=14, color='#333')
ax.text(0.175, 0.68, 'Merkle Root', ha='center', fontsize=14, color='#333')
ax.text(0.175, 0.61, 'Timestamp', ha='center', fontsize=14, color='#333')

# Nonce input
nonce_box = FancyBboxPatch((0.05, 0.15), 0.25, 0.25,
                            boxstyle="round,pad=0.02", facecolor=MLORANGE,
                            edgecolor='black', linewidth=2)
ax.add_patch(nonce_box)
ax.text(0.175, 0.35, 'NONCE', ha='center', fontsize=16, fontweight='bold', color='white')
ax.text(0.175, 0.25, 'Try: 0, 1, 2, ...', ha='center', fontsize=14, color='white')
ax.text(0.175, 0.18, '(random search)', ha='center', fontsize=14, color='white', style='italic')

# Arrow to hash function
ax.annotate('', xy=(0.38, 0.50), xytext=(0.30, 0.50),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# SHA-256 hash function
hash_box = FancyBboxPatch((0.38, 0.35), 0.24, 0.30,
                           boxstyle="round,pad=0.02", facecolor=MLBLUE,
                           edgecolor='black', linewidth=2)
ax.add_patch(hash_box)
ax.text(0.50, 0.55, 'SHA-256', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.50, 0.48, '(twice)', ha='center', fontsize=14, color='white')
ax.text(0.50, 0.40, '256-bit output', ha='center', fontsize=14, color='white', style='italic')

# Arrow to target comparison
ax.annotate('', xy=(0.70, 0.50), xytext=(0.62, 0.50),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Target comparison
target_box = FancyBboxPatch((0.70, 0.35), 0.25, 0.30,
                             boxstyle="round,pad=0.02", facecolor='#F0F0F0',
                             edgecolor='black', linewidth=2)
ax.add_patch(target_box)
ax.text(0.825, 0.58, 'Hash < Target?', ha='center', fontsize=15, fontweight='bold', color='#333')
ax.text(0.825, 0.48, '0000...xyz', ha='center', fontsize=14, family='monospace', color='#555')
ax.text(0.825, 0.40, '(leading zeros)', ha='center', fontsize=14, color='#666')

# Success path (green)
success_box = FancyBboxPatch((0.75, 0.05), 0.20, 0.15,
                              boxstyle="round,pad=0.02", facecolor=MLGREEN,
                              edgecolor='black', linewidth=2)
ax.add_patch(success_box)
ax.text(0.85, 0.125, 'Valid Block!', ha='center', fontsize=14, fontweight='bold', color='white')

ax.annotate('', xy=(0.85, 0.20), xytext=(0.825, 0.35),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(0.90, 0.28, 'YES', fontsize=14, fontweight='bold', color=MLGREEN)

# Failure path (back to nonce)
ax.annotate('', xy=(0.175, 0.15), xytext=(0.70, 0.35),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2,
                           connectionstyle="arc3,rad=-0.3"))
ax.text(0.40, 0.08, 'NO -> Try another nonce', fontsize=14, color=MLRED, fontweight='bold')

# Key insight
insight_text = 'Hard to find (billions of tries) | Easy to verify (one hash)'
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F4E8', edgecolor=MLGREEN)
ax.text(0.50, 0.92, insight_text, ha='center', fontsize=14, fontweight='bold',
        bbox=props, color='#333')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Proof-of-Work: The Hash Puzzle', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
