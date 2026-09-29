"""Generate paper-2-quadratic-damping.png in the caller's cwd.

Python 3.14; numpy 2.3.5 and matplotlib 3.10.7 as in the root pyproject.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
c=.15
def field(v):return np.array([v[1],-np.sin(v[0])-c*v[1]*abs(v[1])])
def trajectory(v0,steps=5000,dt=.02):
 v=np.array(v0,dtype=float);out=[v.copy()]
 for _ in range(steps):
  k1=field(v);k2=field(v+dt*k1/2);k3=field(v+dt*k2/2);k4=field(v+dt*k3)
  v+=dt*(k1+2*k2+2*k3+k4)/6;out.append(v.copy())
 return np.array(out)
fig,ax=plt.subplots(1,2,figsize=(11.2,4.4),dpi=100,facecolor='white')
for radius,color in [(.28,'#2c7fb8'),(.57,'#126a8a')]:
 v=trajectory([radius,0]);ax[0].plot(v[:,0],v[:,1],color=color,lw=.8)
 i=85;ax[0].annotate('',v[i+6],v[i],arrowprops={'arrowstyle':'->','color':color})
ax[0].set(xlim=(-.66,.66),ylim=(-.66,.66),xlabel=r'$\theta$ near 0',ylabel=r'$\omega$',title='Nonlinear attracting spiral\nlinearized eigenvalues ±i')
grid=np.linspace(-.55,.55,150);xx,yy=np.meshgrid(grid,grid)
vx=yy;vy=-np.sin(np.pi+xx)-c*yy*np.abs(yy)
ax[1].streamplot(xx,yy,vx,vy,density=.8,color='#176eab',linewidth=.9,arrowsize=1.15)
ax[1].plot(grid,grid,'--',color='#b16724',lw=1,label='unstable tangent')
ax[1].plot(grid,-grid,'--',color='#777',lw=1,label='stable tangent')
ax[1].legend(loc='upper left',fontsize=8)
ax[1].set(xlim=(-.55,.55),ylim=(-.55,.55),xlabel=r'$\theta-\pi$ near 0',ylabel=r'$\omega$',title='Unstable saddle\nlinearized eigenvalues ±1')
for a in ax:
 a.axhline(0,color='#aaa',lw=.6);a.axvline(0,color='#aaa',lw=.6);a.plot(0,0,'ko',ms=3);a.set_aspect('equal');a.spines[['top','right']].set_visible(False)
fig.suptitle('Pendulum with quadratic damping (c = 0.15)',fontsize=12)
fig.tight_layout();fig.savefig('paper-2-quadratic-damping.png',facecolor='white',transparent=False)
