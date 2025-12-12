"""
UTXO vs Account Model
Bitcoin vs Ethereum comparison
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'UTXO vs Account',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/06_utxo_vs_account'
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

# Left: Bitcoin UTXO
ax.text(0.25, 0.92, 'Bitcoin: UTXO Model', ha='center', fontsize=14,
        fontweight='bold', color=MLORANGE)

# UTXO boxes
utxo1 = FancyBboxPatch((0.08, 0.60), 0.12, 0.18,
                        boxstyle="round,pad=0.01", facecolor=MLORANGE,
                        edgecolor='black', linewidth=1.5)
ax.add_patch(utxo1)
ax.text(0.14, 0.72, 'UTXO', ha='center', fontsize=9, fontweight='bold', color='white')
ax.text(0.14, 0.65, '5 BTC', ha='center', fontsize=10, color='white')

# Arrow showing spend
ax.annotate('', xy=(0.30, 0.69), xytext=(0.22, 0.69),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.text(0.26, 0.73, 'Spend', fontsize=8, ha='center')

# New UTXOs
utxo2 = FancyBboxPatch((0.30, 0.70), 0.10, 0.13,
                        boxstyle="round,pad=0.01", facecolor=MLGREEN,
                        edgecolor='black', linewidth=1.5)
ax.add_patch(utxo2)
ax.text(0.35, 0.78, '2 BTC', ha='center', fontsize=9, color='white')
ax.text(0.35, 0.72, 'Bob', ha='center', fontsize=8, color='white')

utxo3 = FancyBboxPatch((0.30, 0.55), 0.10, 0.13,
                        boxstyle="round,pad=0.01", facecolor=MLBLUE,
                        edgecolor='black', linewidth=1.5)
ax.add_patch(utxo3)
ax.text(0.35, 0.63, '3 BTC', ha='center', fontsize=9, color='white')
ax.text(0.35, 0.57, 'Change', ha='center', fontsize=8, color='white')

ax.text(0.14, 0.50, 'Destroyed', ha='center', fontsize=9, color=MLRED)

# Right: Ethereum Account
ax.text(0.75, 0.92, 'Ethereum: Account Model', ha='center', fontsize=14,
        fontweight='bold', color=MLBLUE)

# Account boxes
acc_alice = FancyBboxPatch((0.55, 0.60), 0.15, 0.18,
                            boxstyle="round,pad=0.01", facecolor=MLBLUE,
                            edgecolor='black', linewidth=1.5)
ax.add_patch(acc_alice)
ax.text(0.625, 0.72, 'Alice', ha='center', fontsize=10, fontweight='bold', color='white')
ax.text(0.625, 0.65, '5 ETH', ha='center', fontsize=10, color='white')

# Arrow showing transfer
ax.annotate('', xy=(0.80, 0.69), xytext=(0.72, 0.69),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.text(0.76, 0.73, '-2 ETH', fontsize=8, ha='center')

# Updated balances
acc_alice2 = FancyBboxPatch((0.80, 0.70), 0.12, 0.13,
                             boxstyle="round,pad=0.01", facecolor=MLBLUE,
                             edgecolor='black', linewidth=1.5)
ax.add_patch(acc_alice2)
ax.text(0.86, 0.78, 'Alice', ha='center', fontsize=9, color='white')
ax.text(0.86, 0.72, '3 ETH', ha='center', fontsize=9, color='white')

acc_bob = FancyBboxPatch((0.80, 0.55), 0.12, 0.13,
                          boxstyle="round,pad=0.01", facecolor=MLGREEN,
                          edgecolor='black', linewidth=1.5)
ax.add_patch(acc_bob)
ax.text(0.86, 0.63, 'Bob', ha='center', fontsize=9, color='white')
ax.text(0.86, 0.57, '+2 ETH', ha='center', fontsize=9, color='white')

ax.text(0.625, 0.50, 'Persists', ha='center', fontsize=9, color=MLGREEN)

# Comparison table at bottom
comparisons = [
    ('Stateless', 'Stateful'),
    ('Parallel validation', 'Sequential nonces'),
    ('Simple, secure', 'Complex, flexible'),
    ('Limited scripting', 'Full smart contracts'),
]

ax.axhline(y=0.42, color='#888', linestyle='-', linewidth=1)

for i, (utxo, acc) in enumerate(comparisons):
    y = 0.35 - i * 0.08
    ax.text(0.25, y, utxo, ha='center', fontsize=9, color=MLORANGE)
    ax.text(0.75, y, acc, ha='center', fontsize=9, color=MLBLUE)

# Dividing line
ax.axvline(x=0.50, color='#888', linestyle='--', linewidth=1.5, alpha=0.5)

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.98)
ax.axis('off')

ax.set_title('Transaction Models: UTXO vs Account', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
