"""Conceptual beam apparatus and synthetic rigid-rotor Stark spectra.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
Diagram method: van Vaals (1983), chapter I, section 2, pp. 11-14.
Signals are normalized illustrative profiles, never measured HCl spectra.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def rotor_levels(field_ratio, jmax=24):
    """M=0: Hamiltonian divided by B; field_ratio = mu E / B.

<j,0|cos(theta)|j+1,0> = (j+1)/sqrt((2j+1)(2j+3)).
"""
    j = np.arange(jmax + 1, dtype=float)
    coupling = -field_ratio * (j[:-1] + 1) / np.sqrt((2*j[:-1] + 1) * (2*j[:-1] + 3))
    matrix = np.diag(j * (j + 1)) + np.diag(coupling, 1) + np.diag(coupling, -1)
    return np.linalg.eigvalsh(matrix)


def main():
    np.testing.assert_allclose(rotor_levels(0)[:3], [0, 2, 6])
    eps = 1e-3
    levels = rotor_levels(eps)
    np.testing.assert_allclose(levels[:2], [-eps**2/6, 2+eps**2/10], atol=1e-12)
    np.testing.assert_allclose(rotor_levels(.6)[:3], rotor_levels(-.6)[:3], atol=1e-12)
    np.testing.assert_allclose(rotor_levels(.6, 16)[:3], rotor_levels(.6, 24)[:3], atol=1e-12)
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig = plt.figure(figsize=(9, 6.2), layout='constrained')
    grid = fig.add_gridspec(2, 1, height_ratios=[1.1, 1])
    top = fig.add_subplot(grid[0]); top.set(xlim=(-.3, 10.3), ylim=(-.1, 3)); top.axis('off')
    for x, width, label in [(0, 1.3, 'Source +\napertures'), (2, 1.3, 'A\nState selector'), (4, 1.8, 'C\nUniform field'), (6.6, 1.3, 'B\nState analyzer'), (8.6, 1.4, 'Detector\nArrival rate')]:
        top.add_patch(FancyBboxPatch((x, .8), width, .9, boxstyle='round,pad=.05', facecolor='#edf3f7', edgecolor='#637d91'))
        top.text(x+width/2, 1.25, label, ha='center', va='center', fontsize=11)
    for x1, x2 in [(1.35,1.9),(3.35,3.9),(5.85,6.5),(7.95,8.5)]:
        top.annotate('', xy=(x2,1.25), xytext=(x1,1.25), arrowprops={'arrowstyle':'->','color':'#2679ab','lw':2})
    top.annotate('Scanned radiation', xy=(4.9,1.77), xytext=(4.9,2.45), ha='center', arrowprops={'arrowstyle':'->','color':'#c36922','lw':2})
    top.text(5, .35, 'Beam travels through vacuum; resonance can change transmission through B.', ha='center', fontsize=11)
    top.set_title('Conceptual apparatus (not a reconstruction of the HCl instrument)', fontsize=13)
    ax = fig.add_subplot(grid[1]); x = np.linspace(-.09, .19, 1401)
    for field, color in [(0, '#2679ab'), (.6, '#c36922')]:
        ev = rotor_levels(field); centre = ev[1]-ev[0]-2
        y = 1-.35*np.exp(-((x-centre)/.013)**2)
        assert abs(x[np.argmin(y)]-centre) <= (x[1]-x[0])/2 + 1e-12
        ax.plot(x, y, color=color, lw=2, label=fr'$\mu E/B={field:g}$')
        ax.axvline(centre, color=color, ls=':', alpha=.5)
    ax.plot(x, np.ones_like(x), color='#777777', ls='--', label='Radiation off')
    ax.set(xlabel=r'Energy detuning $(h\nu-2B)/B$', ylabel='Normalized arrival rate', ylim=(.6,1.08), title='Synthetic signal: rigid rotor, M = 0, lowest rotational transition')
    ax.legend(loc='lower left', ncol=3, fontsize=10)
    ax.spines[['top','right']].set_visible(False)
    fig.suptitle('Dipole evidence: field-dependent resonance', fontsize=17)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), dpi=120, facecolor='white', bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
