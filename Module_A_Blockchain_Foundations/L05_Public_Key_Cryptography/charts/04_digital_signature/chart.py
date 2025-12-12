"""
ECDSA Digital Signature Process
Shows signing and verification workflow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'ECDSA Digital Signature Process',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/04_digital_signature'
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

# Signing section (top)
ax.text(0.25, 0.95, 'SIGNING (Alice)', ha='center', fontsize=14, fontweight='bold', color=MLBLUE)

# Signing steps
sign_steps = [
    (0.08, 0.75, 'Message\nm', MLBLUE),
    (0.25, 0.75, 'Hash\nh=SHA256(m)', MLORANGE),
    (0.42, 0.75, 'Sign with\nPrivate Key', MLRED),
    (0.60, 0.75, 'Signature\n(r, s)', MLPURPLE),
]

for i, (x, y, text, color) in enumerate(sign_steps):
    box = FancyBboxPatch((x - 0.07, y - 0.08), 0.14, 0.16,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            fontweight='bold', color='white')

    if i < len(sign_steps) - 1:
        next_x = sign_steps[i + 1][0]
        ax.annotate('', xy=(next_x - 0.08, y), xytext=(x + 0.08, y),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Send arrow
ax.annotate('', xy=(0.75, 0.50), xytext=(0.60, 0.67),
            arrowprops=dict(arrowstyle='->', color='#333', lw=2))
ax.text(0.70, 0.60, 'Send:\nm + (r,s)', ha='center', fontsize=10, color='#444')

# Verification section (bottom)
ax.text(0.75, 0.95, 'VERIFICATION (Anyone)', ha='center', fontsize=14, fontweight='bold', color=MLGREEN)

# Verification steps
verify_steps = [
    (0.60, 0.30, 'Received\nm, (r, s)', MLLAVENDER),
    (0.75, 0.30, 'Compute\nh=SHA256(m)', MLORANGE),
    (0.90, 0.30, 'Verify with\nPublic Key', MLGREEN),
]

for i, (x, y, text, color) in enumerate(verify_steps):
    box = FancyBboxPatch((x - 0.07, y - 0.08), 0.14, 0.16,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1.5, alpha=0.85)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=9,
            fontweight='bold', color='white' if color != MLLAVENDER else '#333')

    if i < len(verify_steps) - 1:
        next_x = verify_steps[i + 1][0]
        ax.annotate('', xy=(next_x - 0.08, y), xytext=(x + 0.08, y),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Result
result_box = FancyBboxPatch((0.83, 0.08), 0.14, 0.12,
                             boxstyle="round,pad=0.02", facecolor=MLGREEN,
                             edgecolor='black', linewidth=2)
ax.add_patch(result_box)
ax.text(0.90, 0.14, 'Valid?', ha='center', va='center', fontsize=11,
        fontweight='bold', color='white')

ax.annotate('', xy=(0.90, 0.20), xytext=(0.90, 0.22),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))

# Key properties box
props_text = 'Properties:\n- Authentication\n- Integrity\n- Non-repudiation'
props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLPURPLE, alpha=0.95)
ax.text(0.15, 0.30, props_text, ha='left', va='center', fontsize=10,
        bbox=props, color='#333')

# Warning about nonce
warn_text = 'CRITICAL: Never reuse nonce!'
warn_props = dict(boxstyle='round,pad=0.2', facecolor='#FFE0E0', edgecolor=MLRED)
ax.text(0.42, 0.55, warn_text, ha='center', va='center', fontsize=10,
        fontweight='bold', bbox=warn_props, color=MLRED)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title('ECDSA: Digital Signature Workflow', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
