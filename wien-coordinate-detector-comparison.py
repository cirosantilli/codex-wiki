"""Compare spectral densities and a generic measurement chain.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

H = 6.62607015e-34
C = 299792458.0
K = 1.380649e-23
T = 5000.0


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10.4, 6.4), layout='constrained')
    grid = fig.add_gridspec(2, 1, height_ratios=[3.5, 1.5])
    ax = fig.add_subplot(grid[0])
    wavelength = np.linspace(0.18, 2.6, 1800)
    x = H * C / (wavelength * 1e-6 * K * T)
    curves = [(5, 4.965114231744276, '#7143a3', 'Energy per wavelength: Bλ', '-'),
              (4, 3.920690394872886, '#b55a16', 'Photon counts per wavelength: λBλ / hc', '--'),
              (3, 2.821439372122079, '#197686', 'Energy per frequency: Bν(c/λ)', '-.')]
    for power, root, color, label, style in curves:
        y = (x / root) ** power * np.expm1(root) / np.expm1(x)
        peak = H * C / (K * T * root) * 1e6
        ax.plot(wavelength, y, color=color, lw=2.2, ls=style, label=label)
        ax.plot(peak, 1, 'o', color=color)
        ax.axvline(peak, color=color, alpha=0.35, lw=1, ymax=0.84)
        ax.text(peak, 1.16 if power == 5 else 1.07, f'{peak:.3f} μm', color=color, ha='center', fontsize=10)
    ax.set(xlim=(0.18, 2.6), ylim=(0, 1.24), xlabel='Wavelength λ (μm)',
           ylabel='Each density / its own maximum',
           title='Stipulated 5000 K blackbody: the same radiation, different peaks')
    ax.grid(alpha=0.18)
    ax.legend(loc='upper right', fontsize=9, frameon=False, bbox_to_anchor=(1, 0.85))
    chain = fig.add_subplot(grid[1]); chain.axis('off')
    labels = ['Source\nBλ(T)', 'Slit + disperser\nfinite spectral bin',
              'Detector\nresponse Rᵢ(λ)', 'Readout\nSᵢ − background',
              'Calibration\nfit temperature']
    centers = np.linspace(0.1, 0.9, 5)
    for center, label in zip(centers, labels):
        chain.add_patch(FancyBboxPatch((center - 0.085, 0.47), 0.17, 0.34,
                        boxstyle='round,pad=0.008', edgecolor='#557080',
                        facecolor='#f3f7fa', transform=chain.transAxes))
        chain.text(center, 0.64, label, ha='center', va='center', fontsize=9,
                   transform=chain.transAxes)
    for a, b in zip(centers[:-1], centers[1:]):
        chain.annotate('', xy=(b - 0.09, 0.64), xytext=(a + 0.09, 0.64),
                       arrowprops={'arrowstyle': '->', 'color': '#34495e'},
                       xycoords='axes fraction')
    chain.text(0.5, 0.16, 'Generic linear channel: Sᵢ − Sᵢ,₀ = G ∫ Rᵢ(λ) Bλ(T) dλ',
               ha='center', fontsize=12, transform=chain.transAxes)
    fig.savefig(Path(__file__).stem + '.png', dpi=130, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
