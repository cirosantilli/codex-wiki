"""Draw impedance locus, modulus and phase; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    resistance, capacitance = 100.0, 1e-6
    frequencies = np.geomspace(100, 100000, 700)
    impedances = resistance - 1j / (2 * np.pi * frequencies * capacitance)
    crossover = 1 / (2 * np.pi * resistance * capacitance)
    blue, orange, green = '#1565a8', '#c55d14', '#247650'
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10.4, 5.3))
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.65], left=.12, right=.97, bottom=.18, top=.79, wspace=.43, hspace=.36)
    locus = fig.add_subplot(grid[:, 0]); magnitude = fig.add_subplot(grid[0, 1]); phase = fig.add_subplot(grid[1, 1], sharex=magnitude)
    fig.suptitle('How the ideal series RC impedance changes with frequency', fontsize=15, y=.97)
    fig.text(.5, .885, r'$R=100\ \Omega$, $C=1\ \mu\mathrm{F}$: predictions of the stipulated model', ha='center')
    locus.axhline(0, color='.5', lw=1)
    locus.plot(impedances.real, impedances.imag, color=blue, lw=2.5)
    locus.annotate('', (100, -500), (100, -950), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': 2.5})
    locus.text(113, -730, 'Increasing\nfrequency', color=blue, va='center')
    locus.scatter([100], [0], marker='o', s=48, facecolor='white', edgecolor=green, lw=1.7, zorder=5)
    locus.text(110, 48, r'$Z\to R$', color=green, fontsize=11)
    samples = [(100, '100 Hz', blue), (1000, '1000 Hz', orange), (crossover, r'$f_*$', green)]
    for f, label, color in samples:
        z = resistance - 1j / (2 * np.pi * f * capacitance)
        locus.scatter([z.real], [z.imag], color=color, s=40, zorder=6)
        if f == 100:
            locus.text(87, z.imag, label, ha='right', va='center', color=color)
        elif f == 1000:
            locus.annotate(label, (z.real, z.imag), xytext=(22, -355), color=color, arrowprops={'arrowstyle': '-', 'color': color})
        else:
            locus.annotate(label, (z.real, z.imag), xytext=(42, -48), color=color, arrowprops={'arrowstyle': '-', 'color': color})
        magnitude.scatter([f], [abs(z)], color=color, s=32, zorder=6)
        phase.scatter([f], [np.degrees(np.angle(z))], color=color, s=32, zorder=6)
    locus.set(xlim=(0, 190), ylim=(-1750, 190), xlabel=r'Real part ($\Omega$)', ylabel=r'Imaginary part ($\Omega$)', title='Locus: fixed real part')
    locus.set_xticks([0, 100]); locus.set_yticks([-1500, -1000, -500, 0])
    fig.text(.12, .025, 'Locus axes use different scales; the entire locus is vertical.', fontsize=9, color='.35')
    magnitude.loglog(frequencies, np.abs(impedances), color=blue, lw=2.3)
    magnitude.axhline(resistance, color=green, ls='--', lw=1)
    magnitude.text(14000, 122, r'$|Z|\to100\ \Omega$', color=green, fontsize=10)
    magnitude.annotate(r'$\sqrt{2}R$ at $f_*$', (crossover, np.sqrt(2)*resistance), xytext=(3300, 420), color=green, arrowprops={'arrowstyle': '->', 'color': green}, fontsize=10)
    magnitude.set(ylabel=r'$|Z|$ ($\Omega$)', ylim=(85, 2200), title='Magnitude and signed phase of impedance')
    magnitude.tick_params(labelbottom=False)
    phase.semilogx(frequencies, np.degrees(np.angle(impedances)), color=blue, lw=2.3)
    phase.axhline(-45, color=green, ls=':', lw=1)
    phase.text(8000, -57, r'$\phi=-45^\circ$ at $f_*$', color=green, fontsize=10)
    phase.text(220, -31, '1000 Hz: −57.858°', color=orange, fontsize=10)
    phase.set(xlim=(100, 100000), ylim=(-93, 3), xlabel='Frequency (Hz)', ylabel=r'$\phi$ (degrees)', yticks=[-90, -45, 0])
    for ax in [magnitude, phase]:
        ax.axvline(crossover, color=green, ls=':', lw=1)
        ax.grid(alpha=.16)
    for ax in [locus, magnitude, phase]:
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
