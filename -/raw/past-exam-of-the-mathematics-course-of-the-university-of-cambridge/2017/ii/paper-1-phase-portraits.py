"""Original sketches for Cambridge 2017 II paper 1 Q30. Output PNG in CWD.
Tested with Python 3.14.4, matplotlib 3.10.7+dfsg1, numpy 2.3.5.
Project requirements: Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2017-ii-paper-1-mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
fig,axs=plt.subplots(1,3,figsize=(10.8,4.2),dpi=100,facecolor='white')
a=np.linspace(-1.25,1.25,201);X,Y=np.meshgrid(a,a)
for ax,beta in zip(axs,[.5,2.,1.]):
 U=X*(-1+X*X+beta*Y*Y);V=Y*(-1+beta*X*X+Y*Y)
 speed=np.hypot(U,V);denom=np.maximum(speed,1e-8)
 ax.streamplot(a,a,U/denom,V/denom,density=1.05,color='#6c7f8a',linewidth=.65,arrowsize=.8)
 for sign in [-1,1]: ax.plot(a,sign*a,':',color='#b6c2c9',lw=.7)
 ax.axhline(0,color='#b6c2c9',lw=.7);ax.axvline(0,color='#b6c2c9',lw=.7)
 ax.plot(0,0,'o',color='#1a9850',ms=6,label='sink')
 if beta==1:
  ang=np.linspace(0,2*np.pi,401);ax.plot(np.cos(ang),np.sin(ang),color='#d73027',lw=2,label='equilibrium circle')
 else:
  s=1/np.sqrt(1+beta)
  axis=np.array([[1,0],[-1,0],[0,1],[0,-1]])
  diagonal=np.array([[s,s],[s,-s],[-s,s],[-s,-s]])
  saddles,sources=(axis,diagonal) if beta<1 else (diagonal,axis)
  ax.plot(saddles[:,0],saddles[:,1],'s',color='#fdae61',markeredgecolor='#6b4c11',ms=5,label='saddle')
  ax.plot(sources[:,0],sources[:,1],'^',color='#d73027',ms=6,label='source')
 if beta!=1:
  def rhs(z):
   x,y=z
   return np.array([x*(-1+x*x+beta*y*y),y*(-1+beta*x*x+y*y)])
  def backward(seed):
   z=np.array(seed,dtype=float);pts=[z.copy()];step=-.02
   for _ in range(3500):
    k1=rhs(z);k2=rhs(z+step*k1/2);k3=rhs(z+step*k2/2);k4=rhs(z+step*k3)
    z=z+step*(k1+2*k2+2*k3+k4)/6
    if np.max(abs(z))>1.3:break
    pts.append(z.copy())
    if np.linalg.norm(rhs(z))<1e-7:break
   return np.array(pts)
  eps=1e-4
  if beta<1:
   seed=[1+beta/(2*(beta-2))*eps**2,eps]
  else:
   seed=[s+eps,s-eps]
  arc=backward(seed)
  first=True
  for swap in [False,True]:
   for sx in [-1,1]:
    for sy in [-1,1]:
     points=arc[:,::-1] if swap else arc
     ax.plot(sx*points[:,0],sy*points[:,1],color='#2166ac',lw=1.3,label='separatrix' if first else None)
     first=False
 ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),xlabel='$x$',ylabel='$y$',title=rf'$\beta={beta:g}$')
 ax.set_aspect('equal');ax.legend(loc='lower center',bbox_to_anchor=(.5,-.30),fontsize=6.5,frameon=False,ncol=4)
fig.subplots_adjust(left=.07,right=.99,bottom=.26,top=.90,wspace=.27)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
