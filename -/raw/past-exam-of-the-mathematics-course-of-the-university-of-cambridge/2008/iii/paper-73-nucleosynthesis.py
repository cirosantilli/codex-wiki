"""Original 2007-2008 abundance comparison, not a current likelihood or BBN solver.
Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Emits cwd basename PNG;
honors MPLCONFIGDIR. Near eta10=6, theory fits are from arXiv:0712.1100.
D and Li adopted ranges: same review; He: astro-ph/0701580; WMAP:0803.0547.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

eta = np.linspace(3, 8.5, 550)
curves = [2.68*(6/eta)**1.6, .2483+.0016*(eta-6), 4.30*(eta/6)**2]
observations = [(2.43, 2.95), (.2477-.0029, .2477+.0029), (10**.0, 10**.2)]
labels = [r'$10^5\mathrm{D/H}$', r'$Y_p$', r'$10^{10}\,{}^7\mathrm{Li/H}$']
limits = [(0, 9), (.236, .258), (0, 9)]
central, sigma = 274*.02273, 274*.00062
fig, axes = plt.subplots(3, 1, figsize=(8.2, 7.3), dpi=140, sharex=True, facecolor='white')
for ax, theory, observed, ylabel, ylim in zip(axes, curves, observations, labels, limits):
    ax.set_facecolor('white')
    ax.axvspan(central-sigma, central+sigma, color='#d8d8d8', label='WMAP5 density interval')
    ax.axhspan(*observed, color='#d3e7f3', label='Representative observed range')
    ax.plot(eta, theory, '--', color='#b13d3d', lw=1.7, label='Trend outside local fit interval')
    local = (eta >= 5.7) & (eta <= 6.5)
    ax.plot(eta[local], theory[local], color='#b13d3d', lw=2.5, label='Standard BBN fit near preferred density')
    ax.set(ylabel=ylabel, ylim=ylim, xlim=(3, 8.5))
    ax.grid(alpha=.22)
axes[0].legend(loc='upper right', fontsize=8, framealpha=.95)
axes[-1].set_xlabel(r'$\eta_{10}=10^{10}n_b/n_\gamma\simeq274\Omega_bh^2$')
fig.suptitle('Primordial abundance consistency: a 2007-2008 comparison', fontsize=13)
fig.text(.5, .018, 'No modern-data claim; dashed curves are schematic extrapolations, not a full nuclear-network calculation.',
         ha='center', fontsize=8)
fig.tight_layout(rect=(0, .045, 1, .965))
fig.savefig(Path('paper-73-nucleosynthesis.png'), facecolor='white', transparent=False)
plt.close(fig)
