"""
Symmetric vs Asymmetric Cryptography Comparison
Visual comparison of the two cryptographic approaches
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Symmetric vs Asymmetric Cryptography',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/01_symmetric_vs_asymmetric'
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

# --- Symmetric Cryptography (left) ---
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')
ax1.set_title('Symmetric Cryptography', fontsize=14, fontweight='bold', color=MLORANGE, pad=10)

# Alice
ax1.add_patch(Circle((0.15, 0.7), 0.08, facecolor=MLBLUE, edgecolor='black', linewidth=2))
ax1.text(0.15, 0.7, 'A', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax1.text(0.15, 0.55, 'Alice', ha='center', fontsize=14, color='#333')

# Bob
ax1.add_patch(Circle((0.85, 0.7), 0.08, facecolor=MLGREEN, edgecolor='black', linewidth=2))
ax1.text(0.85, 0.7, 'B', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax1.text(0.85, 0.55, 'Bob', ha='center', fontsize=14, color='#333')

# Same key for both
key_box = FancyBboxPatch((0.35, 0.65), 0.3, 0.12, boxstyle="round,pad=0.02",
                          facecolor=MLORANGE, edgecolor='black', linewidth=2)
ax1.add_patch(key_box)
ax1.text(0.5, 0.71, 'Same Key K', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Arrows to key
ax1.annotate('', xy=(0.35, 0.71), xytext=(0.23, 0.7),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2))
ax1.annotate('', xy=(0.65, 0.71), xytext=(0.77, 0.7),
            arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2))

# Message flow
ax1.annotate('', xy=(0.77, 0.35), xytext=(0.23, 0.35),
            arrowprops=dict(arrowstyle='->', color='#666', lw=2))
ax1.text(0.5, 0.40, 'Encrypted Message', ha='center', fontsize=14, color='#666')

# Problem box
prob_box = FancyBboxPatch((0.15, 0.08), 0.7, 0.15, boxstyle="round,pad=0.02",
                           facecolor='#FFE0E0', edgecolor=MLRED, linewidth=2)
ax1.add_patch(prob_box)
ax1.text(0.5, 0.155, 'Problem: How to share K securely?', ha='center', va='center',
        fontsize=14, color=MLRED, fontweight='bold')

# --- Asymmetric Cryptography (right) ---
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_title('Asymmetric Cryptography', fontsize=14, fontweight='bold', color=MLGREEN, pad=10)

# Alice
ax2.add_patch(Circle((0.15, 0.7), 0.08, facecolor=MLBLUE, edgecolor='black', linewidth=2))
ax2.text(0.15, 0.7, 'A', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax2.text(0.15, 0.55, 'Alice', ha='center', fontsize=14, color='#333')

# Bob
ax2.add_patch(Circle((0.85, 0.7), 0.08, facecolor=MLGREEN, edgecolor='black', linewidth=2))
ax2.text(0.85, 0.7, 'B', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax2.text(0.85, 0.55, 'Bob', ha='center', fontsize=14, color='#333')

# Bob's public key (shared)
pub_box = FancyBboxPatch((0.55, 0.78), 0.22, 0.12, boxstyle="round,pad=0.02",
                          facecolor=MLGREEN, edgecolor='black', linewidth=2)
ax2.add_patch(pub_box)
ax2.text(0.66, 0.84, 'Public Key', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Bob's private key (secret)
priv_box = FancyBboxPatch((0.72, 0.50), 0.22, 0.12, boxstyle="round,pad=0.02",
                           facecolor=MLRED, edgecolor='black', linewidth=2)
ax2.add_patch(priv_box)
ax2.text(0.83, 0.56, 'Private Key', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Arrow from public key to Alice
ax2.annotate('', xy=(0.23, 0.75), xytext=(0.55, 0.84),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax2.text(0.35, 0.85, 'Shared openly', ha='center', fontsize=14, color=MLGREEN)

# Message flow
ax2.annotate('', xy=(0.77, 0.35), xytext=(0.23, 0.35),
            arrowprops=dict(arrowstyle='->', color='#666', lw=2))
ax2.text(0.5, 0.40, 'Encrypted with Public Key', ha='center', fontsize=14, color='#666')

# Solution box
sol_box = FancyBboxPatch((0.15, 0.08), 0.7, 0.15, boxstyle="round,pad=0.02",
                          facecolor='#E0FFE0', edgecolor=MLGREEN, linewidth=2)
ax2.add_patch(sol_box)
ax2.text(0.5, 0.155, 'Solution: No secret key exchange needed!', ha='center', va='center',
        fontsize=14, color=MLGREEN, fontweight='bold')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
