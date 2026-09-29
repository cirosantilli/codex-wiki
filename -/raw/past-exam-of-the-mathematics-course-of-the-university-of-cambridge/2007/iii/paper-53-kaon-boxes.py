"""Original kaon-mixing box contractions; Python 3.14, root NumPy/Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def wave(ax, a, b, label, offset=(0, 0)):
    a, b = np.array(a), np.array(b)
    t = np.linspace(0, 1, 401)
    d = b-a
    n = np.array([-d[1], d[0]])/np.linalg.norm(d)
    z = a[:, None]+d[:, None]*t+n[:, None]*0.045*np.sin(16*np.pi*t)
    ax.plot(*z, color='black', lw=1.6)
    mid = (a+b)/2+offset
    ax.text(*mid, label, ha='center', va='center', fontsize=16)


def fermion(ax, a, b, label=None, offset=(0, 0)):
    a, b = np.array(a), np.array(b)
    ax.plot([a[0], b[0]], [a[1], b[1]], color='black', lw=1.6)
    ax.annotate('', xy=a+0.61*(b-a), xytext=a+0.40*(b-a),
                arrowprops={'arrowstyle': '-|>', 'color': 'black', 'lw': 1.5})
    if label:
        mid = (a+b)/2+offset
        ax.text(*mid, label, ha='center', va='center', fontsize=16)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.52, 4.8), dpi=100, facecolor='white')
    for k, ax in enumerate(axes):
        ax.set(xlim=(-1.15, 2.25), ylim=(-0.7, 2.4), aspect='equal')
        ax.axis('off')
        tl, tr, bl, br = (0, 1.5), (1.2, 1.5), (0, 0), (1.2, 0)
        fermion(ax, (-0.9, 1.5), tl, r'$d$', (0, .20))
        fermion(ax, tr, (2.1, 1.5), r'$s$', (0, .20))
        fermion(ax, bl, (-0.9, 0), r'$\bar s$', (0, -.22))
        fermion(ax, (2.1, 0), br, r'$\bar d$', (0, -.22))
        if k == 0:
            fermion(ax, tl, tr, r'$u_i$', (0, .22))
            fermion(ax, br, bl, r'$u_j$', (0, -.22))
            wave(ax, tl, bl, r'$W$', (-.24, 0))
            wave(ax, tr, br, r'$W$', (.24, 0))
        else:
            fermion(ax, tl, bl, r'$u_i$', (-.24, 0))
            fermion(ax, br, tr, r'$u_j$', (.24, 0))
            wave(ax, tl, tr, r'$W$', (0, .22))
            wave(ax, bl, br, r'$W$', (0, -.22))
        ax.text(.6, 2.18, 'Box contraction '+str(k+1), ha='center', fontsize=16)
        ax.text(.6, -.62, r'$i,j\in\{u,c,t\}$', ha='center', fontsize=15)
    fig.suptitle(r'$K^0=d\bar s\ \longrightarrow\ \bar K^0=s\bar d$', fontsize=19)
    fig.subplots_adjust(left=.025, right=.975, top=.84, bottom=.04, wspace=.12)
    fig.savefig(Path.cwd()/'paper-53-kaon-boxes.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
