"""Original single-frequency model; emit matching PNG to the current directory.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
The incident and transmitted amplitudes are normalized separately. This is not
an interface amplitude solution, a pulse calculation, or measured material data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 1.5
    colors = ['#176ba0', '#b44f24']
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.9), dpi=120,
                             gridspec_kw={'height_ratios': [1, 1.25]}, facecolor='white')
    fig.subplots_adjust(left=.095, right=.97, bottom=.16, top=.83, hspace=.42)
    for ax in axes:
        ax.axvspan(-2.15, 0, color='#eef6fc')
        ax.axvspan(0, 2.15, color='#fff4e7')
        ax.axvline(0, color='#555555', lw=1.3)
        ax.set_xlim(-2.1, 2.1)
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_xticks(np.arange(-2, 2.1, .5))
    top, bottom = axes
    for lo, hi, index, color in [(-2.1, 0, 1, colors[0]), (0, 2.1, n, colors[1])]:
        x = np.linspace(lo, hi, 800)
        top.plot(x, np.cos(2 * np.pi * index * x), color=color, lw=2.3)
        for m in range(-3, 4):
            crest = m / index
            if lo < crest < hi:
                top.plot([crest, crest], [-1, 1], color=color, alpha=.27, ls=':')
    for start, length, label, color in [(-2, 1, r'$\lambda_0$', colors[0]),
                                       (2/3, 2/3, r'$\lambda=2\lambda_0/3$', colors[1])]:
        top.annotate('', xy=(start+length, 1.35), xytext=(start, 1.35),
                     arrowprops={'arrowstyle': '<->', 'color': color, 'lw': 1.5})
        top.text(start+length/2, 1.48, label, ha='center', color=color, fontsize=12)
    top.set_ylim(-1.2, 1.85)
    top.set_yticks([-1, 0, 1])
    top.set_ylabel('Normalized field')
    top.set_title('One instant: phase repeats over a shorter distance', fontsize=13, pad=12)
    t = np.linspace(0, 2, 1001)
    for m in range(-5, 3):
        for index, color, left in [(1, colors[0], True), (n, colors[1], False)]:
            x = (m + t) / index
            mask = x <= 0 if left else x >= 0
            bottom.plot(x[mask], t[mask], color=color, lw=2)
    # A chosen crest crosses the interface at t/T=1.
    for p, q in [((-.8, .2), (-.2, .8)), ((.1, 1.15), (.5, 1.75))]:
        bottom.annotate('', xy=q, xytext=p,
                        arrowprops={'arrowstyle': '-|>', 'lw': 3.2, 'color': '#222222'})
    bottom.plot([0, 0], [0, 2], 'o', color='#222222', ms=5)
    bottom.text(-1.97, 1.62, r'$v_{\rm ph}=c$', fontsize=13,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .95})
    bottom.text(.8, .19, r'$v_{\rm ph}=2c/3$', fontsize=13,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .95})
    bottom.annotate('Successive crests at interface:\nsame period $T=1/f$', xy=(0, 1),
                    xytext=(.85, 1.05), fontsize=10,
                    arrowprops={'arrowstyle': '->', 'color': '#333333'},
                    bbox={'facecolor': 'white', 'edgecolor': '#bbbbbb'})
    bottom.set_ylim(0, 2)
    bottom.set_yticks([0, 1, 2])
    bottom.set_ylabel(r'Time $t/T$')
    bottom.set_xlabel(r'Position $z/\lambda_0$   (propagation toward $+z$)')
    bottom.set_title('Crest trajectories: less distance in the same time', fontsize=13, pad=10)
    fig.suptitle('Refractive index changes phase spacing and phase speed', fontsize=17, y=.975)
    fig.text(.30, .905, r'Vacuum: $n=1$', ha='center', fontsize=13, color=colors[0])
    fig.text(.73, .905, r'Chosen medium: $n=3/2$', ha='center', fontsize=13, color=colors[1])
    fig.text(.5, .045, 'Stationary interface at normal incidence; single frequency.\n'
             'Equal normalized components; reflection omitted. Original model, not measured data.',
             ha='center', fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
