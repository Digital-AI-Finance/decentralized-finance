"""
Blockchain Positions on the Trilemma
Scatter plot showing where different chains fall
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Trilemma Positions',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L11_Scalability_Trilemma/charts/06_trilemma_positions'
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

# Axes: Decentralization (x) vs Scalability (y), color = security
# Data: (decentralization, scalability, security_score, name, color)
blockchains = [
    (90, 10, 95, 'Bitcoin', MLBLUE),
    (70, 35, 90, 'Ethereum L1', MLBLUE),
    (75, 80, 88, 'Ethereum + L2', MLGREEN),
    (60, 50, 80, 'Cardano', MLGREEN),
    (40, 75, 70, 'Polkadot', MLORANGE),
    (20, 85, 60, 'EOS', MLORANGE),
    (35, 95, 65, 'Solana', MLRED),
    (5, 98, 50, 'Centralized DB', MLPURPLE),
]

for dec, scale, sec, name, color in blockchains:
    # Size based on security
    size = sec * 3
    ax.scatter(dec, scale, s=size, color=color, alpha=0.7, edgecolor='black', linewidth=1.5)
    # Label
    offset_x = 5 if name not in ['Solana', 'EOS'] else -5
    offset_y = 5 if name not in ['Ethereum L1', 'Bitcoin'] else -8
    ha = 'left' if offset_x > 0 else 'right'
    ax.annotate(name, (dec, scale), xytext=(dec + offset_x, scale + offset_y),
                fontsize=10, fontweight='bold', ha=ha)

# Ideal corner annotation
ax.annotate('Ideal\n(impossible?)', xy=(90, 90), fontsize=11, ha='center',
            style='italic', color='#888')
ax.scatter(90, 90, s=150, color='#888', alpha=0.3, marker='*')

# Axes labels and styling
ax.set_xlabel('Decentralization Score', fontsize=13)
ax.set_ylabel('Scalability Score (TPS)', fontsize=13)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Quadrant labels
ax.text(85, 5, 'Decentralized\nNot Scalable', ha='center', fontsize=9,
        color=MLBLUE, alpha=0.7)
ax.text(15, 95, 'Scalable\nNot Decentralized', ha='center', fontsize=9,
        color=MLRED, alpha=0.7)

# Size legend
ax.scatter([], [], s=50*3, color='gray', alpha=0.7, label='Security: Low')
ax.scatter([], [], s=75*3, color='gray', alpha=0.7, label='Security: Medium')
ax.scatter([], [], s=95*3, color='gray', alpha=0.7, label='Security: High')
ax.legend(loc='lower right', fontsize=9, title='Bubble Size = Security')

ax.grid(True, alpha=0.3)
ax.set_title('Blockchain Trilemma Positioning', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
