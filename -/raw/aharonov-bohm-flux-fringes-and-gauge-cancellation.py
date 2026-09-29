"""Original two-path model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes its own basename PNG into the current directory.
Curves are calculated examples, not measured electron interference data.
"""
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig, (ax, gauge) = plt.subplots(1, 2, figsize=(12, 6.5), facecolor='white',
                                  gridspec_kw={'width_ratios': [1.12, 1]})
    position = np.linspace(-.35, 1.65, 1601)
    colors = ['#186aaf', '#c25a17', '#5f4599']
    for flux, color, label in zip([0, .25, .5], colors,
                                 [r'$\Phi=0$', r'$\Phi=h/(4e)$', r'$\Phi=h/(2e)$']):
        phase = -2*np.pi*flux
        intensity = 1.25 + np.cos(2*np.pi*position + phase)
        ax.plot(position, intensity, color=color, lw=2.4, label=label)
    ax.set(title='Chosen flux translates the carrier fringes', xlabel=r'Screen position $y/d$',
           ylabel=r'Intensity $I(y)$', xlim=(-.35, 1.65), ylim=(0, 2.65))
    ax.set_yticks([.25, 1.25, 2.25], [r'$1/4$', r'$5/4$', r'$9/4$'])
    ax.grid(alpha=.18)
    ax.legend(loc='upper right', fontsize=11)
    ax.annotate('', xy=(.25, 2.4), xytext=(0, 2.4),
                arrowprops={'arrowstyle': '<->', 'color': '#333333'})
    ax.text(.125, 2.5, r'$d/4$', ha='center', fontsize=11)
    ax.text(.5, -.27, r'$\mathcal{V}=4/5$ at every fixed flux; period $h/e$',
            ha='center', transform=ax.transAxes, fontsize=12)

    gauge.set_title('Vertex gauges move both path sums together')
    phases = [Fraction(0), Fraction(0), Fraction(0), Fraction(1, 2)]
    chi = [Fraction(1, 3), Fraction(-1, 4), Fraction(2, 5), Fraction(1, 7)]
    edges = [(0, 1), (1, 3), (0, 2), (2, 3)]
    transformed = [a + chi[j] - chi[i] for a, (i, j) in zip(phases, edges)]
    sums = [(sum(phases[:2]), sum(phases[2:])),
            (sum(transformed[:2]), sum(transformed[2:]))]
    ylevels = [1, 0]
    for y, pair in zip(ylevels, sums):
        upper, lower = map(float, pair)
        gauge.plot([upper, lower], [y, y], c='#656565', lw=2)
        gauge.scatter([upper], [y], c=colors[0], s=95, zorder=4)
        gauge.scatter([lower], [y], c=colors[1], s=95, zorder=4)
        for value, color, dy in [(pair[0], colors[0], .16), (pair[1], colors[1], -.22)]:
            numerator = '' if value.numerator == 1 else str(value.numerator)
            text = '$0$' if value == 0 else rf'${numerator}\pi/{value.denominator}$'
            gauge.text(float(value), y+dy, text, color=color, ha='center', fontsize=12)
    gauge.axvline(0, color='#999999', ls=':', lw=1)
    gauge.set(xlim=(-.35, .7), ylim=(-.45, 1.5), xlabel=r'Open-path phase sum / $\pi$')
    gauge.set_yticks([1, 0], ['Before', 'After'])
    gauge.set_xticks([-.25, 0, .25, .5])
    gauge.spines[['top', 'right']].set_visible(False)
    gauge.text(.5, -.27, r'$\delta=-\pi/2$, $W_C=-i$, $I=5/4$: unchanged',
               ha='center', transform=gauge.transAxes, fontsize=12)
    fig.suptitle('A physical flux change shifts interference; a gauge change preserves it',
                 fontsize=16, y=.97)
    fig.subplots_adjust(left=.075, right=.97, top=.83, bottom=.27, wspace=.42)
    fig.text(.51, .045, 'Original scalar model: mutually coherent paths, fixed envelopes, electron charge −e.',
             ha='center', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
