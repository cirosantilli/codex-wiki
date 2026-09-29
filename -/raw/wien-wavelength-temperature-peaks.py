"""Plot ideal wavelength peaks; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../wien-wavelength-temperature-peaks.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

H = 6.62607015e-34
C = 299792458.0
K = 1.380649e-23
X = 4.965114231744276
B = H * C / (K * X)


def normalized_spectrum(wavelength, temperature):
    x = H * C / (wavelength * K * temperature)
    return (x / X) ** 5 * np.expm1(X) / np.expm1(np.minimum(x, 700))


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.2), layout='constrained')
    wavelength = np.geomspace(0.15, 80, 1600)
    temperatures = [300, 1000, 5000]
    colors = ['#197686', '#b55a16', '#7143a3']
    for temperature, color in zip(temperatures, colors):
        peak = B / temperature * 1e6
        left.plot(wavelength, normalized_spectrum(wavelength * 1e-6, temperature),
                  color=color, label=f'{temperature} K: {peak:.3f} μm', lw=2)
        left.plot(peak, 1, 'o', color=color)
        right.plot(temperature, peak, 'o', color=color, zorder=4)
        right.annotate(f'{temperature} K\n{peak:.3f} μm', (temperature, peak),
                       xytext=(8, 5), textcoords='offset points', fontsize=10)
    left.set(xscale='log', xlim=(0.15, 80), ylim=(0, 1.42),
             xlabel='Wavelength λ (μm)', ylabel='Bλ / its own peak value',
             title='The shape shifts as temperature changes')
    left.legend(loc='upper right', fontsize=9, frameon=False)
    t = np.geomspace(150, 12000, 400)
    right.plot(t, B / t * 1e6, color='#34495e', lw=2)
    right.set(xscale='log', yscale='log', xlim=(150, 12000), ylim=(0.18, 25),
              xlabel='Temperature T (K)', ylabel='Wavelength peak λmax (μm)',
              title='λmax T = 2897.772 μm K')
    for ax in (left, right):
        ax.grid(alpha=0.18, which='both')
    fig.savefig(Path(__file__).stem + '.png', dpi=130, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
