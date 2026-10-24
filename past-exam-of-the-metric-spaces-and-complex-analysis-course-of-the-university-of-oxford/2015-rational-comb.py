"""Generate 2015-rational-comb.png in the current directory; Python 3.14, NumPy/Matplotlib."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.8), dpi=110, facecolor='white')
    teeth = np.unique(np.r_[np.arange(-2, 13) / 5, 1.0])
    for panel, ax in enumerate(axes):
        for q in teeth:
            color = '#2563eb' if q < 1 else '#b45309' if q > 1 else '#15803d'
            ax.plot([q, q], [0, 1], color=color, lw=1.3, alpha=0.8)
        ax.plot([-0.45, 2.45], [1, 1], color='#334155', lw=2)
        if panel:
            ax.scatter([1], [1], s=85, facecolors='white', edgecolors='#111827', lw=1.7, zorder=6)
            ax.annotate('deleted point', xy=(1, 1), xytext=(1.25, 1.18),
                        fontsize=9, arrowprops={'arrowstyle': '->', 'lw': 0.8})
            ax.text(1.045, 0.42, 'residual tooth', rotation=90, color='#15803d', fontsize=9)
        else:
            ax.plot([0.4, 0.4, 1.8, 1.8], [0.25, 1, 1, 0.6], color='#b91c1c', lw=2.7)
        ax.set(xlim=(-0.45, 2.45), ylim=(-0.06, 1.32), xlabel='$x$', ylabel='$y$')
        ax.set_yticks([0, 1])
        ax.set_xticks([0, 1, 2])
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_facecolor('white')
        ax.set_title('A path through the top line' if not panel else 'Connected, but no escape path from the tooth', fontsize=10)
    fig.tight_layout(pad=1.6)
    fig.savefig('2015-rational-comb.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
