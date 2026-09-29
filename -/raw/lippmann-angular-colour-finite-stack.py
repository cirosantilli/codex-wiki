"""Plot calculated Lippmann angular selection and weak finite-grating spectra.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7. Run from _media.
No measured data. Identical weak planes; constant refractive index; no absorption.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def peak_nm(alpha_deg, n=1.5, d_nm=200):
    return 2*n*d_nm*np.sqrt(1-(np.sin(np.deg2rad(alpha_deg))/n)**2)


def normalized_response(wavelength_nm, planes, alpha_deg=0):
    # Direct complex sum avoids removable singularities of the sine quotient.
    delta = 2*np.pi*(peak_nm(alpha_deg)/np.asarray(wavelength_nm)-1)
    return np.abs(np.exp(1j*np.arange(planes)[:, None]*delta).mean(axis=0))**2


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout='constrained')
    angles = np.linspace(0, 70, 400)
    ax = axes[0]
    ax.plot(angles, peak_nm(angles), color='#a5422b', lw=2, label='Unchanged spacing: d = 200 nm')
    ax.plot(angles, .95*peak_nm(angles), color='#805ca5', lw=2, ls='--', label='Chosen shrinkage: d = 190 nm')
    for angle in [0, 30, 45]:
        peak = peak_nm(angle)
        ax.scatter([angle], [peak], color='#a5422b', s=22, zorder=4)
        ax.annotate(f'{peak:.2f}', (angle, peak), (6, 9), textcoords='offset points', fontsize=9)
    ax.set(xlim=(-2, 72), ylim=(435, 625), xlabel='External readout angle in air (degrees)',
           ylabel='Selected vacuum wavelength (nm)', title='Angular shift and shrinkage')
    ax.legend(loc='lower left', frameon=False, fontsize=9)
    ax.grid(alpha=.2)
    ax = axes[1]
    wavelengths = np.linspace(440, 730, 6001)
    for planes, angle, color, style in [(10, 0, '#709a73', '--'),
                                       (30, 0, '#a5422b', '-'),
                                       (30, 45, '#216c9e', '-')]:
        ax.plot(wavelengths, normalized_response(wavelengths, planes, angle),
                color=color, ls=style, lw=1.8, label=f'N = {planes}, external angle {angle}°')
    ax.set(xlim=(440, 730), ylim=(0, 1.12), xlabel='Vacuum wavelength (nm)',
           ylabel=r'Normalized reflectance shape $F_N$', title='Finite weak stack: all curves calculated')
    ax.legend(loc='upper right', frameon=False, fontsize=9)
    ax.grid(alpha=.2)
    fig.suptitle('Illustrative Lippmann readout model · constant n = 1.5', fontsize=13)
    fig.savefig(Path(__file__).stem+'.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
