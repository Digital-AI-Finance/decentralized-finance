"""
Metcalfe's Law Visualization
Showing network value growth with user count
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': "Metcalfe's Law",
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L31_Token_Classification/charts/04_metcalfes_law'
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
MLGRAY = '#888888'

fig, ax = plt.subplots(figsize=(10, 6))

# Number of users
users = np.linspace(10, 1000, 100)

# Metcalfe's Law: V proportional to n^2
metcalfe_value = (users ** 2) / 1000  # Scaled for visualization

# Linear value (for comparison)
linear_value = users / 1

# Actual BTC-like data (simulated to show some deviation)
np.random.seed(42)
actual_value = metcalfe_value * (1 + 0.2 * np.sin(users/50) + np.random.normal(0, 0.05, len(users)))
actual_value = np.maximum(actual_value, 0)

ax.plot(users, metcalfe_value, '-', color=MLBLUE, linewidth=2.5, label="Metcalfe's Law (V = n²)")
ax.plot(users, linear_value, '--', color=MLGRAY, linewidth=2, label='Linear Growth (V = n)')
ax.scatter(users[::10], actual_value[::10], s=30, color=MLORANGE, alpha=0.7, label='Actual Network (simulated)', zorder=5)

# Add annotations
ax.annotate('Network effects\naccelerate growth', xy=(700, 490), fontsize=10, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD', edgecolor=MLBLUE))

ax.set_xlabel('Number of Users (Active Addresses)', fontsize=12)
ax.set_ylabel('Network Value (Normalized)', fontsize=12)
ax.set_xlim(0, 1050)
ax.set_ylim(0, 1100)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

ax.set_title("Metcalfe's Law: Network Value vs. User Growth", fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
