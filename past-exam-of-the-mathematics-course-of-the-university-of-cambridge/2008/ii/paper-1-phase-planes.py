"""Phase portraits and stable-manifold basin; output only to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path as PolygonPath

def rhs(v,k):
 x,y=v
 return np.array([y,-x+x*x-k*y])
def trace(v,k,dt,steps=18000):
 out=[v.copy()]
 for _ in range(steps):
  a=rhs(v,k);b=rhs(v+.5*dt*a,k);c=rhs(v+.5*dt*b,k);d=rhs(v+dt*c,k)
  w=v+dt*(a+2*b+2*c+d)/6
  if w[0]>4.5:
   frac=(4.5-v[0])/(w[0]-v[0]);out.append(v+frac*(w-v));break
  out.append(w.copy());v=w
  if abs(v[0])>12 or abs(v[1])>18:break
 return np.array(out)

fig,axs=plt.subplots(1,2,figsize=(11,5.2),dpi=110)
fig.patch.set_facecolor('white')
x=np.linspace(-1.25,2.55,220);y=np.linspace(-2.7,2.7,220);xx,yy=np.meshgrid(x,y)
for ax,k in zip(axs,[0,.1]):
 ax.set_facecolor('white');ax.streamplot(x,y,yy,-xx+xx*xx-k*yy,density=.65,color='#b5b5b5',linewidth=.5,arrowsize=.75)
 ax.plot(0,0,'o',color='#1565c0');ax.plot(1,0,'o',color='#c62828')
 ax.axhline(0,color='black',lw=.5);ax.axvline(0,color='black',lw=.5)
 ax.set(xlim=(x[0],x[-1]),ylim=(y[0],y[-1]),xlabel='x',ylabel='y',title=f'k = {k:g}')
 ax.annotate('saddle',(1,0),xytext=(9,11),textcoords='offset points')
# Conservative separatrices, exact energy level 1/6.
a=np.linspace(-.5,1,650);z=(1-a)*np.sqrt(np.maximum((2*a+1)/3,0))
for sign in [-1,1]:axs[0].plot(a,sign*z,color='#c62828',lw=2)
a=np.linspace(1,2.55,300);z=(a-1)*np.sqrt((2*a+1)/3)
for sign in [-1,1]:axs[0].plot(a,sign*z,color='#c62828',lw=2)
energy=yy*yy/2+xx*xx/2-xx**3/3
axs[0].contour(xx,yy,energy,levels=[.025,.07,.12,.155],colors='#1565c0',linewidths=.7)
axs[0].annotate('centre',(0,0),xytext=(-52,-20),textcoords='offset points')
# Numerical saddle manifolds of damped system, using eigenvector starts.
k=.1;ls=(-k-np.sqrt(k*k+4))/2;lu=(-k+np.sqrt(k*k+4))/2;eps=1e-5
left=trace(np.array([1-eps,-ls*eps]),k,-.004)
right=trace(np.array([1+eps,ls*eps]),k,-.004)
poly=np.vstack([left[::-1],right])
assert PolygonPath(poly).contains_point((0,0))
assert not PolygonPath(poly).contains_point((2,0))
inside=PolygonPath(poly).contains_points(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)
axs[1].contourf(xx,yy,inside.astype(int),levels=[.5,1.5],colors=['#dbeafe'],alpha=.85,zorder=0)
for v in [left,right]:axs[1].plot(v[:,0],v[:,1],color='#c62828',lw=2)
for sign in [-1,1]:
 v=trace(np.array([1+sign*eps,sign*lu*eps]),k,.004,steps=17000)
 axs[1].plot(v[:,0],v[:,1],color='#ef6c00',lw=1.4,ls='--')
axs[1].annotate('stable focus',(0,0),xytext=(-76,17),textcoords='offset points')
axs[1].annotate('Basin of the origin',(.5,-.3),xytext=(-.7,-1.5),fontsize=9,color='#1565c0',arrowprops={'arrowstyle':'->','color':'#1565c0','lw':.8})
fig.suptitle('Quadratic oscillator: saddle separatrices and basin (shaded)',fontsize=12)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-1-phase-planes.png',facecolor='white',transparent=False)
plt.close(fig)
