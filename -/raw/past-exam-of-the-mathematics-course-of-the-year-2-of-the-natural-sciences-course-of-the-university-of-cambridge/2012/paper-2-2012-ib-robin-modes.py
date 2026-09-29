"""Original Robin heat-mode illustration. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored _media directory; white PNG output is relative to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,1,600);t=np.linspace(0,.5,600)
fig,axes=plt.subplots(1,2,figsize=(9,4.8),facecolor='white')
colors=['#b34b2e','#236a98','#398065']
labels=[r'$e^{-x}$',r'$\pi\cos(\pi x)-\sin(\pi x)$',r'$2\pi\cos(2\pi x)-\sin(2\pi x)$']
spatial=[np.exp(-x)/np.sqrt((1-np.exp(-2))/2)]
for n in [1,2]:spatial.append((n*np.pi*np.cos(n*np.pi*x)-np.sin(n*np.pi*x))/np.sqrt((n*n*np.pi*np.pi+1)/2))
for y,color,label in zip(spatial,colors,labels):axes[0].plot(x,y,color=color,label=label,lw=2)
axes[0].axhline(0,color='#a7b0bc',lw=.7)
axes[0].set(xlabel='$x$',ylabel='Normalized spatial amplitude',title='Spatial modes, each with unit squared norm')
axes[0].legend(fontsize=8,loc='upper center',bbox_to_anchor=(.5,-.23),framealpha=1)
for exponent,color,label in zip([1,-np.pi**2,-4*np.pi**2],colors,[r'$e^t$',r'$e^{-\pi^2t}$',r'$e^{-4\pi^2t}$']):
    axes[1].semilogy(t,np.exp(exponent*t),color=color,label=label,lw=2)
axes[1].set(xlabel='$t$',ylabel='Time factor (logarithmic scale)',title='Growth and decay of the time factors')
axes[1].legend(fontsize=10)
for ax in axes:ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
fig.suptitle(r'Heat flow with $u_x(0)=-u(0)$ and $u_x(1)=-u(1)$',fontsize=15,y=.98)
fig.text(.5,.02,'The left boundary can supply energy; growth is present when the initial exponential-mode coefficient is nonzero.',ha='center',fontsize=9)
fig.subplots_adjust(left=.075,right=.97,top=.8,bottom=.31,wspace=.3)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
