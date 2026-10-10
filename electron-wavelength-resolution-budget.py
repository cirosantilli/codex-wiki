"""Original wavelength / heuristic blur model, not instrument measurements.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
All blur terms are defined in optics.bigb; no measured parameters are fitted.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

H = 6.62607015e-34
E = 1.602176634e-19
M = 9.1093837e-31
C = 299792458.


def wavelength(volts):
    energy = E*np.asarray(volts)
    return H/np.sqrt(2*M*energy*(1+energy/(2*M*C*C)))


def blur_terms(alpha):
    lam = wavelength(100000.)
    diffraction = .61*lam/alpha
    spherical = 1e-3*alpha**3
    chromatic = 1e-3*alpha*(.7/100000.)
    residual = np.full_like(alpha, 1e-10)
    total = np.sqrt(diffraction**2+spherical**2+chromatic**2+residual**2)
    return diffraction, spherical, chromatic, residual, total


def main():
    plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.4), dpi=110, facecolor='white')
    fig.subplots_adjust(left=.075, right=.97, bottom=.30, top=.79, wspace=.29)
    ax = axes[0]
    voltage = np.geomspace(20, 300, 400)
    ax.plot(voltage, wavelength(voltage*1000)*1e12, color='#176c9e', linewidth=2.2)
    for kv, offset in [(30, (9, 4)), (100, (-8, 13)), (300, (-65, 13))]:
        pm = float(wavelength(kv*1000)*1e12)
        ax.plot(kv, pm, 'o', color='#176c9e', markersize=5)
        ax.annotate(f'{kv} kV: {pm:.3f} pm', (kv, pm), xytext=offset,
                    textcoords='offset points', fontsize=10)
    ax.set(xlabel='Accelerating voltage U (kV)', ylabel='Electron wavelength λ (pm)',
           xlim=(20, 325), ylim=(1.3, 9.5), title='Relativistic de Broglie relation')
    ax.grid(alpha=.2)
    ax = axes[1]
    alpha = np.geomspace(.0005, .03, 700)
    terms = blur_terms(alpha)
    for values, label, color, style in zip(
        terms,
        ['Ideal diffraction', 'Assumed spherical blur', 'Assumed chromatic blur',
         'Assumed residual blur', 'Quadrature model total'],
        ['#176c9e', '#c0582c', '#307d46', '#888888', '#202a32'],
        ['-', '-', '-', ':', '-']):
        ax.loglog(alpha*1000, values*1e9, label=label, color=color,
                  linestyle=style, linewidth=2.4 if label.endswith('total') else 1.7)
    a = .61*float(wavelength(100000.))
    s, t = 1e-3, 1e-3*.7/100000.
    # Exact minimizer of a²/α² + s²α⁶ + t²α² + b0², in the declared model.
    alpha_opt = (2*a*a/(np.sqrt(t**4+12*s*s*a*a)+t*t))**.25
    b_opt = float(blur_terms(np.array([alpha_opt]))[-1][0])
    ax.plot(alpha_opt*1000, b_opt*1e9, 'o', color='#202a32', markersize=5)
    ax.annotate(f'Model minimum\n{alpha_opt*1000:.2f} mrad, {b_opt*1e9:.3f} nm',
                (alpha_opt*1000, b_opt*1e9), xytext=(1.1, 4), textcoords='data',
                fontsize=10, bbox={'facecolor':'white', 'edgecolor':'none', 'pad':2},
                arrowprops={'arrowstyle':'->', 'color':'#202a32'})
    ax.set(xlabel='Aperture semi-angle α (mrad)', ylabel='Characteristic image scale (nm)',
           xlim=(.5, 30), ylim=(.01, 40), title='100 kV: aperture and assumed blur')
    ax.grid(which='both', alpha=.15)
    ax.legend(loc='upper left', bbox_to_anchor=(0, -.25), fontsize=9, ncol=2,
              frameon=False, columnspacing=1, handlelength=2)
    fig.suptitle('A short wavelength permits detail; lens blur can still hide it', y=.96, fontsize=16)
    fig.text(.5, .865, r'Chosen model: $C_s=C_c=1$ mm, $\Delta K=0.7$ eV, $b_0=0.10$ nm',
             ha='center', fontsize=11, color='#4c5964')
    fig.text(.25, .10, 'Calculated points; negligible starting energy.\nNo measurements or performance specifications.',
             ha='center', fontsize=10, color='#4c5964')
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
