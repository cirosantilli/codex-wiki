"""Original bcc(111) top-layer and reciprocal-space sketches; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

a = 3.165  # angstrom
L = np.sqrt(2) * a
t1 = np.array([L, 0.0]); t2 = np.array([L / 2, np.sqrt(3) * L / 2])
fig, axs = plt.subplots(1, 2, figsize=(10, 4.6), layout='constrained', facecolor='white')
for m in range(-3, 4):
    for n in range(-3, 4):
        pos = m * t1 + n * t2
        if -6 < pos[0] < 9 and -5 < pos[1] < 8:
            axs[0].plot(*pos, 'o', ms=10, mec='#245c9f', mfc='white')
axs[0].add_patch(Polygon([np.zeros(2), t1, t1 + t2, t2], fc='#e9eef9', ec='#245c9f', lw=1.5, zorder=0))
for t, label, dy in [(t1, 't₁', -0.7), (t2, 't₂', 0.4)]:
    axs[0].annotate('', t, (0, 0), arrowprops={'arrowstyle': '->', 'color': '#b45309', 'lw': 2})
    axs[0].text(*(t * 0.55 + np.array([0, dy])), label, fontsize=13)
axs[0].text(1, 6.9, f'L = √2 a = {L:.3f} Å\nCell area = √3 a² = {np.sqrt(3)*a*a:.3f} Å²', fontsize=10, bbox={'facecolor':'white','edgecolor':'none','alpha':0.9})
axs[0].set(xlim=(-5.5, 8), ylim=(-4.7, 8), xlabel='In-plane coordinate / Å', ylabel='In-plane coordinate / Å', title='Only atoms in the top (111) layer')
# Reciprocal basis with t_i dot b_j = 2 pi delta_ij.
B = 2 * np.pi * np.linalg.inv(np.column_stack([t1, t2])).T
for m in range(-2, 3):
    for n in range(-2, 3):
        pos = B @ np.array([m, n]); axs[1].plot(*pos, 'o', ms=5, color='0.6')
r = 4 * np.pi / (3 * L)
verts = r * np.column_stack([np.cos(np.arange(6)*np.pi/3), np.sin(np.arange(6)*np.pi/3)])
axs[1].add_patch(Polygon(verts, fc='#e9eef9', ec='#245c9f', lw=2))
axs[1].plot(0, 0, 'o', color='#245c9f'); axs[1].text(0.04, 0.05, 'Γ', fontsize=13)
axs[1].text(-1.1, 1.37, f'Area = (2π)² / Aₛ\n       = {(2*np.pi)**2/(np.sqrt(3)*a*a):.3f} Å⁻²', fontsize=11)
axs[1].set(xlim=(-1.8, 1.8), ylim=(-1.8, 1.8), xlabel='k₁ / Å⁻¹', ylabel='k₂ / Å⁻¹', title='First surface Brillouin zone')
for ax in axs:
    ax.set_aspect('equal'); ax.spines[['top', 'right']].set_visible(False); ax.grid(alpha=0.12)
fig.savefig(Path('paper-2-tungsten-surface.png'), dpi=140, facecolor='white');plt.close(fig)
