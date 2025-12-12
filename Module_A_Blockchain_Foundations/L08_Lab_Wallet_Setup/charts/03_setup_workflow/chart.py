"""
Wallet Setup Workflow
Step-by-step process
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

CHART_METADATA = {
    'title': 'Setup Workflow',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L08_Lab_Wallet_Setup/charts/03_setup_workflow'
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

# Workflow steps
steps = ['1. Download\nWallet', '2. Create\nNew Wallet', '3. Backup\nSeed Phrase',
         '4. Verify\nBackup', '5. Add\nPassword', '6. Test\nRecovery']
x_positions = [0.1, 0.25, 0.4, 0.55, 0.7, 0.85]
colors = [MLBLUE, MLBLUE, MLRED, MLRED, MLORANGE, MLGREEN]

for i, (x, step, color) in enumerate(zip(x_positions, steps, colors)):
    rect = mpatches.FancyBboxPatch((x - 0.06, 0.35), 0.12, 0.3,
                                    boxstyle="round,pad=0.02",
                                    facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 0.5, step, ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    if i < len(steps) - 1:
        ax.annotate('', xy=(x_positions[i+1] - 0.06, 0.5), xytext=(x + 0.06, 0.5),
                   arrowprops=dict(arrowstyle='->', color='gray', lw=2))

# Time estimates
times = ['2 min', '1 min', '5 min', '3 min', '2 min', '5 min']
for x, time in zip(x_positions, times):
    ax.text(x, 0.25, time, ha='center', va='center', fontsize=14, color='gray')

# Importance labels
ax.text(0.325, 0.75, 'CRITICAL STEPS', ha='center', va='center', fontsize=14,
        fontweight='bold', color=MLRED,
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFEBEE', edgecolor=MLRED))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

ax.set_title('Wallet Setup Workflow (18 minutes total)', fontweight='bold', fontsize=14, pad=10)

plt.tight_layout()
output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
