"""Render discrete and continuous expected-value examples to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.array([-1., 2., 8.])
    probabilities = np.array([.5, .3, .2])
    mean = np.dot(values, probabilities)
    assert np.isclose(probabilities.sum(), 1)
    assert np.isclose(mean, 1.7)
    assert np.isclose(np.dot(values - mean, probabilities), 0)
    assert np.isclose(np.dot(values**2, probabilities), 14.5)
    assert np.isclose(np.dot(abs(values), probabilities), 2.7)
    assert mean not in values
    y = np.linspace(0, 1, 4001)
    density = 2*y
    integrand = y*density
    assert np.isclose(np.trapezoid(density, y), 1)
    assert np.isclose(np.trapezoid(integrand, y), 2/3, atol=1e-7)

    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14})
    fig, (discrete, continuous) = plt.subplots(
        1, 2, figsize=(12, 5.6), dpi=120, facecolor='white')
    discrete.vlines(values, 0, probabilities, color='#246ea0', lw=4)
    discrete.scatter(values, probabilities, s=75, color='#246ea0', zorder=4)
    for value, mass in zip(values, probabilities):
        discrete.text(value, mass+.028, f'P(X = {value:g}) = {mass:g}',
                      ha='center', fontsize=11, color='#205d87')
    discrete.axvline(mean, color='#c06620', linestyle='--', lw=2,
                     label=r'$E[X]=1.7$')
    discrete.scatter([mean], [0], s=120, marker='^', color='#c06620',
                     zorder=5, clip_on=False)
    discrete.text(.5, 1.14, r'$(-1)(0.5)+2(0.3)+8(0.2)=1.7$',
                  transform=discrete.transAxes, fontsize=12, ha='center')
    discrete.set(xlim=(-2.7, 9.7), ylim=(0, .65),
                 xlabel='Outcome x', ylabel='Probability mass',
                 title='Discrete mean: a balance point, not an outcome')
    discrete.set_xticks([-1, 2, 8], ['−1', '2', '8'])
    discrete.legend(loc='upper right', frameon=False)

    continuous.plot(y, density, color='#657687', lw=2, linestyle='--',
                    label=r'Density $f_Y(y)=2y$: area 1')
    continuous.plot(y, integrand, color='#2c8467', lw=3,
                    label=r'Weighted curve $y f_Y(y)=2y^2$')
    continuous.fill_between(y, 0, integrand, color='#2c8467', alpha=.22)
    continuous.text(.12, .9, r'Shaded area $=E[Y]=2/3$',
                    color='#20614c', fontsize=13,
                    bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9})
    continuous.set(xlim=(0, 1), ylim=(0, 2.25), xlabel='Outcome y',
                   ylabel='Curve height (dimensionless)',
                   title='Continuous mean: weight the density by y')
    continuous.legend(loc='upper left', frameon=False, fontsize=10.5)
    for ax in (discrete, continuous):
        ax.grid(color='#e6eaed', alpha=.8)
        ax.spines[['top', 'right']].set_visible(False)
    fig.suptitle('Expected value combines outcomes with their probabilities',
                 fontsize=16, y=.97)
    fig.text(.5, .035, 'Both examples use dimensionless outcomes; all probability weights sum or integrate to one',
             ha='center', fontsize=11)
    fig.subplots_adjust(left=.075, right=.98, bottom=.20, top=.82, wspace=.30)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
