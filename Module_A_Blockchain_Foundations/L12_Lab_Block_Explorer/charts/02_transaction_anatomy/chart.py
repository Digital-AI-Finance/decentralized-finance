"""
Transaction Anatomy
Components of a blockchain transaction
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'TX Anatomy',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L12_Lab_Block_Explorer/charts/02_transaction_anatomy'
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

fig, ax = plt.subplots(figsize=(10, 6))

# Transaction box
main_rect = mpatches.FancyBboxPatch((0.1, 0.15), 0.8, 0.7,
                                     boxstyle="round,pad=0.02",
                                     facecolor='#E3F2FD', edgecolor=MLBLUE, linewidth=3)
ax.add_patch(main_rect)
ax.text(0.5, 0.9, 'TRANSACTION', ha='center', va='center', fontsize=14, fontweight='bold', color=MLBLUE)

# Components
components = [
    (0.18, 0.7, 'TX Hash', '0x7f9...3ab', MLPURPLE),
    (0.18, 0.55, 'From', '0xSender...', MLORANGE),
    (0.18, 0.4, 'To', '0xReceiver...', MLORANGE),
    (0.18, 0.25, 'Value', '1.5 ETH', MLGREEN),
    (0.55, 0.7, 'Block', '18,234,567', MLBLUE),
    (0.55, 0.55, 'Gas Used', '21,000', MLRED),
    (0.55, 0.4, 'Gas Price', '25 Gwei', MLRED),
    (0.55, 0.25, 'Status', 'Success', MLGREEN),
]

for x, y, label, value, color in components:
    ax.text(x, y, f'{label}:', ha='left', va='center', fontsize=10, fontweight='bold', color=color)
    ax.text(x + 0.18, y, value, ha='left', va='center', fontsize=10, color='gray')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Transaction Anatomy: Key Fields to Analyze', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
