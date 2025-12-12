"""
Wallet Types Comparison
Security vs Convenience tradeoff
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Wallet Types',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L08_Lab_Wallet_Setup/charts/01_wallet_types'
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

wallets = ['Exchange\nWallet', 'Mobile\nWallet', 'Desktop\nWallet', 'Hardware\nWallet', 'Paper\nWallet']
security = [3, 5, 6, 9, 8]
convenience = [9, 8, 6, 4, 2]
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN, MLPURPLE]

x = np.arange(len(wallets))
width = 0.35

bars1 = ax.bar(x - width/2, security, width, label='Security', color=MLGREEN, edgecolor='black')
bars2 = ax.bar(x + width/2, convenience, width, label='Convenience', color=MLBLUE, edgecolor='black')

ax.set_ylabel('Score (1-10)', fontsize=15)
ax.set_xticks(x)
ax.set_xticklabels(wallets, fontsize=14)
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=14)
ax.grid(True, alpha=0.3, axis='y')

# Add annotation
ax.annotate('Recommended\nfor Lab', xy=(3, 9), xytext=(3, 10.5),
            fontsize=14, ha='center', fontweight='bold', color=MLGREEN,
            arrowprops=dict(arrowstyle='->', color=MLGREEN))

ax.set_title('Wallet Types: Security vs Convenience Tradeoff', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
