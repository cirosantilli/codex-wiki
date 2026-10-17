"""Original illustrative negative-resist model; Python 3.14/numpy/matplotlib.

This is not digitized exam artwork. The chosen intensity and thresholds explain
qualitative dose mapping, not the preceding graph-read numerical answers.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DA, DB = 10.0, 50.0

def retention(dose):
    return np.clip(np.log(np.maximum(dose, 1e-12) / DA) / np.log(DB / DA), 0, 1)

x = np.linspace(-2, 2, 801)
intensity = 1 + 29 * np.exp(-(x / .9)**4)
dose = np.geomspace(1, 200, 500)
fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.8), layout='constrained')
fig.patch.set_facecolor('white')
axes[0].semilogx(dose, retention(dose), color='#286a85', lw=2)
for d, label in [(DA, r'$D_a$'), (DB, r'$D_b$')]:
    axes[0].axvline(d, color='.65', ls=':', lw=1)
    axes[0].text(d, .1, label, ha='right', va='bottom')
axes[0].set(xlabel=r'Dose (mJ cm$^{-2}$)', ylabel=r'Remaining thickness $t/t_0$',
            title='Declared negative-resist response', ylim=(-.04, 1.06))
axes[1].plot(x, intensity, color='#286a85', lw=2)
axes[1].set(xlabel=r'Position ($\mu$m)', ylabel=r'Intensity (mW cm$^{-2}$)',
            title='Chosen smooth test intensity', ylim=(0, 34))
for tau, color in [(1, '#91709b'), (2, '#286a85'), (4, '#b65c38')]:
    axes[2].plot(x, retention(tau * intensity), lw=2, color=color,
                 label=f'{tau:g} s exposure')
axes[2].set(xlabel=r'Position ($\mu$m)', ylabel=r'Remaining thickness $t/t_0$',
            title='Less exposure narrows the ridge', ylim=(-.04, 1.06))
axes[2].legend(fontsize=8.5)
for ax in axes:
    ax.grid(alpha=.17)
fig.savefig('paper-1-resist-response.png', dpi=150, facecolor='white')
plt.close(fig)
