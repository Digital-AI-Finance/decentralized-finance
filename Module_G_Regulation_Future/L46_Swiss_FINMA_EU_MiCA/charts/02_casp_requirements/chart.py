"""
MiCA CASP Capital Requirements
Bar chart showing minimum capital by service type
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'CASP Requirements',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA/charts/02_casp_requirements'
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

# CASP services and minimum capital requirements
services = ['Custody &\nAdmin', 'Trading\nPlatform', 'Exchange\nServices', 'Order\nExecution',
            'Advice &\nPortfolio', 'Transfer\nServices']
capital = [125, 150, 125, 125, 50, 50]  # Thousands EUR

colors = [MLBLUE if c < 100 else (MLORANGE if c < 150 else MLRED) for c in capital]

bars = ax.bar(services, capital, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add value labels
for bar, val in zip(bars, capital):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            f'{val}k', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Minimum Capital (EUR thousands)', fontsize=12)
ax.set_ylim(0, 180)
ax.grid(True, alpha=0.3, axis='y')

# Add threshold line
ax.axhline(y=125, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax.text(5.5, 128, 'Standard tier', fontsize=9, color='gray', ha='right')

ax.set_title('MiCA CASP Minimum Capital Requirements', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
