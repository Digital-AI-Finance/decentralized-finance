"""
Solidity Data Types Overview
Shows value types vs reference types
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Solidity Data Types',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals/charts/02_data_types_overview'
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

# Value Types (left column)
value_types = [
    ('uint/int', 'uint256, int128...', MLBLUE),
    ('address', '20-byte Ethereum addr', MLBLUE),
    ('bool', 'true/false', MLBLUE),
    ('bytes1-32', 'Fixed-size bytes', MLBLUE),
    ('enum', 'User-defined states', MLBLUE),
]

# Reference Types (right column)
ref_types = [
    ('arrays', 'uint[], string[]', MLORANGE),
    ('mappings', 'mapping(K => V)', MLORANGE),
    ('structs', 'Custom data types', MLORANGE),
    ('string', 'Dynamic UTF-8', MLORANGE),
    ('bytes', 'Dynamic byte array', MLORANGE),
]

# Draw headers
ax.text(0.25, 0.92, 'Value Types', fontsize=14, fontweight='bold',
        ha='center', va='center', color=MLBLUE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.text(0.75, 0.92, 'Reference Types', fontsize=14, fontweight='bold',
        ha='center', va='center', color=MLORANGE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

# Draw value types
y_start = 0.78
y_spacing = 0.14
for i, (name, desc, color) in enumerate(value_types):
    y = y_start - i * y_spacing
    box = FancyBboxPatch((0.05, y - 0.05), 0.40, 0.10,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1, alpha=0.15)
    ax.add_patch(box)
    ax.text(0.08, y, name, fontsize=11, fontweight='bold', va='center', color=color)
    ax.text(0.42, y, desc, fontsize=9, va='center', ha='right', color='#555')

# Draw reference types
for i, (name, desc, color) in enumerate(ref_types):
    y = y_start - i * y_spacing
    box = FancyBboxPatch((0.55, y - 0.05), 0.40, 0.10,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1, alpha=0.15)
    ax.add_patch(box)
    ax.text(0.58, y, name, fontsize=11, fontweight='bold', va='center', color=color)
    ax.text(0.92, y, desc, fontsize=9, va='center', ha='right', color='#555')

# Add key differences at bottom
props_val = dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor=MLBLUE)
props_ref = dict(boxstyle='round,pad=0.2', facecolor='#FFF3E0', edgecolor=MLORANGE)

ax.text(0.25, 0.06, 'Copied when assigned\nStored directly in memory/storage',
        ha='center', va='center', fontsize=9, bbox=props_val, color=MLBLUE)
ax.text(0.75, 0.06, 'Passed by reference\nRequire data location (storage/memory/calldata)',
        ha='center', va='center', fontsize=9, bbox=props_ref, color=MLORANGE)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Solidity Data Types', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
