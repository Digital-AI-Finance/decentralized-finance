"""
Finality Timeline
Shows different finality types and their time to finality
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Finality Timeline',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L10_Consensus_Comparison/charts/03_finality_timeline'
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

# Finality types (y positions)
finality_types = [
    ('PBFT\n(Hyperledger)', 4, 0.001, MLPURPLE, 'Instant'),  # ~1ms
    ('DPoS\n(EOS)', 3, 2, MLORANGE, '2 sec'),
    ('PoS\n(Ethereum)', 2, 768, MLGREEN, '12.8 min'),  # 768 seconds
    ('PoW\n(Bitcoin)', 1, 3600, MLBLUE, '60 min'),  # 1 hour
]

# Time scale (log)
ax.set_xscale('log')
ax.set_xlim(0.0001, 10000)

# Draw timeline bars
for name, y, time_sec, color, label in finality_types:
    # Bar from 0 to time
    ax.barh(y, time_sec, height=0.5, color=color, alpha=0.8, left=0.0001)

    # Label on the right
    ax.text(time_sec * 1.5, y, label, va='center', fontsize=14, fontweight='bold')

    # Name on the left
    ax.text(0.00005, y, name, va='center', ha='right', fontsize=14)

# Add vertical lines for reference points
reference_times = [
    (1, '1 sec'),
    (60, '1 min'),
    (600, '10 min'),
    (3600, '1 hour'),
]

for t, label in reference_times:
    ax.axvline(x=t, color='#888', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(t, 4.7, label, ha='center', fontsize=14, color='#555')

# Finality type annotations
ax.text(0.001, 0.3, 'INSTANT FINALITY\n(Deterministic)', ha='center',
        fontsize=14, color=MLPURPLE, fontweight='bold')
ax.text(100, 0.3, 'ECONOMIC FINALITY\n(Slashing guarantee)', ha='center',
        fontsize=14, color=MLGREEN, fontweight='bold')
ax.text(5000, 0.3, 'PROBABILISTIC\n(Confirmation depth)', ha='center',
        fontsize=14, color=MLBLUE, fontweight='bold')

ax.set_xlabel('Time to Finality (seconds, log scale)', fontsize=16)
ax.set_yticks([])
ax.set_ylim(0, 5)

ax.set_title('Consensus Finality Comparison', fontweight='bold', fontsize=15, pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
