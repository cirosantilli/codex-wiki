"""Original Euler-Heun geometry; emits an opaque PNG to the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})
    fig, (ax, zoom) = plt.subplots(1, 2, figsize=(11, 4.8),
                                  gridspec_kw={'width_ratios': [1.6, 1]}, layout='constrained')
    h, k1 = 0.2, 1.0
    k2 = 1 + h * k1
    euler, heun = 1 + h * k1, 1 + h * (k1 + k2) / 2
    exact = math.exp(h)
    t = np.linspace(0, h, 200)
    ax.plot(t, np.exp(t), color='black', lw=2, label='Exact $e^t$')
    ax.plot([0, h], [1, euler], color='#2675ad', lw=2, label='$k_1=1$: Euler predictor')
    ax.plot([0, h], [1, 1 + h * k2], '--', color='#b35412', lw=1.6,
            label='$k_2=1.2$ transported to start')
    ax.plot([0, h], [1, heun], color='#268544', lw=2,
            label='Mean slope $1.1$: Heun output')
    tx = np.array([0.175, 0.225])
    ax.plot(tx, euler + k2 * (tx - h), color='#b35412', lw=2.5)
    ax.scatter([0, h], [1, euler], s=50, color='#2675ad', zorder=5)
    ax.scatter([h], [heun], s=45, color='#268544', zorder=5)
    ax.annotate('Stage 2 samples $f$ here\n$(0.2,1.2)$; slope $k_2=1.2$',
                xy=(h, euler), xytext=(0.07, 1.032),
                arrowprops={'arrowstyle': '->', 'color': '#b35412'}, color='#b35412')
    ax.annotate('Stage 1: $(0,1)$', xy=(0, 1), xytext=(0.012, 0.995))
    ax.set(xlim=(-0.005, 0.235), ylim=(0.98, 1.258), xlabel='Time $t$', ylabel='State $y$',
           title='Two sampled slopes, one averaged increment')
    ax.legend(loc='upper left', fontsize=9, framealpha=1)
    ax.grid(alpha=.2)
    xs = [0.0, 0.65, 1.3]
    for x, y, color in zip(xs, [euler, heun, exact], ['#2675ad', '#268544', 'black']):
        zoom.scatter(x, y, s=70, color=color, zorder=5)
        zoom.annotate(f'{y:.9f}', (x, y), xytext=(0, -21 if x == .65 else 9),
                      textcoords='offset points', ha='center', fontsize=10)
    zoom.axhline(euler, color='#2675ad', lw=1, alpha=.4)
    zoom.axhline(heun, color='#268544', lw=1, alpha=.4)
    zoom.axhline(exact, color='black', lw=1, alpha=.4)
    zoom.annotate('', xy=(.29, heun), xytext=(.29, euler),
                  arrowprops={'arrowstyle': '<->', 'color': '#2675ad'})
    zoom.text(.32, 1.210, '$d=0.020000$', va='center', fontsize=10)
    zoom.annotate('', xy=(1.68, exact), xytext=(1.68, heun),
                  arrowprops={'arrowstyle': '<->', 'color': '#268544'})
    zoom.text(.78, 1.233, 'Heun local defect\n$0.001402758$', ha='center', color='#268544')
    zoom.set(xlim=(-.3, 1.85), ylim=(1.196, 1.239), ylabel='Endpoint state (magnified)',
             title='Pair difference versus actual defect', xticks=xs,
             xticklabels=['Euler', 'Heun', 'Exact'])
    zoom.grid(axis='y', alpha=.2)
    fig.suptitle("Euler-Heun on $y'=y$, $y(0)=1$, $h=0.2$", fontsize=15)
    fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
