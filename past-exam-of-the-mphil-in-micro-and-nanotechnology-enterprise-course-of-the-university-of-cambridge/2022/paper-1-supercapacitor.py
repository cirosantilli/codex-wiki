"""Original qualitative electrochemical storage models; Python 3.14/numpy/matplotlib.

Curves are normalized illustrative models, not measured material data.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(9, 6.4), layout='constrained')
fig.patch.set_facecolor('white')
t = np.linspace(0, 1, 401)
axes[0, 0].plot(t, .12 + .8*t, color='#286a85', label='Charge')
axes[0, 0].plot(1+t, .88 - .8*t, color='#b65c38', label='Discharge')
axes[0, 0].plot([1, 1], [.92, .88], color='.3', lw=1.5)
axes[0, 0].annotate('Current reversal: 2IR step', xy=(1, .9), xytext=(.8, .42),
                    fontsize=9, arrowprops={'arrowstyle': '->', 'color': '.4'})
axes[0, 0].set(title='Nearly constant capacitance', xlabel='Time (normalized)',
               ylabel='Voltage (normalized)', ylim=(0, 1))
axes[0, 0].legend(fontsize=8, loc='upper left')
state = np.linspace(.02, .98, 400)
battery = .55 + .075*np.log(state/(1-state))
axes[0, 1].plot(state, battery+.04, color='#286a85', label='Charge')
axes[0, 1].plot(2-state, battery-.04, color='#b65c38', label='Discharge')
axes[0, 1].set(title='Illustrative battery plateau', xlabel='Time (normalized)',
               ylabel='Voltage (normalized)', ylim=(0, 1))
axes[0, 1].legend(fontsize=8)
v = np.linspace(-1, 1, 401)
axes[1, 0].plot(v, np.ones_like(v), color='#286a85', label='Ideal constant C')
axes[1, 0].plot(v, 1+.6*v*v, '--', color='#91709b', label='Possible double-layer minimum')
axes[1, 0].set(title='Two double-layer idealizations', xlabel=r'Potential relative to zero-charge point',
               ylabel='Specific differential C (normalized)', ylim=(.7, 1.9))
axes[1, 0].legend(fontsize=8)
redox = 1 + 1.7/np.cosh(3*(v-.15))**2
axes[1, 1].plot(v, redox, color='#286a85', label='Background + redox contribution')
axes[1, 1].axhline(1, color='.6', ls='--', lw=1)
axes[1, 1].set(title='One possible pseudocapacitive contribution',
               xlabel='Potential (normalized)', ylabel='Specific differential C (normalized)',
               ylim=(.7, 3))
axes[1, 1].legend(fontsize=8)
for ax in axes.flat:
    ax.grid(alpha=.16)
fig.savefig('paper-1-supercapacitor.png', dpi=150, facecolor='white')
plt.close(fig)
