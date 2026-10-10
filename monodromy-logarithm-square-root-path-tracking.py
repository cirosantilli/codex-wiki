"""Track the original quarter-circle and clockwise three-quarter-circle routes.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

BLUE = '#176aab'
ORANGE = '#c45419'
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12})
fig, (log_ax, sqrt_ax) = plt.subplots(1, 2, figsize=(8, 4.3), dpi=140, facecolor='white')
t = np.linspace(0, 1, 401)
theta_a = np.pi * t / 2
theta_b = -3 * np.pi * t / 2
for ax in (log_ax, sqrt_ax):
    ax.set_facecolor('white')
    ax.spines[['top', 'right']].set_visible(False)

log_ax.plot(t, theta_a / np.pi, color=BLUE, lw=2.5, label='Path A')
log_ax.plot(t, theta_b / np.pi, color=ORANGE, lw=2.5, label='Path B')
log_ax.axhline(0, color='#d1d5da', lw=0.8, zorder=0)
log_ax.axvline(2 / 3, color='#aaaaaa', lw=1, ls=':')
log_ax.text(0.67, -0.12, 'B crosses cut', fontsize=9, rotation=90, va='top')
log_ax.scatter([1, 1], [0.5, -1.5], color=[BLUE, ORANGE], zorder=5)
log_ax.annotate('', xy=(1.075, 0.5), xytext=(1.075, -1.5),
                arrowprops={'arrowstyle': '<->', 'color': '#333333'})
log_ax.text(1.105, -0.5, r'$2\pi i$', fontsize=11, va='center')
log_ax.text(0.48, 0.47, r'$L_A(1)=\pi i/2$', color=BLUE, fontsize=10)
log_ax.text(0.25, -1.6, r'$L_B(1)=-3\pi i/2$', color=ORANGE, fontsize=10)
log_ax.set(title='Logarithm: continuous angle', xlabel='Path parameter t',
           ylabel=r'$\operatorname{Im}L(t)\,/\,\pi$', xlim=(-0.04, 1.28), ylim=(-1.8, 0.8))
log_ax.set_xticks([0, 0.5, 1])
log_ax.set_yticks([-1.5, -1, -0.5, 0, 0.5])
log_ax.legend(loc='lower left', bbox_to_anchor=(0, 0.21), frameon=False, fontsize=10)

for theta, color in [(theta_a, BLUE), (theta_b, ORANGE)]:
    w = np.exp(0.5j * theta)
    sqrt_ax.plot(w.real, w.imag, color=color, lw=2.5)
    index = 200
    sqrt_ax.annotate('', xy=(w[index + 16].real, w[index + 16].imag),
                     xytext=(w[index].real, w[index].imag),
                     arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2})
    sqrt_ax.scatter([w[-1].real], [w[-1].imag], color=color, zorder=5)
sqrt_ax.axhline(0, color='#d1d5da', lw=0.8, zorder=0)
sqrt_ax.axvline(0, color='#d1d5da', lw=0.8, zorder=0)
sqrt_ax.plot([-2 ** -0.5, 2 ** -0.5], [-2 ** -0.5, 2 ** -0.5], color='#aaaaaa', lw=1, ls=':')
sqrt_ax.scatter([1], [0], color='#222222', s=30, zorder=5)
sqrt_ax.text(1.03, 0.09, 'start: 1', fontsize=9)
sqrt_ax.text(-0.19, 0.92, r'$S_A(1)=(1+i)/\sqrt{2}$', color=BLUE, fontsize=10)
sqrt_ax.text(-1.15, -1.18, r'$S_B(1)=-(1+i)/\sqrt{2}$', color=ORANGE, fontsize=10)
sqrt_ax.set(title='Square root: half the angle', xlabel=r'$\operatorname{Re}S(t)$',
            ylabel=r'$\operatorname{Im}S(t)$', xlim=(-1.3, 1.4), ylim=(-1.35, 1.22))
sqrt_ax.set_aspect('equal')
sqrt_ax.set_xticks([-1, 0, 1])
sqrt_ax.set_yticks([-1, 0, 1])
fig.text(0.5, 0.045, 'Both source paths end at i. Continuation remembers how each path got there.', ha='center', fontsize=11)
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.20, top=0.88, wspace=0.38)
fig.savefig(Path('monodromy-logarithm-square-root-path-tracking.png'), facecolor='white')
plt.close(fig)
