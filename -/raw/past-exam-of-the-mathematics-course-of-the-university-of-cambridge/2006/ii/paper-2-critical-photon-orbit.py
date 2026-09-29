"""Critical Schwarzschild photon orbit; Python 3.14.4.
Dependencies numpy 2.3.5 and matplotlib 3.10.7; output basename to CWD.
Caller MPLCONFIGDIR is preserved. Distances are in units of M.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    phi0 = np.arccosh(2)
    phi = np.linspace(phi0+0.25, phi0+5*np.pi, 2400)
    c = np.cosh(phi)
    radius = 3*(c+1)/(c-2)
    keep = radius <= 13
    phi, radius = phi[keep], radius[keep]
    xx, yy = radius*np.cos(phi), radius*np.sin(phi)
    fig, ax = plt.subplots(figsize=(6.2, 6.2), facecolor='white')
    ax.set_facecolor('white')
    ax.plot(xx, yy, lw=1.7, label='Incoming critical branch')
    ax.plot(xx, -yy, lw=1.2, alpha=0.65, label='Reflected outgoing branch')
    angles = np.linspace(0, 2*np.pi, 500)
    ax.plot(3*np.cos(angles), 3*np.sin(angles), '--', color='black', label=r'Photon circle $r=3M$')
    ax.fill(2*np.cos(angles), 2*np.sin(angles), color='0.85', label=r'Horizon $r=2M$')
    direction = np.array([np.cos(phi0), np.sin(phi0)])
    normal = np.array([-np.sin(phi0), np.cos(phi0)])
    asym = np.sqrt(27)*normal[:, None]+direction[:, None]*np.linspace(0, 12, 100)
    ax.plot(asym[0], asym[1], ':', color='0.4', label=r'Asymptote offset $3\sqrt{3}M$')
    j = min(120, len(xx)-2)
    ax.annotate('', xy=(xx[j+25], yy[j+25]), xytext=(xx[j], yy[j]),
                arrowprops={'arrowstyle':'->', 'color':'tab:blue', 'lw':1.5})
    ax.set(xlim=(-10, 9), ylim=(-7, 13), xlabel=r'$x/M$', ylabel=r'$y/M$',
           title='Critical photon orbit spiralling toward the photon sphere')
    ax.set_aspect('equal')
    ax.legend(loc='lower left', fontsize=8)
    fig.tight_layout()
    fig.savefig('paper-2-critical-photon-orbit.png', dpi=135, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
