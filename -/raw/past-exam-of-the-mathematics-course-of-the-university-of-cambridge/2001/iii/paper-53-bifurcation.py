#!/usr/bin/env python3
"""Original attracting-orbit sketch for the quadratic period-doubling cascade."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

MU_INFINITY = 1.40115518909205


def draw():
    parameters = np.unique(np.concatenate((np.linspace(0, 1.35, 1400),
        np.linspace(1.35, MU_INFINITY, 1600))))
    orbit = np.zeros_like(parameters)
    for _ in range(6000):
        orbit = 1 - parameters * orbit * orbit
    samples = []
    for _ in range(128):
        orbit = 1 - parameters * orbit * orbit
        samples.append(orbit.copy())
    figure, ax = plt.subplots(figsize=(9.2, 5.5), facecolor='white')
    ax.set_facecolor('white')
    ax.scatter(np.tile(parameters, 128), np.concatenate(samples), s=.07,
               color='#1e3e55', alpha=.35, rasterized=True, linewidths=0)
    for value, label in [(0.75, r'$b_1=3/4$'), (1.25, r'$b_2=5/4$')]:
        ax.axvline(value, color='#777777', linestyle='--', linewidth=.8)
        ax.text(value - .014, -.535, label, ha='right', fontsize=11)
    superstable = [(1., r'$s_1$'), (1.31070264133683, r'$s_2$'),
                   (1.38154748443206, r'$s_3$')]
    ax.scatter([p[0] for p in superstable], np.zeros(3), s=30,
               color='#b24b31', zorder=4, label='Critical-point returns: superstable cycles')
    for value, label in superstable:
        ax.annotate(label, (value, 0), xytext=(-13, -29), textcoords='offset points',
                    fontsize=11, ha='right', arrowprops={'arrowstyle':'-', 'color':'#b24b31'})
    ax.axvline(MU_INFINITY, color='#b24b31', linewidth=1)
    ax.text(MU_INFINITY - .01, 1.015, r'$s_\infty$', ha='right', va='bottom', fontsize=12)
    ax.text(.33, .42, 'Stable fixed point', color='#1e3e55', fontsize=12)
    ax.text(.94, -.32, 'Period 2', color='#1e3e55', fontsize=12)
    ax.text(MU_INFINITY-.01, -.48, '4, 8, 16, ...', ha='right', color='#1e3e55', fontsize=11)
    inset = ax.inset_axes([.065, .12, .35, .30])
    mask = parameters >= 1.36
    inset.scatter(np.tile(parameters[mask], 128), np.asarray(samples)[:,mask].ravel(),
                  s=.12, color='#1e3e55', alpha=.4, linewidths=0)
    inset.set(xlim=(1.36, MU_INFINITY), ylim=(-.42,.17),
              title='Central branches (zoom)')
    inset.set_xticks([1.37, 1.40])
    inset.tick_params(labelsize=8)
    inset.title.set_fontsize(9)
    inset.grid(alpha=.12)
    ax.set(xlim=(0, MU_INFINITY + .02), ylim=(-.59, 1.09),
           xlabel=r'Parameter $\mu$', ylabel='Attracting orbit value $x$',
           title=r'Quadratic map $x\mapsto1-\mu x^2$: primary cascade')
    ax.grid(alpha=.13)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', fontsize=10, framealpha=.95)
    figure.tight_layout()
    figure.savefig(Path('paper-53-bifurcation.png'), dpi=150,
                   facecolor='white', transparent=False)
    plt.close(figure)


if __name__ == '__main__':
    draw()
