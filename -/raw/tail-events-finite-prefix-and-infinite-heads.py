"""Draw finite-prefix ambiguity for a literal tail event (Python 3.14)."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=110, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 5.4))
    ax.axis('off')
    blue, orange, green, ink = '#1766a3', '#d16a13', '#16815b', '#202a35'
    ax.text(0.3, 5.02, 'The same finite record has opposite infinite extensions',
            fontsize=17, weight='bold', color=ink)
    ax.text(0.3, 4.65, '1 = heads     0 = tails     A = infinitely many heads', fontsize=12, color=ink)
    ax.add_patch(FancyBboxPatch((0.3, 1.35), 2.55, 2.72,
                              boxstyle='round,pad=0.08', facecolor='#eaf3fa', edgecolor=blue))
    ax.text(1.58, 3.8, 'Same observed prefix', ha='center', fontsize=12, color=blue)
    for y in (3.1, 2.1):
        ax.text(1.58, y, '0  0  1  0', ha='center', fontsize=18, weight='bold', color=blue)
    ax.plot([3.15, 3.15], [1.65, 3.55], '--', color='#97a1ab', lw=1.5)
    ax.text(3.15, 3.9, 'unobserved future', ha='left', fontsize=12, color=ink)
    ax.text(3.5, 3.1, '1  0  1  0  1  0  …', fontsize=18, color=green)
    ax.text(3.5, 2.71, 'Continue alternating forever: belongs to A', fontsize=12, color=green)
    ax.text(3.5, 2.1, '0  0  0  0  0  0  …', fontsize=18, color=orange)
    ax.text(3.5, 1.71, 'Continue with tails forever: outside A', fontsize=12, color=orange)
    ax.text(0.3, 0.82, 'Edit any finite prefix → membership in A stays the same.', fontsize=13, color=ink)
    ax.text(0.3, 0.4, 'But the exact first-head time can change: 0 0 1 0 → 1 0 1 0.', fontsize=12, color=ink)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png', facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
