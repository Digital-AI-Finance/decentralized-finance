"""
UTXO Model Visualization
Shows how unspent transaction outputs work as coins
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'UTXO Model',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/01_utxo_model'
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

# Draw wallet UTXOs on left
ax.text(0.12, 0.92, "Alice's Wallet", ha='center', fontsize=14, fontweight='bold', color=MLBLUE)
ax.text(0.12, 0.86, "(UTXOs owned)", ha='center', fontsize=11, color='#555')

# UTXOs as coins
utxos = [
    (0.05, 0.70, '0.5 BTC', MLGREEN),
    (0.12, 0.55, '0.3 BTC', MLGREEN),
    (0.19, 0.70, '0.7 BTC', MLGREEN),
]

for x, y, label, color in utxos:
    coin = Circle((x, y), 0.06, facecolor=color, edgecolor='#333', linewidth=2)
    ax.add_patch(coin)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

ax.text(0.12, 0.40, 'Total: 1.5 BTC', ha='center', fontsize=12, fontweight='bold', color=MLGREEN)

# Transaction in center
tx_box = FancyBboxPatch((0.35, 0.35), 0.30, 0.40,
                         boxstyle="round,pad=0.02", facecolor=MLLAVENDER,
                         edgecolor='black', linewidth=2)
ax.add_patch(tx_box)
ax.text(0.50, 0.70, 'TRANSACTION', ha='center', fontsize=13, fontweight='bold', color=MLPURPLE)

# Inputs
ax.text(0.50, 0.60, 'Inputs:', ha='center', fontsize=11, fontweight='bold', color='#333')
ax.text(0.50, 0.53, '0.5 BTC (consumed)', ha='center', fontsize=10, color=MLRED)
ax.text(0.50, 0.47, '0.3 BTC (consumed)', ha='center', fontsize=10, color=MLRED)

# Outputs
ax.text(0.50, 0.40, 'Outputs:', ha='center', fontsize=11, fontweight='bold', color='#333')

# Arrow from UTXOs to TX
ax.annotate('', xy=(0.35, 0.55), xytext=(0.25, 0.55),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# New UTXOs on right
ax.text(0.82, 0.92, 'New UTXOs', ha='center', fontsize=14, fontweight='bold', color=MLORANGE)

# Output UTXOs
new_utxos = [
    (0.75, 0.60, '0.6 BTC', MLORANGE, "Bob's UTXO"),
    (0.89, 0.60, '0.19 BTC', MLGREEN, "Alice's change"),
]

for x, y, label, color, desc in new_utxos:
    coin = Circle((x, y), 0.055, facecolor=color, edgecolor='#333', linewidth=2)
    ax.add_patch(coin)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    ax.text(x, y - 0.12, desc, ha='center', fontsize=10, color='#555')

# Arrow from TX to outputs
ax.annotate('', xy=(0.70, 0.55), xytext=(0.65, 0.55),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Fee annotation
ax.text(0.82, 0.40, 'Fee: 0.01 BTC', ha='center', fontsize=11,
        fontweight='bold', color=MLRED)
ax.text(0.82, 0.33, '(0.8 - 0.6 - 0.19)', ha='center', fontsize=10, color='#666')

# Key insight box
insight_text = 'UTXOs are consumed entirely, change returned as new UTXO'
props = dict(boxstyle='round,pad=0.3', facecolor='#E8F4E8', edgecolor=MLGREEN, alpha=0.95)
ax.text(0.50, 0.12, insight_text, ha='center', va='center', fontsize=11,
        fontweight='bold', bbox=props, color='#333')

# Remaining UTXO annotation
ax.text(0.12, 0.25, '0.7 BTC remains\n(unspent)', ha='center', fontsize=10,
        color='#555', style='italic')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('UTXO Model: Unspent Transaction Outputs', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
