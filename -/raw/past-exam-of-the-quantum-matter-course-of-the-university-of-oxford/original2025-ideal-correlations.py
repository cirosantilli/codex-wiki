"""Python 3.14, NumPy and Matplotlib; write same-basename PNG to Path.cwd()."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2025-quantum-matter-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def correlation(n, temperature, r):
    """hbar=m=omega=ell=1; return G/(N/pi), condensate part and fugacity."""
    b = 1 / temperature
    j = np.arange(1, int(np.ceil(38 / b)) + 1, dtype=float)
    q = np.exp(-j * b)
    excited_trace = q * (2 - q) / (-np.expm1(-j * b)) ** 2
    lo, hi = 0., 1.
    for _ in range(90):
        z = (lo + hi) / 2
        number = z / (1 - z) + np.dot(z ** j, excited_trace)
        if number < n:
            lo = z
        else:
            hi = z
    z = (lo + hi) / 2
    n0 = z / (1 - z)
    assert abs(n0 + np.dot(z ** j, excited_trace) - n) / n < 1e-9
    q2 = q ** 2
    base = np.exp(-r ** 2 / 2)
    exponent = -np.log1p(-q2[:, None]) - r[None, :] ** 2 * (q2 / (1 - q2))[:, None]
    thermal = base * np.sum(z ** j[:, None] * np.expm1(exponent), axis=0) / n
    condensate = n0 / n * base
    return condensate + thermal, condensate, z


def main():
    out = Path.cwd()
    n = 10000
    tc = np.sqrt(6 * n) / np.pi
    r = np.linspace(0, 3.6, 1100)
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.3), layout='constrained')
    axes[0].plot(r, np.exp(-r ** 2 / 2), color='#126782', lw=2)
    axes[0].set(title=r'$T=0$', ylim=(0, 1.04))
    for ax, fraction in zip(axes[1:], (.6, 1.5)):
        total, condensate, z = correlation(n, fraction * tc, r)
        ax.plot(r, total, color='#126782', lw=2, label='Total')
        if fraction < 1:
            ax.plot(r, condensate, color='#e07a24', lw=1.7, ls=':', label='Condensate')
            ax.legend(frameon=False, fontsize=9)
            inset = ax.inset_axes([.45, .42, .5, .29])
            inset.plot(r, total, color='#126782', lw=1.5)
            inset.plot(r, condensate, color='#e07a24', ls=':', lw=1.5)
            inset.set(xlim=(0, .35), ylim=(condensate[0] - .003, total[0] + .003))
            inset.set_title('Central thermal peak', fontsize=8)
            inset.tick_params(labelsize=7)
            inset.spines[['top', 'right']].set_visible(False)
        ax.set(title=rf'$T={fraction:g}T_c$', ylim=(0, 1.05 * total[0]))
    for ax in axes:
        ax.set(xlabel=r'$r/\ell$', ylabel=r'$G(r)/(N/(\pi\ell^2))$', xlim=(0, 3.6))
        ax.spines[['top', 'right']].set_visible(False)
    axes[2].text(.95, .9, 'Enlarged vertical scale', transform=axes[2].transAxes, ha='right', fontsize=9)
    fig.savefig(out / (Path(__file__).stem + '.png'), dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
