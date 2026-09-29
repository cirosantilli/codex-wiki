"""Original phase portraits; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-65-predator-prey.png to the caller's working directory.
Caller-supplied MPLCONFIGDIR is left unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def main():
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.3), constrained_layout=True)
    cases = [(1.2, .4, 'Extinction'), (.6, .6, 'Predator extinction'), (.4, .3, 'Coexistence')]
    for ax, (a, b, title) in zip(axes[:3], cases):
        xs = np.linspace(0, 1.05, 110); ys = np.linspace(0, 1.6, 110)
        x, y = np.meshgrid(xs, ys)
        u = x*((1-a-x)/a-y); v=y*(x/b-1)
        ax.streamplot(xs, ys, u, v, density=.85, linewidth=.6, arrowsize=.8, color='#416c96')
        ax.plot(xs, np.maximum((1-a-xs)/a, 0), ':', color='#be7832', lw=1)
        ax.axvline(b, color='#be7832', ls=':', lw=1)
        points=[(0,0,'O')]
        if a<1: points.append((1-a,0,'E'))
        if a+b<1: points.append((b,(1-a-b)/a,'P'))
        for px,py,label in points:
            ax.plot(px,py,'ko',ms=4,clip_on=False);ax.annotate(label,(px,py),xytext=(5,5),textcoords='offset points')
        ax.set(xlim=(0,1.05),ylim=(0,1.6),xlabel='prey x',ylabel='predator y',title=f'{title}\na={a:g}, b={b:g}')
    ax=axes[3];aa=np.linspace(.001,1.5,700);bb=np.linspace(.001,1,600);a,b=np.meshgrid(aa,bb)
    regions=np.where(a>1,0,np.where(a+b>1,1,2));colors=['#cbd9e9','#ffe0b0','#b6e0c4']
    ax.pcolormesh(aa,bb,regions,cmap=ListedColormap(colors),vmin=0,vmax=2,shading='nearest',rasterized=True)
    ax.plot([1,1],[0,1],'k-',lw=1);ax.plot([0,1],[1,0],'k-',lw=1)
    ax.text(1.18,.5,'O sink',ha='center');ax.text(.75,.72,'E sink',ha='center');ax.text(.28,.23,'P sink',ha='center')
    ax.set(xlim=(0,1.5),ylim=(0,1),xlabel='a',ylabel='b',title='ODE parameter regions')
    fig.savefig('paper-65-predator-prey.png',dpi=150,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
