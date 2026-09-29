"""Generate paper-329-rod-dissipation.png in the caller's working directory."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(1,2,figsize=(11.4,3.6),dpi=100,facecolor='white')
theta=np.linspace(0,np.pi,601)
ax[0].plot(theta,np.sin(2*theta)**2,lw=2,color='#176eab')
ax[0].set(xticks=np.arange(5)*np.pi/4,xticklabels=['0',r'$\pi/4$',r'$\pi/2$',r'$3\pi/4$',r'$\pi$'],xlabel=r'Orientation $\theta$',ylabel=r'$D^\prime / D^\prime_{\max}$',title='Axial strain controls dissipation',ylim=(-.04,1.12))
ax[0].annotate('extension',(np.pi/4,1),xytext=(.18,.65),arrowprops={'arrowstyle':'->'})
ax[0].annotate('compression',(3*np.pi/4,1),xytext=(2.5,.65),arrowprops={'arrowstyle':'->'})
tau=np.linspace(-8,8,1001)
ax[1].plot(tau,4*tau**2/(1+tau**2)**2,lw=2,color='#176eab')
ax[1].set(xlabel=r'Time $\gamma t$ ($\gamma>0$)',ylabel=r'$D^\prime / D^\prime_{\max}$',title='Finite area beneath the time curve',ylim=(-.04,1.12))
ax[1].annotate('gradient alignment',(0,0),xytext=(1.3,.3),arrowprops={'arrowstyle':'->'})
for a in ax:a.grid(alpha=.22);a.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig('paper-329-rod-dissipation.png',facecolor='white',transparent=False)
