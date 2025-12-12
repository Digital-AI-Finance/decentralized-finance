"""
DeFi Total Value Locked (TVL) Growth Over Time
Shows the evolution of DeFi ecosystem from 2019 to 2024
[SYNTHETIC DATA]
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'DeFi Total Value Locked (TVL) Growth 2019-2024',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/charts/tvl_growth'
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

# Synthetic TVL data (approximate historical trends)
dates = [
    '2019-01', '2019-07', '2020-01', '2020-07', '2021-01', '2021-05',
    '2021-11', '2022-05', '2022-11', '2023-05', '2023-11', '2024-05', '2024-11'
]
tvl_billions = [
    0.3, 0.5, 1.0, 4.0, 18.0, 80.0,  # Early days to DeFi Summer
    180.0, 120.0, 40.0, 48.0, 52.0, 85.0, 95.0  # Peak, crash, recovery
]

# Convert dates to datetime for better plotting
x = [datetime.strptime(d, '%Y-%m') for d in dates]

# Create the chart
fig, ax = plt.subplots(figsize=(10, 5))

# Plot TVL line
ax.plot(x, tvl_billions, color='black', linewidth=2, marker='o', markersize=4)

# Fill area under curve
ax.fill_between(x, tvl_billions, alpha=0.2, color='gray')

# Mark key events
events = [
    (datetime.strptime('2020-07', '%Y-%m'), 4.0, 'DeFi Summer\n2020', -40),
    (datetime.strptime('2021-11', '%Y-%m'), 180.0, 'Peak\n$180B', 10),
    (datetime.strptime('2022-11', '%Y-%m'), 40.0, '2022 Crash\n(Terra/FTX)', -45),
    (datetime.strptime('2024-05', '%Y-%m'), 85.0, '2024 Recovery', 10)
]

for event_date, event_tvl, label, y_offset in events:
    ax.annotate(label,
                xy=(event_date, event_tvl),
                xytext=(0, y_offset),
                textcoords='offset points',
                fontsize=14,
                ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.set_xlabel('Year')
ax.set_ylabel('Total Value Locked (Billion USD)')
ax.set_title('DeFi Total Value Locked (TVL) Growth 2019-2024')
ax.set_ylim(0, 200)

# Format y-axis to show billions
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'${int(y)}B'))

# Add grid
ax.grid(alpha=0.3, linestyle=':', linewidth=0.5)

# Rotate x-axis labels
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Add note about synthetic data
fig.text(0.99, 0.01, '[SYNTHETIC - Approximate historical trends]',
         ha='right', va='bottom', fontsize=14, style='italic', alpha=0.6)

plt.tight_layout()

# Save as PDF
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")

plt.close()
