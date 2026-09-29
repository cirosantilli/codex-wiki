"""Original qualitative DLVO sketch. Python 3.14; NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7), facecolor='white', gridspec_kw={'width_ratios': [1.2, 1]})
h = np.linspace(.045, 15, 8001)
curves = [(.5, '#286ca5', 'low salt'), (1.7, '#47814a', 'more salt'),
          (10/np.e, '#cd8b28', 'barrier reaches zero'), (6, '#b44c49', 'high salt')]
for kappa, color, label in curves:
    potential = 40*np.exp(-kappa*h)-4/h
    for ax in axes:
        ax.plot(h, potential, color=color, linewidth=2, label=label)
for ax in axes:
    ax.axhline(0, color='#555555', linewidth=.8)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(alpha=.14)
    ax.set_xlabel('surface gap $h$ (chosen length unit)')
axes[0].set(xlim=(0, 6), ylim=(-12, 29), ylabel=r'interaction $U/(k_BT)$')
axes[0].set_title('Repulsive barrier and contact attraction', fontsize=11)
axes[0].legend(loc='upper right', frameon=False, fontsize=9)
axes[0].annotate('primary well\ncontinues downwards', xy=(.095, -11), xytext=(1.0, -8.0), fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='#555555'))
critical_gap = np.e/10
axes[0].plot(critical_gap, 0, 'o', color='#cd8b28', markersize=5)
axes[0].annotate('limiting zero barrier', xy=(critical_gap, 0), xytext=(1.5, 5.6), fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='#8b641f'))
axes[1].set(xlim=(1, 14), ylim=(-4.2, .45), ylabel=r'interaction $U/(k_BT)$')
axes[1].set_title('Outer attractive region (vertical magnification)', fontsize=11)
axes[1].annotate('shallow secondary\nminimum at low salt', xy=(12.4, -.24), xytext=(6.0, -1.8), fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='#286ca5'), color='#245f8b')
fig.text(.5, .025, r'Illustrative tail: $U/(k_BT)=40e^{-\kappa h}-4/h$; molecular contact forces are not modelled.',
         ha='center', fontsize=10)
fig.subplots_adjust(left=.07, right=.98, top=.87, bottom=.20, wspace=.29)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
