"""Original timelike AdS geodesic family; Python3.14/NumPy2.3/Matplotlib3.10.
PNG basename is written to caller CWD. Caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.3,7),facecolor='white')
T=np.linspace(-np.pi,np.pi,701);r=np.pi/2
for v in [-.95,-.8,-.55,-.25,0,.25,.55,.8,.95]:
 rho=np.arcsin(v*np.sin(T));ax.plot(rho,T,lw=1.5,color='#0072b2',alpha=.78)
for x in [-r,r]:ax.plot([x,x],[-np.pi-.35,np.pi+.35],color='#333333',lw=3)
for time,label in [(-np.pi,r'$P_-$'),(0,r'$P$'),(np.pi,r'$P_+$')]:
 ax.scatter([0],[time],color='#d55e00',s=40,zorder=5);ax.text(.12,time+.08,label,fontsize=12)
ax.text(-1.25,2.6,r'$\sin\rho=v\sin T$',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.text(-1.2,-2.65,r'$|v|<1$',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.set(xlim=(-r-.25,r+.25),ylim=(-np.pi-.45,np.pi+.45),xlabel=r'signed conformal position $\rho$',ylabel=r'unwrapped global time $T$')
ax.set_xticks([-r,0,r],labels=[r'$-\pi/2$','0',r'$\pi/2$']);ax.set_yticks([-np.pi,0,np.pi],labels=[r'$-\pi$','0',r'$\pi$'])
ax.set_aspect('equal',adjustable='box');ax.set_title('Timelike geodesics through an arbitrary AdS event\nIsometry places P at the center; family continues beyond plot',fontsize=11)
ax.spines[['top','right']].set_visible(False);fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
