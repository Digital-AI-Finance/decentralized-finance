"""
Security Audit Funnel
Shows layers of security defense
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Audit Funnel',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L43_Smart_Contract_Security/charts/03_audit_funnel'
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

# Security layers and their bug detection rates (cumulative)
layers = ['Internal\nReview', 'Automated\nTools', 'Manual\nAudit', 'Formal\nVerification', 'Bug\nBounty']
bugs_found = [30, 55, 85, 95, 99]  # Cumulative percentage
incremental = [30, 25, 30, 10, 4]
colors = ['#CCCCCC', MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

x = np.arange(len(layers))

bars = ax.bar(x, bugs_found, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

# Add cumulative and incremental labels
for bar, cum, inc in zip(bars, bugs_found, incremental):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{cum}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
            f'+{inc}%', ha='center', va='center', fontsize=9, color='white', fontweight='bold')

ax.set_ylabel('Cumulative Bugs Found (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(layers, fontsize=10)
ax.set_ylim(0, 110)

ax.grid(True, alpha=0.3, axis='y')

# Annotation
ax.text(0.5, -0.15, 'Defense in depth: Each layer catches bugs the previous layers missed',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('Security Audit Funnel: Defense in Depth', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
