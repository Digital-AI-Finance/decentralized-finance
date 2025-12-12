"""Solidity Function Types Comparison"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

functions = ['view', 'pure', 'payable', 'nonpayable']
gas_cost = [0, 0, 21000, 21000]  # Approximate
state_change = [0, 0, 100, 100]
colors = [MLGREEN, MLGREEN, MLORANGE, MLBLUE]

x = np.arange(len(functions))
width = 0.35

bars1 = ax.bar(x - width/2, gas_cost, width, label='Gas Cost (base)', color=MLBLUE, edgecolor='black')
bars2 = ax.bar(x + width/2, state_change, width, label='State Change', color=MLORANGE, edgecolor='black')

ax.set_ylabel('Relative Cost/Impact', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(functions, fontsize=11)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3, axis='y')

# Add annotations
ax.text(0, -8000, 'Read-only', ha='center', fontsize=9, style='italic')
ax.text(1, -8000, 'No state', ha='center', fontsize=9, style='italic')
ax.text(2, -8000, 'Accepts ETH', ha='center', fontsize=9, style='italic')
ax.text(3, -8000, 'Modifies state', ha='center', fontsize=9, style='italic')

ax.set_title('Solidity Function Types: Gas and State Impact', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
print(f"Chart saved")
