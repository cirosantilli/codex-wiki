"""Original analytical curves, u=(U,a*t); run from _media, Python 3.14.

Spatial units: m; time: s; U=1 m/s; a=1 m/s^2; T=2 s.
This plots exact parameterizations, not fitted or experimental data.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    U, a, T = 1.0, 1.0, 2.0
    x = np.linspace(0, U*T, 501)
    t = x/U
    tau = T-x/U
    streamline = a*T*x/U
    pathline = a*t*t/2
    streakline = a*(T*T-tau*tau)/2
    assert np.allclose(streakline, a*T*x/U-a*x*x/(2*U*U))
    assert np.allclose(np.gradient(pathline, t)[1:-1], a*t[1:-1])
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12,
                         'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(8.2, 5.9), layout='constrained')
    fig.suptitle('Three curves, three questions', fontsize=17)
    ax.set_title('Analytical field: U = 1 m/s, a = 1 m/s²; observation T = 2 s', pad=12)
    # All arrows represent the velocity at the SAME physical time T.
    gx, gy = np.meshgrid(np.linspace(0.2, 1.9, 6), np.linspace(0.15, 3.85, 8))
    ax.quiver(gx, gy, U*np.ones_like(gx), a*T*np.ones_like(gy),
              angles='xy', scale_units='xy', scale=10, color='#d1d5db', width=0.003,
              zorder=0)
    ax.plot(x, streamline, color='#078150', lw=2.6,
            label='Streamline through source: frozen T = 2 s')
    ax.plot(x, pathline, color='#ce6809', lw=2.7,
            label='Pathline: one particle, t = 0 to 2 s')
    ax.plot(x, streakline, color='#7c3f99', lw=2.7,
            label='Streakline: releases τ = 0 to 2 s, all seen at T')
    for y, color, txt in [(0.5, '#ce6809', '0.5 m'), (1.5, '#7c3f99', '1.5 m'),
                           (2.0, '#078150', '2.0 m')]:
        ax.scatter([1], [y], s=45, color=color, zorder=5)
        ax.annotate(txt, (1, y), xytext=(9, -16 if y==1.5 else 6),
                    textcoords='offset points', color=color, weight='bold')
    ax.scatter([0, 2], [0, 2], color='#20252c', s=40, zorder=6)
    ax.annotate('fixed source', (0, 0), xytext=(12, 7), textcoords='offset points')
    ax.annotate('oldest particle at T', (2, 2), xytext=(-8, -28),
                ha='right', textcoords='offset points', fontsize=10)
    ax.axvline(1, color='#777777', lw=0.8, ls=':', zorder=0)
    ax.set(xlabel='x (m)', ylabel='y (m)', xlim=(-0.07, 2.15), ylim=(-0.09, 4.35))
    ax.set_xticks(np.arange(0, 2.1, 0.5))
    ax.grid(alpha=0.13)
    ax.legend(loc='upper left', fontsize=9, framealpha=1)
    fig.supxlabel('Grey arrows: instantaneous velocity direction at T. Curves are exact analytical models.',
                  fontsize=9)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
