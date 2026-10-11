"""Original periodic graph. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

White PNG is saved to cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi,2*np.pi,1100)
y=np.exp(np.sin(x)**2)
fig,ax=plt.subplots(figsize=(7.0,3.7),layout='constrained',facecolor='white')
ax.plot(x,y,color='#0072b2',lw=2)
minima=np.arange(-1,3)*np.pi
maxima=np.array([-.5,.5,1.5])*np.pi
ax.plot(minima,np.ones_like(minima),'o',color='#009e73',ms=5,label='Minima')
ax.plot(maxima,np.full_like(maxima,np.e),'o',color='#d55e00',ms=5,label='Maxima')
ax.set(xlim=(-np.pi-.15,2*np.pi+.15),ylim=(.75,3.0),xlabel=r'$x$',ylabel=r'$y$',
       title=r'$y=\exp(\sin^2 x)$: period $\pi$')
ax.set_xticks(np.array([-1,-.5,0,.5,1,1.5,2])*np.pi,
              [r'$-\pi$',r'$-\pi/2$','$0$',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'])
ax.set_yticks([1,np.e],['$1$','$e$'])
ax.legend(loc='upper right',ncols=2,fontsize=9)
ax.grid(alpha=.18)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
