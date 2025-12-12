"""
Security Levels for Key Storage
Tier comparison
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Security Levels',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L08_Lab_Wallet_Setup/charts/02_security_levels'
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

# Security tiers
tiers = ['Tier 1:\nBasic', 'Tier 2:\nIntermediate', 'Tier 3:\nAdvanced', 'Tier 4:\nMaximum']
scores = [3, 6, 8, 10]
examples = ['Exchange custody', 'Hot wallet + 2FA', 'Hardware wallet', 'Multi-sig + cold storage']
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN]

bars = ax.barh(tiers, scores, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

for bar, example in zip(bars, examples):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            example, ha='left', va='center', fontsize=14, style='italic')

ax.set_xlabel('Security Score', fontsize=15)
ax.set_xlim(0, 14)
ax.grid(True, alpha=0.3, axis='x')

# Lab recommendation
ax.axvline(x=6, color=MLPURPLE, linestyle='--', linewidth=2, alpha=0.7)
ax.text(6.2, 3.5, 'Lab\nMinimum', fontsize=14, color=MLPURPLE, fontweight='bold')

ax.set_title('Key Storage Security Tiers', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
