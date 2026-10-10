"""Exact variances versus coordinate replacement budgets in three toy models.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; output to CWD.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def summarize(mass, marginal, function):
    mean = sum(q*function(x) for x, q in mass.items())
    variance = sum(q*(function(x)-mean)**2 for x, q in mass.items())
    halves = [sum(q*(marginal[i] if y else 1-marginal[i])
                   * (function(x)-function(x[:i]+(y,)+x[i+1:]))**2
                   for x, q in mass.items() for y in (0, 1))/2 for i in range(2)]
    return variance, halves


def main():
    p = (F(3, 10), F(3, 5))
    mass = {x: (p[0] if x[0] else 1-p[0])*(p[1] if x[1] else 1-p[1])
            for x in product((0, 1), repeat=2)}
    data = [summarize(mass, p, max), summarize(mass, p, lambda x: x[0]+2*x[1]),
            summarize({(0, 0): F(1, 2), (1, 1): F(1, 2)}, (F(1, 2), F(1, 2)), sum)]
    assert data == [(F(126, 625), [F(21, 250), F(21, 125)]),
                    (F(117, 100), [F(21, 100), F(24, 25)]), (F(1), [F(1, 4), F(1, 4)])]
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, axs = plt.subplots(1, 3, figsize=(11, 5.7), dpi=100, sharey=True)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.27, top=0.70, wspace=0.20)
    colors = ['#1764a0', '#c56812']
    titles = ['Independent, maximum', 'Independent, weighted sum', 'Dependent, shared input']
    subtitles = [r'$Z=\max(X_1,X_2)$', r'$W=X_1+2X_2$', r'$X_1=X_2=B,\quad W=2B$']
    for ax, (variance, halves), title, subtitle in zip(axs, data, titles, subtitles):
        v = float(variance); h = list(map(float, halves)); bound = sum(h)
        ax.bar(0, v, width=0.62, color='#45596b')
        ax.bar(1, h[0], width=0.62, color=colors[0])
        ax.bar(1, h[1], bottom=h[0], width=0.62, color=colors[1])
        ax.text(0, v+0.035, f'{v:g}', ha='center', weight='bold')
        ax.text(1, bound+0.035, f'{bound:g}', ha='center', weight='bold')
        ax.set_xticks([0, 1], ['Actual\nvariance', 'Replacement\nsum'])
        ax.set(xlim=(-0.6, 1.6), ylim=(0, 1.38))
        ax.set_title(title+'\n'+subtitle, fontsize=12, pad=17)
        ax.grid(axis='y', alpha=0.18); ax.set_axisbelow(True)
        ax.spines[['top', 'right']].set_visible(False)
    axs[0].set_ylabel('Variance or half squared-change expectation')
    axs[0].text(0.5, -0.38, 'Valid bound\n0.2016 ≤ 0.252', transform=axs[0].transAxes, ha='center', color='#1764a0')
    axs[1].text(0.5, -0.38, 'Equality\n1.17 = 0.21 + 0.96', transform=axs[1].transAxes, ha='center', color='#1764a0')
    axs[2].text(0.5, -0.38, 'NOT a valid bound\n1 > 0.25 + 0.25', transform=axs[2].transAxes, ha='center', color='#b13c32', weight='bold')
    axs[2].annotate('Independence fails', xy=(1, 0.51), xytext=(0.45, 0.85), ha='center',
                    fontsize=11, color='#b13c32', arrowprops={'arrowstyle': '->', 'color': '#b13c32'})
    fig.suptitle('Efron–Stein: a variance budget needs independent inputs', y=0.96, fontsize=17)
    fig.legend(handles=[Patch(color='#45596b', label='Actual variance'),
                        Patch(color=colors[0], label='Coordinate 1 contribution'),
                        Patch(color=colors[1], label='Coordinate 2 contribution')],
               loc='upper center', bbox_to_anchor=(0.5, 0.895), ncol=3, frameon=False, fontsize=11)
    fig.text(0.5, 0.035, 'Constructed models, exact enumeration • First two: p₁ = 0.3, p₂ = 0.6. Third: P(B = 1) = 0.5.', ha='center', fontsize=11)
    fig.savefig(Path(__file__).stem+'.png', dpi=100, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
