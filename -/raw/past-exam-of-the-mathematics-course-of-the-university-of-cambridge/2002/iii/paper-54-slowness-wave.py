"""Stable orthotropic elastic slowness and wave surfaces.
Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7. Outputs basename to caller CWD.
"""
import os
from pathlib import Path
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'paper-54-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def branch(theta, sign):
 d=np.sqrt(5+4*np.cos(4*theta))
 dp=-8*np.sin(4*theta)/d
 dpp=-32*np.cos(4*theta)/d-64*np.sin(4*theta)**2/d**3
 lam=(5+sign*d)/2
 lp=sign*dp/2
 lpp=sign*dpp/2
 v=np.sqrt(lam)
 vp=lp/(2*v)
 vpp=lpp/(2*v)-lp**2/(4*v**3)
 return v,vp,vpp

theta=np.linspace(0,2*np.pi,4001)
n=np.column_stack((np.cos(theta),np.sin(theta)))
t=np.column_stack((-np.sin(theta),np.cos(theta)))
fig, axs=plt.subplots(1,2,figsize=(10.2,4.9),layout='constrained',facecolor='white')
for sign, color, label in [(1,'#bb4422','Quasi-P'),(-1,'#2266aa','In-plane shear')]:
 v,vp,_=branch(theta,sign)
 s=n/v[:,None]
 g=v[:,None]*n+vp[:,None]*t
 axs[0].plot(*s.T,color=color,label=label)
 axs[1].plot(*g.T,color=color,label=label)
sh=np.sqrt(1.2)
axs[0].plot(*(n/sh).T,'--',color='#448844',label='Out-of-plane shear')
axs[1].plot(*(sh*n).T,'--',color='#448844',label='Out-of-plane shear')
# Locate genuine zeros of v+v''; these are stationary points of the wave-surface map.
v,vp,vpp=branch(theta,-1)
h=v+vpp
roots=[]
for i in np.flatnonzero(h[:-1]*h[1:]<0):
 lo,hi=theta[i],theta[i+1]
 for _ in range(50):
  mid=(lo+hi)/2
  f=sum(branch(mid,-1)[::2])
  if sum(branch(lo,-1)[::2])*f<=0:hi=mid
  else:lo=mid
 roots.append((lo+hi)/2)
for angle in roots:
 v,vp,_=branch(angle,-1)
 q=v*np.array([np.cos(angle),np.sin(angle)])+vp*np.array([-np.sin(angle),np.cos(angle)])
 axs[1].plot(*q,'o',ms=4,color='#2266aa')
axs[0].set(title='Slowness surface cross-section',xlabel=r'$p_1$',ylabel=r'$p_2$')
axs[1].set(title='Unit-time wave surface (group velocities)',xlabel=r'$g_1$',ylabel=r'$g_2$')
axs[1].text(.02,.03, 'Dots: shear-wave cusps', transform=axs[1].transAxes, fontsize=9)
for ax in axs:
 ax.axhline(0,color='.75',lw=.7);ax.axvline(0,color='.75',lw=.7)
 ax.set_aspect('equal');ax.grid(alpha=.16);ax.legend(fontsize=8,loc='upper right')
fig.savefig(Path.cwd()/'paper-54-slowness-wave.png',dpi=135,facecolor='white',transparent=False)
plt.close(fig)
