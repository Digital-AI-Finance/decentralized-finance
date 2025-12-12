"""
Token Unlock Price Impact
Dual-axis chart showing unlocks and price correlation
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Unlock Price Impact',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L30_Distribution_Vesting/charts/04_unlock_price_impact'
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

fig, ax1 = plt.subplots(figsize=(10, 6))

# Timeline: days around unlock event
days = np.arange(-30, 31)

# Price pattern: typical drop around unlock
np.random.seed(42)
price = 100 + 5 * np.sin(days / 10) + np.random.normal(0, 2, len(days))
# Add dip around unlock event
unlock_effect = -15 * np.exp(-((days) ** 2) / 100)
price = price + unlock_effect
# Recovery after
price[15:] = price[15:] + 0.3 * (days[15:] - 15)

# Circulating supply
supply = np.ones_like(days, dtype=float) * 100  # Million tokens
supply[days >= 0] = 120  # 20M tokens unlocked

ax1.plot(days, price, '-', color=MLBLUE, linewidth=2.5, label='Token Price')
ax1.fill_between(days, price, alpha=0.2, color=MLBLUE)
ax1.set_xlabel('Days Relative to Unlock Event', fontsize=12)
ax1.set_ylabel('Token Price ($)', fontsize=12, color=MLBLUE)
ax1.tick_params(axis='y', labelcolor=MLBLUE)
ax1.set_ylim(70, 120)

ax2 = ax1.twinx()
ax2.fill_between(days, supply, alpha=0.3, color=MLORANGE, step='post')
ax2.set_ylabel('Circulating Supply (M)', fontsize=12, color=MLORANGE)
ax2.tick_params(axis='y', labelcolor=MLORANGE)
ax2.set_ylim(80, 140)

# Add unlock event marker
ax1.axvline(x=0, color=MLRED, linestyle='--', linewidth=2, alpha=0.7)
ax1.annotate('Unlock\nEvent', xy=(0, 85), xytext=(-15, 75),
            fontsize=10, fontweight='bold', color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED))

# Add annotations
ax1.annotate('Front-running\n(selling before)', xy=(-10, 98), fontsize=9, ha='center')
ax1.annotate('Recovery\n(adoption growth)', xy=(20, 95), fontsize=9, ha='center')

ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left', fontsize=10)

ax1.set_title('Token Unlock Event: Price Impact Pattern', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
