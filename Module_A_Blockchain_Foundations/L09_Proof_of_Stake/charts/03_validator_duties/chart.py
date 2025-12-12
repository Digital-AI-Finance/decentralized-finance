"""
Validator Duties
Shows attestation, proposal, and sync committee responsibilities
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Validator Duties',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L09_Proof_of_Stake/charts/03_validator_duties'
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

# Central validator
validator_circle = Circle((0.50, 0.50), 0.12, facecolor=MLPURPLE,
                           edgecolor='black', linewidth=2)
ax.add_patch(validator_circle)
ax.text(0.50, 0.50, 'VALIDATOR', ha='center', va='center',
        fontsize=12, fontweight='bold', color='white')

# Three duties around the validator
duties = [
    (0.15, 0.75, 'Attestation', MLBLUE, 'Every Epoch\n(~6.4 min)', '~99% of rewards'),
    (0.85, 0.75, 'Block Proposal', MLGREEN, 'Occasional\n(~2 months)', 'TX fees + rewards'),
    (0.50, 0.12, 'Sync Committee', MLORANGE, 'Rare\n(~27 hours/2 yr)', 'Light client help'),
]

for x, y, title, color, freq, reward in duties:
    box = FancyBboxPatch((x - 0.12, y - 0.10), 0.24, 0.20,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.05, title, ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(x, y - 0.03, freq, ha='center', va='center',
            fontsize=9, color='white')

    # Arrow from validator to duty
    ax.annotate('', xy=(x, y - 0.10 + 0.02), xytext=(0.50, 0.50),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.5,
                               connectionstyle="arc3,rad=-0.2"))

# Timing info at bottom
timing_text = 'Slot = 12 seconds  |  Epoch = 32 slots = 6.4 minutes'
props = dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0', edgecolor='#333')
ax.text(0.50, 0.92, timing_text, ha='center', fontsize=11,
        bbox=props, color='#333')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('Validator Responsibilities in Ethereum PoS', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
