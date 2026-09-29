"""Python 3.14; root NumPy/Matplotlib dependencies. Writes one opaque PNG to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import pi,sqrt
fig,axes=plt.subplots(2,3,figsize=(10.8,4.6),dpi=100,facecolor='white')
angles=[pi/6,pi/3,pi/2,2*pi/3,5*pi/6,pi]
labels=[r'$\theta=\pi/6$: saddle dominates',r'$\theta=\pi/3$: moving endpoint grows',r'$\theta=\pi/2$: half saddle, endpoint grows',r'$\theta=2\pi/3$: no saddle segment',r'$\theta=5\pi/6$: two endpoint terms',r'$\theta=\pi$: fixed endpoint dominates']
a=-1/sqrt(2)
def arrow(ax,z,index=None,color='#185a9d'):
 index=len(z)//2 if index is None else index
 index=max(1,min(len(z)-2,index))
 ax.annotate('',xy=(z[index+1].real,z[index+1].imag),xytext=(z[index-1].real,z[index-1].imag),arrowprops={'arrowstyle':'->','color':color,'lw':1.8,'mutation_scale':13})
for ax,theta,title in zip(axes.flat,angles,labels):
 b=np.exp(1j*theta)
 ax.axhline(0,color='.78',lw=.7);ax.axvline(0,color='.78',lw=.7)
 ax.plot([a,b.real],[0,b.imag],ls='--',color='.68',lw=1,label='Original segment')
 if abs(theta-pi/2)<1e-8:
  z=np.linspace(a,0,120).astype(complex);ax.plot(z.real,z.imag,color='#185a9d',lw=2);arrow(ax,z)
  z=1j*np.linspace(0,1,120);ax.plot(z.real,z.imag,color='#c4382f',lw=2);arrow(ax,z,color='#c4382f')
 elif abs(theta-pi)<1e-8:
  z=np.linspace(a,-1,100).astype(complex);ax.plot(z.real,z.imag,color='#c4382f',lw=2);arrow(ax,z,color='#c4382f')
 else:
  curve=np.sqrt(b*b+np.linspace(0,4,240,dtype=complex))
  if theta>pi/2:curve=-curve
  realpath=np.linspace(a,curve[-1].real,160).astype(complex)
  ax.plot(realpath.real,realpath.imag,color='#185a9d',lw=2);arrow(ax,realpath)
  ax.plot([curve[-1].real,curve[-1].real],[0,curve[-1].imag],color='.55',lw=1,ls=':')
  path=curve[::-1];ax.plot(path.real,path.imag,color='#c4382f',lw=2);arrow(ax,path,index=170,color='#c4382f')
  ax.text(curve[-1].real,curve[-1].imag+.11,r'$\infty$' if theta<pi/2 else r'$-\infty$',ha='center',fontsize=10)
 ax.scatter([0],[0],marker='x',color='black',s=38,zorder=4);ax.text(.04,-.17,'saddle 0',fontsize=8)
 ax.scatter([a],[0],color='#185a9d',s=23,zorder=4);ax.text(a-.1,-.17,r'$a=-1/\sqrt{2}$',fontsize=8,ha='right')
 ax.scatter([b.real],[b.imag],color='#c4382f',s=26,zorder=4);ax.text(b.real+.04,b.imag+.07,r'$b=e^{i\theta}$',fontsize=9)
 ax.set(xlim=(-2.4,2.4),ylim=(-.3,1.4),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
 ax.set_aspect('equal',adjustable='box');ax.set_title(title,fontsize=9,pad=10);ax.tick_params(labelsize=8)
fig.suptitle('Gaussian steepest-descent deformations: integration directions',fontsize=13,y=.985)
fig.text(.5,.025,'Blue: real saddle or fixed-end path. Red: endpoint path. Dotted connectors vanish at infinity.',ha='center',fontsize=10)
fig.subplots_adjust(left=.07,right=.985,bottom=.15,top=.88,wspace=.27,hspace=.42)
fig.savefig('paper-336-gaussian-descent-paths.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
