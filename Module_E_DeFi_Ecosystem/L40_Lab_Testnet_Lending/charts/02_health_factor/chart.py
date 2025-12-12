"""Health Factor and Liquidation Zones"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728'

fig, ax = plt.subplots(figsize=(10, 6))

health_factors = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]
zones = ['LIQUIDATED', 'LIQUIDATED', 'LIQUIDATION', 'DANGER', 'CAUTION', 'SAFE', 'VERY SAFE']
colors = [MLRED, MLRED, MLRED, MLORANGE, MLORANGE, MLGREEN, MLGREEN]

bars = ax.barh(range(len(health_factors)), health_factors, color=colors, edgecolor='black', linewidth=1.5, height=0.6)

for i, (bar, hf, zone) in enumerate(zip(bars, health_factors, zones)):
    ax.text(bar.get_width() + 0.1, i, f'HF = {hf}', va='center', fontsize=10, fontweight='bold')
    ax.text(3.5, i, zone, va='center', fontsize=10, ha='center', color=colors[i], fontweight='bold')

ax.axvline(x=1.0, color=MLRED, linestyle='--', linewidth=2, alpha=0.7)
ax.text(1.05, 6.3, 'Liquidation\nThreshold', fontsize=9, color=MLRED)

ax.set_yticks(range(len(health_factors)))
ax.set_yticklabels([f'Position {i+1}' for i in range(len(health_factors))])
ax.set_xlabel('Health Factor', fontsize=12)
ax.set_xlim(0, 4.5)
ax.set_title('Health Factor Determines Liquidation Risk', fontweight='bold', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
