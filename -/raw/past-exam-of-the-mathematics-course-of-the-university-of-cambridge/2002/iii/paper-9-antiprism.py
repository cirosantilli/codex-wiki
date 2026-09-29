"""Draw C_8 squared; run from the desired PNG output directory."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

positions = {}
for i in range(8):
    angle = math.pi / 2 - i * math.pi / 4
    radius = 1.25 if i % 2 == 0 else 0.57
    positions[i] = (radius * math.cos(angle), radius * math.sin(angle))
fig, ax = plt.subplots(figsize=(6.2, 5.7), facecolor='white')
ax.set_facecolor('white')
for i in range(8):
    for j in range(i + 1, 8):
        if (i - j) % 8 in (1, 2, 6, 7):
            x, y = zip(positions[i], positions[j])
            ax.plot(x, y, color='#677686', linewidth=1.7, zorder=1)
for i, (x, y) in positions.items():
    color = '#b83e39' if i in (0, 4) else '#2465aa' if i in (2, 6) else '#424b55'
    ax.scatter([x], [y], s=410, color=color, edgecolor='white', linewidth=1.6, zorder=3)
    ax.text(x, y, str(i), ha='center', va='center', color='white', fontsize=12, fontweight='bold', zorder=4)
ax.set_title('A four-connected graph without the prescribed two-linkage', fontsize=12, pad=17)
ax.text(0, -1.54, 'Required pairs: 0–4 (red) and 2–6 (blue)', ha='center', fontsize=11)
ax.set_xlim(-1.55, 1.55)
ax.set_ylim(-1.65, 1.55)
ax.set_aspect('equal')
ax.axis('off')
fig.tight_layout()
fig.savefig(Path('paper-9-antiprism.png'), dpi=120, facecolor='white', transparent=False)
plt.close(fig)
