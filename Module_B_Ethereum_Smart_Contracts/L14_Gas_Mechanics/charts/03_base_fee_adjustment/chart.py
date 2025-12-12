"""
Base Fee Adjustment Mechanism
Shows how base fee changes based on block fullness
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Base Fee Adjustment',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics/charts/03_base_fee_adjustment'
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

# Simulate base fee over blocks
np.random.seed(42)
blocks = np.arange(0, 50)
base_fee = [30]  # Start at 30 Gwei

# Simulate varying block fullness
for i in range(1, 50):
    # Random fullness between 30% and 80%
    fullness = np.random.uniform(0.3, 0.8)
    target = 0.5  # 50% target
    gas_limit = 30_000_000

    # Calculate adjustment
    adjustment = (fullness - target) / target / 8
    new_base = base_fee[-1] * (1 + adjustment)
    base_fee.append(max(1, new_base))

# Plot base fee
ax.plot(blocks, base_fee, linewidth=2.5, color=MLBLUE, label='Base Fee')

# Target line
ax.axhline(y=30, color=MLORANGE, linestyle='--', linewidth=1.5, alpha=0.7, label='Initial base fee')

# Annotations for key events
ax.annotate('High demand\n(blocks > 50% full)', xy=(15, 38), fontsize=9,
            ha='center', color=MLRED)
ax.annotate('Lower demand\n(blocks < 50% full)', xy=(35, 26), fontsize=9,
            ha='center', color=MLGREEN)

# Add rule box
props = dict(boxstyle='round,pad=0.3', facecolor='#E8E8E8', edgecolor='#888')
rule_text = 'Block > 50% full: Base fee +up to 12.5%\nBlock < 50% full: Base fee -up to 12.5%'
ax.text(0.98, 0.98, rule_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props)

ax.set_xlabel('Block Number', fontsize=13)
ax.set_ylabel('Base Fee (Gwei)', fontsize=13)
ax.set_xlim(0, 50)
ax.set_ylim(20, 45)

ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)

ax.set_title('EIP-1559 Base Fee Adjustment Mechanism', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
