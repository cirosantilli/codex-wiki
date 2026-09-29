"""Original dimensionless model illustrations; no source figures are reproduced.
Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes the PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def logistic(rate, initial, steps):
    values = np.empty(steps + 1)
    values[0] = initial
    for t in range(steps):
        values[t+1] = rate * values[t] * (1-values[t])
    return values


def growth_rates(k, diffusion):
    jacobian = np.array([[1.,1.],[-3.,-2.]])
    return np.array([np.linalg.eigvals(jacobian-wave**2*diffusion).real.max()
                     for wave in k])


fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.7), layout='constrained')
colors = ['#245d98', '#c15a2a', '#54803b']
for rate, color in zip([2.8,3.2,4.], colors):
    x = logistic(rate, .2, 260)
    axes[0].plot(np.arange(230,261), x[230:], '.-', ms=3, lw=.9,
                 color=color, label=f'r = {rate:g}')
axes[0].set(title='One rule, three dynamical regimes', xlabel='Iteration',
            ylabel='State x', ylim=(0,1))
axes[0].legend(frameon=False, fontsize=8)
a, b = logistic(4.,.2,40), logistic(4.,.200001,40)
axes[1].semilogy(np.arange(41), np.maximum(np.abs(a-b),1e-16),
                 color='#245d98', lw=1.3)
axes[1].set(title='Sensitivity at r = 4', xlabel='Iteration',
            ylabel='Absolute trajectory separation', ylim=(1e-7,1))
k = np.linspace(0,1.3,600)
axes[2].plot(k, growth_rates(k,np.diag([1.,10.])), color='#c15a2a',
             label='unequal diffusion: D = diag(1,10)')
axes[2].plot(k, growth_rates(k,np.eye(2)), color='#245d98', ls='--',
             label='equal diffusion: D = identity')
axes[2].axhline(0,color='black',lw=.7)
lo, hi = np.sqrt((4-np.sqrt(6))/10), np.sqrt((4+np.sqrt(6))/10)
axes[2].axvspan(lo,hi,color='#c15a2a',alpha=.1)
# Illustrate an allowed unstable mode on a length-10, no-flux interval.
k_mode = 2*np.pi/10
axes[2].scatter([k_mode],growth_rates(np.array([k_mode]),np.diag([1.,10.])),
                 color='#c15a2a',s=22,zorder=3)
axes[2].set(title='Diffusion can destabilize coupling', xlabel='Wavenumber k',
            ylabel='Largest real part of mode eigenvalues', ylim=(-1.3,.2))
axes[2].legend(frameon=False,fontsize=7,loc='lower left')
for ax in axes:
    ax.tick_params(labelsize=8)
    ax.title.set_fontsize(10)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
