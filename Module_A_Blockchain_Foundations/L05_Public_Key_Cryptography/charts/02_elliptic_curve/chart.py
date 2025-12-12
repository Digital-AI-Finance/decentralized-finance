"""
Elliptic Curve Visualization
Shows the secp256k1 curve used in Bitcoin with point addition
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

CHART_METADATA = {
    'title': 'Elliptic Curve secp256k1',
    'url': 'https://github.com/Digital-AI-Finance/Blockchain_Crypto/tree/main/Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography/charts/02_elliptic_curve'
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

# Plot elliptic curve y^2 = x^3 + 7 (secp256k1, but over reals for visualization)
x = np.linspace(-2, 4, 1000)
# Only plot where x^3 + 7 >= 0
y_squared = x**3 + 7
valid = y_squared >= 0
x_valid = x[valid]
y_pos = np.sqrt(y_squared[valid])
y_neg = -np.sqrt(y_squared[valid])

ax.plot(x_valid, y_pos, color=MLPURPLE, linewidth=3, label='$y^2 = x^3 + 7$')
ax.plot(x_valid, y_neg, color=MLPURPLE, linewidth=3)

# Point P
Px, Py = 1.0, np.sqrt(1**3 + 7)
ax.scatter([Px], [Py], s=150, color=MLBLUE, zorder=5, edgecolor='black', linewidth=2)
ax.text(Px + 0.15, Py + 0.3, 'P', fontsize=14, fontweight='bold', color=MLBLUE)

# Point Q
Qx, Qy = 2.5, np.sqrt(2.5**3 + 7)
ax.scatter([Qx], [Qy], s=150, color=MLGREEN, zorder=5, edgecolor='black', linewidth=2)
ax.text(Qx + 0.15, Qy + 0.3, 'Q', fontsize=14, fontweight='bold', color=MLGREEN)

# Line through P and Q
slope = (Qy - Py) / (Qx - Px)
x_line = np.linspace(-1.5, 4, 100)
y_line = Py + slope * (x_line - Px)
ax.plot(x_line, y_line, color=MLORANGE, linestyle='--', linewidth=2, alpha=0.7, label='Line through P, Q')

# Find intersection point R' (solving cubic)
# For visualization, approximate
Rx = 3.2
Ry_neg = -np.sqrt(Rx**3 + 7)
ax.scatter([Rx], [Ry_neg], s=150, color=MLRED, zorder=5, edgecolor='black', linewidth=2)
ax.text(Rx + 0.15, Ry_neg - 0.4, 'R = P + Q', fontsize=12, fontweight='bold', color=MLRED)

# Show reflection line
Ry_pos = np.sqrt(Rx**3 + 7)
ax.plot([Rx, Rx], [Ry_neg, Ry_pos], color=MLRED, linestyle=':', linewidth=2, alpha=0.7)
ax.scatter([Rx], [Ry_pos], s=80, color=MLRED, zorder=4, alpha=0.5, edgecolor='black')
ax.text(Rx + 0.15, Ry_pos + 0.2, "R'", fontsize=11, color=MLRED, alpha=0.7)

# Axis
ax.axhline(y=0, color='gray', linewidth=0.5)
ax.axvline(x=0, color='gray', linewidth=0.5)

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_xlim(-2, 4.5)
ax.set_ylim(-5, 5)

ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)

# Equation box
eq_text = "Bitcoin's secp256k1 curve:\n$y^2 = x^3 + 7$ (mod p)\n\nPoint Addition:\nR = P + Q"
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=MLPURPLE, alpha=0.95)
ax.text(0.02, 0.98, eq_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props, color='#333')

plt.title('Elliptic Curve Cryptography: Point Addition', fontweight='bold', fontsize=15, pad=10)
plt.tight_layout()

output_path = Path(__file__).parent / 'chart.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Chart saved to: {output_path.absolute()}")
plt.close()
