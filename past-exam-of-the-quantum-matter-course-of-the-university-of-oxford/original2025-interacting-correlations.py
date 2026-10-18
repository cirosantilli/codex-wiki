"""Python 3.14, NumPy and Matplotlib; write same-basename PNG to Path.cwd()."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2025-quantum-matter-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def radial_gp(coupling=100 * np.pi, dr=.0125, rmax=9.):
    """Cell-centred radial finite volumes; hbar=m=omega=1, integral |phi|^2=1."""
    r = (np.arange(round(rmax / dr)) + .5) * dr
    weights = 2 * np.pi * r * dr
    lower = -.5 * (r - dr / 2) / (r * dr ** 2)
    upper = -.5 * (r + dr / 2) / (r * dr ** 2)
    diag = -lower - upper
    potential = r ** 2 / 2
    phi = np.sqrt(np.maximum(np.sqrt(coupling / np.pi) - potential, 1e-8) / coupling)
    phi /= np.sqrt(np.dot(weights, phi ** 2))
    dt = .025
    for iteration in range(8000):
        b = 1 + dt * (diag + potential + coupling * phi ** 2)
        rhs = phi.copy()
        for i in range(1, len(r)):
            factor = dt * lower[i] / b[i - 1]
            b[i] -= factor * dt * upper[i - 1]
            rhs[i] -= factor * rhs[i - 1]
        new = np.empty_like(phi)
        new[-1] = rhs[-1] / b[-1]
        for i in range(len(r) - 2, -1, -1):
            new[i] = (rhs[i] - dt * upper[i] * new[i + 1]) / b[i]
        new /= np.sqrt(np.dot(weights, new ** 2))
        change = np.sqrt(np.dot(weights, (new - phi) ** 2))
        phi = new
        if change < 2e-12:
            break
    hphi = (diag + potential + coupling * phi ** 2) * phi
    hphi[1:] += lower[1:] * phi[:-1]
    hphi[:-1] += upper[:-1] * phi[1:]
    mu = np.dot(weights, phi * hphi)
    residual = np.sqrt(np.dot(weights, (hphi - mu * phi) ** 2))
    assert residual < 1e-7, (iteration, change, residual)
    return r, phi, {'mu': float(mu), 'residual': float(residual), 'iterations': iteration + 1,
                    'normalization': float(np.dot(weights, phi ** 2)), 'dr': dr}


def main():
    out = Path.cwd()
    coupling = 100 * np.pi
    r, phi, info = radial_gp(coupling)
    # Quadratic extrapolation in r at the regular origin.
    phi0 = (9 * phi[0] - phi[1]) / 8
    mu_tf = np.sqrt(coupling / np.pi)
    radius = np.sqrt(2 * mu_tf)
    s = np.concatenate(([0.], r / radius))
    gp = coupling / mu_tf * phi0 * np.concatenate(([phi0], phi))
    tf = np.sqrt(np.maximum(1 - s ** 2, 0))
    fig, axes = plt.subplots(1, 2, figsize=(9.3, 3.7), layout='constrained')
    axes[0].plot(s, tf, color='#e07a24', ls='--', lw=2, label='Thomas–Fermi')
    axes[0].plot(s, gp, color='#126782', lw=2, label='Full radial GP')
    axes[0].axvline(1, color='.7', ls=':', lw=1)
    axes[0].set(xlim=(0, 1.4), ylim=(0, 1.1), xlabel=r'$r/R_{\rm TF}$',
                ylabel=r'$G(r)/(\mu_{\rm TF}/g)$', title='Kinetic energy smooths the edge')
    axes[0].legend(frameon=False, fontsize=9)
    broad = gp / gp[0]
    # These illustrative weights are not a Bogoliubov calculation.
    depletion_weight = .12
    short = depletion_weight * np.exp(-.5 * (s / .065) ** 2)
    sketch = (1 - depletion_weight) * broad + short
    axes[1].plot(s, broad, color='#126782', lw=2, label='GP, normalized at centre')
    axes[1].plot(s, sketch, color='#a62f5b', lw=2, label='With depletion (schematic)')
    axes[1].plot(s, short, color='.45', ls=':', lw=1.5, label='Short-range contribution')
    axes[1].set(xlim=(0, 1.4), ylim=(0, 1.1), xlabel=r'$r/R_{\rm TF}$',
                ylabel=r'$G(r)/G(0)$', title='Depletion changes mode occupations')
    axes[1].legend(frameon=False, fontsize=8, loc='upper right')
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(out / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)
    print(info)


if __name__ == '__main__':
    main()
