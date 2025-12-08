"""
Hash Avalanche Effect Visualization
Shows how SHA-256 produces vastly different outputs for minimal input changes
[SYNTHETIC DATA]
"""

import hashlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Hash Avalanche Effect - SHA-256 Bit Differences',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/hash_avalanche'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9
})

def hamming_distance(hash1, hash2):
    """Calculate Hamming distance between two hashes (number of differing bits)"""
    bytes1 = bytes.fromhex(hash1)
    bytes2 = bytes.fromhex(hash2)
    distance = 0
    for b1, b2 in zip(bytes1, bytes2):
        xor = b1 ^ b2
        distance += bin(xor).count('1')
    return distance

# Generate synthetic data showing avalanche effect
base_input = "blockchain"
variations = [
    ("Original", base_input),
    ("+1 char", base_input + "x"),
    ("+space", base_input + " "),
    ("Capital", base_input.capitalize()),
    ("+digit", base_input + "1"),
    ("Reverse", base_input[::-1]),
]

# Calculate hashes and distances
base_hash = hashlib.sha256(base_input.encode()).hexdigest()
distances = []
labels = []

for label, input_str in variations:
    current_hash = hashlib.sha256(input_str.encode()).hexdigest()
    distance = hamming_distance(base_hash, current_hash)
    distances.append(distance)
    labels.append(label)

# Create the chart
fig, ax = plt.subplots(figsize=(8, 5))

# Use grayscale-friendly colors
bars = ax.bar(range(len(labels)), distances, color='#4d4d4d', edgecolor='black', linewidth=0.8)

# Highlight the original (0 distance)
bars[0].set_color('#cccccc')
bars[0].set_edgecolor('black')

ax.set_ylabel('Hamming Distance (Bits Changed)')
ax.set_xlabel('Input Variation')
ax.set_title('SHA-256 Avalanche Effect: Minimal Input Change, Maximal Output Difference')
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylim(0, 256)

# Add horizontal line at 128 (expected average for random changes)
ax.axhline(y=128, color='black', linestyle='--', linewidth=0.8, alpha=0.5, label='Expected (~128 bits)')

# Add value labels on bars
for i, (bar, dist) in enumerate(zip(bars, distances)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 3,
            f'{dist}',
            ha='center', va='bottom', fontsize=9)

ax.legend(loc='upper right')
ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC]', ha='right', va='bottom', fontsize=8, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
