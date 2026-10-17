"""Independent Hill responses and trajectories; Python 3.14/matplotlib 3.10.7.

Write paper-3-single-gene.png to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def hill(u, K, n):
    u = np.asarray(u)
    return u**n / (K**n + u**n)


def rhs(s, X):
    Y, Z = s
    return np.array([2*hill(X, 1, 2)-Y, 3*hill(X, 2, 4)-Z])


def integrate(f, initial, times):
    out = np.empty((len(times), len(initial)))
    out[0] = initial
    for j, dt in enumerate(np.diff(times)):
        s = out[j]
        k1 = f(s)
        k2 = f(s+dt*k1/2)
        k3 = f(s+dt*k2/2)
        k4 = f(s+dt*k3)
        out[j+1] = s + dt*(k1+2*k2+2*k3+k4)/6
    return out


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)
    X = np.linspace(0, 5, 501)
    axes[0].plot(X, 2*hill(X, 1, 2), label=r'$Y^*: K=1,\ n=2$', color='#176b9c')
    axes[0].plot(X, 3*hill(X, 2, 4), label=r'$Z^*: K=2,\ n=4$', color='#c05526')
    axes[0].scatter([1,2], [1,1.5], color=['#176b9c','#c05526'], zorder=4)
    axes[0].set(xlabel='Input concentration X', ylabel='Equilibrium concentration', title='Different thresholds and steepness')
    axes[0].legend(loc='lower right')
    t = np.linspace(0, 8, 801)
    for initial, ls in [([0,0], '-'), ([3,4], '--')]:
        out = integrate(lambda s: rhs(s, 2), initial, t)
        exact = np.array([1.6,1.5])+(np.array(initial)-[1.6,1.5])*np.exp(-t[:,None])
        assert np.max(np.abs(out-exact)) < 1e-8
        axes[1].plot(t, out[:,0], ls, color='#176b9c', label=f'Y, initial {initial}')
        axes[1].plot(t, out[:,1], ls, color='#c05526', label=f'Z, initial {initial}')
    axes[1].axhline(1.6, color='#176b9c', alpha=.3, lw=1)
    axes[1].axhline(1.5, color='#c05526', alpha=.3, lw=1)
    axes[1].set(xlabel='Time (inverse degradation-rate units)', ylabel='Concentration', title=r'Both starts converge: $X=2$')
    axes[1].legend(fontsize=8)
    for ax in axes:
        ax.grid(alpha=.18);ax.set_ylim(bottom=0)
    fig.savefig(Path('paper-3-single-gene.png'), dpi=125, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
