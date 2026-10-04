"""Original contour diagram; tested Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write the PNG basename to the caller's CWD and honor supplied MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/paper-86-mplconfig')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), dpi=140, facecolor='white')
    ax = axes[0]
    u = np.linspace(-3, 3, 601)
    v = (1 + np.sqrt(1 + 4*u*u))/2
    ax.fill_between(u, v, 4, color='#e3edf7')
    ax.plot(u, v, color='#1764ab', linewidth=2)
    for at in [-1.8, 1.1]:
        to = at + .45
        ax.annotate('', xy=(to, (1+np.sqrt(1+4*to*to))/2), xytext=(at, (1+np.sqrt(1+4*at*at))/2), arrowprops={'arrowstyle':'->', 'color':'#1764ab', 'lw':2})
    ax.text(0, 3.45, 'Reflected transform analytic\nClose upward for x > 0', ha='center', fontsize=9)
    ax.text(.12, 1.08, r'$i\alpha$', fontsize=11)
    ax.text(2.45, 3.1, r'$L$', color='#1764ab', fontsize=12)
    ax.set(xlim=(-3,3), ylim=(-.35,4), xlabel=r'$\mathrm{Re}\,k$', ylabel=r'$\mathrm{Im}\,k$', title=r'Half-line drift contour ($\alpha=1$)')
    ax = axes[1]
    ax.fill_between([-3,0], -3, 0, color='#e8f2e5')
    ax.text(-1.5, -1.5, 'Global relation\n'+r'$\rho_x+\rho_y=0$', ha='center', fontsize=10)
    ax.annotate('', xy=(3,0), xytext=(0,0), arrowprops={'arrowstyle':'->', 'color':'#1764ab', 'lw':2.5})
    ax.annotate('', xy=(0,3), xytext=(0,0), arrowprops={'arrowstyle':'->', 'color':'#be472c', 'lw':2.5})
    ax.scatter([1,0], [0,1], color=['#1764ab','#be472c'], s=30, zorder=5)
    ax.text(2,.18,r'$\ell_x$',color='#1764ab',fontsize=12)
    ax.text(.18,2,r'$\ell_y$',color='#be472c',fontsize=12)
    ax.text(1,-.45,r'$\sqrt{\lambda}$',ha='center',fontsize=10)
    ax.text(.15,1,r'$i\sqrt{\lambda}$',fontsize=10)
    ax.set(xlim=(-3,3.2), ylim=(-3,3.2), xlabel=r'$\mathrm{Re}\,k$', ylabel=r'$\mathrm{Im}\,k$', title=r'Quadrant reconstruction rays ($\lambda=1$)', aspect='equal')
    for ax in axes:
        ax.set_facecolor('white')
        ax.axhline(0,color='#555555',lw=.7,zorder=0)
        ax.axvline(0,color='#555555',lw=.7,zorder=0)
        ax.grid(alpha=.12)
    fig.tight_layout()
    fig.savefig('paper-86-spectral-contours.png', facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
