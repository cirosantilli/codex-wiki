"""Original, diffusion-free release model; each panel fixes observation time.

Continuous origin release starts at t=0 s, with five highlighted release times.
Dashed paths show histories, dots show current positions. No measurement data.
Run in _media under Python 3.14; output filename comes from the script name.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


def main():
    U, a = 1.0, 1.0  # m/s, m/s^2
    releases = np.arange(0, 2.01, 0.5)  # seconds
    norm = Normalize(0, 2)
    cmap = plt.get_cmap('viridis')
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.9), layout='constrained')
    fig.suptitle('One source, many particles: freeze the observation time', fontsize=15)
    for ax, T in zip(axes, [1.0, 2.0]):
        tau_curve = np.linspace(0, T, 401)
        sx = U*(T-tau_curve)
        sy = a*(T*T-tau_curve*tau_curve)/2
        assert np.allclose(sy, a*T*sx/U-a*sx*sx/(2*U*U))
        ax.plot(sx, sy, color='#171b21', lw=2.1, label='Streakline at this T')
        for tau in releases[releases <= T]:
            t = np.linspace(tau, T, 251)
            x = U*(t-tau)
            y = a*(t*t-tau*tau)/2
            color = cmap(norm(tau))
            ax.plot(x, y, '--', color=color, lw=1.7)
            ax.scatter(x[-1], y[-1], color=color, edgecolor='#20252c',
                       linewidth=0.5, s=58, zorder=5)
            # Velocity at observation T differs from the streakline tangent.
            if tau < T:
                ax.quiver(x[-1], y[-1], U, a*T, angles='xy',
                          scale_units='xy', scale=9, color='#777777', width=0.005)
            assert abs(x[0]) < 1e-14 and abs(y[0]) < 1e-14
        ax.set(xlabel='x (m)', ylabel='y (m)', xlim=(-0.1, 2.35), ylim=(-0.12, 2.55))
        ax.set_title(f'Observation T = {T:g} s', fontsize=13)
        ax.set_aspect('equal')
        ax.grid(alpha=0.15)
        ax.set_xticks([0, 0.5, 1, 1.5, 2])
        ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5])
        ax.annotate('source', (0, 0), xytext=(6, 10), textcoords='offset points', fontsize=10)
        ax.legend(loc='upper left', fontsize=9, framealpha=1)
    cb = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), ax=axes, shrink=0.86, pad=0.025)
    cb.set_label('Particle release time τ (s)')
    cb.set_ticks(releases)
    fig.supxlabel('Dots: positions now. Dashed: earlier pathlines. Grey arrows: velocity now.\n'
                  'Analytical model, no diffusion: U = 1 m/s; a = 1 m/s²; continuous release from t = 0 s.',
                  fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
