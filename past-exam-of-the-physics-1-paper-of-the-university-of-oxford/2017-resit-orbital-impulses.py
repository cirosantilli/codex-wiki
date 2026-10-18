"""Four osculating Kepler ellipses; output only the matching PNG in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(2,2,figsize=(9.2,8),layout='constrained')
theta=np.linspace(0,2*np.pi,1000)
r0=np.array([0.,1.]);vc=np.array([-1.,0.]);kick=.18
cases=[('a: forward tangential',np.array([-kick,0.])),('b: radially outward',np.array([0.,kick])),('c: backward tangential',np.array([kick,0.])),('d: radially inward',np.array([0.,-kick]))]
for ax,(label,dv) in zip(axes.flat,cases):
 v=vc+dv;h=np.cross(np.r_[r0,0.],np.r_[v,0.])[2]
 e=(np.dot(v,v)-1)*r0-np.dot(r0,v)*v
 directions=np.column_stack((np.cos(theta),np.sin(theta)))
 rad=h*h/(1+directions@e);xy=rad[:,None]*directions
 ax.plot(np.cos(theta),np.sin(theta),'--',color='.65',label='original circle')
 ax.plot(xy[:,0],xy[:,1],color='#1f77b4',lw=2,label='new ellipse')
 ax.scatter([0],[0],s=85,color='#dfaa2b',zorder=5)
 ax.scatter([0],[1],s=35,color='black',zorder=6)
 ax.annotate('',xy=r0+1.8*dv,xytext=r0,arrowprops=dict(arrowstyle='->',color='#c33',lw=2.5))
 ax.set(title=label,xlim=(-1.7,1.7),ylim=(-2.5,1.5),aspect='equal',xlabel=r'$x/r_0$',ylabel=r'$y/r_0$')
 ax.grid(alpha=.15)
axes[0,0].legend(loc='lower left',fontsize=8)
fig.suptitle('Small velocity changes at the top of a counterclockwise orbit',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
