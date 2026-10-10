"""Chosen wire-address and calibrated charge-centroid toy models.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
No measured data; adjacent anode wires need not obey this assumed linear law.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.7), facecolor='white')
    fig.subplots_adjust(left=.075, right=.97, bottom=.20, top=.73, wspace=.29)
    blue, orange = '#166ca3', '#c96213'
    ax = axes[0]
    pitch = np.linspace(.2, 3, 150)
    ax.plot(pitch, pitch / np.sqrt(12), color=blue, lw=2.5)
    for p in (1., 2.):
        sd = p / np.sqrt(12)
        ax.scatter(p, sd, color=blue, zorder=3)
        ax.annotate(f'{sd:.3f} mm', (p, sd), xytext=(8, 8), textcoords='offset points', fontsize=10)
    ax.set(xlabel='Chosen pitch p (mm)', ylabel='Error standard deviation (mm)',
           xlim=(0, 3.05), ylim=(0, .95), title='Wire address only')
    ax.text(.08, .87, r'$\sigma_x=p/\sqrt{12}$', transform=ax.transAxes, fontsize=15)
    ax.text(.08, .72, 'One correct nearest-wire address\nUniform positions within each cell',
            transform=ax.transAxes, fontsize=10)
    ax.grid(alpha=.18)
    ax = axes[1]
    u = np.linspace(0, 1, 401)
    p, relative_noise = 2., .02
    sigma = p * relative_noise * np.sqrt((1-u)**2 + u**2)
    ax.plot(u, sigma, color=blue, lw=2.5, label='First-order noise estimate')
    g = 1.1
    bias = p * (g*u/(1-u+g*u)-u)
    ax.plot(u, bias, color=orange, lw=2, linestyle='--', label='Bias if right gain = 1.10')
    ax.scatter(.5, p*relative_noise/np.sqrt(2), color=blue, zorder=3)
    ax.annotate('0.0283 mm', (.5, p*relative_noise/np.sqrt(2)),
                xytext=(0, -22), textcoords='offset points', ha='center', fontsize=10)
    ax.set(xlabel='True fractional position u = x/p', ylabel='Position scale (mm)',
           xlim=(0,1), ylim=(0,.062), title='Two calibrated linear charge signals')
    ax.set_xticks([0,.25,.5,.75,1])
    ax.text(.04, .94, r'$q_L=Q(1-u),\quad q_R=Qu$', transform=ax.transAxes, va='top', fontsize=12)
    ax.grid(alpha=.18)
    ax.legend(loc='lower center', bbox_to_anchor=(.5, -.32), frameon=False, fontsize=9)
    fig.suptitle('Pitch is not a universal resolution guarantee', fontsize=17, y=.97)
    fig.text(.5, .86, 'Chosen teaching models • no measured chamber data', ha='center', fontsize=12)
    fig.text(.5, .80, 'Right panel: p = 2 mm, s/Q = 0.02; no thresholds; small independent channel noise',
             ha='center', fontsize=10)
    fig.text(.5, .025, 'The linear sharing law must be calibrated. Ordinary adjacent anode wires need not obey it.',
             ha='center', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
