"""
Stablecoin MiCA Compliance Status (2024)
Status comparison chart
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Stablecoin Compliance',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA/charts/03_stablecoin_compliance'
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

# Stablecoins and their compliance status (0-100)
stablecoins = ['USDC\n(Circle)', 'EURC\n(Circle)', 'EURS\n(Stasis)', 'USDT\n(Tether)',
               'DAI\n(MakerDAO)', 'BUSD\n(Paxos)']
compliance = [95, 95, 80, 25, 40, 60]  # Compliance level
market_cap = [30, 0.5, 0.1, 95, 5, 0.1]  # Billions USD (approximate)

colors = [MLGREEN if c >= 80 else (MLORANGE if c >= 50 else MLRED) for c in compliance]

# Create bar chart
bars = ax.bar(stablecoins, compliance, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add compliance labels
status_labels = ['Compliant', 'Compliant', 'Compliant', 'Delisted', 'DeFi Exempt', 'Discontinued']
for bar, val, label in zip(bars, compliance, status_labels):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            label, ha='center', va='bottom', fontsize=9, fontweight='bold',
            color=MLGREEN if val >= 80 else (MLORANGE if val >= 50 else MLRED))

ax.set_ylabel('MiCA Compliance Level (%)', fontsize=12)
ax.set_ylim(0, 115)
ax.grid(True, alpha=0.3, axis='y')

# Compliance threshold
ax.axhline(y=80, color=MLGREEN, linestyle='--', alpha=0.5, linewidth=2)
ax.text(5.5, 82, 'Compliance threshold', fontsize=9, color=MLGREEN, ha='right')

ax.set_title('Stablecoin MiCA Compliance Status (December 2024)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
