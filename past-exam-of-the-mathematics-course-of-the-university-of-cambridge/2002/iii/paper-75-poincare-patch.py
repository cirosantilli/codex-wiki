"""Original warped-coordinate patch sketch; Python3.14/NumPy2.3/Matplotlib3.10.
Run in output CWD, with caller's MPLCONFIGDIR respected.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.5,7),facecolor='white');r=np.pi/2
rho=np.linspace(-r,r,601);upper=r+rho
ax.fill_between(rho,-upper,upper,color='#b8dfee',label='full z > 0 Poincare patch')
for x in [-r,r]:ax.plot([x,x],[-np.pi-.25,np.pi+.25],color='#333333',lw=3)
ax.plot(rho,upper,'--',color='#0072b2',lw=1.8);ax.plot(rho,-upper,'--',color='#0072b2',lw=1.8)
b=np.linspace(0,r,301);tb=np.arccos(np.clip(np.cos(b)-np.sin(b),-1,1))
ax.plot(b,tb,color='#d55e00',lw=2,label='brane z = 1 (y = 0)');ax.plot(b,-tb,color='#d55e00',lw=2)
ax.text(.58,1.65,'Poincare horizon',rotation=45,color='#0072b2',fontsize=10)
ax.text(.46,-2.3,'Poincare horizon',rotation=-45,color='#0072b2',fontsize=10)
ax.text(-.55,.1,r'$y>0$ side',fontsize=10)
ax.text(.64,-.12,r'$0<z<1$',fontsize=10)
ax.set(xlim=(-r-.3,r+.3),ylim=(-np.pi-.35,np.pi+.35),xlabel=r'signed conformal position $\rho$',ylabel=r'unwrapped global time $T$')
ax.set_xticks([-r,0,r],labels=[r'$-\pi/2$','0',r'$\pi/2$']);ax.set_yticks([-np.pi,0,np.pi],labels=[r'$-\pi$','0',r'$\pi$'])
ax.set_aspect('equal',adjustable='box');ax.set_title('Randall–Sundrum coordinates in global AdS\nShaded: |T| < pi/2 + rho; z = 1 brane drawn in orange',fontsize=11)
ax.legend(loc='upper left',fontsize=8);ax.spines[['top','right']].set_visible(False);fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
