"""Unit-damping pendulum phase portrait; Python 3.14, root NumPy/Matplotlib.
Opaque basename PNG to cwd only. Uses the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
xmin,xmax=-2.6*np.pi,2.6*np.pi;ymin,ymax=-3.2,3.2
fig,ax=plt.subplots(figsize=(10,6),dpi=100,facecolor='white')
x,y=np.meshgrid(np.linspace(xmin,xmax,35),np.linspace(ymin,ymax,21));dx=y;dy=-y-np.sin(x);speed=np.hypot(dx,dy);speed=np.maximum(speed,1e-8)
ax.quiver(x/np.pi,y,dx/speed/np.pi,dy/speed,color='#b7b7b7',angles='xy',scale_units='xy',scale=7,width=.0022,zorder=1)
def rhs(z):return np.array([z[1],-z[1]-np.sin(z[0])])
def curve(z,dt,steps=2500):
 z=np.array(z,dtype=float);out=[z.copy()]
 for _ in range(steps):
  a=rhs(z);b=rhs(z+dt*a/2);c=rhs(z+dt*b/2);d=rhs(z+dt*c);z=z+dt*(a+2*b+2*c+d)/6
  if abs(z[0])>xmax+.5 or abs(z[1])>ymax+.5:break
  out.append(z.copy())
 return np.array(out)
def draw(z,color,style='-',label=None,reverse=False):
 ax.plot(z[:,0]/np.pi,z[:,1],style,color=color,lw=1.6,label=label,zorder=3)
 if len(z)>40:
  j=min(len(z)//2,240);lo,hi=(j+12,j) if reverse else (j,j+12)
  ax.annotate('',xy=(z[hi,0]/np.pi,z[hi,1]),xytext=(z[lo,0]/np.pi,z[lo,1]),arrowprops={'arrowstyle':'->','color':color,'lw':1.3},zorder=4)
for i,initial in enumerate([(-.7*np.pi,2.4),(.55*np.pi,-2.7),(1.1*np.pi,2.6),(-2*np.pi,.8)]):draw(curve(initial,.016),'#245786',label='Typical damped trajectories' if i==0 else None)
rm=(-1-np.sqrt(5))/2;rp=(-1+np.sqrt(5))/2
for j,saddle in enumerate([-np.pi,np.pi]):
 for sign in [-1,1]:
  delta=sign*1e-4
  draw(curve([saddle+delta,rm*delta],-.016),'#7756a5','--',label='Stable separatrices' if j==0 and sign==-1 else None,reverse=True)
  draw(curve([saddle+delta,rp*delta],.016),'#ba7437',label='Unstable saddle branches' if j==0 and sign==-1 else None)
ax.scatter([-2,0,2],[0,0,0],s=50,color='#228855',zorder=6,label='Spiral sinks')
ax.scatter([-1,1],[0,0],s=60,marker='x',lw=2,color='#aa3333',zorder=6,label='Saddles')
ax.set(xlim=(xmin/np.pi,xmax/np.pi),ylim=(ymin,ymax),xlabel=r'Unwrapped angle $x/\pi$',ylabel=r'Angular velocity $y$',title=r'Damped pendulum: $\dot x=y$, $\dot y=-y-\sin x$')
ax.set_xticks([-2,-1,0,1,2]);ax.axhline(0,color='#cccccc',lw=.6);ax.grid(alpha=.15);ax.set_facecolor('white');ax.legend(loc='upper left',fontsize=9,framealpha=.95)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-2-pendulum-phase.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
