"""Original topology examples. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes the matching PNG into the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 5.0), facecolor='white', layout='constrained')
    colors = plt.get_cmap('viridis')(np.linspace(0.12, 0.8, 6))
    for panel, ax in enumerate(axes):
        ax.set_facecolor('white')
        for m, color in enumerate(colors, 1):
            eps = 1/(m+2)
            xs = [eps, eps, 1-eps, 1-eps]
            ys = [0, m, m, 0]
            ax.plot(xs, ys, color=color, lw=1.5)
        if panel:
            ax.plot([0.5,0.5], [1,6.7], color='#b4472f', lw=2.0)
            ax.annotate('Central ray', xy=(0.5,5.5), xytext=(0.66,6.35), fontsize=9,
                        arrowprops={'arrowstyle':'->','color':'#555555'})
        ax.scatter([0,1], [0,0], s=30, color='#b4472f', zorder=5)
        ax.annotate('p', (0,0), xytext=(-7,-15), textcoords='offset points')
        ax.annotate('q', (1,0), xytext=(3,-15), textcoords='offset points')
        ax.set(xlim=(-0.06,1.09), ylim=(-0.45,6.9), xlabel='Horizontal coordinate', ylabel='Height')
        ax.set_xticks([0,0.5,1]);ax.set_yticks([0,2,4,6])
        ax.spines[['top','right']].set_visible(False)
        ax.grid(alpha=0.13)
    axes[0].set_title('Separate arcs: p and q share a quasi-component', fontsize=10)
    axes[1].set_title('With a ray: each tail is connected', fontsize=10)
    fig.suptitle('Higher arcs escape every bounded region away from the two sides', fontsize=11)
    fig.savefig(Path.cwd()/'2010-escaping-arcs.png', dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
