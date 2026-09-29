"""Original figure; Python 3.14, root-pinned numpy/matplotlib.

Writes only paper-54-conformal-diagram.png to the caller's current directory.
Any supplied MPLCONFIGDIR is retained.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def compactify(time, radius):
    p = np.arctan(time-radius)
    q = np.arctan(time+radius)
    return (q-p)/np.pi, (q+p)/np.pi


def main():
    fig, ax = plt.subplots(figsize=(5.2, 6.4), dpi=150, facecolor='white')
    ax.set_facecolor('white')
    ax.plot([0, 0, 1, 0], [-1, 1, 0, -1], color='#18212b', linewidth=1.8)
    ax.fill([0, 0, 1], [-1, 1, 0], color='#f5f7fa', zorder=0)
    ax.plot([0, 1], [0, 0], color='#c9cfd8', linewidth=.8, zorder=1)
    parameter = 2*np.tan(np.linspace(-np.pi/2+.001, np.pi/2-.001, 2400))
    time = parameter
    radius = np.abs(.35*time+.65)
    rr, tt = compactify(time, radius)
    ax.plot(rr, tt, color='#774ba4', linewidth=2.2, label='timelike geodesic')
    center_time = -.12
    past_radius = (1+center_time)/2
    future_radius = (1-center_time)/2
    ax.plot([past_radius, 0, future_radius], [past_radius-1, center_time, 1-future_radius], color='#dc7c12', linewidth=2.2, label='null geodesic')
    time = .3+.1*parameter
    radius = np.abs(parameter+1.2)
    rr, tt = compactify(time, radius)
    ax.plot(rr, tt, color='#24806c', linewidth=2.2, label='spacelike geodesic')
    ax.scatter([0, 0, 1], [-1, 1, 0], color='#18212b', s=20, zorder=4)
    ax.text(-.02, 1.045, r'$i^+$', ha='center', fontsize=15)
    ax.text(-.02, -1.075, r'$i^-$', ha='center', fontsize=15)
    ax.text(1.04, 0, r'$i^0$', va='center', fontsize=15)
    ax.text(.66, .42, r'$\mathcal{I}^+$', rotation=-45, fontsize=15)
    ax.text(.66, -.42, r'$\mathcal{I}^-$', rotation=45, fontsize=15)
    ax.text(-.085, 0, 'regular center', rotation=90, ha='center', va='center', fontsize=10)
    ax.text(.37, .85, r'$|T|+R<\pi$', fontsize=12)
    ax.set_xlim(-.16, 1.22)
    ax.set_ylim(-1.17, 1.17)
    ax.set_aspect('equal')
    ax.set_xticks([0, .5, 1], ['0', r'$\pi/2$', r'$\pi$'])
    ax.set_yticks([-1, -.5, 0, .5, 1], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
    ax.set_xlabel('$R$')
    ax.set_ylabel('$T$')
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='lower right', fontsize=8.5, frameon=True, facecolor='white', framealpha=1)
    ax.set_title('Minkowski conformal compactification\nAngular two-spheres suppressed', fontsize=12)
    fig.tight_layout()
    fig.savefig('paper-54-conformal-diagram.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
