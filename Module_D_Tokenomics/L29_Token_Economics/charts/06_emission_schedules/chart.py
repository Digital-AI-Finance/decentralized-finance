"""
Emission Schedule Comparison
Line chart comparing different emission schedule types
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Emission Schedules',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L29_Token_Economics/charts/06_emission_schedules'
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

# Years from project launch
years = np.arange(0, 11)

# Different emission schedules (cumulative supply as %)
max_supply = 100  # Normalized to 100%

# Linear emission: constant rate
linear = 10 * years
linear = np.minimum(linear, max_supply)

# Decreasing emission (Bitcoin halving style)
halving = max_supply * (1 - 0.5 ** (years / 4))

# Exponential decay (rapid initial, then slow)
exp_decay = max_supply * (1 - np.exp(-0.5 * years))

# Front-loaded (DeFi style)
front_loaded = max_supply * (1 - (1 - years/10) ** 3)
front_loaded = np.minimum(front_loaded, max_supply)

ax.plot(years, linear, 'o-', color=MLBLUE, linewidth=2.5, markersize=6, label='Linear: 10%/year')
ax.plot(years, halving, 's-', color=MLORANGE, linewidth=2.5, markersize=6, label='Halving: Bitcoin-style')
ax.plot(years, exp_decay, '^-', color=MLGREEN, linewidth=2.5, markersize=6, label='Exponential Decay')
ax.plot(years, front_loaded, 'd-', color=MLRED, linewidth=2.5, markersize=6, label='Front-loaded: DeFi-style')

# Add annotations
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5)
ax.text(10.2, 50, '50%', fontsize=9, va='center', color='gray')

ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
ax.text(10.2, 100, '100%', fontsize=9, va='center', color='gray')

ax.set_xlabel('Years from Launch', fontsize=12)
ax.set_ylabel('Cumulative Supply (%)', fontsize=12)
ax.set_xlim(-0.5, 11)
ax.set_ylim(0, 110)

ax.legend(loc='lower right', fontsize=10)
ax.grid(True, alpha=0.3)

ax.set_title('Token Emission Schedule Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
