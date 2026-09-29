"""Draw de Sitter geodesics and causal horizons; write opaque PNG to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
T = np.linspace(-pi / 2, pi / 2, 1001)
chi = np.linspace(-pi, pi, 1501)
fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.2), dpi=100, facecolor='white')
blue, orange, purple = '#245c8e', '#bf6423', '#6f4b86'
for ax in axes:
    ax.set(xlim=(-pi, pi), ylim=(-pi / 2, pi / 2), xlabel=r'Periodic angle $\chi$', ylabel=r'Conformal time $T$')
    ax.set_aspect('equal')
    ax.set_xticks([-pi, -pi / 2, 0, pi / 2, pi], [r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$', r'$\pi$'])
    ax.set_yticks([-pi / 2, 0, pi / 2], [r'$-\pi/2$', '$0$', r'$\pi/2$'])
    ax.grid(alpha=.18)
    ax.tick_params(labelsize=11)
    ax.spines[['top', 'bottom']].set_linestyle('--')
    ax.spines[['left', 'right']].set_color('#7b8790')
    ax.text(0, pi / 2 + .11, r'$\mathcal{I}^{+}$: future spacelike boundary', ha='center', fontsize=11)

ax = axes[0]
for j, alpha in enumerate([-2, -1, 0, 1, 2]):
    ax.plot(np.arcsin(np.tanh(alpha) * np.sin(T)), T, color=blue, lw=1.7,
            label='Timelike' if j == 0 else None)
    ax.plot(chi, np.arcsin(np.tanh(alpha) * np.sin(chi)), color=purple, lw=1.3,
            label='Spacelike (closed)' if j == 0 else None)
ax.plot(T, T, color=orange, lw=2, label='Null')
ax.plot(-T, T, color=orange, lw=2)
ax.scatter([0], [0], s=36, color='#111111', zorder=5)
ax.set_title('All geodesic types through one point', fontsize=13, pad=35)
ax.legend(loc='upper left', fontsize=10, framealpha=.97)

ax = axes[1]
XX, YY = np.meshgrid(np.linspace(-pi, pi, 700), np.linspace(-pi / 2, pi / 2, 350))
# The chosen lift has shortest angular distance |chi| <= pi.
can_send = np.abs(XX) < pi / 2 - YY
can_receive = np.abs(XX) < YY + pi / 2
region = can_send.astype(int) + 2 * can_receive.astype(int)
from matplotlib.colors import ListedColormap
ax.pcolormesh(XX, YY, region, shading='auto', cmap=ListedColormap(['#ffffff', '#e5f0fa', '#f9ecdf', '#e6e1f0']), vmin=0, vmax=3, rasterized=True)
for j, sign in enumerate([-1, 1]):
    ax.plot(sign * (pi / 2 - T), T, color=blue, lw=2, label='Future event horizon' if j == 0 else None)
    ax.plot(sign * (T + pi / 2), T, color=orange, lw=2, label='Past event horizon' if j == 0 else None)
ax.plot(np.zeros_like(T), T, color='#202b36', lw=2, label='Observer')
ax.text(0, -.12, 'Static\npatch', ha='center', va='center', fontsize=11, color='#342947')
ax.set_title('Signals to and from a complete observer', fontsize=13, pad=35)
ax.legend(loc='lower right', fontsize=9, framealpha=.97)
fig.subplots_adjust(left=.075, right=.985, bottom=.22, top=.79, wspace=.24)
for ax in axes:
    box = ax.get_position()
    fig.text((box.x0 + box.x1) / 2, .095, 'Left and right edges are identified', ha='center', fontsize=10, color='#465764')
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
