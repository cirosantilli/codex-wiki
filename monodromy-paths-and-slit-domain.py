"""Draw original continuation routes and a cut-domain homotopy.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#176aab'
ORANGE = '#c45419'
GREEN = '#2b8051'
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12})
fig, axes = plt.subplots(1, 2, figsize=(8, 4.3), dpi=140, facecolor='white')
t = np.linspace(0, 1, 401)
a = np.exp(1j * np.pi * t / 2)
b = np.exp(-3j * np.pi * t / 2)
segment = 1 - t + 1j * t


def arrow(ax, z, index, color):
    ax.annotate('', xy=(z[index + 14].real, z[index + 14].imag),
                xytext=(z[index].real, z[index].imag),
                arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2})


for ax in axes:
    ax.set_facecolor('white')
    ax.axhline(0, color='#d1d5da', lw=0.8, zorder=0)
    ax.axvline(0, color='#d1d5da', lw=0.8, zorder=0)
    ax.scatter([0], [0], s=45, facecolor='white', edgecolor='#333333', zorder=8)
    ax.text(0.07, -0.18, '0 excluded', fontsize=9)
    ax.scatter([1, 0], [0, 1], color='#252525', s=24, zorder=8)
    ax.text(1.07, 0.06, r'$a=1$')
    ax.text(0.08, 1.07, r'$b=i$')
    ax.set(xlim=(-1.35, 1.4), ylim=(-1.27, 1.37), xlabel=r'$\operatorname{Re}z$', ylabel=r'$\operatorname{Im}z$')
    ax.set_aspect('equal')
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.spines[['top', 'right']].set_visible(False)

ax = axes[0]
ax.set_title(r'Punctured plane: $\mathbb{C}\setminus\{0\}$', pad=14)
ax.plot(a.real, a.imag, color=BLUE, lw=2.5)
ax.plot(b.real, b.imag, color=ORANGE, lw=2.5)
arrow(ax, a, 180, BLUE)
arrow(ax, b, 70, ORANGE)
arrow(ax, b, 230, ORANGE)
ax.text(0.75, 0.7, r'$\gamma_A$', color=BLUE)
ax.text(-1.04, -0.65, r'$\gamma_B$', color=ORANGE)
ax.text(0.5, -0.23, 'A, then reverse B: one positive loop',
        transform=ax.transAxes, ha='center', fontsize=10)

ax = axes[1]
ax.set_title(r'Slit domain: cut $(-\infty,0]$', pad=14)
ax.plot([-1.35, 0], [0, 0], color='#b12434', lw=3, zorder=3)
ax.text(-1.22, 0.13, 'branch cut', color='#b12434', fontsize=10)
ax.plot(b.real, b.imag, color=ORANGE, lw=1.8, ls='--', alpha=0.65)
ax.scatter([-1], [0], marker='x', color='#b12434', s=65, zorder=8)
ax.text(-1.15, -0.49, 'B crosses cut\nat t = 2/3', fontsize=9, color=ORANGE)
for s in np.linspace(0.15, 0.85, 5):
    h = (1 - s) * a + s * segment
    ax.plot(h.real, h.imag, color='#bad7c8', lw=1.2)
ax.plot(a.real, a.imag, color=BLUE, lw=2.5)
ax.plot(segment.real, segment.imag, color=GREEN, lw=2.5)
arrow(ax, a, 180, BLUE)
arrow(ax, segment, 200, GREEN)
ax.text(0.83, 0.65, r'$\gamma_A$', color=BLUE)
ax.text(0.34, 0.29, r'$\sigma$', color=GREEN)
ax.text(0.5, -0.23, 'A deforms to the segment; B is excluded',
        transform=ax.transAxes, ha='center', fontsize=10)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.23, top=0.86, wspace=0.38)
fig.savefig(Path('monodromy-paths-and-slit-domain.png'), facecolor='white')
plt.close(fig)
