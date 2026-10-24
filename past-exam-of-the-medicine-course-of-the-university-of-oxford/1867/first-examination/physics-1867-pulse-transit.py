"""Original finite-speed pressure-pulse model; write the PNG to CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
These are illustrative model curves, not measured patient data.
"""
from pathlib import Path
import os
root = next(p for p in Path(__file__).resolve().parents if (p / 'ourbigbook.json').is_file())
os.environ.setdefault('MPLCONFIGDIR', str(root / '_out/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    t = np.linspace(-0.05, 0.4, 1501)
    distance, speed, first = 0.5, 5.0, 0.1
    delay = distance/speed
    pulse = lambda z: np.exp(-0.5*((z-first)/0.025)**2)
    fig, ax = plt.subplots(figsize=(8.4, 4.6), layout='constrained')
    fig.set_facecolor('white')
    ax.set_facecolor('white')
    ax.plot(t*1000, pulse(t), lw=2.3, color='#24618b', label='First sensor')
    ax.plot(t*1000, pulse(t-delay), lw=2.3, color='#c46c25', label='Second sensor, 0.5 m farther')
    for time in [first, first+delay]:
        ax.axvline(time*1000, color='#aaaaaa', ls=':', lw=1)
    ax.annotate('', ((first+delay)*1000, 1.1), (first*1000, 1.1),
                arrowprops=dict(arrowstyle='<->', lw=1.3, color='#333333'))
    ax.text((first+delay/2)*1000, 1.13, r'$\Delta t=L/c=100$ ms', ha='center')
    ax.set(xlim=(-50, 400), ylim=(-0.04, 1.32),
           xlabel='Time (ms)', ylabel='Pressure increment (arbitrary units)',
           title=r'Finite propagation: $p(L,t)=p(0,t-L/c)$')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(color='#e2e2e2', lw=0.7)
    ax.text(0.02, 0.07, 'Illustrative model: c = 5 m/s.\nNo patient measurements are plotted.',
            transform=ax.transAxes, fontsize=10, va='bottom',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.92, pad=3))
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=130, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
