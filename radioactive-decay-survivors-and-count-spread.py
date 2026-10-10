"""Illustrate a stipulated independent radioactive-decay model; write to cwd."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    initial = 1000
    half_life = 3.0
    rate = math.log(2) / half_life
    time = np.linspace(0, 12, 401)
    survival = np.exp(-rate * time)
    mean = initial * survival
    spread = np.sqrt(initial * survival * (1 - survival))
    rng = np.random.default_rng(7)
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 12})
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 5.0), dpi=120)
    fig.patch.set_facecolor('white')
    for index in range(9):
        lifetimes = rng.exponential(1 / rate, size=initial)
        survivors = initial - np.searchsorted(np.sort(lifetimes), time, side='right')
        left.step(time, survivors, where='post', color='#6e8da7', alpha=0.48,
                  linewidth=0.9, label='Independent simulated histories' if index == 0 else None)
    left.fill_between(time, mean - spread, mean + spread, color='#e6ab02', alpha=0.22,
                      label='Mean ± one standard deviation')
    left.plot(time, mean, color='#b45d08', linewidth=2.0, label='Exact expected survivor count')
    left.scatter([0, 3, 6, 9, 12], [1000, 500, 250, 125, 62.5], s=22, color='#b45d08', zorder=5)
    left.set(xlabel='Time (hours)', ylabel='Surviving parent nuclei', xlim=(0, 12), ylim=(0, 1040),
             title='One history has steps; the mean is smooth')
    left.set_xticks([0, 3, 6, 9, 12])
    left.grid(alpha=0.17)
    left.legend(loc='upper right', fontsize=8, framealpha=0.95)
    probability = 1 / 8
    count = np.arange(initial + 1)
    log_mass = np.array([math.lgamma(initial + 1) - math.lgamma(int(k) + 1)
                        - math.lgamma(initial - int(k) + 1)
                        + k * math.log(probability)
                        + (initial - k) * math.log1p(-probability) for k in count])
    mass = np.exp(log_mass)
    assert abs(mass.sum() - 1) < 2e-12
    right.bar(count, mass, width=0.9, color='#386f93', alpha=0.85)
    right.axvline(125, color='#b45d08', linestyle='--', linewidth=1.6, label='Mean = 125 nuclei')
    right.set(xlabel='Surviving parent nuclei after 9 hours', ylabel='Probability of this integer count',
              xlim=(70, 185), title='Exact binomial law after three half-lives')
    right.text(0.97, 0.93, 'N = 1000, p = 1/8\nStandard deviation ≈ 10.46 nuclei',
               ha='right', va='top', transform=right.transAxes, fontsize=9,
               bbox={'facecolor': 'white', 'edgecolor': '#dddddd', 'alpha': 0.95})
    right.grid(axis='y', alpha=0.17)
    right.legend(loc='upper left', fontsize=8)
    fig.text(0.5, 0.018, 'Chosen model only: constant independent decay rates, no replenishment and no detector effects.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.055, 1, 1), w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
