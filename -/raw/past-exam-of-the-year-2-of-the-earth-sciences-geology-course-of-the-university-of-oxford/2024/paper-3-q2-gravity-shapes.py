"""Original infinite-strike gravity models, not traced from the source figure.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; basename PNG to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def profile(x, top, bottom, burial=.04):
    z = np.linspace(burial,1.04,2501)
    b = top+(bottom-top)*(z-burial)
    # Vertical attraction integrated analytically along x and infinite strike.
    return -np.trapezoid(np.arctan((b[:,None]-x)/z[:,None])-np.arctan((-b[:,None]-x)/z[:,None]),z,axis=0)


def main():
    plt.rcParams.update({'font.size':10})
    fig, axes = plt.subplots(2,3,figsize=(11.5,5.6),layout='constrained',gridspec_kw={'height_ratios':[2,1]})
    x = np.linspace(-2.5,2.5,1001)
    for j,(top,bottom,title) in enumerate(((1,.45,'Narrows downward'),(.72,.72,'Vertical sides'),(.45,1,'Widens downward'))):
        g = profile(x,top,bottom); g /= abs(g.min())
        grad = np.abs(np.gradient(g,x)); k=np.argmax(grad[:len(x)//2])
        ax=axes[0,j]; ax.plot(x,g,color='#175b89',lw=2)
        ax.plot([x[k],-x[k]],[g[k],g[k]],'o',color='#a42f21',label='Maximum slope')
        ax.axhline(0,color='0.5',lw=.7);ax.axhline(-.5,color='0.6',lw=.6,ls=':')
        ax.set(title=title,xlabel='Across strike (relative distance)',ylabel='Gravity / |central minimum|',ylim=(-1.12,.08))
        ax.legend(fontsize=8,loc='upper right')
        ax=axes[1,j]; ax.add_patch(Polygon([(-top,.04),(top,.04),(bottom,1.04),(-bottom,1.04)],facecolor='#e9d7b9',edgecolor='black'))
        ax.axhline(0,color='0.3',lw=.8);ax.set(xlim=(-2.5,2.5),ylim=(1.2,-.1),ylabel='Depth');ax.set_xticks([])
    fig.suptitle('Negative density contrast: slope position within a gravity trough\nSame thickness; normalized amplitudes; infinite strike and flat observation surface')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
