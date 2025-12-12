"""
Blockchain Gaming Sustainability Factors
Radar/spider chart comparing P2E vs Play-and-Earn models
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Gaming Sustainability',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse/charts/05_gaming_sustainability'
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

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))

# Success factors
categories = ['Fun\nGameplay', 'Sustainable\nTokenomics', 'Low Entry\nBarrier',
              'True\nOwnership', 'Scalability', 'Community']
N = len(categories)

# Scores for different models (1-10)
p2e_axie = [3, 2, 3, 7, 5, 8]      # Axie-style P2E
play_and_earn = [8, 7, 8, 7, 7, 7]  # Play-and-Earn model

# Complete the radar by repeating first value
p2e_axie += p2e_axie[:1]
play_and_earn += play_and_earn[:1]

# Angles for each category
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Plot
ax.plot(angles, p2e_axie, 'o-', linewidth=2, label='P2E (Axie-style)', color=MLRED, markersize=6)
ax.fill(angles, p2e_axie, alpha=0.25, color=MLRED)

ax.plot(angles, play_and_earn, 'o-', linewidth=2, label='Play-and-Earn', color=MLGREEN, markersize=6)
ax.fill(angles, play_and_earn, alpha=0.25, color=MLGREEN)

# Set labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=14, fontweight='bold')
ax.set_ylim(0, 10)

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=14)

ax.set_title('Blockchain Gaming Model Comparison', fontweight='bold', fontsize=15, pad=20)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
