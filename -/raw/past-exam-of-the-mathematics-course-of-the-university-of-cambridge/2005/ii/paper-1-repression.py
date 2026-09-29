"""Original mutual-repression phase plane. Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes only the same-basename opaque PNG to caller CWD.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,3.3,140);X,Y=np.meshgrid(x,x)
U=3/(1+Y*Y)-X;V=3/(1+X*X)-Y
fig,ax=plt.subplots(figsize=(5.9,5.1),dpi=120,facecolor='white')
ax.streamplot(x,x,U,V,color='#a0a8b5',density=1.0,linewidth=.7,arrowsize=.8)
ax.plot(3/(1+x*x),x,color='#007d76',label=r'$\dot x=0$')
ax.plot(x,3/(1+x*x),color='#b35c1b',label=r'$\dot y=0$')
lo=(3-np.sqrt(5))/2;hi=(3+np.sqrt(5))/2
ax.scatter([lo,hi],[hi,lo],s=65,color='#125bb3',label='stable equilibria',zorder=5)
mid=float(np.roots([1,0,1,-3])[np.isreal(np.roots([1,0,1,-3]))].real[0])
ax.scatter([mid],[mid],s=65,facecolor='white',edgecolor='#c93434',linewidth=1.8,label='saddle',zorder=6)
ax.set(xlim=(0,3.3),ylim=(0,3.3),xlabel='$x$',ylabel='$y$',title=r'Bounded mutual repression: $m=n=2$, $\lambda=3$')
ax.set_aspect('equal');ax.legend(fontsize=9,loc='upper right');fig.tight_layout()
fig.savefig('paper-1-repression.png',facecolor='white',transparent=False);plt.close(fig)
