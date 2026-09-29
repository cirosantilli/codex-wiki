"""Original Friedmann sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the same-basename opaque PNG to the caller's CWD.
Uses any MPLCONFIGDIR supplied by the caller without changing it.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    # C=4/9 and |Lambda|=4/3 give sinh(t), t, sin(t) powers 2/3.
    t = np.linspace(0, 3.4, 700)
    closed_t = np.unique(np.r_[np.linspace(0, np.pi, 700), np.pi / 2])
    fig, ax = plt.subplots(figsize=(7.0, 4.5), layout='constrained', facecolor='white')
    ax.plot(t, np.sinh(t) ** (2 / 3), label=r'$\Lambda>0$: $\sinh^{2/3}t$')
    ax.plot(t, t ** (2 / 3), label=r'$\Lambda=0$: $t^{2/3}$')
    ax.plot(closed_t, np.maximum(np.sin(closed_t), 0) ** (2 / 3),
            label=r'$\Lambda<0$: $\sin^{2/3}t$')
    ax.scatter([np.pi / 2, np.pi], [1, 0], color='C2', s=24, zorder=4)
    ax.annotate('maximum', (np.pi / 2, 1), xytext=(1.45, 1.65),
                arrowprops={'arrowstyle': '->', 'color': 'C2'})
    ax.annotate('recollapse', (np.pi, 0), xytext=(2.43, 0.55),
                arrowprops={'arrowstyle': '->', 'color': 'C2'})
    ax.set(xlabel='Dimensionless proper time', ylabel='Scale factor (common dust normalization)',
           title='Flat dust expansion and cosmological constant', xlim=(0, 3.45), ylim=(0, 6.3))
    ax.grid(alpha=0.2)
    ax.legend(loc='upper left')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
