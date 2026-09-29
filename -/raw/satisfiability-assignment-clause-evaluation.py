"""Draw one SAT candidate evaluation; tested with Python 3.14 and matplotlib 3.10.7.

Run from _media; the opaque PNG is written to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.size': 13, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    ax.set(xlim=(0, 10), ylim=(0, 5.2))
    ax.axis('off')
    ink, blue, green = '#172c40', '#dfeefa', '#e0f3e9'
    ax.text(5, 4.9, 'Testing one complete assignment', ha='center', weight='bold', fontsize=20, color=ink)
    ax.text(5, 4.4, r'$F=(x\vee y)\wedge(\neg x\vee z)\wedge(\neg y\vee\neg z)$', ha='center', fontsize=18, color=ink)

    def box(x, y, width, height, text, color, size=16):
        ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle='round,pad=0.06,rounding_size=0.10', facecolor=color, edgecolor='#688397', linewidth=1.3))
        ax.text(x + width / 2, y + height / 2, text, ha='center', va='center', fontsize=size, color=ink)

    def arrow(start, end):
        ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle': '-|>', 'color': '#688397', 'lw': 1.5, 'mutation_scale': 13})

    ax.text(1.25, 3.85, 'Assignment', ha='center', color=ink, weight='bold')
    box(0.35, 1.15, 1.8, 2.35, '$x=0$\n\n$y=1$\n\n$z=0$', blue, 18)
    ax.text(4.05, 3.85, 'Literal values → OR', ha='center', color=ink, weight='bold')
    ax.text(6.75, 3.85, 'Clause values', ha='center', color=ink, weight='bold')
    rows = [(3.15, r'$x\vee y:\quad0\vee1$', r'$C_1=1$'),
            (2.30, r'$\neg x\vee z:\quad1\vee0$', r'$C_2=1$'),
            (1.45, r'$\neg y\vee\neg z:\quad0\vee1$', r'$C_3=1$')]
    for y, literals, clause in rows:
        arrow((2.22, y), (2.73, y))
        box(2.8, y - 0.30, 2.55, 0.60, literals, '#f3f7fa', 16)
        arrow((5.42, y), (6.02, y))
        box(6.1, y - 0.30, 1.25, 0.60, clause, green, 17)
        arrow((7.42, y), (8.12, 2.30))
    box(8.2, 1.75, 1.35, 1.1, 'AND\n$F=1$', green, 18)
    ax.text(5, 0.70, 'Every clause is true under the same assignment.', ha='center', fontsize=15, color=ink)
    ax.text(5, 0.28, '(0, 1, 0) is a satisfying assignment: the answer is SAT.', ha='center', fontsize=15, color='#17613e')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
