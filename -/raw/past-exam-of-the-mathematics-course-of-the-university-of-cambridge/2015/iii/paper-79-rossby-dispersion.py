"""Generate an original Rossby dispersion/reflection sketch in the caller's cwd.
Tested with Python 3.14, NumPy 2.3.5 and matplotlib 3.10.7.
MPLCONFIGDIR is supplied by the caller and is never overridden here.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (ax, circle) = plt.subplots(1, 2, figsize=(9, 5), dpi=100, facecolor='white')
    k = np.linspace(-5, 5, 1601)
    for ell, color in [(0, '#006e9c'), (0.6, '#a53f00'), (1.5, '#42783a')]:
        ax.plot(k, -k/(k*k+ell*ell+1), color=color, linewidth=2, label=f'$l/a={ell:g}$')
    w, ell = -0.3, 0.6
    centre = -1/(2*w)
    radius = np.sqrt(1/(4*w*w)-1)
    offset = np.sqrt(radius*radius-ell*ell)
    ki, kr = centre-offset, centre+offset
    ax.axhline(0, color='0.55', linewidth=0.7)
    ax.axvline(0, color='0.55', linewidth=0.7)
    ax.axhline(w, color='0.55', linestyle=':', linewidth=1)
    ax.scatter([ki, kr], [w, w], color='black', s=23, zorder=4)
    ax.set(xlabel='$k/a$', ylabel=r'$\omega a/\beta$', title='Frequency at fixed meridional wavenumber')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=0.15)
    angle = np.linspace(0, 2*np.pi, 801)
    circle.plot(centre+radius*np.cos(angle), radius*np.sin(angle), color='#006e9c', linewidth=2)
    circle.axhline(0, color='0.55', linewidth=0.7)
    circle.axvline(0, color='0.55', linewidth=0.7)
    circle.plot([0, centre+radius+0.3], [ell, ell], ':', color='0.5')
    circle.scatter([ki, kr], [ell, ell], color='black', s=25, zorder=4)
    circle.scatter([centre], [0], marker='+', color='0.4', s=65)
    circle.annotate('Incident\nwestward group', (ki, ell), xytext=(ki-0.1, ell+0.5), ha='center', fontsize=9,
                    arrowprops={'arrowstyle': '->', 'color': '0.25'})
    circle.annotate('Reflected\neastward group', (kr, ell), xytext=(kr+0.05, ell+0.5), ha='center', fontsize=9,
                    arrowprops={'arrowstyle': '->', 'color': '0.25'})
    circle.set(xlabel='$k/a$', ylabel='$l/a$', title=r'Constant frequency: $\omega a/\beta=-0.3$')
    circle.set_xlim(-0.1, centre+radius+0.3)
    circle.set_ylim(-1.55, 1.55)
    circle.set_aspect('equal', adjustable='box')
    circle.grid(alpha=0.15)
    fig.suptitle('Rossby waves: phase travels west, reflected energy travels east', fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig('paper-79-rossby-dispersion.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
