"""
Global Crypto Regulatory Spectrum
Horizontal bar chart showing countries by regulatory approach
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Regulatory Spectrum',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L45_Global_Regulation/charts/01_regulatory_spectrum'
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

# Countries and their regulatory stance (1=Hostile, 5=Permissive)
countries = ['China', 'India', 'South Korea', 'Brazil', 'Japan',
             'UK', 'Germany', 'USA', 'Singapore', 'Switzerland', 'UAE', 'El Salvador']
scores = [1.0, 2.0, 2.5, 2.5, 3.0, 3.5, 3.5, 3.0, 4.0, 4.5, 4.5, 5.0]

# Color based on score
colors = []
for s in scores:
    if s <= 1.5:
        colors.append(MLRED)
    elif s <= 2.5:
        colors.append(MLORANGE)
    elif s <= 3.5:
        colors.append('#CCCCCC')
    else:
        colors.append(MLGREEN)

y_pos = np.arange(len(countries))
bars = ax.barh(y_pos, scores, color=colors, edgecolor='black', linewidth=1.2, height=0.7)

ax.set_yticks(y_pos)
ax.set_yticklabels(countries, fontsize=14)
ax.set_xlim(0, 5.5)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(['Hostile', 'Restrictive', 'Developing', 'Permissive', 'Embracing'], fontsize=14)

# Add score labels
for bar, score in zip(bars, scores):
    ax.text(score + 0.1, bar.get_y() + bar.get_height()/2, f'{score:.1f}',
            va='center', fontsize=14)

ax.axvline(x=3, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax.grid(True, alpha=0.3, axis='x')

ax.set_title('Global Crypto Regulatory Spectrum (2024-2025)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
