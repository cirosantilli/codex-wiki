"""Original band/state diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Run from _media. Energies are deliberately arbitrary; no device parameters fit.
The n reservoir is left, p reservoir right; positive V lowers p electron energies.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

BLUE = '#2468a0'
ORANGE = '#cc7420'
GREEN = '#168253'
GAP = 2.2
ECN = -0.5
EVP0 = 0.5


def transfer_window(v):
    """Zero-T same-energy occupied-to-empty intervals, arbitrary energy units."""
    if v >= 0:
        return max(ECN, -v), min(0.0, EVP0 - v), 'n to p'
    return max(0.0, -GAP), min(-v, EVP0 - v), 'p to n'


def main():
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 11,
                         'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(2, 3, figsize=(12, 7.2), sharey=True)
    choices = [(0.0, 'Equilibrium'), (0.25, 'Forward: window opens'),
               (0.70, 'Forward: window shrinks'), (1.15, 'Forward: no band overlap'),
               (-0.70, 'Reverse: p to n transfer')]
    for ax, (v, title) in zip(axes.flat, choices):
        evp = EVP0 - v
        ecp = evp + GAP
        mup = -v
        # Only neutral reservoir states are shaded. The barrier has no added states.
        ax.fill_between([0, .30], -3.0, ECN-GAP, color=BLUE, alpha=.8)
        ax.fill_between([0, .30], 0, 3.5, facecolor='white',
                        edgecolor=ORANGE, hatch='///', linewidth=0)
        ax.fill_between([0, .30], ECN, 0, color=BLUE, alpha=.8)
        ax.fill_between([.70, 1], mup, evp, facecolor='white',
                        edgecolor=ORANGE, hatch='///', linewidth=0)
        ax.fill_between([.70, 1], -3.0, mup, color=BLUE, alpha=.8)
        ax.fill_between([.70, 1], ecp, 3.5, facecolor='white',
                        edgecolor=ORANGE, hatch='///', linewidth=0)
        x = np.linspace(0, 1, 301)
        u = np.clip((x-.30)/.40, 0, 1)
        bend = u*u*(3-2*u)
        ec = ECN + (ecp-ECN)*bend
        ax.plot(x, ec, color='#303940', lw=1.6)
        ax.plot(x, ec-GAP, color='#303940', lw=1.6)
        ax.plot([0, .32], [0, 0], '--', color=BLUE, lw=1.4)
        ax.plot([.68, 1], [mup, mup], '--', color=BLUE, lw=1.4)
        ax.text(.015, .11, r'$\mu_n$', color=BLUE, fontsize=10)
        ax.text(.88, mup+.10, r'$\mu_p$', color=BLUE, fontsize=10)
        ax.text(.03, ECN-.25, r'$E_{c,n}$', fontsize=9)
        ax.text(.73, evp+.13, r'$E_{v,p}$', fontsize=9)
        lo, hi, direction = transfer_window(v)
        if hi > lo:
            ax.plot([.50, .50], [lo, hi], color=GREEN, lw=5, solid_capstyle='butt')
            e = (lo+hi)/2
            ends = ((.24, e), (.76, e)) if v > 0 else ((.76, e), (.24, e))
            ax.annotate('', xy=ends[1], xytext=ends[0],
                        arrowprops={'arrowstyle': '->', 'color': GREEN, 'lw': 2})
            note = f'transfer window = {hi-lo:.2f}'
        else:
            note = 'net current = 0' if v == 0 else 'direct band transfer closed'
        ax.text(.5, -3.43, note, ha='center', color=GREEN, fontsize=9)
        ax.set_title(f'{title}\n$qV={v:+.2f}$ (chosen units)', pad=9)
        ax.set_xlim(-.04, 1.04)
        ax.set_ylim(-3.6, 3.65)
        ax.set_xticks([.15, .50, .85], [r'$n^+$', 'thin barrier', r'$p^+$'])
        ax.tick_params(axis='x', length=0)
        ax.set_yticks([-2, 0, 2])
        ax.spines[['top', 'right', 'bottom']].set_visible(False)
        ax.set_ylabel('Electron energy (arbitrary units)')
    key = axes.flat[-1]
    key.axis('off')
    key.legend(handles=[Patch(facecolor=BLUE, alpha=.8, label='occupied reservoir states'),
                        Patch(facecolor='white', edgecolor=ORANGE, hatch='///',
                              label='empty reservoir states'),
                        Patch(facecolor=GREEN, label='same-energy transfer window')],
               loc='upper left', frameon=False, fontsize=10)
    key.text(.03, .60, 'Each arrow conserves electron energy.\n'
             'Available final states are essential.\n\n'
             r'Positive bias: $\mu_n-\mu_p=qV$.' '\n'
             'At zero bias the occupations balance.\n\n'
             'Reservoir occupations use $T=0$.\n'
             'Band bending and barrier width are\n'
             'schematic; momentum selection and\n'
             'phonon assistance are omitted.', transform=key.transAxes,
             va='top', linespacing=1.45)
    fig.suptitle('Tunnel diode: occupied and empty states must overlap in energy', fontsize=15, y=.99)
    fig.text(.5, .012, 'Original qualitative construction; not a measured band profile or a fit to an Esaki device.',
             ha='center', fontsize=10)
    fig.tight_layout(rect=(0, .035, 1, .94), h_pad=2.0, w_pad=2.2)
    out = Path.cwd() / (Path(__file__).stem + '.png')
    fig.savefig(out, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
