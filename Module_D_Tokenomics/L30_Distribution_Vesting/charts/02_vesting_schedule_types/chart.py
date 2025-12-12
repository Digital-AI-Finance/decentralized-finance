"""
Vesting Schedule Types Comparison
Line chart comparing linear, stepped, and accelerated vesting
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Vesting Schedule Types',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L30_Distribution_Vesting/charts/02_vesting_schedule_types'
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

# Months from TGE
months = np.arange(0, 49)

# Linear vesting: 1-year cliff, then linear for 36 months
linear = np.zeros_like(months, dtype=float)
linear[12:] = np.linspace(0, 100, len(months[12:]))

# Stepped vesting: 25% per year (quarterly steps)
stepped = np.zeros_like(months, dtype=float)
stepped[12:] = 25  # After 1 year cliff
stepped[24:] = 50  # After 2 years
stepped[36:] = 75  # After 3 years
stepped[48:] = 100  # After 4 years

# Accelerated vesting: more upfront (risky)
accelerated = np.zeros_like(months, dtype=float)
accelerated[6:] = 30  # 30% at 6 months
accelerated[12:] = 50 + (months[12:] - 12) * (50 / 36)
accelerated = np.minimum(accelerated, 100)

# Back-loaded vesting: more at end (best alignment)
backloaded = np.zeros_like(months, dtype=float)
backloaded[12:] = 10  # Small amount at cliff
backloaded[24:] = 25  #
backloaded[36:] = 50  #
backloaded[48:] = 100  # Big unlock at end

ax.plot(months, linear, '-', color=MLBLUE, linewidth=2.5, label='Linear (12mo cliff, 48mo total)')
ax.plot(months, stepped, '--', color=MLORANGE, linewidth=2.5, label='Stepped (25% per year)')
ax.plot(months, accelerated, '-.', color=MLRED, linewidth=2.5, label='Accelerated (risky)')
ax.plot(months, backloaded, ':', color=MLGREEN, linewidth=3, label='Back-loaded (best alignment)')

# Add cliff annotation
ax.axvline(x=12, color='gray', linestyle='--', alpha=0.5)
ax.text(12.5, 95, '1-Year\nCliff', fontsize=9, va='top', color='gray')

ax.set_xlabel('Months from TGE', fontsize=12)
ax.set_ylabel('% Tokens Unlocked', fontsize=12)
ax.set_xlim(0, 50)
ax.set_ylim(0, 105)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

ax.set_title('Vesting Schedule Types Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
