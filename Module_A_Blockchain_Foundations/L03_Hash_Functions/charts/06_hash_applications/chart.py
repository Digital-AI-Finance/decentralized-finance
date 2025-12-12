"""
Hash Function Applications Comparison
Shows different use cases and their hash function requirements
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Hash Function Applications',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/06_hash_applications'
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

# Applications and their property requirements (0-5 scale)
applications = ['Password\nStorage', 'File\nIntegrity', 'Digital\nSignatures', 'Blockchain\nPoW', 'Git\nVersion Control', 'SSL/TLS\nCertificates']

# Properties: Preimage, Collision, Speed (inverted - lower is better for security apps)
# Score interpretation: Higher = more important for this application
preimage = [5, 4, 5, 5, 3, 5]      # Preimage resistance importance
collision = [3, 5, 5, 3, 4, 5]     # Collision resistance importance
speed = [1, 4, 4, 5, 4, 4]         # Speed importance (1=slow preferred, 5=fast needed)

x = np.arange(len(applications))
width = 0.25

# Create bars
bars1 = ax.bar(x - width, preimage, width, label='Preimage Resistance',
               color=MLPURPLE, edgecolor='black', linewidth=1)
bars2 = ax.bar(x, collision, width, label='Collision Resistance',
               color=MLORANGE, edgecolor='black', linewidth=1)
bars3 = ax.bar(x + width, speed, width, label='Speed Requirement',
               color=MLGREEN, edgecolor='black', linewidth=1)

# Labels and formatting
ax.set_ylabel('Importance (1=Low, 5=Critical)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(applications, fontsize=11)
ax.set_ylim(0, 6)

# Legend
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Grid
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add hash function used labels below
hash_funcs = ['bcrypt\nArgon2', 'SHA-256\nSHA-3', 'SHA-256\nEd25519', 'SHA-256\n(double)', 'SHA-1*\nSHA-256', 'SHA-256\nSHA-384']
for i, hf in enumerate(hash_funcs):
    ax.text(i, -0.8, hf, ha='center', va='top', fontsize=9, color='#666', style='italic')

ax.text(-0.8, -0.8, 'Hash Used:', ha='right', va='top', fontsize=9, color='#666', fontweight='bold')

# Note
ax.text(0.5, -0.18, '*SHA-1 deprecated; Git transitioning to SHA-256', transform=ax.transAxes,
        ha='center', fontsize=10, color=MLRED, style='italic')

plt.title('Hash Function Applications: Property Requirements', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()
plt.subplots_adjust(bottom=0.22)

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
