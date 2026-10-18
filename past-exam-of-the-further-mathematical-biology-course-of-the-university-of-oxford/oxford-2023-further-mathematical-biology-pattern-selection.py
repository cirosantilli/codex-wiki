"""Generate dispersion and early-mode sketches in cwd; Python 3.14, NumPy, Matplotlib."""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2023-fmb-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Linear perturbations only; no nonlinear pattern simulation is represented.
db, dn, mu, b0, lam = .002, .04, .5, 2., 2.5
nstar = lam/(mu*(1+b0**2))
eta = lam*(b0**2-1)/(1+b0**2)**2
chis = [.6, .8, 1.5, 3.]
colors = ['#777777', '#2463a4', '#d48228', '#a43c53']
k = np.linspace(0, 40, 1000)
mode = np.arange(1, 17)
km = mode*np.pi
x = np.linspace(0, 1, 800)
def growth(k, chi):
    q = k*k
    coupling = chi*eta/(1+nstar)**2
    return -(1+mu+(db+dn)*q)/2 + np.sqrt((mu-1+(dn-db)*q)**2+4*coupling*q)/2
fig = plt.figure(figsize=(10.5, 6.7), layout='constrained')
grid = fig.add_gridspec(3, 2, height_ratios=[1.4, .75, .75])
ax = fig.add_subplot(grid[0, :])
for chi, color in zip(chis, colors):
    ax.plot(k, growth(k, chi), color=color, lw=1.6, label=rf'$\chi_b={chi:g}$')
    ax.scatter(km[km<=40], growth(km[km<=40], chi), s=13, color=color, zorder=4)
ax.axhline(0, color='black', lw=.8)
ax.set(xlabel='Wavenumber k (dots: allowed k = mπ)', ylabel='Larger growth rate σ₊',
       xlim=(0, 40), ylim=(-1.05, 3.2), title='Increasing chemotaxis changes which spatial mode grows fastest')
ax.legend(loc='upper right', ncol=2)
selected = []
for j, (chi, color) in enumerate(zip(chis, colors)):
    a = fig.add_subplot(grid[1+j//2, j%2])
    rates = growth(km, chi)
    m = int(mode[np.argmax(rates)])
    best = float(rates.max())
    selected.append({'chi_b':chi, 'm_fast':m if best>0 else None,
                     'largest_discrete_growth_rate':best})
    if best > 0:
        q = (m*np.pi)**2
        kappa = chi/(1+nstar)**2
        ratio = (1+db*q+best)/(kappa*q)
        a.plot(x, np.cos(m*np.pi*x), color=color, label='b perturbation')
        a.plot(x, ratio*np.cos(m*np.pi*x), color=color, ls='--', label='n perturbation')
        title = rf'$\chi_b={chi:g}$: fastest mode $m={m}$, $\sigma_+={best:.3f}$'
    else:
        a.axhline(0, color=color, lw=2)
        title = rf'$\chi_b={chi:g}$: every allowed mode decays'
    a.set(xlim=(0, 1), ylim=(-1.4, 1.4), xlabel='x', ylabel='Mode shape', title=title)
    a.axhline(0, color='0.7', lw=.5)
    a.title.set_fontsize(10)
    if best>0:
        a.legend(fontsize=7, loc='upper right')
fig.suptitle('Early pattern selection: d_b=0.002, d_n=0.04, μ=0.5, b₀=2, λ=2.5', fontsize=12)
fig.savefig('oxford-2023-further-mathematical-biology-pattern-selection.png', dpi=145, facecolor='white')
if __name__ == '__main__':
    import json
    print(json.dumps(selected, indent=2))
