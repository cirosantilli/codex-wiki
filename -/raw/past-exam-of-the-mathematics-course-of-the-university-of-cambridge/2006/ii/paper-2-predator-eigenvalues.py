"""Eigenvalue moduli; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Write the PNG basename to caller CWD; respect caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    b = 0.5
    r = np.linspace(1.000001, 3.2, 1200)
    n = r*np.log(r)/(r-b)
    tau = 1+b*n/r
    root = np.lib.scimath.sqrt(tau*tau-4*n)
    lo, hi = 1.000001, np.e
    for _ in range(60):
        mid = (lo+hi)/2
        if mid*np.log(mid)/(mid-b) < 1:
            lo = mid
        else:
            hi = mid
    crit = (lo+hi)/2
    fig, ax = plt.subplots(figsize=(7, 4.4), facecolor='white')
    ax.set_facecolor('white')
    ax.plot(r, np.abs((tau+root)/2), label=r'$|\lambda_+|$', lw=2)
    ax.plot(r, np.abs((tau-root)/2), '--', label=r'$|\lambda_-|$', lw=2)
    ax.axhline(1, color='black', lw=1)
    ax.axvline(crit, color='0.5', ls=':', label=r'$r_*$')
    ax.set(xlabel=r'$r$', ylabel='Eigenvalue modulus', ylim=(0, 1.35),
           title=r'Discrete predator-prey stability, $b=1/2$')
    ax.legend()
    fig.tight_layout()
    fig.savefig('paper-2-predator-eigenvalues.png', dpi=135, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
