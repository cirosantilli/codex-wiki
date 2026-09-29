"""Original constant-electric-force velocity plot; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    time = np.linspace(0, 8, 601)
    initial_transverse_momentum = 0.75  # in units mc: initial velocity 0.6c
    den = np.sqrt(1+initial_transverse_momentum**2+time**2)
    parallel = time/den
    transverse = initial_transverse_momentum/den
    speed = np.hypot(parallel, transverse)
    fig, ax = plt.subplots(figsize=(6.9, 4.1), layout='constrained')
    ax.plot(time, parallel, color='#174ea6', lw=2.3, label=r'Along force: $v_\parallel/c$')
    ax.plot(time, transverse, color='#bb5566', lw=2.3, label=r'Transverse: $v_\perp/c$')
    ax.plot(time, speed, color='#228833', lw=1.7, ls='--', label=r'Total speed: $|\mathbf{v}|/c$')
    ax.axhline(1, color='#777777', lw=1, ls=':')
    ax.text(0.2, 1.015, 'Light-speed limit', fontsize=9, color='#555555')
    ax.set(xlim=(0, 8), ylim=(0, 1.09), xlabel=r'Scaled time $|e|Et/(mc)$',
           ylabel='Velocity in units of c', title='A fixed force does not imply fixed acceleration')
    ax.legend(loc='center right', frameon=False, fontsize=10)
    ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / '2018-q1-electric-velocity.png', dpi=150, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
