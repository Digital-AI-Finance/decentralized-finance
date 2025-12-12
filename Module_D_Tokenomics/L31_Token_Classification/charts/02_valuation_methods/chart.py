"""
Token Valuation Methods Comparison
Horizontal bar showing applicability and reliability of each method
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Valuation Methods',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_D_Tokenomics/L31_Token_Classification/charts/02_valuation_methods'
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

# Valuation methods
methods = ['NVT Ratio', "Metcalfe's\nLaw", 'DCF\nAnalysis', 'Comparable\nAnalysis', 'Cost of\nProduction']

# Metrics
applicability = [9, 8, 4, 7, 3]  # How widely applicable
reliability = [6, 5, 7, 6, 8]  # How reliable when applicable
ease_of_use = [8, 7, 5, 6, 7]  # How easy to calculate

y_pos = np.arange(len(methods))
height = 0.25

bars1 = ax.barh(y_pos - height, applicability, height, label='Broad Applicability',
                color=MLBLUE, edgecolor='black', linewidth=0.5)
bars2 = ax.barh(y_pos, reliability, height, label='Reliability',
                color=MLGREEN, edgecolor='black', linewidth=0.5)
bars3 = ax.barh(y_pos + height, ease_of_use, height, label='Ease of Use',
                color=MLORANGE, edgecolor='black', linewidth=0.5)

ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=14)
ax.set_xlabel('Score (1-10)', fontsize=15)
ax.set_xlim(0, 11)

ax.legend(loc='lower right', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')

# Add annotations
ax.text(0.5, -0.12, 'Use multiple methods; no single approach is definitive for crypto valuation',
        transform=ax.transAxes, ha='center', fontsize=14,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor=MLORANGE))

ax.set_title('Token Valuation Methods Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
