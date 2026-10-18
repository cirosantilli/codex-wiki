"""Plot the unloaded series-RC / parallel-RC voltage divider response."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 14, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    w = np.logspace(-3, 3, 1801)
    transfer = 1/(3+1j*(w-1/w))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4), layout='constrained')
    axes[0].semilogx(w, abs(transfer), color='#1c6591', lw=2.5)
    axes[0].plot([1], [1/3], 'o', color='#333333')
    axes[0].annotate(r'$|H(1)|=1/3$', (1, 1/3), xytext=(3, 0.30), arrowprops={'arrowstyle': '->', 'color': '#444444'}, fontsize=12)
    axes[0].set(title='Amplitude ratio', ylabel=r'$|V_{\rm out}/V_{\rm in}|$', ylim=(0, 0.37))
    axes[1].semilogx(w, np.angle(transfer, deg=True), color='#147d63', lw=2.5)
    axes[1].axhline(0, color='#777777', lw=0.8)
    axes[1].plot([1], [0], 'o', color='#333333')
    axes[1].set(title='Output phase relative to input', ylabel='Phase (degrees)', ylim=(-100, 100), yticks=[-90, -45, 0, 45, 90])
    for ax in axes:
        ax.axvline(1, color='#777777', ls=':', lw=1.2)
        ax.grid(which='both', alpha=0.2)
        ax.set(xlabel=r'$\omega RC$', xlim=(1e-3, 1e3))
    fig.suptitle('Series RC feeding parallel RC: unloaded output, positive polarity', fontsize=15)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
