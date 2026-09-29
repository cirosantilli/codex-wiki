"""Original coupled-endpoint Green-kernel figure; writes matching PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white',
                     'axes.facecolor': 'white', 'savefig.facecolor': 'white'})

def green(x, source):
    return (source-1)*x+1-2*source+np.maximum(x-source,0)

fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.7), layout='constrained')
x=np.linspace(1,2,601)
for source,color in [(1.25,'#21618c'),(1.75,'#a93226')]:
    axes[0].plot(x,green(x,source),color=color,lw=2,label=rf'$\xi={source}$')
    axes[0].scatter([source],[green(source,source)],color=color,s=28,zorder=3)
    axes[0].axvline(source,color=color,ls=':',alpha=.45)
axes[0].set(xlabel='$x$',ylabel=r'$g(x,\xi)$',xlim=(1,2),
            title='Continuous values; unit slope jumps')
axes[0].grid(alpha=.2)
axes[0].legend(loc='lower right')
source=np.linspace(1,2,251)
X,S=np.meshgrid(x,source)
defect=green(X,S)-green(S,X)
im=axes[1].pcolormesh(X,S,defect,shading='auto',cmap='RdBu_r',vmin=-2,vmax=2,rasterized=True)
axes[1].plot([1,2],[1,2],color='#333',lw=.8,ls='--')
axes[1].set(xlabel='$x$',ylabel=r'$\xi$',title=r'$g(x,\xi)-g(\xi,x)=2(x-\xi)$',aspect='equal')
fig.colorbar(im,ax=axes[1],label='Reciprocity defect',shrink=.9)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
