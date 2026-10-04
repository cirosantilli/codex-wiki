"""Trigonometric integrating-factor sketches. Root NumPy/Matplotlib, Python 3.14.
Save only PNG basename in caller CWD; respect MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def ticks(ax):
    ax.set_xticks([0, np.pi/4, np.pi/2], ['0', r'$\pi/4$', r'$\pi/2$'])
    ax.set_yticks([0, np.pi/4, np.pi/2], ['0', r'$\pi/4$', r'$\pi/2$'])


def main():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    ax = axes[0]
    X, Y = np.meshgrid(np.linspace(.055, 1.51, 15), np.linspace(.055, 1.51, 15))
    slope = np.tan(X)*np.tan(Y); norm = np.sqrt(1+slope*slope)
    dx = .035/norm; dy = .035*slope/norm
    lines = np.stack([np.stack([X-dx, Y-dy], -1), np.stack([X+dx, Y+dy], -1)], -2).reshape(-1, 2, 2)
    ax.add_collection(LineCollection(lines, colors='#357393', linewidths=1.1))
    ax.set(xlim=(0, np.pi/2), ylim=(0, np.pi/2), xlabel='x', ylabel='y')
    ax.set_aspect('equal'); ticks(ax)
    ax.set_title('First-quadrant direction field', fontsize=10)
    ax = axes[1]
    for C in [-.8, -.5, -.2, 0., .2, .5, .8]:
        limit = np.arccos(abs(C)) if C else np.pi/2
        x = np.linspace(-limit, limit, 601)
        y = np.arcsin(np.clip(C/np.cos(x), -1, 1)) if C else np.zeros_like(x)
        ax.plot(x, y, lw=1.6, label=f'C={C:g}')
    ax.set(xlim=(-np.pi/2, np.pi/2), ylim=(-np.pi/2, np.pi/2), xlabel='x', ylabel='y')
    ax.set_xticks([-np.pi/2, 0, np.pi/2], [r'$-\pi/2$', '0', r'$\pi/2$'])
    ax.set_yticks([-np.pi/2, 0, np.pi/2], [r'$-\pi/2$', '0', r'$\pi/2$'])
    ax.set_aspect('equal'); ax.set_title(r'Regularized family: $\cos x\sin y=C$', fontsize=10)
    ax.legend(fontsize=6, loc='upper center', ncols=2)
    ax = axes[2]
    x = np.linspace(0, np.pi/2-.004, 700)
    y = np.sqrt(-2*np.log(np.cos(x)))
    ax.plot(x, y, color='#a24e25', lw=2, label=r'$y=\sqrt{-2\log\cos x}$')
    ax.plot(x, x, color='#929292', ls='--', label='initial tangent y=x')
    ax.axvline(np.pi/2, color='#999999', ls=':')
    ax.set(xlim=(0, 1.68), ylim=(0, 3.5), xlabel='x', ylabel='y')
    ax.set_xticks([0, np.pi/4, np.pi/2], ['0', r'$\pi/4$', r'$\pi/2$'])
    ax.set_title('Positive higher-order solution', fontsize=10)
    ax.legend(fontsize=7, loc='upper left')
    for ax in axes: ax.grid(alpha=.12)
    fig.suptitle('Integrating factors: level curves and a derivative-dependent first integral', fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .91))
    fig.savefig(Path.cwd()/'paper-2-integrating-factor.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
