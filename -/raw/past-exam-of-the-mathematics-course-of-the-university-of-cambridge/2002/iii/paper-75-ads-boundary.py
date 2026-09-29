"""Original conformal-strip sketch. Tested with Python3.14, NumPy2.3, Matplotlib3.10.
Run from the desired output directory; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.2,7.2),facecolor='white')
r=np.pi/2;top=1.5*np.pi
for x in [-r,r]:ax.plot([x,x],[-top,top],color='#303030',lw=3)
ax.plot([0,0],[-top,top],color='#bbbbbb',lw=1,ls=':')
for x0,T0 in [(0,-np.pi/2),(0,np.pi/2)]:
 for d in [-1,1]:
  x=np.linspace(x0,d*r,80);T=T0+np.abs(x-x0)
  ax.plot(x,T,color='#0072b2',lw=1.6)
ax.text(0,-.5,'center of signed diameter',ha='center',fontsize=9,color='#555555')
ax.text(-r-.20,0,'timelike conformal boundary',rotation=90,ha='center',va='center',fontsize=10)
ax.text(r+.20,0,'timelike conformal boundary',rotation=90,ha='center',va='center',fontsize=10)
ax.annotate('',xy=(0,top+.38),xytext=(0,top-.1),arrowprops={'arrowstyle':'->'});ax.text(0,top+.55,r'$i^+:\ T\to+\infty$',ha='center')
ax.annotate('',xy=(0,-top-.38),xytext=(0,-top+.1),arrowprops={'arrowstyle':'->'});ax.text(0,-top-.67,r'$i^-:\ T\to-\infty$',ha='center')
ax.text(.12,2.5,'radial null rays',color='#0072b2',fontsize=10)
ax.set(xlim=(-r-.5,r+.5),ylim=(-top-.8,top+.8),xlabel=r'signed conformal position $\rho$',ylabel=r'unwrapped global time $T$')
ax.set_xticks([-r,0,r],labels=[r'$-\pi/2$','0',r'$\pi/2$'])
ax.set_yticks([-np.pi,0,np.pi],labels=[r'$-\pi$','0',r'$\pi$'])
ax.set_aspect('equal',adjustable='box')
ax.set_title('Universal cover of AdS\nSigned diameter; transverse directions suppressed',fontsize=12)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
