"""NFT Evaluation Workflow - Step-by-step evaluation process"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

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

fig, ax = plt.subplots(figsize=(10, 6))

# Workflow steps
steps = [
    'Project\nResearch',
    'Team\nVerification',
    'On-Chain\nAnalysis',
    'Risk\nAssessment',
    'Final\nDecision'
]

colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

# Draw workflow boxes
for i, (step, color) in enumerate(zip(steps, colors)):
    # Box
    rect = mpatches.FancyBboxPatch((i*2, 0.5), 1.5, 1.5,
                                    boxstyle="round,pad=0.1",
                                    edgecolor=color, facecolor=color, alpha=0.3, linewidth=2)
    ax.add_patch(rect)

    # Text
    ax.text(i*2 + 0.75, 1.25, step, ha='center', va='center',
            fontsize=13, fontweight='bold', color=color)

    # Arrow to next step
    if i < len(steps) - 1:
        ax.arrow(i*2 + 1.6, 1.25, 0.3, 0, head_width=0.2, head_length=0.15,
                fc='gray', ec='gray', linewidth=1.5)

# Add sub-labels
sub_labels = [
    'Roadmap\nCommunity\nUtility',
    'Doxxed?\nTrack Record?\nLinkedIn',
    'Contract\nHolders\nTrading',
    'Liquidity\nSecurity\nMarket',
    'Buy/Hold\nAvoid'
]

for i, label in enumerate(sub_labels):
    ax.text(i*2 + 0.75, -0.1, label, ha='center', va='top',
            fontsize=10, color='gray', style='italic')

ax.set_xlim(-0.5, 10)
ax.set_ylim(-0.8, 2.5)
ax.axis('off')
ax.set_title('NFT Project Evaluation Workflow', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
