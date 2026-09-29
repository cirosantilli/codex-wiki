"""Original shared-genome schematic; Python 3.14, matplotlib 3.10.7.

Run from _media with MPLBACKEND=Agg. The toy genes and outputs are invented.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle

COLORS = {'H': '#54846b', 'A': '#b96528', 'B': '#5969b0'}
GENES = ('H', 'A', 'B')
EXPRESSION = ({'H', 'A'}, {'H', 'B'})


def main():
    fig, ax = plt.subplots(figsize=(10, 5.7), dpi=140, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 5.7))
    ax.axis('off')
    ax.text(5, 5.4, 'Shared genome, different expression', ha='center', fontsize=20, weight='bold')
    ax.text(5, 5.03, 'Two illustrative nucleated cell states — not measured cell types', ha='center', fontsize=11)
    for x, active, name in zip((2.65, 7.35), EXPRESSION, ('State 1', 'State 2')):
        ax.add_patch(FancyBboxPatch((x-2.05, 1.67), 4.1, 3, boxstyle='round,pad=0.08,rounding_size=0.3', facecolor='#f5f7fb', edgecolor='#526177', linewidth=1.5))
        ax.text(x, 4.34, name, ha='center', fontsize=15, weight='bold')
        ax.add_patch(FancyBboxPatch((x-1.5, 3.01), 3, 0.95, boxstyle='round,pad=0.05', facecolor='white', edgecolor='#53647c'))
        ax.text(x, 3.76, 'Nucleus: all three genes retained', ha='center', fontsize=10)
        for j, gene in enumerate(GENES):
            gx = x - 0.95 + 0.95*j
            ax.add_patch(Rectangle((gx-0.32, 3.13), 0.64, 0.36, facecolor='white', edgecolor=COLORS[gene], linewidth=2))
            ax.text(gx, 3.31, gene, ha='center', va='center', fontsize=12, color=COLORS[gene], weight='bold')
            if gene in active:
                ax.add_patch(FancyArrowPatch((gx, 3.04), (gx, 2.67), arrowstyle='-|>', mutation_scale=12, color=COLORS[gene]))
                ax.add_patch(Circle((gx, 2.45), 0.16, color=COLORS[gene]))
                ax.text(gx, 2.14, gene+' on', ha='center', fontsize=11, color=COLORS[gene])
            else:
                ax.text(gx, 2.45, 'off', ha='center', va='center', fontsize=11, color='#6c707a')
        ax.text(x, 1.85, 'Colored outputs: illustrative RNA / protein production', ha='center', fontsize=9)
    ax.text(5, 1.22, 'Same H, A, B sequences; different activity patterns', ha='center', fontsize=13, weight='bold')
    ax.text(5, 0.86, 'Three independently switchable toy genes allow 2³ = 8 profiles.', ha='center', fontsize=11)
    ax.text(5, 0.33, 'Caveat: mature mammalian red blood cells lose their nucleus.\nThey are not two nucleated states with shared nuclear DNA.', ha='center', va='center', fontsize=11, color='#7a2f2f', bbox={'boxstyle':'round,pad=0.35', 'fc':'#fff4f1', 'ec':'#bd8175'})
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.03, top=0.98)
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
