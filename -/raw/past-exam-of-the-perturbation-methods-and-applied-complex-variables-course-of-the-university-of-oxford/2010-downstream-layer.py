"""Original exact-solution plot; Python 3.14; root NumPy/Matplotlib versions.
Writes PNG to the current working directory. Uses standard-library erfc.
"""
from math import erfc
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-6,35,450);y=np.linspace(0,12,190);X,Y=np.meshgrid(x,y)
b=np.sqrt(np.maximum((np.hypot(X,Y)-X)/2,0));U=np.vectorize(erfc,otypes=[float])(b)
fig,ax=plt.subplots(figsize=(8,3.7),layout='constrained',facecolor='white')
im=ax.pcolormesh(X,Y,U,vmin=0,vmax=1,cmap='Blues',shading='auto')
cs=ax.contour(X,Y,U,levels=[.1,.5,.9],colors='#b34227',linewidths=1)
ax.clabel(cs,inline=True,fmt='u = %.1f',fontsize=9)
ax.plot([0,35],[0,0],color='#b34227',lw=2)
ax.set(xlabel='x',ylabel='y',title='Mixed-boundary convection–diffusion: downstream layer widens as √x')
fig.colorbar(im,ax=ax,label='u')
fig.savefig('2010-downstream-layer.png',dpi=155,facecolor='white')
