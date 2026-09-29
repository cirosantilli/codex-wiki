"""Original hypothetical finite-band model; no measured optical constants.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    wavelength_nm = np.linspace(400, 700, 1601)
    wavelength_m = wavelength_nm * 1e-9
    index = 1.28 + .04*(500/wavelength_nm)**2
    alpha = 1/137.036  # explicitly chosen rounded fine-structure constant
    colors = ['#bf571c', '#007c83', '#6359a5']
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.5), dpi=130, facecolor='white')
    axes[0].plot(wavelength_nm, index, color='#183e66', lw=2.5, label=r'$n(\lambda)$')
    axes[0].axhline(1/.75, color=colors[0], ls='--', label=r'$1/\beta$ for $\beta=0.75$')
    cutoff = 500*np.sqrt(.04/(1/.75-1.28))
    axes[0].axvline(cutoff, color=colors[0], ls=':', lw=1.4)
    axes[0].text(447, 1.337, f'{cutoff:.2f} nm\nthreshold', fontsize=10, color=colors[0])
    for beta, color in zip([.75, .78, .90], colors):
        active = beta*index > 1
        angle = np.full_like(index, np.nan)
        angle[active] = np.degrees(np.arccos(1/(beta*index[active])))
        yield_m2 = 2*np.pi*alpha/wavelength_m**2*np.maximum(0, 1-1/(beta*index)**2)
        # dN/(dx_cm d lambda_nm) = SI density * 1e-2 * 1e-9
        axes[1].plot(wavelength_nm, angle, color=color, lw=2.3, label=rf'$\beta={beta:.2f}$')
        axes[2].plot(wavelength_nm, yield_m2*1e-11, color=color, lw=2.3, label=rf'$\beta={beta:.2f}$')
    axes[0].set_ylabel('Refractive index (dimensionless)')
    axes[1].set_ylabel('Emission angle to track (degrees)')
    axes[2].set_ylabel(r'Produced photons / (cm $\cdot$ nm)')
    for ax, title in zip(axes, ['Index and onset', 'Allowed directions', 'Frank–Tamm spectrum, z = 1']):
        ax.set_title(title, fontsize=12)
        ax.set_xlabel('Vacuum wavelength (nm)')
        ax.set_xlim(400, 700)
        ax.grid(alpha=.23)
        ax.legend(fontsize=9, frameon=False, loc='best')
    axes[1].set_ylim(0, 40)
    axes[2].set_ylim(bottom=0)
    fig.suptitle(r'Chosen model: $n(\lambda)=1.28+0.04(500\,\mathrm{nm}/\lambda)^2$', fontsize=15)
    fig.text(.5, .02,
             '400–700 nm only; constant particle speed; no absorption or collection losses; calculated emission, not observed glow',
             ha='center', fontsize=10)
    fig.tight_layout(rect=(0, .06, 1, .91), w_pad=2)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
