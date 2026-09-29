"""Render advanced-coordinate Schwarzschild radial null rays to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def outgoing_ray(initial_radius):
    radius, advanced = [initial_radius], [0.0]
    step = 0.002
    def slope(r):
        return 0.5*(1-1/r)
    while advanced[-1] < 6 and 0.08 < radius[-1] < 3.6:
        r = radius[-1]
        k1 = slope(r)
        k2 = slope(r+step*k1/2)
        k3 = slope(r+step*k2/2)
        k4 = slope(r+step*k3)
        radius.append(r+step*(k1+2*k2+2*k3+k4)/6)
        advanced.append(advanced[-1]+step)
    return np.array(radius), np.array(advanced)


def main():
    fig, ax = plt.subplots(figsize=(7, 5), dpi=130, facecolor='white')
    ax.set_facecolor('white')
    ax.axvspan(0, 1, color='#f9e7da', alpha=0.8)
    ax.axvline(1, color='0.2', ls='--', lw=1.5)
    ax.annotate('', xy=(1, 5.7), xytext=(1, 4.9),
                arrowprops={'arrowstyle': '-|>', 'color': '0.2', 'lw': 1.4})
    for initial in [0.3, 0.57, 0.82, 1.16, 1.48, 1.95, 2.55]:
        r, v = outgoing_ray(initial)
        ax.plot(r, v, color='#b76722', lw=1.5)
        j = max(1, len(r)//2)
        jump = max(1, min(100, len(r)//8))
        end = min(j+jump, len(r)-1)
        ax.annotate('', xy=(r[end], v[end]), xytext=(r[j], v[j]),
                    arrowprops={'arrowstyle': '-|>', 'color': '#b76722', 'lw': 1.4})
    for v in [1.2, 3.0, 4.8]:
        ax.plot([0.12, 3.4], [v, v], color='#245f91', lw=1.4)
        for r in [0.67, 2.6]:
            ax.annotate('', xy=(r-0.23, v), xytext=(r+0.23, v),
                        arrowprops={'arrowstyle': '-|>', 'color': '#245f91', 'lw': 1.4})
    ax.text(0.5, 5.6, 'Black-hole\ninterior', ha='center', va='center', fontsize=10)
    ax.text(1.05, 0.2, 'Horizon', rotation=90, va='bottom', fontsize=10)
    ax.set(xlim=(0, 3.5), ylim=(0, 6), xlabel=r'Areal radius $r/r_s$',
           ylabel=r'Advanced time $cv/r_s$',
           title='Future-directed radial light rays')
    ax.legend(handles=[Line2D([], [], color='#245f91', label='Ingoing: constant v'),
                       Line2D([], [], color='#b76722', label='Outgoing null family')],
              loc='upper right', fontsize=9, framealpha=0.95)
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path('2017-advanced-null-rays.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
