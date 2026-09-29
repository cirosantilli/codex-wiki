"""Original plot of the constraint and elliptical contours; output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(7.5, 6.2), layout='constrained')
    theta = np.linspace(0, 2*np.pi, 801)
    for level in [1, 2, 3, 5, 8]:
        highlight = level == 3
        ax.plot(np.sqrt(level/2)*np.cos(theta), np.sqrt(level)*np.sin(theta),
                color='#1764ab' if highlight else '#aaaaaa', lw=2.2 if highlight else .8,
                label='$f=3$' if highlight else None)
    x = np.linspace(-.2, 3.4, 601)
    ax.plot(x, (x-2)**2, color='#b14928', lw=2.3, label=r'$y=(x-2)^2$')
    pts = [(np.sqrt(1.5),0),( -np.sqrt(1.5),0),(0,np.sqrt(3)),(0,-np.sqrt(3))]
    offsets = [(5,-20),(-52,-20),(8,3),(8,-5)]
    labels = [r'$(\sqrt{3/2},0)$',r'$(-\sqrt{3/2},0)$',r'$(0,\sqrt{3})$',r'$(0,-\sqrt{3})$']
    for (px, py), offset, label in zip(pts, offsets, labels):
        ax.scatter([px],[py],s=22,color='#1764ab',zorder=4)
        ax.annotate(label,(px,py),xytext=offset,textcoords='offset points',fontsize=10)
    ax.scatter([1],[1],s=48,color='black',zorder=5)
    ax.annotate('$(1,1)$: minimum', (1,1), xytext=(1.65,1.5),
                arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=10)
    ax.axhline(0,color='#555555',linewidth=.7)
    ax.axvline(0,color='#555555',linewidth=.7)
    ax.set(aspect='equal',xlim=(-2.1,3.4),ylim=(-2.35,3.35),xlabel='$x$',ylabel='$y$',
           title=r'$f=2x^2+y^2$: first contact at $f=3$')
    ax.legend(loc='lower right')
    ax.grid(alpha=.15)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
