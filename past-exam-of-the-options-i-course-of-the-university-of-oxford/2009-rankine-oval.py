"""Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Write the PNG in CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-1.1,2.1,560);y=np.linspace(-1.25,1.25,440)
X,Y=np.meshgrid(x,y);Z=X+1j*Y;c=.25
with np.errstate(divide='ignore',invalid='ignore'):
 V=1-c/(Z*(Z-1));psi=Y+c*np.angle(Z/(Z-1))
mask=(np.abs(Z)<.055)|(np.abs(Z-1)<.055)
u=np.ma.array(V.real,mask=mask);v=np.ma.array(-V.imag,mask=mask)
fig,ax=plt.subplots(figsize=(9,6),facecolor='white');ax.set_facecolor('white')
ax.streamplot(x,y,u,v,density=1.35,color='#7eadd0',linewidth=.8,arrowsize=1)
# Separate half-plane contours avoid the logarithm cut on the source–sink segment.
for half in [Y>.005,Y<-.005]:
 ax.contour(X,Y,np.ma.array(psi,mask=~half|mask),levels=[0],colors=['#134f78'],linewidths=2)
r=np.sqrt(1+4*c);st=[(1-r)/2,(1+r)/2]
ax.scatter(st,[0,0],color='#252525',s=35,zorder=6,label='Stagnation points')
ax.scatter([0,1],[0,0],color=['#c64836','#593998'],s=55,zorder=7)
ax.annotate('source',(0,0),xytext=(-.1,-.22),fontsize=11)
ax.annotate('sink',(1,0),xytext=(.93,-.22),fontsize=11)
ax.set(xlabel='$x$',ylabel='$y$',title='Uniform stream with a source and sink: Rankine oval',xlim=(-1.1,2.1),ylim=(-1.25,1.25))
ax.set_aspect('equal');ax.legend(loc='upper right',framealpha=1);fig.tight_layout()
fig.savefig('2009-rankine-oval.png',dpi=160,facecolor='white');plt.close(fig)
