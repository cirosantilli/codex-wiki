"""Draw impedance geometry and normalized timing; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def main():
    resistance, capacitance, frequency = 100.0, 1e-6, 1000.0
    omega = 2 * np.pi * frequency
    reactance = -1 / (omega * capacitance)
    impedance = resistance + 1j * reactance
    phase = np.angle(impedance)
    delay_ms = -phase / omega * 1000
    blue, orange, green, purple = '#1565a8', '#c55d14', '#247650', '#8a4395'
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12, 'figure.facecolor': 'white'})
    fig, (geometry, timing) = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={'width_ratios': [1, 1.45]})
    fig.subplots_adjust(left=.08, right=.975, bottom=.16, top=.79, wspace=.39)
    fig.suptitle('Impedance geometry and the corresponding phase delay', fontsize=15, y=.965)
    fig.text(.5, .875, r'Ideal series RC: $R=100\ \Omega$, $C=1\ \mu\mathrm{F}$, $f=1000\ \mathrm{Hz}$', ha='center')
    geometry.axhline(0, color='.55', lw=.8)
    geometry.axvline(0, color='.55', lw=.8)
    geometry.annotate('', (resistance, reactance), (0, 0), arrowprops={'arrowstyle': '-|>', 'lw': 2.7, 'color': blue})
    geometry.annotate('', (resistance, 0), (0, 0), arrowprops={'arrowstyle': '-|>', 'lw': 2.4, 'color': green})
    geometry.annotate('', (resistance, reactance), (resistance, 0), arrowprops={'arrowstyle': '-|>', 'lw': 2.4, 'color': purple})
    geometry.plot([0, resistance], [reactance, reactance], ':', color='.65')
    geometry.add_patch(Arc((0, 0), 62, 62, theta1=np.degrees(phase), theta2=0, color=blue, lw=1.5))
    geometry.text(35, -27, r'$\phi=-57.858^\circ$', color=blue, fontsize=10)
    geometry.text(45, 13, r'$R=100\ \Omega$', color=green, ha='center')
    geometry.text(111, -70, r'$X=-159.155\ \Omega$', color=purple, rotation=90, va='center', fontsize=10)
    geometry.text(8, -133, r'$|Z|=187.964\ \Omega$', color=blue, rotation=0, fontsize=10)
    geometry.scatter([resistance], [reactance], color=blue, s=24, zorder=5)
    geometry.set(xlim=(-22, 142), ylim=(-187, 31), xlabel=r'Real part ($\Omega$)', ylabel=r'Imaginary part ($\Omega$)', title='One complex number: magnitude and angle')
    geometry.set_aspect('equal', adjustable='box')
    geometry.set_xticks([0, 50, 100]); geometry.set_yticks([-150, -100, -50, 0])
    t_ms = np.linspace(-.25, 1.1, 900)
    current = np.cos(omega * t_ms / 1000)
    voltage = np.cos(omega * t_ms / 1000 + phase)
    timing.plot(t_ms, current, color=orange, lw=2.3, label=r'$i(t)/I_{\mathrm{peak}}=\cos\omega t$')
    timing.plot(t_ms, voltage, color=blue, lw=2.3, label=r'$v(t)/V_{\mathrm{peak}}=\cos(\omega t+\phi)$')
    timing.axhline(0, color='.65', lw=.8)
    for peak, color in [(0, orange), (delay_ms, blue)]:
        timing.plot([peak, peak], [.98, 1.30], '--', color=color, lw=1)
    timing.annotate('', (delay_ms, 1.25), (0, 1.25), arrowprops={'arrowstyle': '<->', 'color': '.25', 'lw': 1.3})
    timing.text(.41, 1.21, f'Current peak comes first\nSeparation: {delay_ms:.6f} ms', va='center', fontsize=10)
    timing.set(xlim=(-.25, 1.1), ylim=(-1.15, 1.44), xlabel='Time (ms)', ylabel='Signal divided by its own peak magnitude', title='Current leads voltage; amplitudes normalized')
    timing.set_yticks([-1, 0, 1]); timing.grid(alpha=.16)
    timing.legend(loc='lower right', fontsize=9, framealpha=1)
    for ax in [geometry, timing]:
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
