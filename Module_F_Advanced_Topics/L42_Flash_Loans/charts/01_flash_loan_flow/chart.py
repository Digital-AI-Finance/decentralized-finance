"""
Flash Loan Transaction Flow
Shows the atomic nature of flash loans
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'Flash Loan Flow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_F_Advanced_Topics/L42_Flash_Loans/charts/01_flash_loan_flow'
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

# Steps in flash loan
steps = ['1. Request\nLoan', '2. Receive\nFunds', '3. Execute\nStrategy', '4. Repay\nLoan + Fee', '5. Transaction\nConfirmed']
x_positions = [1, 2, 3, 4, 5]
y_position = 0.5

# Draw flow
colors = [MLBLUE, MLGREEN, MLORANGE, MLGREEN, MLBLUE]
for i, (step, x, color) in enumerate(zip(steps, x_positions, colors)):
    circle = plt.Circle((x, y_position), 0.35, color=color, alpha=0.7, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y_position, str(i+1), ha='center', va='center', fontsize=16, fontweight='bold', color='white')
    ax.text(x, y_position - 0.55, step, ha='center', va='top', fontsize=10, fontweight='bold')

# Draw arrows between circles
for i in range(len(x_positions) - 1):
    ax.annotate('', xy=(x_positions[i+1] - 0.4, y_position),
                xytext=(x_positions[i] + 0.4, y_position),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))

# Add atomic transaction box
atomic_box = mpatches.FancyBboxPatch((0.5, -0.3), 5, 1.4, boxstyle="round,pad=0.1",
                                       facecolor='none', edgecolor=MLRED, linewidth=3, linestyle='--')
ax.add_patch(atomic_box)
ax.text(3, 1.2, 'ATOMIC TRANSACTION', ha='center', fontsize=14, fontweight='bold', color=MLRED)
ax.text(3, 1.0, 'All steps succeed or all revert', ha='center', fontsize=11, style='italic', color='gray')

ax.set_xlim(0, 6)
ax.set_ylim(-0.6, 1.5)
ax.set_aspect('equal')
ax.axis('off')

ax.set_title('Flash Loan Transaction Flow', fontweight='bold', fontsize=14, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
