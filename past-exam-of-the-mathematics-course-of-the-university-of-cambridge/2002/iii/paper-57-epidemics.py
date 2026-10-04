"""Farm-size epidemic comparison; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the desired output directory; writes only paper-57-epidemics.png.
MPLCONFIGDIR, if set by the caller, is left unchanged.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = np.array([1., 3.])
P = np.array([.5, .5])
DT = .01
T = np.arange(0., 35. + DT / 2., DT)


def solve(case, homogeneous=False):
    n = np.array([2.]) if homogeneous else N
    p = np.array([1.]) if homogeneous else P
    susceptibility = n if case != 'b' else np.ones_like(n)
    infectiousness = n if case != 'a' else np.ones_like(n)
    beta = .5 if case == 'c' else 1.
    k = len(n)
    state = np.r_[.999 * p, .001 * p, np.zeros(k)]
    result = np.empty((len(T), 3 * k))
    def rhs(z):
        s, i = z[:k], z[k:2*k]
        incidence = beta * susceptibility * s * np.dot(infectiousness, i)
        return np.r_[-incidence, incidence - i, i]
    for j in range(len(T)):
        result[j] = state
        if j + 1 < len(T):
            a = rhs(state)
            b = rhs(state + DT*a/2)
            c = rhs(state + DT*b/2)
            d = rhs(state + DT*c)
            state += DT*(a+2*b+2*c+d)/6
    s, i = result[:, :k], result[:, k:2*k]
    return result, i.sum(axis=1), (s @ n)/s.sum(axis=1), (i @ n)/i.sum(axis=1)


def main():
    fig, axes = plt.subplots(2, 3, figsize=(11.8, 6.2), sharex=True, facecolor='white')
    titles = ['(a) Size-dependent susceptibility', '(b) Size-dependent infectivity', '(c) Both size-dependent']
    for j, case in enumerate('abc'):
        _, prevalence, susceptible_mean, infected_mean = solve(case)
        _, homogeneous, _, _ = solve(case, True)
        axes[0, j].plot(T, prevalence, color='#185b90', label='Heterogeneous farms', lw=2)
        axes[0, j].plot(T, homogeneous, color='#ce7522', label='Homogeneous comparison', lw=1.8, ls='--')
        axes[0, j].set_title(titles[j], fontsize=10)
        axes[1, j].plot(T, susceptible_mean, color='#247841', label='Susceptible farms', lw=2)
        axes[1, j].plot(T, infected_mean, color='#96367f', label='Infected farms', lw=2)
        axes[1, j].axhline(2., color='#777777', label='Population mean', ls=':', lw=1.5)
        axes[1, j].set_xlabel('Time (mean infectious periods)')
        for ax in axes[:, j]:
            ax.set_facecolor('white')
            ax.grid(alpha=.2)
            ax.set_xlim(0, 35)
        axes[0, j].set_ylim(0, .23)
        axes[1, j].set_ylim(.95, 2.65)
    axes[0, 0].set_ylabel('Fraction of farms infected')
    axes[1, 0].set_ylabel('Mean livestock count')
    axes[0, 0].legend(fontsize=8)
    axes[1, 0].legend(fontsize=8)
    fig.suptitle('Equally many farms with 1 or 3 animals; homogeneous reproduction number 2', fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .95))
    fig.savefig(Path.cwd() / 'paper-57-epidemics.png', dpi=110, facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
