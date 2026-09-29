"""Original standard-linear-solid spectra. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(-4, 3, 1801)
g_r, g_u = 1., 100.
g1 = g_r+(g_u-g_r)*x*x/(1+x*x)
g2 = (g_u-g_r)*x/(1+x*x)
loss = g2/g1
fig, axes = plt.subplots(3, 1, figsize=(8.0, 7.8), sharex=True, facecolor='white')
labels = [(g1/g_u, '#286ca5', r'$G_1/G_U$'), (g2/g_u, '#47814a', r'$G_2/G_U$'),
          (loss, '#aa4c68', r'$\tan\delta$')]
for ax, (values, color, ylabel) in zip(axes, labels):
    ax.semilogx(x, values, color=color, linewidth=2.4)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(alpha=.15)
    ax.spines[['top', 'right']].set_visible(False)
    ax.axvspan(1e-4, .015, color='#e9f2f9', alpha=.7, zorder=0)
    ax.axvspan(15, 1e3, color='#f1ece2', alpha=.7, zorder=0)
axes[0].set_yscale('log')
axes[0].set_ylim(.005, 1.8)
axes[0].text(.002, .03, 'relaxed\nrubbery plateau', ha='center', fontsize=9)
axes[0].text(150, .68, 'unrelaxed\nglassy limit', ha='center', fontsize=9)
axes[0].text(.065, .85, 'relaxation region', fontsize=10)
axes[0].axhline(g_r/g_u, color='#286ca5', linestyle=':', linewidth=.8)
axes[1].plot(1, (g_u-g_r)/(2*g_u), 'o', color='#47814a')
axes[1].annotate(r'loss-modulus peak: $\omega\tau_r=1$', xy=(1, (g_u-g_r)/(2*g_u)),
                 xytext=(5, .39), fontsize=10, arrowprops=dict(arrowstyle='->', color='#47814a'))
peak = np.sqrt(g_r/g_u)
height = (g_u-g_r)/(2*np.sqrt(g_r*g_u))
axes[2].plot(peak, height, 'o', color='#aa4c68')
axes[2].annotate(r'loss-tangent peak: $\omega\tau_r=\sqrt{G_R/G_U}$', xy=(peak, height),
                 xytext=(.65, 4.25), fontsize=10, arrowprops=dict(arrowstyle='->', color='#aa4c68'))
axes[2].set(xlim=(1e-4, 1e3), ylim=(0, 5.8), xlabel=r'normalized frequency $\omega\tau_r$')
axes[0].set_title(r'A solid with $G_U/G_R=100$: different storage and loss responses', fontsize=13, pad=15)
fig.subplots_adjust(left=.12, right=.97, top=.91, bottom=.10, hspace=.17)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
