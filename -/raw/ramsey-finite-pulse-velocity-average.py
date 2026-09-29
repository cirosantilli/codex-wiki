"""Original square-pulse Ramsey model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes ramsey-finite-pulse-velocity-average.png to CWD.
No measured data or historical apparatus parameters. No SciPy is required.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

REGION_LENGTH = 0.10  # m, each square interaction region
GAP_LENGTH = 1.00  # m, edge-to-edge drive-free gap
SPEED_SCALE = 200.0  # m/s, also chosen reference speed
OMEGA = 2 * np.pi * 500.0  # rad/s, on-resonance Rabi angular frequency


def probability(delta, tau, flight, omega=OMEGA):
    """Same-phase pulses, initial g, final e, delta = omega_0 - omega_drive."""
    q = np.hypot(omega, delta)
    c = np.cos(q * tau / 2)
    s = np.sin(q * tau / 2)
    return 4 * (omega / q) ** 2 * s**2 * (
        c * np.cos(delta * flight / 2)
        - delta / q * s * np.sin(delta * flight / 2)
    ) ** 2


def beam_average(delta, samples=8001):
    """Integrate an effusive flux PDF; neglected tails have total weight < 4e-10."""
    logv = np.linspace(0.0, np.log(1600.0), samples)
    v = np.exp(logv)
    weights = 2 * v**4 / SPEED_SCALE**4 * np.exp(-(v / SPEED_SCALE) ** 2)
    delta = np.atleast_1d(delta)
    result = np.empty(delta.shape)
    for start in range(0, len(delta), 128):
        d = delta[start:start + 128, None]
        result[start:start + 128] = np.trapezoid(
            probability(d, REGION_LENGTH / v, GAP_LENGTH / v) * weights, logv, axis=1
        )
    return result


def single_speed_fwhm():
    """Bisection of the first positive half-height crossing in ordinary Hz."""
    low, high = 0.0, 100.0
    for _ in range(60):
        mid = (low + high) / 2
        p = probability(2 * np.pi * mid, REGION_LENGTH / SPEED_SCALE,
                        GAP_LENGTH / SPEED_SCALE)
        if p > 0.5:
            low = mid
        else:
            high = mid
    return low + high


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8), layout='constrained')
    for ax, span, label in zip(axes, (1600, 220), ('Wide scan', 'Central fringe')):
        df = np.linspace(-span, span, 3201)
        delta = -2 * np.pi * df
        mono = probability(delta, REGION_LENGTH / SPEED_SCALE, GAP_LENGTH / SPEED_SCALE)
        avg = beam_average(delta)
        ax.plot(df, mono, color='#225b91', lw=1.6, label='One speed: 200 m/s')
        ax.plot(df, avg, color='#ce6327', lw=2.0, label='Effusive speed average')
        if span == 220:
            ax.plot(df, np.cos(np.pi * df * GAP_LENGTH / SPEED_SCALE) ** 2,
                    color='#777777', ls='--', lw=1.2, label='Instantaneous pulses, one speed')
        ax.set(xlabel=r'Drive offset $\nu-\nu_0$ (Hz)', ylim=(-0.03, 1.06),
               xlim=(-span, span), title=label)
        ax.grid(alpha=0.17)
    axes[0].set_ylabel(r'Transfer probability $P_{g\to e}$')
    axes[0].legend(loc='upper right', fontsize=9, framealpha=0.95)
    axes[1].legend(loc='upper right', fontsize=8, framealpha=0.95)
    axes[1].text(0.03, 0.70, f'Finite-pulse FWHM\n(one speed): {single_speed_fwhm():.1f} Hz',
                 transform=axes[1].transAxes, fontsize=10,
                 bbox={'facecolor': 'white', 'edgecolor': '#dddddd', 'alpha': 0.9})
    fig.suptitle('Ramsey spectroscopy: finite pulses and a distribution of flight times', fontsize=14)
    fig.supxlabel(r'Chosen model: $\ell=0.10$ m, $L=1.00$ m, $u=v_*=200$ m/s; '
                  r'$\Omega=2\pi\times500$ rad/s. No measured data.', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120)
    plt.close(fig)


if __name__ == '__main__':
    main()
