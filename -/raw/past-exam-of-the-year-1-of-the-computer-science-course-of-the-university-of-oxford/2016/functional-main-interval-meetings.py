"""Plot the four-interval meeting counterexample; write a PNG to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5,
as documented by the repository's top-level pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    intervals = [(0, 1), (1, 3), (2, 4), (4, 5)]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.5), sharey=True)
    fig.patch.set_facecolor('white')
    for ax, times, title, colour in [
        (axes[0], [0.5, 2.5, 4.5], 'Choose 2.5 first: three meetings', '#bb3030'),
        (axes[1], [1, 4], 'Earliest ends: two meetings', '#177342'),
    ]:
        ax.set_facecolor('white')
        for i, (start, end) in enumerate(intervals):
            y = 4 - i
            ax.plot([start, end], [y, y], '-o', color='#285a92', lw=4,
                    ms=6, solid_capstyle='round', zorder=3)
        for t in times:
            ax.axvline(t, color=colour, lw=1.5, ls='--', alpha=0.9)
        ax.set_title(title, fontsize=12)
        ax.set_xlim(-0.3, 5.3)
        ax.set_ylim(0.5, 4.5)
        ax.set_xticks([0, 1, 2, 2.5, 3, 4, 5] if ax is axes[0]
                      else [0, 1, 2, 3, 4, 5])
        ax.set_yticks([4, 3, 2, 1], ['Person 1', 'Person 2', 'Person 3', 'Person 4'])
        ax.set_xlabel('Meeting time')
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='x', alpha=0.15)
    fig.tight_layout(pad=1.3)
    fig.savefig(Path(__file__).stem + '.png', dpi=130, facecolor='white',
                transparent=False, metadata={'Software': 'codex-wiki figure generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
