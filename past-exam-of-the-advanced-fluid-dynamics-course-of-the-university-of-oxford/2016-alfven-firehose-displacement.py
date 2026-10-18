from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 12})
fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.4), dpi=120, facecolor='white')
z = np.linspace(-np.pi, np.pi, 501)
xi = 0.33 * np.cos(z)
for ax, stable in zip(axes, (True, False)):
    ax.set_facecolor('white')
    ax.axhline(0, color='0.62', lw=1.1, ls='--', label='Unperturbed field line')
    ax.plot(z, xi, color='#2268a3', lw=2.6, label='Displaced field line')
    ax.annotate('', xy=(-0.2, 0.33), xytext=(-0.2, 0), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#2268a3'})
    ax.text(-0.42, 0.14, r'$\xi_y$', color='#2268a3', ha='right')
    force_end = 0.08 if stable else 0.61
    force_color = '#26764e' if stable else '#b83434'
    ax.annotate('', xy=(0.2, force_end), xytext=(0.2, 0.33), arrowprops={'arrowstyle': '->', 'lw': 2.6, 'color': force_color})
    ax.text(0.48, (0.33 + force_end)/2, 'Restoring force' if stable else 'Amplifying force', color=force_color, va='center')
    ax.annotate('', xy=(2.5, -0.59), xytext=(1.2, -0.59), arrowprops={'arrowstyle': '->', 'color': '0.2', 'lw': 1.6})
    ax.text(1.85, -0.54, r'$\mathbf{B}_0$', ha='center')
    ax.set_title(r'$\mathcal{T}_0>0$: Alfvén oscillation' if stable else r'$\mathcal{T}_0<0$: firehose growth')
    ax.set_xlabel(r'$k_{\parallel}z$')
    ax.set_ylabel('Transverse position (arbitrary scale)')
    ax.set_xticks([-np.pi, 0, np.pi], [r'$-\pi$', '0', r'$\pi$'])
    ax.set_yticks([])
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-0.72, 0.82)
    ax.spines[['top', 'right']].set_visible(False)
axes[0].legend(loc='upper left', fontsize=9, frameon=False)
fig.suptitle(r'Bending force: $\rho_0\partial_t^2\xi_y=\mathcal{T}_0\partial_z^2\xi_y$', y=0.99)
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
