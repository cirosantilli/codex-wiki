"""Original normalized Hamaker and DLVO examples; Python 3.14/numpy/matplotlib.

DLVO W=-1/x^2+B exp(-x/lambda), B=1.8, chosen dimensionless examples.
No short-range repulsive core is included; the near-zero divergence is outside
this continuum sketch. Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(2,2,figsize=(10,6.5),layout='constrained')
fig.patch.set_facecolor('white')
x=np.linspace(.7,5,700)
axes[0,0].plot(x,-x**-6,color='#9274a0',label='Atom pair: −x⁻⁶')
axes[0,0].plot(x,-x**-2,color='#2d718b',label='Half-spaces: −x⁻²')
axes[0,0].set(xlabel='Separation / reference separation',ylabel='Separately normalized potential',
              title='Different dimensions; shared normalized comparison',ylim=(-2.5,.1))
axes[0,0].legend(fontsize=8)
for ax,length,title in [(axes[0,1],.4,'High screening: example without a barrier'),
                         (axes[1,0],4,'Low screening: a positive barrier')]:
    xx=np.geomspace(.5,80,1800)
    attraction=-1/xx**2
    repulsion=1.8*np.exp(-xx/length)
    total=attraction+repulsion
    ax.plot(xx,attraction,'--',color='#9274a0',label='Attractive contribution')
    ax.plot(xx,repulsion,':',color='#b6623e',label='Repulsive contribution')
    ax.plot(xx,total,color='#2d718b',lw=2,label='Total')
    ax.set(xlim=(.5,18),ylim=(-1.6,1.4),xlabel='Separation (normalized)',
           ylabel='Energy per area (normalized)',title=title)
    if length==4:
        ix=np.argmax(total)
        ax.annotate('Barrier',xy=(xx[ix],total[ix]),xytext=(7,1),fontsize=10,
                    arrowprops={'arrowstyle':'->','color':'.3'})
    ax.legend(fontsize=7.7,loc='lower right')
ax=axes[1,1]
xx=np.linspace(25,90,1800)
total=-1/xx**2+1.8*np.exp(-xx/4)
ax.plot(xx,total,color='#2d718b',lw=2)
ax.set(xlabel='Separation (normalized)',ylabel='Energy per area (normalized)',
       title='Low-salt far tail: eventually attractive',ylim=(-.00075,.0022))
imin=np.argmin(total)
ax.annotate('Shallow secondary minimum',xy=(xx[imin],total[imin]),
            xytext=(50,.00125),fontsize=9,arrowprops={'arrowstyle':'->','color':'.3'})
for ax in axes.flat:
    ax.axhline(0,color='.5',lw=.7);ax.grid(alpha=.15)
fig.savefig('paper-2-hamaker-dlvo.png',dpi=150,facecolor='white')
plt.close(fig)
