"""
Token Classification: FINMA vs MiCA
Side-by-side comparison chart
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Token Classification',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA/charts/01_token_classification'
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# FINMA Token Classification
finma_categories = ['Payment\nTokens', 'Utility\nTokens', 'Asset\nTokens']
finma_regulation = [40, 20, 90]  # Regulation intensity (0-100)
colors_finma = [MLBLUE, MLGREEN, MLORANGE]

bars1 = ax1.barh(finma_categories, finma_regulation, color=colors_finma, edgecolor='black', height=0.5)
ax1.set_xlim(0, 110)
ax1.set_xlabel('Regulatory Intensity', fontsize=14)
ax1.set_title('Swiss FINMA', fontweight='bold', fontsize=16)
ax1.axvline(x=50, color='gray', linestyle='--', alpha=0.5)

# Add labels
for bar, val in zip(bars1, finma_regulation):
    label = 'AML Only' if val < 50 else ('Minimal' if val < 30 else 'Securities Law')
    if val == 40:
        label = 'AML Only'
    elif val == 20:
        label = 'Minimal'
    else:
        label = 'Securities'
    ax1.text(val + 2, bar.get_y() + bar.get_height()/2, label, va='center', fontsize=14)

# MiCA Token Classification
mica_categories = ['E-Money\nTokens', 'Asset-Ref.\nTokens', 'Other\nCrypto']
mica_regulation = [95, 80, 40]  # Regulation intensity
colors_mica = [MLRED, MLORANGE, MLBLUE]

bars2 = ax2.barh(mica_categories, mica_regulation, color=colors_mica, edgecolor='black', height=0.5)
ax2.set_xlim(0, 110)
ax2.set_xlabel('Regulatory Intensity', fontsize=14)
ax2.set_title('EU MiCA', fontweight='bold', fontsize=16)
ax2.axvline(x=50, color='gray', linestyle='--', alpha=0.5)

# Add labels
mica_labels = ['Banking-like', 'Capital+Reserve', 'Whitepaper']
for bar, val, label in zip(bars2, mica_regulation, mica_labels):
    ax2.text(val + 2, bar.get_y() + bar.get_height()/2, label, va='center', fontsize=14)

plt.suptitle('Token Classification Frameworks', fontweight='bold', fontsize=14, y=0.98)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
