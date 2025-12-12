"""
Impermanent Loss vs Price Change
Shows IL curve for different price ratios
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Impermanent Loss',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_E_DeFi_Ecosystem/L34_AMM_Mechanics/charts/03_impermanent_loss'
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

# Price ratio from 0.2x to 5x
price_ratio = np.linspace(0.2, 5, 200)

# IL formula: 2*sqrt(r)/(1+r) - 1
il = (2 * np.sqrt(price_ratio) / (1 + price_ratio)) - 1
il_percent = il * 100

ax.plot(price_ratio, il_percent, '-', color=MLRED, linewidth=2.5)
ax.fill_between(price_ratio, il_percent, 0, alpha=0.2, color=MLRED)

# Mark key points
key_ratios = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0]
key_labels = ['0.5x (-50%)', '1.0x (0%)', '1.5x (+50%)', '2.0x (+100%)', '3.0x (+200%)', '4.0x (+300%)']
for ratio, label in zip(key_ratios, key_labels):
    il_val = (2 * np.sqrt(ratio) / (1 + ratio)) - 1
    ax.plot(ratio, il_val * 100, 'o', color=MLORANGE, markersize=10, zorder=5)
    y_offset = -3 if ratio == 1.0 else 2
    ax.annotate(f'{il_val*100:.1f}%', xy=(ratio, il_val*100),
                xytext=(0, y_offset), textcoords='offset points',
                fontsize=14, ha='center', fontweight='bold')

# Add reference line at 0
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax.axvline(x=1, color=MLGREEN, linestyle='--', linewidth=1, alpha=0.7)
ax.text(1.05, -3, 'No change\n(IL = 0)', fontsize=14, color=MLGREEN)

ax.set_xlabel('Price Ratio (Final / Initial)', fontsize=15)
ax.set_ylabel('Impermanent Loss (%)', fontsize=15)
ax.set_xlim(0, 5.2)
ax.set_ylim(-30, 5)

ax.grid(True, alpha=0.3)

# Add formula
ax.text(0.95, 0.95, r'$IL = \frac{2\sqrt{r}}{1+r} - 1$', transform=ax.transAxes,
        fontsize=15, va='top', ha='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=MLBLUE))

ax.set_title('Impermanent Loss vs Price Change', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
