"""
RWA Tokenization Process Flow
Step-by-step tokenization diagram
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'RWA Tokenization Process',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/01_rwa_tokenization_process'
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

# Steps in tokenization process
steps = [
    (0.08, 0.7, '1. Asset\nSelection', MLBLUE, 'Real Estate,\nSecurities'),
    (0.28, 0.7, '2. Legal\nStructure', MLPURPLE, 'SPV/LLC\nCreation'),
    (0.48, 0.7, '3. Token\nIssuance', MLORANGE, 'ERC-20/1400\nMinting'),
    (0.68, 0.7, '4. Primary\nSale', MLGREEN, 'Investor\nPurchase'),
    (0.88, 0.7, '5. Secondary\nTrading', MLRED, 'Exchange\nLiquidity'),
]

# Draw step boxes
for x, y, label, color, sublabel in steps:
    rect = mpatches.FancyBboxPatch((x-0.08, y-0.12), 0.16, 0.24,
                                    boxstyle="round,pad=0.01,rounding_size=0.02",
                                    facecolor=color, edgecolor='black',
                                    linewidth=2, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x, y+0.03, label, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')
    ax.text(x, y-0.08, sublabel, ha='center', va='center',
            fontsize=7, color='white', style='italic')

# Draw arrows between steps
arrow_props = dict(arrowstyle='->', color='black', lw=2)
for i in range(len(steps)-1):
    x1 = steps[i][0] + 0.08
    x2 = steps[i+1][0] - 0.08
    ax.annotate('', xy=(x2, 0.7), xytext=(x1, 0.7), arrowprops=arrow_props)

# Bottom info boxes
info_boxes = [
    (0.25, 0.25, 'Legal Layer', '#E3F2FD', 'Off-chain contracts\nlink token to asset'),
    (0.75, 0.25, 'Blockchain Layer', '#E8F5E9', 'On-chain ownership\nand transfer'),
]

for x, y, title, color, text in info_boxes:
    rect = mpatches.FancyBboxPatch((x-0.2, y-0.12), 0.4, 0.24,
                                    boxstyle="round,pad=0.02",
                                    facecolor=color, edgecolor='#888',
                                    linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y+0.05, title, ha='center', va='center',
            fontsize=10, fontweight='bold')
    ax.text(x, y-0.05, text, ha='center', va='center', fontsize=8)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()

ax.set_title('Real-World Asset Tokenization Process', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
