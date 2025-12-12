"""
RWA Regulatory Frameworks by Jurisdiction
Comparing regulatory clarity across regions
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Regulatory Frameworks',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization/charts/04_regulatory_frameworks'
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

# Jurisdictions and regulatory metrics (1-10)
jurisdictions = ['Switzerland', 'Singapore', 'EU (MiCA)', 'USA', 'UK']
metrics = {
    'Legal Clarity': [9, 8, 7, 5, 6],
    'Token-Friendly': [9, 9, 7, 4, 6],
    'Institutional': [8, 9, 8, 8, 7],
}

x = np.arange(len(jurisdictions))
width = 0.25
colors = [MLGREEN, MLBLUE, MLORANGE]

for i, (metric, values) in enumerate(metrics.items()):
    bars = ax.bar(x + i * width - 0.25, values, width, label=metric,
                  color=colors[i], edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(jurisdictions, fontsize=10, fontweight='bold')
ax.set_ylim(0, 11)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# Key frameworks note
ax.text(0.5, -0.12, 'Key: Switzerland DLT Act (2021), Singapore MAS Sandbox, EU MiCA (2024), USA Reg D/A+/S',
        transform=ax.transAxes, ha='center', fontsize=8,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#888'))

ax.set_title('RWA Regulatory Framework Comparison', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
