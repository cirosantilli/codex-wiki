"""Original singular-curve sketches. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

White PNG is saved to cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9.0,4.2),layout='constrained',facecolor='white')
x=np.linspace(0,1.75,800)
axes[0].plot(x,x*x+x**2.5,color='#0072b2',lw=2,label=r'$y_+$')
axes[0].plot(x,x*x-x**2.5,color='#d55e00',lw=2,label=r'$y_-$')
axes[0].plot(0,0,'o',color='#333333',ms=4)
axes[0].set(xlim=(-.05,1.75),ylim=(-1.1,7.3),title='Both real branches',xlabel='$x$',ylabel='$y$')
axes[0].legend(fontsize=10)
x=np.linspace(0,1.1,700)
axes[1].plot(x,x*x-x**2.5,color='#d55e00',lw=2)
points=[(0,0,'$O$'),(64/225,28672/759375,'$I$'),(16/25,256/3125,'$M$'),(1,0,'$Z$')]
for xx,yy,label in points:
    axes[1].plot(xx,yy,'o',color='#333333',ms=4)
    axes[1].annotate(label,(xx,yy),xytext=(5,8),textcoords='offset points',fontsize=10)
axes[1].set(xlim=(-.04,1.1),ylim=(-.07,.11),title='Lower branch: inflection, maximum, zeros',xlabel='$x$',ylabel=r'$y_-$')
axes[1].set_xticks([0,64/225,16/25,1],['$0$',r'$64/225$',r'$16/25$','$1$'])
for ax in axes:
    ax.axhline(0,color='#777777',lw=.8);ax.grid(alpha=.17)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
