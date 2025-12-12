"""
Impermanent Loss Visualization for Automated Market Makers (AMMs)
Shows IL percentage as token price ratio changes from initial deposit
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Impermanent Loss in AMM Liquidity Pools',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/impermanent_loss'
}

# Set font sizes (MANDATORY)
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12
})

def calculate_impermanent_loss(price_ratio):
    """
    Calculate impermanent loss for a given price ratio
    IL = 2*sqrt(r)/(1+r) - 1
    where r is the price ratio (new_price / initial_price)
    """
    il = 2 * np.sqrt(price_ratio) / (1 + price_ratio) - 1
    return il * 100  # Convert to percentage

# Generate price ratios from 0.25x to 4x
price_ratios = np.linspace(0.25, 4, 500)
il_percentages = calculate_impermanent_loss(price_ratios)

# Create the chart
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the IL curve
ax.plot(price_ratios, il_percentages, color='black', linewidth=2, label='Impermanent Loss')

# Fill the area to emphasize loss
ax.fill_between(price_ratios, il_percentages, 0, alpha=0.2, color='gray')

# Mark key points
key_points = [0.5, 1.0, 2.0, 3.0, 4.0]
for ratio in key_points:
    il = calculate_impermanent_loss(ratio)
    ax.plot(ratio, il, 'o', color='black', markersize=6)
    if ratio != 1.0:  # Don't label the zero point
        ax.annotate(f'{il:.1f}%',
                   xy=(ratio, il),
                   xytext=(5, -10 if il < -10 else 5),
                   textcoords='offset points',
                   fontsize=14,
                   ha='left')

# Add vertical line at ratio = 1 (no price change)
ax.axvline(x=1.0, color='black', linestyle='--', linewidth=0.8, alpha=0.5, label='No price change')
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.3)

ax.set_xlabel('Price Ratio (New Price / Initial Price)')
ax.set_ylabel('Impermanent Loss (%)')
ax.set_title('Impermanent Loss vs Price Change in AMM Liquidity Pools')
ax.set_xlim(0.25, 4)
ax.set_ylim(-30, 5)

# Add grid
ax.grid(alpha=0.3, linestyle=':', linewidth=0.5)

# Add legend
ax.legend(loc='lower right')

# Add note explaining the concept
note_text = "Loss relative to holding tokens outside pool"
fig.text(0.15, 0.88, note_text, fontsize=14, style='italic', alpha=0.7)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
