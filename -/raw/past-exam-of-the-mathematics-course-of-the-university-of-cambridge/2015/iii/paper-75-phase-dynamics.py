"""Adler drift and tilted-potential sketches. Python 3.14; root NumPy/Matplotlib.
Writes only the opaque PNG basename in cwd; set MPLCONFIGDIR in the caller.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(-.3,2*np.pi+.3,700)
fig,axs=plt.subplots(2,2,figsize=(10,6),dpi=100,facecolor='white')
for j,w in enumerate((.55,1.25)):
 drift=w-np.sin(theta);potential=-w*theta-np.cos(theta)
 axs[0,j].plot(theta/np.pi,drift,color='#245786',lw=2.2)
 axs[0,j].axhline(0,color='#777777',lw=.9)
 axs[0,j].set_title(('Locked: ' if j==0 else 'Running: ')+rf'$\omega/\epsilon={w}$')
 axs[0,j].set_ylabel(r'Drift $\dot\theta/\epsilon$')
 axs[1,j].plot(theta/np.pi,potential,color='#aa683a',lw=2.2)
 axs[1,j].set_ylabel(r'Potential $V/\epsilon$');axs[1,j].set_xlabel(r'Unwrapped phase $\theta/\pi$')
 if j==0:
  a=np.arcsin(w);b=np.pi-a
  for th,color,lab in [(a,'#228855','Stable / minimum'),(b,'#aa3333','Unstable / maximum')]:
   axs[0,j].scatter(th/np.pi,0,s=32,c=color,zorder=3,label=lab)
   axs[1,j].scatter(th/np.pi,-w*th-np.cos(th),s=32,c=color,zorder=3)
  axs[0,j].legend(loc='upper left',fontsize=8)
 else:
  axs[1,j].annotate('Potential always decreases',xy=(1.35,-w*1.35*np.pi-np.cos(1.35*np.pi)),xytext=(.6,-1.8),arrowprops={'arrowstyle':'->','color':'#666666'},fontsize=9)
 for ax in axs[:,j]:
  ax.set_xlim(-.05,2.05);ax.set_xticks([0,.5,1,1.5,2]);ax.grid(alpha=.17);ax.set_facecolor('white')
fig.suptitle('Phase coupling creates wells only below the locking threshold',fontsize=13)
fig.tight_layout(rect=(0,0,1,.95))
fig.savefig(Path.cwd()/'paper-75-phase-dynamics.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
