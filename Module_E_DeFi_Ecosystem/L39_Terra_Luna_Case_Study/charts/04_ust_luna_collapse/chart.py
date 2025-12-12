"""
UST and LUNA Value Destruction
Before/After comparison of market caps
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'UST LUNA Collapse',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L39_Terra_Luna_Case_Study/charts/04_ust_luna_collapse'
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

# Pre and post collapse values
categories = ['UST', 'LUNA', 'Anchor TVL']
pre_collapse = [18, 40, 14]  # Billions USD
post_collapse = [0.1, 0.01, 0.01]  # Near zero

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, pre_collapse, width, label='May 1, 2022 (Pre)',
               color=MLGREEN, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, post_collapse, width, label='May 15, 2022 (Post)',
               color=MLRED, edgecolor='black', linewidth=1.5)

# Add value labels for pre-collapse
for bar, val in zip(bars1, pre_collapse):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'${val}B', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add "~$0" labels for post-collapse
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            '~$0', ha='center', va='bottom', fontsize=11, fontweight='bold', color=MLRED)

ax.set_ylabel('Market Cap (Billion USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 50)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Add loss annotation
ax.text(0.5, -0.15, 'Total value destroyed: ~$60 billion in 72 hours (99%+ loss)',
        transform=ax.transAxes, ha='center', fontsize=11,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_title('Terra Ecosystem: Value Destruction', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
