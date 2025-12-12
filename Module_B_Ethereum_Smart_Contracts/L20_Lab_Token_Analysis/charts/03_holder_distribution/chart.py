"""Token Holder Distribution Example"""
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({'font.size': 14, 'figure.figsize': (10, 6), 'figure.dpi': 150})
MLBLUE, MLORANGE, MLGREEN, MLRED, MLPURPLE = '#0066CC', '#FF7F0E', '#2CA02C', '#D62728', '#3333B2'

fig, ax = plt.subplots(figsize=(10, 6))

labels = ['Top 10 Holders', 'Top 11-50', 'Top 51-100', 'Remaining Holders']
sizes = [45, 20, 10, 25]
colors = [MLRED, MLORANGE, MLBLUE, MLGREEN]
explode = (0.05, 0, 0, 0)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, textprops={'fontsize': 10})

ax.text(0, -1.3, 'Warning: High concentration (>50% in top 10) = centralization risk', ha='center', fontsize=10, style='italic', color=MLRED)
ax.set_title('Typical Token Holder Distribution', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', bbox_inches='tight', dpi=300)
plt.close()
