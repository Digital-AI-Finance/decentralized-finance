"""
DeFi Technology Stack
Stacked horizontal visualization showing layers
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'DeFi Stack',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L33_Intro_DeFi/charts/03_defi_stack'
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

# Layer definitions
layers = [
    ('Layer 5: Aggregation', '1inch, Yearn, Zapper', '#E1BEE7'),
    ('Layer 4: Application', 'Web Apps, Wallets, Interfaces', '#B39DDB'),
    ('Layer 3: Protocol', 'Uniswap, Aave, Compound, MakerDAO', '#9575CD'),
    ('Layer 2: Asset', 'ETH, USDC, DAI, WBTC, LP Tokens', '#7E57C2'),
    ('Layer 1: Settlement', 'Ethereum, Solana, Arbitrum, Base', '#5E35B1'),
]

y_positions = np.arange(len(layers))
bar_height = 0.7

for i, (layer, examples, color) in enumerate(layers):
    ax.barh(i, 1, height=bar_height, color=color, edgecolor='black', linewidth=1.5)
    ax.text(0.02, i, layer, va='center', ha='left', fontsize=12, fontweight='bold', color='white')
    ax.text(0.98, i, examples, va='center', ha='right', fontsize=10, color='white')

# Add arrow showing composability
ax.annotate('', xy=(1.05, 4), xytext=(1.05, 0),
            arrowprops=dict(arrowstyle='<->', color='black', lw=2))
ax.text(1.12, 2, 'Composability\n(Money Legos)', va='center', ha='left', fontsize=10, rotation=90)

ax.set_xlim(0, 1.25)
ax.set_ylim(-0.5, 4.5)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.set_title('The DeFi Technology Stack', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
