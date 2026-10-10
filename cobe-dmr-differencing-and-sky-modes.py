"""Original quadrupole sky and ideal directional-difference illustration.

Run from _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
No measured COBE data. The great-circle scan is deliberately incomplete.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BASENAME = Path(__file__).stem
Q = 30.0
ALPHA = np.pi/3


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(11, 7.6), layout='constrained')
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.15])
    ax = fig.add_subplot(grid[0, 0], projection='mollweide')
    lon = np.linspace(-np.pi, np.pi, 241)
    lat = np.linspace(-np.pi/2, np.pi/2, 121)
    ll, bb = np.meshgrid(lon, lat)
    sky = Q * (3*np.sin(bb)**2-1)/2
    im = ax.pcolormesh(ll, bb, sky, cmap='RdBu_r', vmin=-Q, vmax=Q, shading='auto', rasterized=True)
    ax.grid(alpha=.3); ax.set_xticklabels([])
    ax.set_title('Chosen axisymmetric quadrupole', pad=15)
    fig.colorbar(im, ax=ax, orientation='horizontal', shrink=.8, pad=.05,
                 label='Temperature relative to a chosen mean (μK)')
    ax = fig.add_subplot(grid[0, 1]); ax.set_aspect('equal'); ax.axis('off')
    ax.set(xlim=(-1.25, 1.25), ylim=(-.5, 1.55))
    ax.set_title('Pair directions separated by 60°')
    origin = np.array([0., -.2])
    for angle, label, color in [(60, 'A', '#2166ac'), (120, 'B', '#cb521d')]:
        end = origin + 1.35*np.array([np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))])
        ax.annotate('', xy=end, xytext=origin, arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': color})
        ax.text(end[0]*1.15, end[1]+.1, label, ha='center', color=color)
    arc = np.linspace(np.pi/3, 2*np.pi/3, 60)
    ax.plot(.6*np.cos(arc), -.2+.6*np.sin(arc), color='#526273')
    ax.text(0, .25, '60°', ha='center')
    ax.text(0, -.45, 'Ideal readout: d = T(A) − T(B)', ha='center')
    ax = fig.add_subplot(grid[1, :])
    phi = np.linspace(0, 2*np.pi, 721)
    ta = Q*(3*np.cos(phi)**2-1)/2
    tb = Q*(3*np.cos(phi+ALPHA)**2-1)/2
    ax.plot(np.rad2deg(phi), ta, color='#2166ac', lw=1.5, label='Beam A: quadrupole')
    ax.plot(np.rad2deg(phi), tb, color='#cb521d', lw=1.5, ls='--', label='Beam B: quadrupole')
    ax.plot(np.rad2deg(phi), ta-tb, color='#6a3d9a', lw=2.4, label='Difference A − B')
    ax.axhline(0, color='#333333', lw=1.4, ls=':', label='Any monopole: zero difference')
    ax.set(xlim=(0, 360), ylim=(-46, 64), xticks=np.arange(0, 361, 60),
           xlabel='Beam A angle φ on a chosen great circle (degrees)', ylabel='Temperature (μK)',
           title='Directional response: T(φ) = 30 P₂(cos φ) μK; beam B at φ + 60°')
    ax.grid(alpha=.2); ax.legend(loc='upper center', ncol=2, fontsize=10, frameon=False)
    fig.suptitle('Ideal sky differencing — calculated modes, not COBE data', fontsize=14)
    fig.savefig(BASENAME+'.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
