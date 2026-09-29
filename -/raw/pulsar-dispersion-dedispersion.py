"""Original cold-plasma delay model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media. All signals are synthetic, noiseless, and deliberately chosen.
Delay = D [(f / 100 MHz)^-2 - (150 MHz / 100 MHz)^-2], D = 0.24 s.
No historical measurements, SciPy, or deconvolution are used.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

D = .24
PERIOD = 1.4
SIGMA = .025


def delay(f_mhz):
    return D * ((np.asarray(f_mhz) / 100) ** -2 - (150 / 100) ** -2)


def signal(t):
    return sum(np.exp(-.5 * ((t - peak) / SIGMA) ** 2) for peak in [.35, .35 + PERIOD])


def model():
    t = np.linspace(0, 2.4, 4801)
    freq = np.linspace(80, 150, 141)
    raw = signal(t[None, :] - delay(freq)[:, None])
    # Inverse time shift: corrected(f,t) = raw(f,t + delay(f)). Evaluate
    # the continuous model to avoid interpolation artifacts or finite-window padding.
    corrected = signal(t[None, :] + delay(freq)[:, None] - delay(freq)[:, None])
    return t, freq, raw, corrected


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    t, freq, raw, corrected = model()
    fig = plt.figure(figsize=(10, 7.2), facecolor='white', layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.1])
    for col, values, title in [(0, raw, 'Before: low frequencies arrive later'), (1, corrected, 'After: channel delays subtracted')]:
        ax = fig.add_subplot(gs[0, col])
        ax.pcolormesh(t, freq, values, shading='auto', cmap='Blues', vmin=0, vmax=1, rasterized=True)
        ax.set(xlim=(.15, .85), xlabel='Time relative to chosen origin (s)', ylabel='Frequency (MHz)', title=title)
        ax.set_yticks([80, 100, 125, 150])
    ax = fig.add_subplot(gs[1, :])
    ax.plot(t, raw.mean(axis=0), color='#a04d10', lw=2, label='Average before alignment')
    ax.plot(t, corrected.mean(axis=0), color='#26718f', lw=2, label='Average after alignment')
    ax.set(xlim=(.15, .85), ylim=(-.03, 1.12), xlabel='Time relative to chosen origin (s)', ylabel='Mean signal (arbitrary units)', title='Align before averaging to preserve a narrow pulse')
    ax.legend(loc='upper right', frameon=False, fontsize=10)
    ax.text(.98, .55, 'Chosen model\nD = 0.24 s\nP = 1.4 s\nGaussian width σ = 0.025 s', transform=ax.transAxes, ha='right', va='center', fontsize=10)
    fig.suptitle('Dispersion and dedispersion: synthetic example', fontsize=16)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
