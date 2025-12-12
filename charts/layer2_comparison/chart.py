"""
Layer 2 Scaling Solutions Comparison
Compares major Ethereum L2 solutions across key metrics
[SYNTHETIC DATA - Approximate characteristics]
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Layer 2 Scaling Solutions Comparison',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/layer2_comparison'
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

# Layer 2 solutions and their characteristics
l2_solutions = ['Optimism', 'Arbitrum', 'zkSync Era', 'StarkNet', 'Polygon\nzkEVM']

# Metrics (approximate/normalized values)
# TPS: Transactions per second (normalized to 0-100 scale)
# Finality: Time to finality in minutes (inverted and normalized: lower is better)
# Security: Security score 0-100 (higher is better)

tps_values = [2000, 4000, 2000, 600, 2000]  # Actual TPS estimates
finality_minutes = [7*24*60, 7*24*60, 24*60, 12*60, 10]  # Challenge period in minutes
security_scores = [95, 95, 85, 80, 90]  # Relative security (Optimistic Rollups score high due to fraud proofs)

# Normalize for visualization
tps_normalized = [min(x/50, 100) for x in tps_values]  # Scale to 0-100
finality_normalized = [100 - min(x/100, 100) for x in finality_minutes]  # Invert: faster = better
security_normalized = security_scores

# Prepare data for grouped bar chart
x = np.arange(len(l2_solutions))
width = 0.25

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

# Create grouped bars
bars1 = ax.bar(x - width, tps_normalized, width, label='Throughput (TPS)',
               color='#1a1a1a', edgecolor='black', linewidth=0.8)
bars2 = ax.bar(x, finality_normalized, width, label='Finality Speed',
               color='#666666', edgecolor='black', linewidth=0.8)
bars3 = ax.bar(x + width, security_normalized, width, label='Security Score',
               color='#b3b3b3', edgecolor='black', linewidth=0.8)

ax.set_ylabel('Normalized Score (0-100)')
ax.set_xlabel('Layer 2 Solution')
ax.set_title('Ethereum Layer 2 Solutions: Key Metrics Comparison')
ax.set_xticks(x)
ax.set_xticklabels(l2_solutions)
ax.set_ylim(0, 110)

# Add value labels on bars
def add_labels(bars, values, is_tps=False):
    for bar, val in zip(bars, values):
        height = bar.get_height()
        label = f'{val}' if not is_tps else f'{val}'
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                label,
                ha='center', va='bottom', fontsize=14, rotation=0)

# Add actual values as labels
for i, (bar, tps) in enumerate(zip(bars1, tps_values)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            f'{tps}',
            ha='center', va='bottom', fontsize=14)

for i, (bar, minutes) in enumerate(zip(bars2, finality_minutes)):
    height = bar.get_height()
    if minutes >= 24*60:
        label = f'{minutes//(24*60)}d'
    elif minutes >= 60:
        label = f'{minutes//60}h'
    else:
        label = f'{minutes}m'
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            label,
            ha='center', va='bottom', fontsize=14)

for i, (bar, score) in enumerate(zip(bars3, security_scores)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            f'{score}',
            ha='center', va='bottom', fontsize=14)

ax.legend(loc='upper left', framealpha=0.9)
ax.grid(axis='y', alpha=0.3, linestyle=':', linewidth=0.5)

# Add note explaining the metrics
note_text = "TPS: Transactions/sec | Finality: Time to final settlement | Security: Relative security score"
fig.text(0.5, 0.02, note_text, ha='center', fontsize=14, style='italic', alpha=0.7)

# Add technology type annotation
tech_annotations = [
    "Optimistic\nRollup",
    "Optimistic\nRollup",
    "ZK\nRollup",
    "ZK\nRollup",
    "ZK\nRollup"
]

for i, (x_pos, tech) in enumerate(zip(x, tech_annotations)):
    ax.text(x_pos, 105, tech, ha='center', fontsize=14,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.7))

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC - Approximate characteristics]',
         ha='right', va='bottom', fontsize=14, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
