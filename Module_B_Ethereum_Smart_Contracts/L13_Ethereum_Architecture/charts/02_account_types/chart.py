"""
Account Types Comparison
EOA vs Contract Account
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Account Types',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture/charts/02_account_types'
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

# Left: EOA
eoa_box = FancyBboxPatch((0.05, 0.20), 0.38, 0.65,
                          boxstyle="round,pad=0.02", facecolor='#E3F2FD',
                          edgecolor=MLBLUE, linewidth=2)
ax.add_patch(eoa_box)

# EOA icon (key)
ax.text(0.24, 0.80, 'EOA', ha='center', fontsize=16, fontweight='bold', color=MLBLUE)
ax.text(0.24, 0.72, 'Externally Owned Account', ha='center', fontsize=10, color=MLBLUE)

# EOA components
components_eoa = [
    ('Address', '0x5aAeb6...', 0.58),
    ('Nonce', 'TX counter', 0.48),
    ('Balance', 'ETH held', 0.38),
    ('Code', 'Empty', 0.28),
]

for label, desc, y in components_eoa:
    ax.text(0.10, y, label + ':', ha='left', fontsize=10, fontweight='bold')
    ax.text(0.27, y, desc, ha='left', fontsize=10, color='#555')

# Key icon
ax.text(0.24, 0.90, 'Controlled by Private Key', ha='center', fontsize=9,
        color='#555', style='italic')

# Right: Contract Account
contract_box = FancyBboxPatch((0.57, 0.20), 0.38, 0.65,
                               boxstyle="round,pad=0.02", facecolor='#FFF3E0',
                               edgecolor=MLORANGE, linewidth=2)
ax.add_patch(contract_box)

ax.text(0.76, 0.80, 'Contract Account', ha='center', fontsize=16, fontweight='bold', color=MLORANGE)
ax.text(0.76, 0.72, 'Smart Contract', ha='center', fontsize=10, color=MLORANGE)

# Contract components
components_contract = [
    ('Address', '0xd4e567...', 0.58),
    ('Nonce', 'Contract count', 0.48),
    ('Balance', 'ETH held', 0.38),
    ('Code', 'Bytecode', 0.28),
]

for label, desc, y in components_contract:
    ax.text(0.62, y, label + ':', ha='left', fontsize=10, fontweight='bold')
    ax.text(0.79, y, desc, ha='left', fontsize=10, color='#555')

ax.text(0.76, 0.90, 'Controlled by Code Logic', ha='center', fontsize=9,
        color='#555', style='italic')

# Comparison at bottom
props = dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#888')
ax.text(0.24, 0.10, 'Can initiate TX', ha='center', fontsize=9,
        bbox=props, color=MLGREEN)
ax.text(0.76, 0.10, 'Cannot initiate TX', ha='center', fontsize=9,
        bbox=props, color=MLRED)

# Arrow between them
ax.annotate('', xy=(0.55, 0.52), xytext=(0.45, 0.52),
            arrowprops=dict(arrowstyle='<->', color='#333', lw=2))
ax.text(0.50, 0.56, 'Both have', ha='center', fontsize=9, color='#555')

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.95)
ax.axis('off')

ax.set_title('Ethereum Account Types', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
