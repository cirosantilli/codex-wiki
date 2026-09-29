"""Draw an original factorial trace; write the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 (no optional dependencies).
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


BLUE = '#235f91'
GREEN = '#287052'
INK = '#23313d'


def box(ax, x, y, width, text, color=BLUE, face='#eef5fb'):
    ax.add_patch(FancyBboxPatch((x - width / 2, y - 0.27), width, 0.54,
                              boxstyle='round,pad=0.04', edgecolor=color,
                              facecolor=face, linewidth=1.5))
    ax.text(x, y, text, ha='center', va='center', fontsize=12, color=INK)


def main():
    fig, ax = plt.subplots(figsize=(11, 6.6), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 11), ylim=(0, 6.6))
    ax.axis('off')
    ax.text(5.5, 6.22, 'Factorial: descend first, multiply on return',
            ha='center', fontsize=19, weight='bold', color=INK)
    ax.text(5.5, 5.84, 'F(0) = 1     •     F(n) = n × F(n − 1) for n ≥ 1',
            ha='center', fontsize=13, color=INK)
    for x, label in [(1.65, 'Calls descend'), (5.5, 'Deepest stack snapshot'),
                     (9.3, 'Answers return')]:
        ax.text(x, 5.35, label, ha='center', fontsize=14, weight='bold', color=INK)
    levels = [4.85, 4.02, 3.19, 2.36, 1.53]
    for i, n in enumerate(range(4, -1, -1)):
        color = GREEN if n == 0 else BLUE
        face = '#eaf5ed' if n == 0 else '#eef5fb'
        box(ax, 1.65, levels[i], 1.8, f'F({n})', color, face)
        if i < 4:
            ax.annotate('', xy=(1.65, levels[i + 1] + 0.32),
                        xytext=(1.65, levels[i] - 0.32),
                        arrowprops={'arrowstyle': '-|>', 'color': BLUE, 'lw': 1.8})
    frames = ['F(0): return 1', 'F(1): wait for 1 × result',
              'F(2): wait for 2 × result', 'F(3): wait for 3 × result',
              'F(4): wait for 4 × result']
    for i, text in enumerate(frames):
        box(ax, 5.5, levels[i], 2.95, text,
            GREEN if i == 0 else BLUE, '#eaf5ed' if i == 0 else '#eef5fb')
    ax.text(7.12, 4.85, 'active', ha='left', va='center', fontsize=11, color=GREEN)
    ax.text(5.5, 0.91, 'Each caller keeps its own n\nand its next instruction.',
            ha='center', va='center', fontsize=12, color=INK)
    results = ['4 × 6 = 24', '3 × 2 = 6', '2 × 1 = 2', '1 × 1 = 1', 'F(0) = 1']
    for i, label in enumerate(results):
        box(ax, 9.3, levels[i], 2.15, label, GREEN, '#eaf5ed')
        if i < 4:
            ax.annotate('', xy=(9.3, levels[i] - 0.32),
                        xytext=(9.3, levels[i + 1] + 0.32),
                        arrowprops={'arrowstyle': '-|>', 'color': GREEN, 'lw': 1.8})
    ax.text(1.65, 0.91, 'Five invocations.\nFour pending multiplications.',
            ha='center', va='center', fontsize=12, color=INK)
    ax.text(9.3, 0.91, 'Pop one completed frame;\nresume its caller.',
            ha='center', va='center', fontsize=12, color=INK)
    ax.text(5.5, 0.28, 'Reaching the base case starts the return journey; the outer call still has work to do.',
            ha='center', fontsize=12, color=INK)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
