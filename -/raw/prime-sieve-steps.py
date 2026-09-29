"""Draw all four sieve passes through 60; write the PNG in the working directory.

Run from _media: MPLBACKEND=Agg python ../prime-sieve-steps.py
Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from math import isqrt
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


def sieve_steps(limit):
    removed = set()
    steps = []
    for p in range(2, isqrt(limit) + 1):
        if p in removed:
            continue
        marked = set(range(p * p, limit + 1, p))
        newly = marked - removed
        steps.append((p, removed.copy(), newly))
        removed.update(marked)
    return steps, sorted(set(range(2, limit + 1)) - removed)


def main():
    steps, primes = sieve_steps(60)
    # Independent trial division checks every survivor and removed integer.
    direct = [n for n in range(2, 61)
              if all(n % d for d in range(2, isqrt(n) + 1))]
    assert primes == direct
    assert [p for p, _, _ in steps] == [2, 3, 5, 7]
    assert [len(new) for _, _, new in steps] == [29, 9, 3, 1]
    assert steps[2][2] == {25, 35, 55}
    assert steps[3][2] == {49}
    assert len(primes) == 17

    colors = dict(new='#b7d7ee', old='#e5e5e5', candidate='#ffffff',
                  prime='#d4ecd8', excluded='#f5f5f5')
    fig, axes = plt.subplots(2, 2, figsize=(10.2, 8.4), dpi=110,
                             facecolor='white')
    for i, (ax, (p, old, newly)) in enumerate(zip(axes.flat, steps)):
        ax.set(xlim=(0, 10), ylim=(0, 6), aspect='equal')
        ax.axis('off')
        survivors = 59 - len(old | newly)
        ax.set_title(f'Pass p = {p}: start at {p}² = {p*p}\n'
                     f'{len(newly)} newly marked; {survivors} survivors',
                     fontsize=12, pad=12)
        for n in range(1, 61):
            x, y = (n - 1) % 10, 5 - (n - 1) // 10
            status = ('excluded' if n == 1 else 'old' if n in old
                      else 'new' if n in newly else 'prime' if i == 3
                      else 'candidate')
            ax.add_patch(Rectangle((x + .04, y + .04), .92, .92,
                                  facecolor=colors[status],
                                  edgecolor='#2c7545' if n == p else '#b8c0c6',
                                  linewidth=2.2 if n == p else .6))
            ax.text(x + .5, y + .5, str(n), ha='center', va='center',
                    fontsize=11, color='#7b7b7b' if status == 'old' else '#20313c',
                    fontweight='bold' if status in ('new', 'prime') or n == p
                    else 'normal')
            if n == 1:
                ax.plot([x + .18, x + .82], [y + .18, y + .82],
                        color='#9b9b9b', linewidth=1)

    fig.suptitle('Sieve through 60: each pass removes only composite numbers',
                 fontsize=16, y=.975)
    handles = [Patch(facecolor=colors[k], edgecolor='#b8c0c6', label=label)
               for k, label in [('new', 'Newly marked'), ('old', 'Marked earlier'),
                                ('candidate', 'Candidate'), ('prime', 'Final prime')]]
    fig.legend(handles=handles, loc='lower center', ncol=4, frameon=False,
               bbox_to_anchor=(.5, .055), fontsize=10)
    fig.text(.5, .025, '1 is excluded.  The outlined cell is p; it is never marked.  '
             'Stop: the next candidate is 11, and 11² > 60.',
             ha='center', fontsize=10)
    fig.subplots_adjust(left=.035, right=.965, top=.87, bottom=.14,
                        wspace=.12, hspace=.38)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
