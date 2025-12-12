"""
ERC-20 Interface Overview
Shows the 6 required functions and 2 events
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'ERC-20 Interface',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard/charts/01_erc20_interface'
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

# Read functions (view)
read_funcs = [
    ('totalSupply()', 'Total token supply'),
    ('balanceOf(address)', 'Get balance'),
    ('allowance(owner, spender)', 'Get allowance'),
]

# Write functions
write_funcs = [
    ('transfer(to, amount)', 'Direct transfer'),
    ('approve(spender, amount)', 'Set allowance'),
    ('transferFrom(from, to, amount)', 'Delegated transfer'),
]

# Events
events = [
    ('Transfer(from, to, value)', 'Emitted on transfer'),
    ('Approval(owner, spender, value)', 'Emitted on approve'),
]

# Draw sections
# Read functions (left)
ax.text(0.17, 0.92, 'View Functions', fontsize=15, fontweight='bold',
        ha='center', va='center', color=MLBLUE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

y_start = 0.78
for i, (func, desc) in enumerate(read_funcs):
    y = y_start - i * 0.18
    box = FancyBboxPatch((0.02, y - 0.06), 0.30, 0.12,
                          boxstyle="round,pad=0.02", facecolor=MLBLUE,
                          edgecolor='black', linewidth=1, alpha=0.2)
    ax.add_patch(box)
    ax.text(0.04, y + 0.02, func, fontsize=14, fontweight='bold', va='center', family='monospace')
    ax.text(0.04, y - 0.03, desc, fontsize=14, va='center', color='#555')

# Write functions (middle)
ax.text(0.52, 0.92, 'State-Changing Functions', fontsize=15, fontweight='bold',
        ha='center', va='center', color=MLGREEN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

for i, (func, desc) in enumerate(write_funcs):
    y = y_start - i * 0.18
    box = FancyBboxPatch((0.37, y - 0.06), 0.30, 0.12,
                          boxstyle="round,pad=0.02", facecolor=MLGREEN,
                          edgecolor='black', linewidth=1, alpha=0.2)
    ax.add_patch(box)
    ax.text(0.39, y + 0.02, func, fontsize=14, fontweight='bold', va='center', family='monospace')
    ax.text(0.39, y - 0.03, desc, fontsize=14, va='center', color='#555')

# Events (right)
ax.text(0.85, 0.92, 'Events', fontsize=15, fontweight='bold',
        ha='center', va='center', color=MLORANGE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

for i, (func, desc) in enumerate(events):
    y = y_start - i * 0.18
    box = FancyBboxPatch((0.70, y - 0.06), 0.28, 0.12,
                          boxstyle="round,pad=0.02", facecolor=MLORANGE,
                          edgecolor='black', linewidth=1, alpha=0.2)
    ax.add_patch(box)
    ax.text(0.72, y + 0.02, func, fontsize=14, fontweight='bold', va='center', family='monospace')
    ax.text(0.72, y - 0.03, desc, fontsize=14, va='center', color='#555')

# Key insight at bottom
props = dict(boxstyle='round,pad=0.3', facecolor='#E8E8E8', edgecolor='#888')
ax.text(0.50, 0.08, 'Optional: name(), symbol(), decimals() for metadata',
        ha='center', fontsize=14, bbox=props)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('ERC-20 Interface Specification', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
