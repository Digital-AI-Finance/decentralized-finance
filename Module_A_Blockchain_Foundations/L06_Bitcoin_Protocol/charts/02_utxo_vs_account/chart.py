"""
UTXO vs Account Model Comparison
Side-by-side comparison of Bitcoin vs Ethereum models
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'UTXO vs Account Model',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol/charts/02_utxo_vs_account'
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

# Left panel: UTXO Model
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis('off')

ax1.set_title('UTXO Model (Bitcoin)', fontsize=14, fontweight='bold', color=MLORANGE, pad=10)

# Draw coins (UTXOs)
utxo_positions = [(0.2, 0.75), (0.5, 0.75), (0.8, 0.75)]
for i, (x, y) in enumerate(utxo_positions):
    coin = Circle((x, y), 0.08, facecolor=MLORANGE, edgecolor='#333', linewidth=2)
    ax1.add_patch(coin)
    ax1.text(x, y, f'{0.3*(i+1):.1f}', ha='center', va='center',
             fontsize=14, fontweight='bold', color='white')

ax1.text(0.5, 0.60, 'Each "coin" is a separate UTXO', ha='center', fontsize=14, color='#555')

# Properties
props_utxo = [
    'Discrete "coins"',
    'Parallel processing',
    'Better privacy',
    'Complex state tracking',
    'No nonce needed',
]

for i, prop in enumerate(props_utxo):
    y = 0.45 - i * 0.08
    ax1.text(0.08, y, '+' if i < 3 else '-', ha='center', fontsize=15,
             fontweight='bold', color=MLGREEN if i < 3 else MLRED)
    ax1.text(0.15, y, prop, ha='left', fontsize=14, color='#333')

# Box around
box1 = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.02",
                       facecolor='white', edgecolor=MLORANGE, linewidth=3, fill=False)
ax1.add_patch(box1)

# Right panel: Account Model
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')

ax2.set_title('Account Model (Ethereum)', fontsize=14, fontweight='bold', color=MLBLUE, pad=10)

# Draw account box
account_box = FancyBboxPatch((0.25, 0.65), 0.50, 0.20,
                              boxstyle="round,pad=0.02", facecolor=MLBLUE,
                              edgecolor='#333', linewidth=2)
ax2.add_patch(account_box)
ax2.text(0.5, 0.78, 'Account', ha='center', fontsize=15, fontweight='bold', color='white')
ax2.text(0.5, 0.70, 'Balance: 1.8 ETH', ha='center', fontsize=14, color='white')

ax2.text(0.5, 0.58, 'Single balance per address', ha='center', fontsize=14, color='#555')

# Properties
props_account = [
    'Simple balance tracking',
    'Easy smart contracts',
    'Lower storage',
    'Sequential nonces',
    'Less privacy',
]

for i, prop in enumerate(props_account):
    y = 0.45 - i * 0.08
    ax2.text(0.08, y, '+' if i < 3 else '-', ha='center', fontsize=15,
             fontweight='bold', color=MLGREEN if i < 3 else MLRED)
    ax2.text(0.15, y, prop, ha='left', fontsize=14, color='#333')

# Box around
box2 = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.02",
                       facecolor='white', edgecolor=MLBLUE, linewidth=3, fill=False)
ax2.add_patch(box2)

plt.suptitle('State Models: UTXO vs Account-Based', fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
