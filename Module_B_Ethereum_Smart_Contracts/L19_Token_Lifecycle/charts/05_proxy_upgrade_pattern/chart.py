"""
Proxy Upgrade Pattern
Visual diagram of transparent proxy pattern
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

CHART_METADATA = {
    'title': 'Proxy Upgrade Pattern',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle/charts/05_proxy_upgrade_pattern'
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

# User box
user_box = FancyBboxPatch((0.05, 0.55), 0.12, 0.20,
                           boxstyle="round,pad=0.02", facecolor='#E8E8E8',
                           edgecolor='black', linewidth=2)
ax.add_patch(user_box)
ax.text(0.11, 0.65, 'Users', ha='center', va='center', fontsize=11, fontweight='bold')

# Proxy contract (central)
proxy_box = FancyBboxPatch((0.28, 0.45), 0.20, 0.35,
                            boxstyle="round,pad=0.02", facecolor=MLBLUE,
                            edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(proxy_box)
ax.text(0.38, 0.72, 'Proxy Contract', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')
ax.text(0.38, 0.58, 'Fixed Address\n0x1234...', ha='center', va='center',
        fontsize=9, color='white')
ax.text(0.38, 0.50, 'Storage', ha='center', va='center',
        fontsize=9, color='#FFE', fontweight='bold')

# Implementation V1 (old)
impl_v1_box = FancyBboxPatch((0.60, 0.65), 0.16, 0.20,
                              boxstyle="round,pad=0.02", facecolor='#999',
                              edgecolor='black', linewidth=1.5, alpha=0.6)
ax.add_patch(impl_v1_box)
ax.text(0.68, 0.75, 'Implementation V1', ha='center', va='center',
        fontsize=9, fontweight='bold', color='white')
ax.text(0.68, 0.68, '(deprecated)', ha='center', va='center',
        fontsize=8, color='#DDD')

# Implementation V2 (current)
impl_v2_box = FancyBboxPatch((0.60, 0.35), 0.16, 0.22,
                              boxstyle="round,pad=0.02", facecolor=MLGREEN,
                              edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(impl_v2_box)
ax.text(0.68, 0.50, 'Implementation V2', ha='center', va='center',
        fontsize=9, fontweight='bold', color='white')
ax.text(0.68, 0.40, 'Logic Only\n(No Storage)', ha='center', va='center',
        fontsize=8, color='white')

# Admin box
admin_box = FancyBboxPatch((0.80, 0.55), 0.12, 0.20,
                            boxstyle="round,pad=0.02", facecolor=MLORANGE,
                            edgecolor='black', linewidth=2, alpha=0.9)
ax.add_patch(admin_box)
ax.text(0.86, 0.65, 'Admin', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')

# Arrows
# User -> Proxy
ax.annotate('', xy=(0.28, 0.65), xytext=(0.17, 0.65),
           arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax.text(0.22, 0.70, 'Call', fontsize=9, ha='center')

# Proxy -> Implementation V2 (delegatecall)
ax.annotate('', xy=(0.60, 0.46), xytext=(0.48, 0.55),
           arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(0.53, 0.44, 'delegatecall', fontsize=9, ha='center', color=MLGREEN, fontweight='bold')

# Admin -> Proxy (upgrade)
ax.annotate('', xy=(0.48, 0.72), xytext=(0.80, 0.72),
           arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=2))
ax.text(0.64, 0.78, 'upgradeTo(v2)', fontsize=9, ha='center', color=MLORANGE, fontweight='bold')

# Strikethrough from proxy to V1
ax.plot([0.48, 0.60], [0.65, 0.75], color='#666', linestyle='--', lw=1.5, alpha=0.5)

# Key points
ax.text(0.50, 0.18, 'Key: Storage stays in Proxy, Logic can be upgraded',
        ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF9C4', edgecolor='#FBC02D'))

# Labels
ax.text(0.05, 0.95, 'Transparent Proxy Pattern', fontsize=9, color='#666',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#F0F0F0', edgecolor='#888'))

ax.set_xlim(0, 1)
ax.set_ylim(0.1, 1)
ax.axis('off')

ax.set_title('Proxy Upgrade Pattern', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
