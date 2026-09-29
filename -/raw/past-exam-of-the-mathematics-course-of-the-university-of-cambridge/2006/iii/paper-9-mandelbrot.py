"""Original parameter-plane sketch; tested with Python 3.14 and root dependencies."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
xr=np.linspace(-2.1,.7,900);yr=np.linspace(-1.3,1.3,840)
C=xr[None,:]+1j*yr[:,None]
Z=np.zeros_like(C);active=np.ones(C.shape,dtype=bool)
for _ in range(420):
 Z[active]=Z[active]**2+C[active]
 active[active]=np.abs(Z[active])<=2
fig,ax=plt.subplots(figsize=(7.2,6),facecolor='white')
ax.imshow(active.astype(int),extent=(xr[0],xr[-1],yr[0],yr[-1]),origin='lower',cmap=ListedColormap(['white','#202020']),interpolation='nearest')
t=np.linspace(0,2*np.pi,800);lam=np.exp(1j*t);card=lam/2-lam**2/4
ax.plot(card.real,card.imag,color='#3174b5',lw=1,label='Main cardioid boundary')
ax.plot(-1+.25*np.cos(t),.25*np.sin(t),color='#bb6f20',lw=1,label='Period-two bulb boundary')
for point,label,end in [(.25,'cusp $c=1/4$',(.38,.43)),(-.75,'attachment $c=-3/4$',(-1.73,-.49))]:
 ax.plot(point,0,'o',color='#a93831',ms=4,zorder=5)
 ax.annotate(label,xy=(point,0),xytext=end,fontsize=10,arrowprops={'arrowstyle':'->','color':'#a93831'},ha='left')
ax.plot([-2,.25],[0,0],color='#202020',lw=.8)
ax.axhline(0,color='#888888',lw=.4,zorder=0);ax.axvline(0,color='#888888',lw=.4,zorder=0)
ax.set(xlabel='$\\operatorname{Re} c$',ylabel='$\\operatorname{Im} c$',title='Mandelbrot set: an informal parameter-plane sketch',xlim=(-2.1,.85),ylim=(-1.3,1.3))
ax.legend(loc='lower right',fontsize=9,frameon=False);fig.tight_layout();fig.savefig('paper-9-mandelbrot.png',dpi=150,facecolor='white')
