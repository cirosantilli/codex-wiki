"""Autonomous scalar direction field. Python 3.14; NumPy/Matplotlib.
Opaque PNG basename output to caller CWD; respects caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def main():
    fig, ax = plt.subplots(figsize=(7, 5))
    xx, yy = np.meshgrid(np.linspace(.12, 4.08, 21), np.linspace(-1.95, 1.95, 23))
    dy = 1-yy*yy; norm = np.sqrt(1+dy*dy)
    dx = .085/norm; sy = .085*dy/norm
    seg = np.stack([np.stack([xx-dx, yy-sy], -1), np.stack([xx+dx, yy+sy], -1)], -2).reshape(-1, 2, 2)
    ax.add_collection(LineCollection(seg, colors='#a4becb', linewidths=.85))
    x = np.linspace(0, 4.2, 800)
    ax.plot(x, np.tanh(x-1), color='#226a9d', lw=2, label=r'$y=\tanh(x-1)$')
    ax.plot(x, 1/np.tanh(x+.65), color='#a64f22', lw=2, label=r'$y=\coth(x+0.65)$')
    xlow = np.linspace(0, 1.58, 700)
    ax.plot(xlow, 1/np.tanh(xlow-1.6), color='#7a3e86', lw=2, label=r'$y=\coth(x-1.6)$, $x<1.6$')
    for y in [-1, 1]: ax.axhline(y, color='#494949', linestyle='--', lw=1)
    ax.axvline(1.6, color='#ad91b4', linestyle=':', lw=1)
    ax.text(1.65, -1.77, 'lower-branch\npole at x=1.6', color='#6e3e7d', fontsize=8)
    ax.set(xlim=(0, 4.2), ylim=(-2, 2), xlabel='x', ylabel='y')
    ax.set_aspect('equal', adjustable='box')
    ax.legend(loc='lower right', fontsize=8)
    ax.set_title('Direction field and three representative solution branches')
    ax.grid(alpha=.13)
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-2-slope-field.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
