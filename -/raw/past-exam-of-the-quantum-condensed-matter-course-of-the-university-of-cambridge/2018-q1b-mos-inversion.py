"""Original biased MOS band schematic; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(8.4, 4.8), layout='constrained')
    ax.axvspan(-1.2, -0.6, color='#dddddd')
    ax.axvspan(-0.6, 0, color='#e9f0fb')
    ax.axvspan(0, 1.6, color='#fff3d7')
    ax.axvspan(0, 0.12, color='#b8e2df')
    x = np.linspace(0, 3.1, 450)
    bend = 0.6 * np.maximum(1-x/1.6, 0)**2
    ax.plot(x, 0.85-bend, color='#174ea6', lw=2.3)
    ax.plot(x, -0.25-bend, color='#bb5566', lw=2.3)
    ax.plot(x, 0.30-bend, color='#888888', lw=1, ls=':')
    ax.plot([0, 3.1], [0, 0], color='#111111', lw=1.3, ls='--')
    ax.plot([-1.2, -0.6], [-0.75, -0.75], color='#111111', lw=1.5, ls='--')
    ax.plot([-0.6, 0], [1.8, 2.2], color='#174ea6', lw=1.8)
    ax.plot([-0.6, 0], [-2.7, -2.3], color='#bb5566', lw=1.8)
    for boundary in [-0.6, 0]:
        ax.axvline(boundary, color='#777777', lw=0.8)
    ax.text(-0.9, 2.65, 'Metal\ngate (+)', ha='center', fontsize=10)
    ax.text(-0.3, 2.65, 'Oxide', ha='center', fontsize=10)
    ax.text(1.6, 2.65, 'p-type semiconductor', ha='center', fontsize=11)
    ax.text(-1.14, -0.55, r'$\widetilde\mu_g$', fontsize=12)
    ax.text(2.15, 0.06, r'$\widetilde\mu_s$', fontsize=12)
    ax.text(2.82, 0.94, r'$E_C$', color='#174ea6', fontsize=12)
    ax.text(2.82, -0.55, r'$E_V$', color='#bb5566', fontsize=12)
    ax.text(2.82, 0.34, r'$E_{\mathrm{intrinsic}}$', color='#666666', ha='right', fontsize=9)
    ax.annotate('Incipient n layer', xy=(0.06, 0.33), xytext=(0.45, 1.7),
                arrowprops={'arrowstyle':'->', 'color':'#333333'}, fontsize=10)
    ax.annotate('', xy=(0.13, -1.35), xytext=(1.6, -1.35),
                arrowprops={'arrowstyle':'<->', 'color':'#775511'})
    ax.text(0.86, -1.65, 'Depletion region\n(negative acceptor ions)', ha='center', va='top', fontsize=9)
    ax.text(2.45, -1.65, 'Neutral bulk\n(holes dominate)', ha='center', va='top', fontsize=9)
    ax.set(xlim=(-1.2, 3.1), ylim=(-3, 3.15), xlabel='Position normal to interface',
           ylabel='Electron energy (schematic)', title='Positive gate bends substrate bands downward')
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(Path.cwd() / '2018-q1b-mos-inversion.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
