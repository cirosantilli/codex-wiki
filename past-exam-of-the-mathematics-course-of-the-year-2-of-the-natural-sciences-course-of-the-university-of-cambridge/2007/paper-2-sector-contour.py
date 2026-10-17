"""Original sector-contour illustration for reciprocal-binomial integrals.

Writes the PNG basename to the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    n, radius, inner = 5, 1.5, .17
    angle = 2*np.pi/n
    fig, ax = plt.subplots(figsize=(6.8, 5.8), layout='constrained')
    theta = np.linspace(0, angle, 501)
    outer = radius*np.exp(1j*theta)
    small = inner*np.exp(1j*theta)
    polygon = np.concatenate([outer, small[::-1]])
    ax.fill(polygon.real, polygon.imag, color='#dceaf7', alpha=.65)
    for z in [np.array([inner, radius]), outer,
              np.array([inner, radius])*np.exp(1j*angle), small]:
        ax.plot(z.real, z.imag, color='#1764ab', lw=2)
    for start, end in [(.55+.0j, 1.0+.0j),
                       (radius*np.exp(.48j), radius*np.exp(.70j)),
                       (1.0*np.exp(1j*angle), .55*np.exp(1j*angle)),
                       (inner*np.exp(.9j), inner*np.exp(.35j))]:
        ax.annotate('', (end.real,end.imag), (start.real,start.imag),
                    arrowprops={'arrowstyle':'-|>','color':'#1764ab','lw':1.8})
    roots=np.exp(1j*(2*np.arange(n)+1)*np.pi/n)
    ax.scatter(roots.real,roots.imag,s=38,color='#777777',label='other roots',zorder=4)
    ax.scatter([roots[0].real],[roots[0].imag],s=54,color='#b14928',label='enclosed pole',zorder=5)
    ax.annotate(r'$z_0=e^{i\pi/n}$', (roots[0].real,roots[0].imag),
                xytext=(8,9),textcoords='offset points')
    ax.annotate(r'$2\pi/n$', (.38*np.cos(angle),.38*np.sin(angle)),
                xytext=(-31,0),textcoords='offset points')
    ax.annotate(r'$\epsilon$',(.12,.13),xytext=(.32,.24),
                arrowprops={'arrowstyle':'->','color':'#555555'})
    ax.axhline(0,color='#888888',lw=.7)
    ax.axvline(0,color='#888888',lw=.7)
    ax.set(aspect='equal',xlim=(-1.2,1.8),ylim=(-1.25,1.75),
           xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',
           title='Illustrative sector contour: n=5')
    ax.legend(loc='lower right',fontsize=10)
    ax.grid(alpha=.15)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
