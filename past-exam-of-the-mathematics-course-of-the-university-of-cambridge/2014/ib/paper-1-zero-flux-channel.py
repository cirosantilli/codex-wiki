"""Original zero-flux channel profile. Saves only its PNG basename in cwd.
Tested on Python 3.14 with NumPy 2.3.5 and matplotlib 3.10.7.
The caller controls MPLCONFIGDIR; this script does not override it.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    depth = np.linspace(0, 1, 601)
    velocity = 3*depth**2-2*depth
    fig, ax = plt.subplots(figsize=(6.6, 4.4), dpi=100, facecolor='white')
    ax.plot(velocity, depth, color='#006e9c', linewidth=2.4)
    ax.fill_betweenx(depth, velocity, 0, where=velocity < 0, color='#a53f00', alpha=0.18)
    ax.fill_betweenx(depth, 0, velocity, where=velocity >= 0, color='#006e9c', alpha=0.15)
    ax.axvline(0, color='0.5', linewidth=0.8)
    ax.axhline(0, color='0.25', linewidth=1)
    ax.axhline(1, color='0.25', linewidth=1)
    ax.scatter([-1/3, 0, 1], [1/3, 2/3, 1], color='#006e9c', zorder=4)
    ax.annotate(r'Minimum $u/U=-1/3$', (-1/3, 1/3), xytext=(0.12, 0.3),
                arrowprops={'arrowstyle': '->', 'color': '0.3'}, fontsize=10)
    ax.text(0.1, 0.68, 'Flow changes direction', fontsize=10)
    ax.text(0.5, 0.09, 'Resting lower wall', ha='center', fontsize=10)
    ax.text(0.5, 0.93, 'Upper wall moves at U', ha='center', fontsize=10)
    ax.set(xlim=(-0.43, 1.12), ylim=(-0.02, 1.02), xlabel=r'Velocity $u/U$', ylabel=r'Height $y/h$',
           title='Zero flux: adverse pressure balances the moving wall')
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig('paper-1-zero-flux-channel.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
