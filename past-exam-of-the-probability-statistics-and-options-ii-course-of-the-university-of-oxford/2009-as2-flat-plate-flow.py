"""Original streamline sketch; Python3.14,numpy2.3.5,matplotlib3.10.7.
Run in the output directory; writes same-basename PNG with a white background.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-3,3,700);y=np.linspace(-2.4,2.4,561)
X,Y=np.meshgrid(x,y);Z=X+1j*Y
root=np.sqrt(Z-1)*np.sqrt(Z+1)
w=(Z-1j*root)/np.sqrt(2)
psi=np.ma.array(w.imag,mask=(np.abs(Y)<.025)&(np.abs(X)<=1.025))
fig,ax=plt.subplots(figsize=(7.1,5.1),facecolor='white');ax.set_facecolor('white')
ax.contour(X,Y,psi,levels=np.arange(-3,3.01,.25),colors='#24719b',linewidths=.85)
ax.plot([-1,1],[0,0],color='black',lw=4,solid_capstyle='butt')
ax.plot([1/np.sqrt(2),-1/np.sqrt(2)],[0,0],'o',color='#d46a16',ms=6,zorder=5,label='Stagnation points on opposite faces')
ax.annotate('',(-1.7,-1.4),(-2.2,-1.9),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#24719b'})
ax.set(xlabel='$x/a$',ylabel='$y/a$',xlim=(-3,3),ylim=(-2.4,2.4),title=r'Flat plate in potential flow, $\alpha=\pi/4$')
ax.set_aspect('equal');ax.legend(loc='upper left',fontsize=9)
fig.tight_layout();fig.savefig(Path(__file__).stem+'.png',dpi=160,facecolor='white')
