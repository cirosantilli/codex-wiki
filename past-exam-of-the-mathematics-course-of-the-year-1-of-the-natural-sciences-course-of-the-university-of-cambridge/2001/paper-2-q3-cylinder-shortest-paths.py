"""Cylinder winding choices and distance graphs. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, (ax, graph) = plt.subplots(1, 2, figsize=(10.8, 4.5), dpi=120, layout='constrained')
    ax.axhline(0, color='.65', lw=.8)
    ax.axhline(1, color='.75', lw=.8)
    ax.plot([0, -np.pi/2], [0, 1], color='#21779a', lw=2.6, label=r'Shortest lift: $k=-1$')
    ax.plot([0, 3*np.pi/2], [0, 1], '--', color='#b86633', lw=1.8, label=r'Longer lift: $k=0$')
    ax.scatter([0, -np.pi/2, 3*np.pi/2], [0, 1, 1], c=['black', '#21779a', '#b86633'], s=35, zorder=5)
    ax.annotate('Start', (0, 0), xytext=(6, -17), textcoords='offset points')
    ax.annotate('Same endpoint', (-np.pi/2, 1), xytext=(-8, 12), textcoords='offset points', color='#21779a')
    ax.annotate('Same endpoint', (3*np.pi/2, 1), xytext=(-72, 12), textcoords='offset points', color='#b86633')
    ax.annotate('', xy=(3*np.pi/2, 1.38), xytext=(-np.pi/2, 1.38), arrowprops={'arrowstyle': '<->', 'color': '.35'})
    ax.text(np.pi/2, 1.47, r'$2\pi$ between lifts', ha='center')
    ax.set(xlim=(-2.3, 5.4), ylim=(-.35, 1.9), xlabel=r'Unrolled coordinate $u=\phi$ (radius one)', ylabel='z', title=r'Two lifts of $(\phi_1,z_1)=(3\pi/2,1)$', xticks=[-np.pi/2, 0, 3*np.pi/2], xticklabels=[r'$-\pi/2$', '0', r'$3\pi/2$'], yticks=[0, 1])
    ax.legend(loc='upper left', bbox_to_anchor=(0, -.19), fontsize=9, frameon=False)
    angle = np.linspace(0, 2*np.pi, 1001)
    m = np.minimum(angle, 2*np.pi-angle)
    graph.plot(angle, m, color='#b86633', lw=2.1, label=r'$z_1=0:\quad L=m$')
    graph.plot(angle, np.sqrt(1+m*m), color='#21779a', lw=2.1, label=r'$z_1=1:\quad L=\sqrt{1+m^2}$')
    graph.axvline(np.pi, color='.6', ls=':', lw=1)
    graph.scatter([np.pi, np.pi], [np.pi, np.sqrt(1+np.pi*np.pi)], color=['#b86633', '#21779a'], s=25, zorder=5)
    graph.annotate(r'$\sqrt{1+\pi^2}$', (np.pi, np.sqrt(1+np.pi*np.pi)), xytext=(12, 10), textcoords='offset points', color='#21779a')
    graph.annotate(r'$\pi$', (np.pi, np.pi), xytext=(-21, -17), textcoords='offset points', color='#b86633')
    graph.set(xlim=(0, 2*np.pi), ylim=(-.08, 3.75), xlabel=r'Endpoint angle $\phi_1$', ylabel='Shortest length L', title=r'$m=\min(\phi_1,2\pi-\phi_1)$', xticks=[0, np.pi, 2*np.pi], xticklabels=['0', r'$\pi$', r'$2\pi$'], yticks=[0, 1, 2, 3])
    graph.grid(alpha=.15)
    graph.legend(loc='upper center', bbox_to_anchor=(.5, -.19), fontsize=9, frameon=False)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
