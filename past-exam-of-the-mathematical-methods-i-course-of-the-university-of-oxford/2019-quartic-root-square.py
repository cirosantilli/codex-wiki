"""Original Argand diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

The only output is the same-basename PNG in the caller's working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(4.8, 4.6), dpi=120, facecolor='white')
    ax.set_facecolor('white')
    t = np.linspace(0, 2*np.pi, 500)
    ax.plot(np.cos(t), np.sin(t), color='#aeb8c1', ls='--', lw=1.1, label='Unit circle')
    z = np.exp(1j*(np.pi/4 + np.arange(4)*np.pi/2))
    ax.plot(np.r_[z.real,z.real[0]], np.r_[z.imag,z.imag[0]], color='#25679c', lw=1.2)
    ax.scatter(z.real,z.imag,color='#25679c',s=45,zorder=4)
    labels=[r'$\frac{1+i}{\sqrt{2}}$',r'$\frac{-1+i}{\sqrt{2}}$',
            r'$\frac{-1-i}{\sqrt{2}}$',r'$\frac{1-i}{\sqrt{2}}$']
    for w,label in zip(z,labels):
        ax.annotate(label,(w.real,w.imag),xytext=(10*np.sign(w.real),12*np.sign(w.imag)),
                    textcoords='offset points',ha='left' if w.real>0 else 'right',
                    va='bottom' if w.imag>0 else 'top',fontsize=13,color='#173248')
    ax.axhline(0,color='#687b8c',lw=.8);ax.axvline(0,color='#687b8c',lw=.8)
    ax.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),aspect='equal',xticks=[-1,0,1],yticks=[-1,0,1])
    ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part')
    ax.set_title(r'Four roots of $z^4=-1$',pad=12)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(length=0,colors='#526473')
    fig.tight_layout(pad=1.3)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False,
                metadata={'Software':'codex-wiki quartic root diagram'})
    plt.close(fig)


if __name__=='__main__':
    main()
