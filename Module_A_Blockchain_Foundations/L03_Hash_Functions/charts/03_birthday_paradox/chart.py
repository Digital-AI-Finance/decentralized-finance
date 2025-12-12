"""
Birthday Paradox Probability Curve
Shows probability of collision as number of samples increases
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Birthday Paradox Probability',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L03_Hash_Functions/charts/03_birthday_paradox'
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
MLLAVENDER = '#ADADE0'

fig, ax = plt.subplots(figsize=(10, 6))

# Birthday problem: probability of at least one collision
# P(collision) = 1 - P(no collision) = 1 - (365/365)(364/365)...(365-n+1)/365
n_people = np.arange(1, 71)
n_days = 365

# Calculate probability of collision
def collision_probability(n, N):
    if n > N:
        return 1.0
    prob_no_collision = 1.0
    for i in range(n):
        prob_no_collision *= (N - i) / N
    return 1 - prob_no_collision

probs = [collision_probability(n, n_days) for n in n_people]

# Plot
ax.plot(n_people, probs, color=MLPURPLE, linewidth=3, label='Collision probability')

# Mark key points
# 50% probability
idx_50 = np.argmin(np.abs(np.array(probs) - 0.5))
ax.axhline(y=0.5, color=MLORANGE, linestyle='--', linewidth=1.5, alpha=0.7)
ax.axvline(x=n_people[idx_50], color=MLORANGE, linestyle='--', linewidth=1.5, alpha=0.7)
ax.scatter([n_people[idx_50]], [probs[idx_50]], color=MLORANGE, s=100, zorder=5)
ax.annotate(f'50% at n={n_people[idx_50]}', xy=(n_people[idx_50], probs[idx_50]),
            xytext=(35, 0.4), fontsize=12, color=MLORANGE,
            arrowprops=dict(arrowstyle='->', color=MLORANGE))

# 99% probability
idx_99 = np.argmin(np.abs(np.array(probs) - 0.99))
ax.scatter([n_people[idx_99]], [probs[idx_99]], color=MLRED, s=100, zorder=5)
ax.annotate(f'99% at n={n_people[idx_99]}', xy=(n_people[idx_99], probs[idx_99]),
            xytext=(55, 0.85), fontsize=12, color=MLRED,
            arrowprops=dict(arrowstyle='->', color=MLRED))

# Fill area under curve
ax.fill_between(n_people, probs, alpha=0.2, color=MLPURPLE)

# Labels
ax.set_xlabel('Number of People (or Hash Samples)', fontsize=13)
ax.set_ylabel('Probability of Collision', fontsize=13)
ax.set_xlim(0, 70)
ax.set_ylim(0, 1.05)

# Grid
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Key insight box
insight_text = 'Birthday Paradox:\nWith 365 possible values,\ncollision likely at n $\\approx$ $\\sqrt{365}$ $\\approx$ 23\n\nFor SHA-256 (2$^{256}$ outputs):\nCollision at $\\approx$ 2$^{128}$ attempts'
props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=MLPURPLE, alpha=0.95)
ax.text(0.98, 0.35, insight_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', horizontalalignment='right', bbox=props, color='#333')

plt.title('Birthday Paradox: Collision Probability vs Sample Size', fontweight='bold', fontsize=15, pad=15)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
