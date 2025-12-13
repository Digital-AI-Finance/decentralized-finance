"""Create all missing charts for lessons 28, 29, 31, 33, 42, 45, 46, 47"""
import os
from pathlib import Path

# Base directory
base_dir = Path(__file__).parent

# ============================================================================
# L28 Lab NFT Evaluation - 3 charts
# ============================================================================

# Chart 1: Evaluation Workflow
chart1_content = '''"""NFT Evaluation Workflow - Step-by-step evaluation process"""
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
    'Project\\nResearch',
    'Team\\nVerification',
    'On-Chain\\nAnalysis',
    'Risk\\nAssessment',
    'Final\\nDecision'
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
    'Roadmap\\nCommunity\\nUtility',
    'Doxxed?\\nTrack Record?\\nLinkedIn',
    'Contract\\nHolders\\nTrading',
    'Liquidity\\nSecurity\\nMarket',
    'Buy/Hold\\nAvoid'
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
'''

chart1_path = base_dir / "Module_C_NFTs_Digital_Assets" / "L28_Lab_NFT_Evaluation" / "charts" / "01_evaluation_workflow"
chart1_path.mkdir(parents=True, exist_ok=True)
(chart1_path / "chart.py").write_text(chart1_content)

# Chart 2: Valuation Factors
chart2_content = '''"""NFT Valuation Factors - Key factors influencing NFT value"""
import matplotlib.pyplot as plt
import numpy as np
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
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

# Valuation factors with importance scores
factors = [
    'Rarity\\n(Traits)',
    'Team\\nCredibility',
    'Community\\nSize',
    'Utility\\nValue',
    'Trading\\nVolume',
    'Floor Price\\nTrend',
    'Holder\\nDistribution',
    'Roadmap\\nDelivery'
]

importance = [9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5]
colors = [MLPURPLE, MLBLUE, MLGREEN, MLORANGE, MLRED, MLPURPLE, MLBLUE, MLGREEN]

# Create spider/radar chart
angles = np.linspace(0, 2 * np.pi, len(factors), endpoint=False).tolist()
importance_plot = importance + [importance[0]]
angles += angles[:1]

ax = plt.subplot(111, projection='polar')
ax.plot(angles, importance_plot, 'o-', linewidth=2, color=MLPURPLE, markersize=8)
ax.fill(angles, importance_plot, alpha=0.25, color=MLPURPLE)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(factors, fontsize=12)
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10, color='gray')
ax.set_title('NFT Valuation Factors\\n(Importance Score 1-10)', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
'''

chart2_path = base_dir / "Module_C_NFTs_Digital_Assets" / "L28_Lab_NFT_Evaluation" / "charts" / "02_valuation_factors"
chart2_path.mkdir(parents=True, exist_ok=True)
(chart2_path / "chart.py").write_text(chart2_content)

# Chart 3: Risk Matrix
chart3_content = '''"""NFT Risk Assessment Matrix - Risk categories and levels"""
import matplotlib.pyplot as plt
import numpy as np
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
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

# Risk categories
categories = ['Liquidity\\nRisk', 'Smart Contract\\nRisk', 'Market\\nRisk',
              'Rug Pull\\nRisk', 'Platform\\nRisk']

# Example risk scores for three NFT projects
project_a = [3, 2, 5, 2, 3]  # Low risk blue-chip
project_b = [6, 5, 7, 5, 6]  # Medium risk
project_c = [9, 8, 8, 9, 7]  # High risk

x = np.arange(len(categories))
width = 0.25

bars1 = ax.bar(x - width, project_a, width, label='Blue-Chip Project (Low Risk)',
               color=MLGREEN, alpha=0.8)
bars2 = ax.bar(x, project_b, width, label='Emerging Project (Medium Risk)',
               color=MLORANGE, alpha=0.8)
bars3 = ax.bar(x + width, project_c, width, label='New Project (High Risk)',
               color=MLRED, alpha=0.8)

# Risk zones
ax.axhspan(0, 4, alpha=0.1, color=MLGREEN, label='Low Risk Zone')
ax.axhspan(4, 7, alpha=0.1, color=MLORANGE, label='Medium Risk Zone')
ax.axhspan(7, 10, alpha=0.1, color=MLRED, label='High Risk Zone')

ax.set_xlabel('Risk Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Risk Score (1-10)', fontsize=14, fontweight='bold')
ax.set_title('NFT Investment Risk Assessment Matrix', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 10)
ax.legend(loc='upper left', fontsize=11)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
'''

chart3_path = base_dir / "Module_C_NFTs_Digital_Assets" / "L28_Lab_NFT_Evaluation" / "charts" / "03_risk_matrix"
chart3_path.mkdir(parents=True, exist_ok=True)
(chart3_path / "chart.py").write_text(chart3_content)

print("Created 3 charts for L28 Lab NFT Evaluation")
