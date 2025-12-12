"""
Hierarchical Deterministic Wallet Structure
Shows the BIP-32 key derivation tree
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'HD Wallet Tree Structure',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/05_hd_wallet_tree'
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

# Master seed at top
seed_box = FancyBboxPatch((0.35, 0.85), 0.30, 0.10,
                           boxstyle="round,pad=0.02", facecolor=MLRED,
                           edgecolor='black', linewidth=2)
ax.add_patch(seed_box)
ax.text(0.5, 0.90, 'Seed Phrase (12-24 words)', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')

# Master key
master_y = 0.70
ax.add_patch(Circle((0.5, master_y), 0.045, facecolor=MLPURPLE, edgecolor='black', linewidth=2))
ax.text(0.5, master_y, 'm', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.text(0.58, master_y, "Master Key", ha='left', va='center', fontsize=10, color='#444')

# Arrow from seed to master
ax.annotate('', xy=(0.5, master_y + 0.045), xytext=(0.5, 0.85),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))

# Purpose level (44')
purpose_y = 0.55
ax.add_patch(Circle((0.5, purpose_y), 0.04, facecolor=MLORANGE, edgecolor='black', linewidth=1.5))
ax.text(0.5, purpose_y, "44'", ha='center', va='center', fontsize=10, fontweight='bold', color='white')
ax.text(0.58, purpose_y, "Purpose (BIP-44)", ha='left', va='center', fontsize=9, color='#444')

ax.annotate('', xy=(0.5, purpose_y + 0.04), xytext=(0.5, master_y - 0.045),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Coin type level
coin_y = 0.40
coin_positions = [0.30, 0.50, 0.70]
coin_labels = ["0'", "60'", "501'"]
coin_names = ['Bitcoin', 'Ethereum', 'Solana']

for x, label, name in zip(coin_positions, coin_labels, coin_names):
    ax.add_patch(Circle((x, coin_y), 0.035, facecolor=MLBLUE, edgecolor='black', linewidth=1.5))
    ax.text(x, coin_y, label, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    ax.text(x, coin_y - 0.08, name, ha='center', va='center', fontsize=9, color='#555')

    # Arrow from purpose
    ax.annotate('', xy=(x, coin_y + 0.035), xytext=(0.5, purpose_y - 0.04),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1))

# Account level (only for Bitcoin branch)
account_y = 0.22
account_positions = [0.20, 0.30, 0.40]
account_labels = ["0'", "1'", "2'"]

for x, label in zip(account_positions, account_labels):
    ax.add_patch(Circle((x, account_y), 0.03, facecolor=MLGREEN, edgecolor='black', linewidth=1.5))
    ax.text(x, account_y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    ax.annotate('', xy=(x, account_y + 0.03), xytext=(0.30, coin_y - 0.035),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1))

# Address level (only for first account)
addr_y = 0.08
addr_positions = [0.12, 0.20, 0.28]
addr_labels = ['0', '1', '2']

for x, label in zip(addr_positions, addr_labels):
    ax.add_patch(Circle((x, addr_y), 0.025, facecolor=MLLAVENDER, edgecolor='black', linewidth=1))
    ax.text(x, addr_y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='#333')

    ax.annotate('', xy=(x, addr_y + 0.025), xytext=(0.20, account_y - 0.03),
                arrowprops=dict(arrowstyle='->', color='#aaa', lw=0.8))

# Labels on right side
labels = [
    (0.85, 0.70, 'Master', 'm'),
    (0.85, 0.55, 'Purpose', "m/44'"),
    (0.85, 0.40, 'Coin Type', "m/44'/0'"),
    (0.85, 0.22, 'Account', "m/44'/0'/0'"),
    (0.85, 0.08, 'Address', "m/44'/0'/0'/0/0"),
]

for x, y, label, path in labels:
    ax.text(x, y, f'{label}:\n{path}', ha='left', va='center', fontsize=9,
            color='#555', family='monospace')

# Level lines
for y in [0.63, 0.48, 0.31, 0.15]:
    ax.axhline(y=y, xmin=0.05, xmax=0.95, color='#ddd', linestyle='-', linewidth=0.5)

# Key insight
insight_text = 'One seed backup = All addresses recoverable'
props = dict(boxstyle='round,pad=0.3', facecolor='#E0FFE0', edgecolor=MLGREEN, alpha=0.95)
ax.text(0.70, 0.90, insight_text, ha='center', va='center', fontsize=10,
        fontweight='bold', bbox=props, color=MLGREEN)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Hierarchical Deterministic Wallet (BIP-32/BIP-44)', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
