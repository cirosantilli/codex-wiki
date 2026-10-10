"""Explicitly stipulated PCR yield models, not observations or fitted kinetics.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run from _media; output uses this script's basename in the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

INITIAL = 100.0
CEILING = 1e8
CYCLES = 40


def model():
    n = np.arange(CYCLES + 1)
    ideal = INITIAL * 2.0 ** n
    constant = INITIAL * 1.8 ** n
    plateau = np.empty(CYCLES + 1)
    efficiency = np.empty(CYCLES + 1)
    plateau[0] = INITIAL
    for k in n:
        efficiency[k] = .9 * (1 - plateau[k] / CEILING)
        if k < CYCLES:
            plateau[k + 1] = plateau[k] * (1 + efficiency[k])
    return n, ideal, constant, plateau, efficiency


def main():
    n, ideal, constant, plateau, efficiency = model()
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.25), dpi=120, facecolor='white')
    fig.subplots_adjust(left=.095, right=.965, top=.80, bottom=.20, wspace=.31)
    fig.suptitle('PCR yield and cycle efficiency: stipulated models', fontsize=16, y=.97)
    fig.text(.5, .89, 'Calculated illustrations only — no laboratory observations. Initial amount N₀ = 100.', ha='center', fontsize=11)
    colors = ['#1769aa', '#c46c1b', '#22835c']
    labels = ['Ideal: Eₙ = 1', 'Constant: Eₙ = 0.8', 'Ceiling model: Eₙ = 0.9(1 − Nₙ/K)']
    for amounts, color, label in zip([ideal, constant, plateau], colors, labels):
        axes[0].plot(n, amounts, color=color, label=label, lw=2.5)
    axes[0].set_yscale('log')
    axes[0].set_ylim(50, 3e14)
    axes[0].set_ylabel('Amplifiable amount Nₙ (copy equivalents)')
    axes[0].axhline(CEILING, color='#777777', lw=1, ls=':')
    axes[0].text(1, CEILING * 1.6, 'Assigned K = 10⁸', fontsize=10, color='#555555')
    axes[0].set_title('Yield (logarithmic vertical scale)', fontsize=12)
    for e, color in zip([np.ones(n.size), np.full(n.size, .8), efficiency], colors):
        axes[1].plot(n, e, lw=2.5, color=color)
    axes[1].set_ylim(-.04, 1.09)
    axes[1].set_ylabel('Eₙ: fractional new yield in cycle n → n + 1')
    axes[1].set_title('Efficiency assigned to the next cycle', fontsize=12)
    for ax in axes:
        ax.set_xlim(0, CYCLES)
        ax.set_xlabel('Completed cycles n')
        ax.grid(alpha=.18)
        ax.spines[['top', 'right']].set_visible(False)
    fig.legend(*axes[0].get_legend_handles_labels(), loc='lower center', bbox_to_anchor=(.5, .045), ncol=3, fontsize=9, frameon=False)
    fig.text(.5, .018, 'Nₙ₊₁ = Nₙ(1 + Eₙ). The ceiling model is an imposed illustration, not a chemical mechanism.', ha='center', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
