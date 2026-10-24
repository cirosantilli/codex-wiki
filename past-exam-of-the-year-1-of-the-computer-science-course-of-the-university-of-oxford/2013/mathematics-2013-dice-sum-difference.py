"""Question 8: joint support of two fair-dice sum and difference; PNG to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7+dfsg1 and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
Run this script by absolute path from the desired output directory.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', str(Path(__file__).resolve().parents[2] / '_out' / 'matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(7.2, 4.8), layout='constrained')
    fig.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set_axisbelow(True)
    ax.grid(color='#e5e5e5', linewidth=0.7)
    ax.axvline(7, color='#ce5846', linestyle='--', linewidth=1)
    ax.axhline(0, color='#ce5846', linestyle='--', linewidth=1)
    sums, differences = zip(*[(a+b, a-b) for a in range(1, 7) for b in range(1, 7)])
    ax.scatter(sums, differences, s=62, color='#237890', zorder=3,
               label='Each filled point has probability 1/36')
    ax.scatter([7], [0], marker='x', s=100, linewidth=2, color='#bc362b', zorder=4)
    ax.annotate('Marginal modes: (7, 0)\nJoint probability = 0', xy=(7, 0),
                xytext=(8.2, 3.4), ha='left', va='center', color='#9c2922',
                bbox={'facecolor': 'white', 'edgecolor': '#d6a39d', 'boxstyle': 'round,pad=0.4'},
                arrowprops={'arrowstyle': '->', 'color': '#9c2922', 'connectionstyle': 'arc3,rad=0.1'})
    ax.set(xlim=(1.4, 12.6), ylim=(-5.6, 5.6), xticks=range(2, 13), yticks=range(-5, 6),
           xlabel=r'Sum $X=S_1+S_2$', ylabel=r'Difference $Y=S_1-S_2$',
           title='Two fair dice: the 36 possible sum and difference pairs')
    ax.legend(loc='lower center', fontsize=9, framealpha=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=140, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
