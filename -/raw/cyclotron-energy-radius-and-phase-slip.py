"""Classical radius and relativistic timing diagnostic for a chosen proton model.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
The prescribed energy ramp diagnoses timing error; it omits cos(phase) feedback.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

E_CHARGE = 1.602176634e-19
PROTON_MASS = 1.67262192595e-27
C = 299792458.0
B = 1.0
KICK_EV = 10000.0


def model(n):
    kinetic_j = np.asarray(n) * KICK_EV * E_CHARGE
    radius_classical = np.sqrt(2 * PROTON_MASS * kinetic_j) / (E_CHARGE * B)
    radius_relativistic = np.sqrt(kinetic_j * (kinetic_j + 2 * PROTON_MASS * C**2)) / (E_CHARGE * B * C)
    coast_error_deg = 180 * kinetic_j / (PROTON_MASS * C**2)
    cumulative_deg = 180 * KICK_EV * E_CHARGE / (PROTON_MASS * C**2) * np.asarray(n) * (np.asarray(n) + 1) / 2
    return kinetic_j / E_CHARGE / 1e6, radius_classical, radius_relativistic, coast_error_deg, cumulative_deg


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    n = np.arange(201)
    energy, rc, rr, step, total = model(n)
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.8), dpi=130)
    axes[0].plot(energy, rc * 100, label='Classical', lw=2.6, c='#286d9f')
    axes[0].plot(energy, rr * 100, '--', label='Relativistic', lw=1.5, c='#be5d29')
    axes[0].set_ylabel('Curvature radius (cm)')
    axes[0].set_title('Larger orbit', fontsize=13)
    axes[0].legend(frameon=False, loc='lower right', fontsize=10)
    axes[0].annotate('Curves nearly overlap\nat these energies', (1.15, 15.5), (0.45, 5),
                     arrowprops={'arrowstyle': '->'}, fontsize=9)
    axes[1].plot(energy, step, c='#26846b', lw=2)
    axes[1].set_ylabel('Excess drive phase per half-turn (degrees)')
    axes[1].set_title('Small error per coast', fontsize=13)
    axes[2].plot(energy, total, c='#9c437c', lw=2)
    axes[2].set_ylabel('Accumulated excess phase (degrees)')
    axes[2].set_title('Many coasts add up', fontsize=13)
    values = (rc[100] * 100, step[100], total[100])
    labels = ('14.450 cm', '0.19184°', '9.688° after 100 coasts')
    for ax, value, label in zip(axes, values, labels):
        ax.scatter([1], [value], c='#202a34', s=27, zorder=4)
        ax.axvline(1, ls=':', c='#7d8790', lw=1)
        ax.annotate(label, (1, value), (0.1, 0.82), textcoords='axes fraction', fontsize=10,
                    arrowprops={'arrowstyle': '->', 'color': '#56616b'})
        ax.set_xlabel('Kinetic energy (MeV)')
        ax.set_xlim(0, 2)
        ax.grid(alpha=0.2)
    fig.suptitle('Chosen proton model: B = 1 T, prescribed 10 keV kicks', fontsize=16, y=0.98)
    fig.text(0.5, 0.08, r'$K_j=j\epsilon$, $\delta\phi_j=\pi K_j/(mc^2)$, $\Phi_N=\pi\epsilon N(N+1)/(2mc^2)$', ha='center', fontsize=12)
    fig.text(0.5, 0.025, 'Phase is summed after each post-kick coast • ideal ramp omits phase feedback • calculated values, not historical data', ha='center', fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.27, top=0.83, wspace=0.53)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
