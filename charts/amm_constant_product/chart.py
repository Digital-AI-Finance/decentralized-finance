"""
AMM Constant Product Formula Visualization (x * y = k)
Shows the hyperbola curve of token reserves in Uniswap-style AMMs
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'AMM Constant Product Formula (x*y=k)',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/amm_constant_product'
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

# Define the constant product
k = 10000  # x * y = k

# Generate x values (Token X reserves)
x = np.linspace(20, 500, 1000)
y = k / x  # Token Y reserves

# Create the chart
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the constant product curve
ax.plot(x, y, color='black', linewidth=2.5, label=f'x · y = {k}')

# Mark initial liquidity point
x_initial = 100
y_initial = k / x_initial
ax.plot(x_initial, y_initial, 'o', color='black', markersize=10,
        label=f'Initial Pool (x={x_initial}, y={y_initial:.0f})')

# Show a trade example
# Trade: User swaps 20 Token X for Token Y
x_after_trade = x_initial + 20
y_after_trade = k / x_after_trade
ax.plot(x_after_trade, y_after_trade, 's', color='gray', markersize=8,
        label=f'After Trade (x={x_after_trade}, y={y_after_trade:.1f})')

# Draw arrows showing the trade
ax.annotate('', xy=(x_after_trade, y_initial), xytext=(x_initial, y_initial),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, linestyle='--'))
ax.annotate('', xy=(x_after_trade, y_after_trade), xytext=(x_after_trade, y_initial),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, linestyle='--'))

# Add labels for the trade
tokens_out = y_initial - y_after_trade
ax.text(x_initial + 10, y_initial + 5, f'+20 Token X', fontsize=14, ha='center')
ax.text(x_after_trade + 15, (y_initial + y_after_trade)/2,
        f'-{tokens_out:.1f} Token Y', fontsize=14, ha='left', rotation=-60)

ax.set_xlabel('Token X Reserve')
ax.set_ylabel('Token Y Reserve')
ax.set_title('Constant Product AMM: x · y = k (Uniswap Model)')
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)

# Add grid
ax.grid(alpha=0.3, linestyle=':', linewidth=0.5)

# Add legend
ax.legend(loc='upper right', framealpha=0.9)

# Add note explaining slippage
note_text = "Larger trades move further along curve (higher slippage)"
fig.text(0.15, 0.88, note_text, fontsize=14, style='italic', alpha=0.7)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
