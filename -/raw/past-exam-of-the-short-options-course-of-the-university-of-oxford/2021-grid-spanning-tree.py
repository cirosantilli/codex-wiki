"""Kruskal tree on the ASO weighted grid; Python 3.14, NumPy/Matplotlib per pyproject.toml."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def main():
    n = 5
    fig, ax = plt.subplots(figsize=(6.6, 6.0), layout='constrained')
    count, cost = 0, 0.
    for y in range(1, n+1):
        for x in range(1, n):
            selected = x >= y-1
            ax.plot([x, x+1], [y, y], color='#1b78ad' if selected else '#dce1e5',
                    lw=3 if selected else 1.2, zorder=2 if selected else 1)
            if selected:
                count += 1
                cost += y
    for x in range(1, n+1):
        for y in range(1, n):
            selected = y >= x
            ax.plot([x, x], [y, y+1], color='#cf6227' if selected else '#dce1e5',
                    lw=3 if selected else 1.2, zorder=2 if selected else 1)
            if selected:
                count += 1
                cost += x+.5
    assert count == n*n-1
    assert np.isclose(cost, (n-1)*(4*n*n+13*n+12)/12)
    xx, yy = np.meshgrid(np.arange(1, n+1), np.arange(1, n+1))
    ax.scatter(xx, yy, s=32, color='#253442', zorder=3)
    ax.set(xticks=range(1,n+1), yticks=range(1,n+1), xlabel=r'Column $x$ (vertical cost $x+1/2$)',
           ylabel=r'Row $y$ (horizontal cost $y$)', title=fr'Kruskal tree: $n={n}$, cost ${cost:g}$',
           xlim=(.6, n+.4), ylim=(.6,n+.4), aspect='equal')
    ax.legend(handles=[Line2D([0],[0], color='#1b78ad', lw=3, label=r'Horizontal: $x\geq y-1$'),
                       Line2D([0],[0], color='#cf6227', lw=3, label=r'Vertical: $y\geq x$'),
                       Line2D([0],[0], color='#dce1e5', lw=2, label='Rejected')],
              loc='upper center', bbox_to_anchor=(.5, -.14), frameon=False, fontsize=10)
    ax.spines[['top','right']].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
