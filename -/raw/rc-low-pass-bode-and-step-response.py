"""Plot original ideal RC predictions; emit PNG into the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    resistance, capacitance = 2200.0, 47e-9
    tau = resistance * capacitance
    fc = 1 / (2 * np.pi * tau)
    blue, orange, gray = '#146eaa', '#b56c0b', '#657382'
    fig = plt.figure(figsize=(10.2, 6.0), dpi=110, facecolor='white')
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.15])
    gain = fig.add_subplot(grid[0, 0])
    phase = fig.add_subplot(grid[1, 0], sharex=gain)
    step = fig.add_subplot(grid[:, 1])
    frequencies = np.geomspace(fc / 100, fc * 100, 600)
    ratio = frequencies / fc
    gain.semilogx(frequencies / 1000, -10 * np.log10(1 + ratio**2), color=blue, lw=2.5)
    gain.scatter([fc / 1000], [-10 * np.log10(2)], color=blue, zorder=3)
    gain.annotate('−3.01 dB', xy=(fc / 1000, -10 * np.log10(2)),
                  xytext=(fc / 1000 * 2.6, -9), fontsize=11,
                  arrowprops={'arrowstyle': '-', 'color': gray})
    gain.set(ylabel='Voltage gain (dB)', ylim=(-42, 2), title='Frequency response')
    gain.tick_params(labelbottom=False)
    phase.semilogx(frequencies / 1000, -np.degrees(np.arctan(ratio)), color=blue, lw=2.5)
    phase.scatter([fc / 1000], [-45], color=blue, zorder=3)
    phase.annotate('−45°', xy=(fc / 1000, -45), xytext=(fc / 1000 * 3, -39),
                   arrowprops={'arrowstyle': '-', 'color': gray}, fontsize=11)
    phase.set(xlabel='Frequency (kHz)', ylabel='Output − input phase (°)', ylim=(-94, 3),
              yticks=[-90, -45, 0])
    for ax in (gain, phase):
        ax.axvline(fc / 1000, color=gray, linestyle=':', lw=1.4)
        ax.grid(True, alpha=.23)
        ax.set_xlim(frequencies[0] / 1000, frequencies[-1] / 1000)
    phase.text(.03, .05, f'Corner: {fc / 1000:.4f} kHz', transform=phase.transAxes, fontsize=11)

    times = np.linspace(0, 1100e-6, 600)
    step.plot([-70, 0, 0, 1100], [0, 0, 3, 3], color=gray, linestyle='--', lw=1.6,
              label='Input step')
    step.plot(times * 1e6, 3 * (-np.expm1(-times / tau)), color=blue, lw=2.5,
              label='C = 47 nF')
    step.plot(times * 1e6, 3 * (-np.expm1(-times / (2 * tau))), color=orange, lw=2.5,
              label='C = 94 nF')
    step.scatter([tau * 1e6], [3 * (1 - np.exp(-1))], color=blue, zorder=3)
    step.annotate('63.2% at 103.4 µs', xy=(tau * 1e6, 3 * (1 - np.exp(-1))),
                  xytext=(220, 1.6), arrowprops={'arrowstyle': '-', 'color': gray}, fontsize=11)
    for scale, color in ((1, blue), (2, orange)):
        settling = scale * tau * np.log(100) * 1e6
        step.plot([settling, settling], [0, 2.97], color=color, linestyle=':', lw=1.2)
        step.scatter([settling], [2.97], color=color, zorder=3)
    step.axhline(2.97, color=gray, lw=1, linestyle=':')
    step.text(540, 2.77, '99% level', fontsize=11, color=gray)
    step.text(450, .55, '1% settling:\n476.2 µs → 952.3 µs', fontsize=12, color=gray)
    step.set(xlabel='Time since step (µs)', ylabel='Voltage (V)',
             xlim=(-70, 1100), ylim=(-.12, 3.23), title='Step response and slower smoothing')
    step.grid(True, alpha=.23)
    step.legend(loc='lower right', fontsize=11)
    fig.suptitle('One RC time constant sets both bandwidth and settling', fontsize=17, y=.98)
    fig.text(.5, .018, 'Ideal model: R = 2.2 kΩ, C = 47 nF, τ = 103.4 µs. Analytical curves; no measured data.',
             ha='center', fontsize=11, color=gray)
    fig.subplots_adjust(left=.085, right=.975, top=.88, bottom=.13, wspace=.32, hspace=.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
