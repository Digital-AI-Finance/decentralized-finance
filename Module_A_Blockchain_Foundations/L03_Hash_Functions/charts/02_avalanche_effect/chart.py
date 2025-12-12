"""
Avalanche Effect Visualization
Shows how 1-bit change causes ~50% of output bits to flip
"""

import matplotlib.pyplot as plt
import numpy as np
import hashlib
from pathlib import Path

CHART_METADATA = {
    'title': 'Avalanche Effect Visualization',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/02_avalanche_effect'
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

# Compute actual SHA-256 hashes
input1 = "blockchain"
input2 = "Blockchain"  # Only 1 bit different (b vs B)

hash1 = hashlib.sha256(input1.encode()).hexdigest()
hash2 = hashlib.sha256(input2.encode()).hexdigest()

# Convert to binary and count differences
def hex_to_binary(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(256)

bin1 = hex_to_binary(hash1)
bin2 = hex_to_binary(hash2)

# Count bit differences
differences = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
percentage = differences / 256 * 100

fig, ax = plt.subplots(figsize=(10, 6))

# Create bit visualization (16x16 grid for 256 bits)
grid_size = 16
bits_grid1 = np.array([int(b) for b in bin1]).reshape(grid_size, grid_size)
bits_grid2 = np.array([int(b) for b in bin2]).reshape(grid_size, grid_size)
diff_grid = (bits_grid1 != bits_grid2).astype(int)

# Plot the difference grid
im = ax.imshow(diff_grid, cmap='RdYlGn_r', aspect='equal', vmin=0, vmax=1)

# Add grid lines
for i in range(grid_size + 1):
    ax.axhline(i - 0.5, color='white', linewidth=0.5)
    ax.axvline(i - 0.5, color='white', linewidth=0.5)

# Labels
ax.set_xticks([])
ax.set_yticks([])

# Title and annotations
ax.set_title(f'Avalanche Effect: SHA-256("{input1}") vs SHA-256("{input2}")',
             fontweight='bold', fontsize=14, pad=15)

# Add statistics box
stats_text = f'Input change: 1 bit (b vs B)\nOutput bits changed: {differences}/256\nPercentage: {percentage:.1f}%'
props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=MLPURPLE, alpha=0.95)
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props, color=MLPURPLE)

# Legend
legend_text = 'Green = Same bit | Red = Different bit'
ax.text(0.5, -0.08, legend_text, transform=ax.transAxes, ha='center',
        fontsize=12, color='#444')

# Show hash prefixes
ax.text(0.5, 1.08, f'Hash 1: {hash1[:16]}...', transform=ax.transAxes, ha='center',
        fontsize=10, color=MLGREEN, family='monospace')
ax.text(0.5, 1.03, f'Hash 2: {hash2[:16]}...', transform=ax.transAxes, ha='center',
        fontsize=10, color=MLRED, family='monospace')

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
