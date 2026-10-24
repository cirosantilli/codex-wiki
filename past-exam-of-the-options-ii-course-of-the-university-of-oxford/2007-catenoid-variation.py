"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-2,2,12001);C=np.cosh(2);y=np.cosh(x);eta=y-C
fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained',facecolor='white')
for ax in axes:ax.set_facecolor('white');ax.grid(alpha=.18)
axes[0].plot(x,y,lw=2.2,label='Stationary profile')
for s in [-.06,.06]:axes[0].plot(x,y+s*eta,ls='--',label=f'Perturbation s={s:+.2f}')
axes[0].scatter([-2,2],[C,C],c='black',s=22,zorder=5);axes[0].set(xlabel='$x$',ylabel='Radius',title='Same positive endpoint radii');axes[0].legend(fontsize=8)
ss=np.linspace(-.08,.08,161)
areas=[2*np.pi*np.trapezoid((y+s*eta)*np.sqrt(1+((1+s)*np.sinh(x))**2),x)for s in ss];J0=2*np.pi*np.trapezoid(y*np.sqrt(1+np.sinh(x)**2),x)
axes[1].plot(ss,np.array(areas)-J0,color='#a63603',lw=2);axes[1].scatter([0],[0],c='black',s=22,zorder=5);axes[1].set(xlabel='Endpoint-preserving perturbation $s$',ylabel='$J(s)-J(0)$',title='A stationary area with a decreasing direction')
fig.suptitle('Zero mean curvature does not ensure a local area minimum')
fig.savefig(Path.cwd()/'2007-catenoid-variation.png',dpi=170,facecolor='white')
