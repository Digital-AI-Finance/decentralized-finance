"""
Hash Chain Verification
Visual showing chain integrity and tamper detection
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'Chain Verification',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L04_Lab_Hash_Experiments/charts/03_chain_verification'
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

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Valid chain (top)
blocks_x = [0.1, 0.3, 0.5, 0.7, 0.9]
block_labels = ['Genesis', 'Block 1', 'Block 2', 'Block 3', 'Block 4']

for i, (x, label) in enumerate(zip(blocks_x, block_labels)):
    rect = mpatches.FancyBboxPatch((x - 0.08, 0.3), 0.16, 0.4,
                                    boxstyle="round,pad=0.02",
                                    facecolor=MLGREEN, edgecolor='black', linewidth=2)
    ax1.add_patch(rect)
    ax1.text(x, 0.5, label, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax1.text(x, 0.35, 'Valid', ha='center', va='center', fontsize=14, color='white')

    # Draw arrows
    if i > 0:
        ax1.annotate('', xy=(x - 0.08, 0.5), xytext=(blocks_x[i-1] + 0.08, 0.5),
                    arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')
ax1.set_title('Valid Chain: All Hashes Match', fontweight='bold', fontsize=15, color=MLGREEN)

# Tampered chain (bottom)
for i, (x, label) in enumerate(zip(blocks_x, block_labels)):
    if i == 2:  # Tampered block
        color = MLRED
        status = 'TAMPERED'
    elif i > 2:  # Broken chain after tamper
        color = MLORANGE
        status = 'Invalid'
    else:
        color = MLGREEN
        status = 'Valid'

    rect = mpatches.FancyBboxPatch((x - 0.08, 0.3), 0.16, 0.4,
                                    boxstyle="round,pad=0.02",
                                    facecolor=color, edgecolor='black', linewidth=2)
    ax2.add_patch(rect)
    ax2.text(x, 0.5, label, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax2.text(x, 0.35, status, ha='center', va='center', fontsize=14, color='white')

    # Draw arrows (broken for tampered)
    if i > 0:
        arrow_color = MLRED if i >= 3 else MLGREEN
        style = '->' if i < 3 else '-[, widthB=0.5'
        ax2.annotate('', xy=(x - 0.08, 0.5), xytext=(blocks_x[i-1] + 0.08, 0.5),
                    arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2,
                                   linestyle='--' if i >= 3 else '-'))

# Add X mark on broken link
ax2.text(0.58, 0.5, 'X', ha='center', va='center', fontsize=16, fontweight='bold', color=MLRED)

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_title('Tampered Chain: Hash Mismatch Detected', fontweight='bold', fontsize=15, color=MLRED)

plt.suptitle('Hash Chain Integrity Verification', fontweight='bold', fontsize=14, y=0.98)
plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
