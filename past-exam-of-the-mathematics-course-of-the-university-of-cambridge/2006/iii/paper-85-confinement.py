"""Original parameter regions and Hamiltonian portrait; output PNG to CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
ax=axs[0]
sigma,mu=np.meshgrid(np.linspace(-1.8,1.8,600),np.linspace(-1.8,1.8,600))
disc=2-(mu-sigma)**2
root=np.sqrt(np.maximum(disc,0))
count=np.where(disc>=0,2*((mu+sigma+root>1e-8).astype(int)+(mu+sigma-root>1e-8).astype(int)),0)
ax.pcolormesh(sigma,mu,count,cmap=ListedColormap(['white','#c8dffa','#ffdba8']),vmin=0,vmax=4,shading='auto',rasterized=True)
stable=(mu<0)&(mu*mu+sigma*sigma>1)
ax.contourf(sigma,mu,stable.astype(float),levels=[.5,1.5],colors='none',hatches=['////'])
theta=np.linspace(0,2*np.pi,800)
ax.plot(np.cos(theta),np.sin(theta),'k',lw=1.3)
x=np.linspace(-1.8,1.8,600)
for sign in [-1,1]:
 y=x+sign*np.sqrt(2)
 keep=x+y>0
 ax.plot(x[keep],y[keep],color='#7b3294',lw=1.6)
for lo,hi in [(-1.8,-1),(1,1.8)]:ax.plot([lo,hi],[0,0],color='#d73027',lw=2)
ax.plot([-1,1],[0,0],'kD',ms=5)
ax.plot([1/np.sqrt(2),-1/np.sqrt(2)],[-1/np.sqrt(2),1/np.sqrt(2)],'k*',ms=10)
ax.set(xlim=(-1.8,1.8),ylim=(-1.8,1.8),xlabel=r'$\sigma$',ylabel=r'$\mu$',title='Equilibrium regions')
ax.set_aspect('equal')
ax.legend(handles=[Patch(facecolor='#c8dffa',label='2 nonzero equilibria'),Patch(facecolor='#ffdba8',label='4 nonzero equilibria'),Patch(facecolor='white',hatch='////',label='origin: strict linear stability')],fontsize=8,loc='upper left')
ax.text(1.03,.09,'Hopf',color='#d73027',fontsize=8)
ax.text(.4,1.55,'nonzero folds',color='#7b3294',fontsize=8)
ax=axs[1]
v,u=np.meshgrid(np.linspace(-2.15,2.15,180),np.linspace(-1.25,1.25,140))
fx=2*u;fy=-v+.5*v**3;speed=np.hypot(fx,fy)
ax.streamplot(v[0],u[:,0],fx/(speed+.08),fy/(speed+.08),color='#bbbbbb',density=.85,linewidth=.6,arrowsize=.7)
H=u*u+.5*v*v-v**4/8
ax.contour(v,u,H,levels=[.05,.15,.3,.44],colors='#2166ac',linewidths=1)
a=np.sqrt(2);vline=np.linspace(-a,a,500)
for sign in [-1,1]:
 uline=sign*(2-vline*vline)/(2*np.sqrt(2))
 ax.plot(vline,uline,color='#b2182b',lw=2)
 x0=-.45 if sign==1 else .45;x1=x0+.18*sign
 ax.annotate('',xy=(x1,sign*(2-x1*x1)/(2*np.sqrt(2))),xytext=(x0,sign*(2-x0*x0)/(2*np.sqrt(2))),arrowprops=dict(arrowstyle='->',color='#b2182b',lw=2))
ax.plot([-a,a],[0,0],'kx',ms=8,mew=2);ax.plot(0,0,'ko',ms=4)
ax.text(-.2,.95,r'$H_{\rm het}=1/2$',color='#b2182b')
ax.set(xlim=(-2.15,2.15),ylim=(-1.25,1.25),xlabel=r'$v$',ylabel=r'$u$',title=r'Hamiltonian limit, $s=1$')
fig.savefig('paper-85-confinement.png',dpi=150,facecolor='white',transparent=False)
