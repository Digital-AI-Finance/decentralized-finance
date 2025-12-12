"""
Consensus Mechanism Comparison
Compares PoW, PoS, DPoS, and other consensus mechanisms
[SYNTHETIC DATA]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Consensus Mechanism Comparison - Key Metrics',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/consensus_comparison'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12
})

# Data (synthetic, representative values)
mechanisms = ['PoW\n(Bitcoin)', 'PoS\n(Ethereum)', 'DPoS\n(EOS)', 'PoA\n(Private)', 'PBFT\n(Hyperledger)']

# Metrics (1-10 scale)
energy_efficiency = [1, 8, 9, 9, 8]
decentralization = [9, 7, 5, 3, 4]
throughput = [2, 5, 8, 9, 7]
security = [9, 8, 6, 7, 7]
finality_speed = [2, 6, 9, 10, 9]

x = np.arange(len(mechanisms))
width = 0.15

fig, ax = plt.subplots(figsize=(10, 6))

# Grayscale-friendly colors
colors = ['#1a1a1a', '#4d4d4d', '#808080', '#a6a6a6', '#d9d9d9']

bars1 = ax.bar(x - 2*width, energy_efficiency, width, label='Energy Efficiency', color=colors[0])
bars2 = ax.bar(x - width, decentralization, width, label='Decentralization', color=colors[1])
bars3 = ax.bar(x, throughput, width, label='Throughput', color=colors[2])
bars4 = ax.bar(x + width, security, width, label='Security', color=colors[3])
bars5 = ax.bar(x + 2*width, finality_speed, width, label='Finality Speed', color=colors[4])

ax.set_ylabel('Score (1-10)')
ax.set_title('Consensus Mechanism Comparison: Trade-offs Analysis', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(mechanisms)
ax.legend(loc='upper right', fontsize=14)
ax.set_ylim(0, 11)
ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

# Add value labels on bars
for bars in [bars1, bars2, bars3, bars4, bars5]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=14)

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC]', ha='right', va='bottom', fontsize=14, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
