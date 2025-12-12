"""
NFT Metadata Permanence Risks
Shows risks to NFT metadata availability
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Metadata Permanence Risks',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS/charts/04_permanence_risks'
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

# Risks with severity and likelihood
risks = [
    'Unpinned\nIPFS Files',
    'Server\nShutdown',
    'Mutable\ntokenURI',
    'Gateway\nFailure',
    'HTTP\nLink Rot'
]

# Severity (1-10)
severity = [9, 10, 8, 6, 7]
# Likelihood (1-10)
likelihood = [7, 5, 4, 6, 8]

x = np.arange(len(risks))
width = 0.35

bars1 = ax.bar(x - width/2, severity, width, label='Severity',
               color=MLRED, edgecolor='black', linewidth=0.5, alpha=0.85)
bars2 = ax.bar(x + width/2, likelihood, width, label='Likelihood',
               color=MLORANGE, edgecolor='black', linewidth=0.5, alpha=0.85)

ax.set_ylabel('Score (1-10)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(risks, fontsize=9, fontweight='bold')
ax.set_ylim(0, 12)

ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Risk score (severity * likelihood / 10)
risk_scores = [s * l / 10 for s, l in zip(severity, likelihood)]
for i, score in enumerate(risk_scores):
    ax.text(i, max(severity[i], likelihood[i]) + 0.5, f'Risk: {score:.1f}',
            ha='center', fontsize=9, fontweight='bold', color='#333')

# Mitigation note
ax.text(0.5, -0.15, 'Mitigation: Pin to multiple services, use immutable tokenURI, prefer IPFS/Arweave over HTTP',
        transform=ax.transAxes, ha='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=MLGREEN))

ax.set_title('NFT Metadata Permanence Risks', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
