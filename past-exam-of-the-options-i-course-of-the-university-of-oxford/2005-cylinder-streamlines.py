"""Original circulating-cylinder streamline plot; Python 3.14, NumPy/Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

a=U=1.;gamma=.4;circulation=4*np.pi*U*a*gamma
x=np.linspace(-3.4,3.4,601);y=np.linspace(-2.4,2.4,451);X,Y=np.meshgrid(x,y);Z=X+1j*Y
R=np.abs(Z);safe=np.maximum(R,a)
psi=U*Y*(1-a*a/safe**2)-circulation/(2*np.pi)*np.log(safe/a)
psi=np.ma.masked_where(R<a,psi)
with np.errstate(divide='ignore',invalid='ignore'):
 velocity=U*(1-a*a/Z**2)-1j*circulation/(2*np.pi*Z)
u=np.where(R>a,velocity.real,np.nan);v=np.where(R>a,-velocity.imag,np.nan)
fig,ax=plt.subplots(figsize=(8,5),facecolor='white')
ax.contour(X,Y,psi,levels=np.arange(-4,2.51,.25),colors='#1769aa',linewidths=.8)
ax.contour(X,Y,psi,levels=[0],colors='#8f3d0a',linewidths=1.6)
ax.streamplot(x,y,u,v,color='#1769aa',density=.7,linewidth=.3,arrowsize=.9,minlength=.2)
ax.add_patch(Circle((0,0),a,facecolor='white',edgecolor='black',lw=1.5,zorder=5))
stag=np.sqrt(1-gamma*gamma);ax.plot([-stag,stag],[gamma,gamma],'o',color='#ad271d',ms=5,zorder=8,label='Surface stagnation points')
ax.annotate('Uniform flow',xy=(-2.2,1.9),xytext=(-3.2,1.9),arrowprops={'arrowstyle':'->'},va='center',fontsize=9)
ax.set(xlim=(-3.4,3.4),ylim=(-2.4,2.4),xlabel='$x/a$',ylabel='$y/a$',title=r'Cylinder flow with $\Gamma/(4\pi Ua)=0.4$')
ax.set_aspect('equal');ax.legend(loc='lower left',fontsize=9);fig.tight_layout();fig.savefig('2005-cylinder-streamlines.png',dpi=150,facecolor='white')
