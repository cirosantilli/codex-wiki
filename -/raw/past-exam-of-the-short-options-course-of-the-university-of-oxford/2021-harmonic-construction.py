"""Generate the ASO 2021 harmonic construction; Python 3.14, NumPy/Matplotlib per pyproject.toml."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def intersection(a, b, c, d):
    p = np.cross(np.cross(np.r_[a, 1.0], np.r_[b, 1.0]),
                 np.cross(np.r_[c, 1.0], np.r_[d, 1.0]))
    return p[:2] / p[2]


def main():
    r0, r1, r2 = (np.array(p, dtype=float) for p in [(0, 0), (4, 0), (1, 0)])
    a = np.array([1.6, 2.5])
    b = (a + r2) / 2
    u = intersection(r0, a, r1, b)
    v = intersection(r0, b, r1, a)
    r3 = intersection(u, v, r0, r1)
    assert np.allclose(r3, [-2, 0])
    fig, ax = plt.subplots(figsize=(8.6, 4.2), layout='constrained')
    ax.plot([-2.5, 4.4], [0, 0], color='#263238', lw=1.6)
    ax.plot(*np.array([r0, a]).T, color='#81909a', lw=1.2)
    ax.plot(*np.array([r1, a]).T, color='#81909a', lw=1.2)
    ax.plot(*np.array([r0, v]).T, color='#81909a', lw=1.2)
    ax.plot(*np.array([r1, u]).T, color='#81909a', lw=1.2)
    ax.plot(*np.array([r2, a]).T, color='#a7afb4', ls=':', lw=1.6)
    ax.plot(*np.array([r3, v]).T, color='#d35400', lw=2)
    labels = [(r0, r'$R_0$', (-8, -22)), (r1, r'$R_1$', (0, -22)),
              (r2, r'$R_2$', (0, -22)), (r3, r'$R_3$', (0, -22)),
              (a, r'$A$', (0, 10)), (b, r'$B$', (10, -5)),
              (u, r'$U$', (-16, 4)), (v, r'$V$', (9, 5))]
    for p, label, offset in labels:
        ax.scatter(*p, s=28, color='#263238', zorder=5)
        ax.annotate(label, p, xytext=offset, textcoords='offset points', ha='center', fontsize=12)
    ax.text(4.3, .14, r'$L$', fontsize=12)
    ax.set(xlim=(-2.6, 4.6), ylim=(-.5, 2.9), aspect='equal',
           title=r'Harmonic construction: $(R_0R_1:R_2R_3)=-1$')
    ax.axis('off')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
