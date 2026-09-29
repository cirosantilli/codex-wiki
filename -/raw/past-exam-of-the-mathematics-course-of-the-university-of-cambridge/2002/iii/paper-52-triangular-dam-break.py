"""Original triangular-channel characteristic plot. Python 3.14; root pinned deps.
Emit the basename PNG to the caller's CWD; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(figsize=(7.4, 4.5), constrained_layout=True)
    t = np.linspace(0, 1.6, 500)
    ax.fill_betweenx(t, -t, 4*t, color='#e8f1fb', label='Rarefaction fan')
    for speed in np.linspace(-1, 4, 12):
        ax.plot(speed*t, t, color='#83acd4', lw=.7)
    for entry in [.06, .15, .32, .55, .85]:
        tt = np.linspace(entry, 1.6, 350)
        xx = 4*tt-5*entry**.4*tt**.6
        ax.plot(xx, tt, color='#d9762b', lw=1.2)
        tr = np.linspace(0, entry, 70)
        ax.plot(tr-2*entry, tr, color='#d9762b', lw=1.2)
    ax.plot(-t, t, color='#214e79', lw=2, label=r'Fan back: $x=-c_0t$')
    ax.plot(4*t, t, color='#8b2635', lw=2, label=r'Dry front: $x=4c_0t$')
    ax.plot([], [], color='#d9762b', label=r'Plus family: $u+c$')
    ax.text(-2.04, 1.2, 'Undisturbed\nreservoir', ha='center', fontsize=9)
    ax.text(5.9, .7, 'Dry bed', ha='center', fontsize=10)
    ax.set(xlabel=r'$x/(c_0t_{\rm ref})$', ylabel=r'$t/t_{\rm ref}$', xlim=(-2.7, 7), ylim=(0, 1.65), title='Triangular-channel dry-bed release')
    ax.grid(alpha=.18)
    ax.legend(loc='upper right', fontsize=8)
    fig.savefig(Path.cwd() / 'paper-52-triangular-dam-break.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)

if __name__ == '__main__':
    main()
