"""Original modal solution of a damped string; write PNG into cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,np.pi,900);h=.3;n=np.arange(1,402,2)[:,None]
b=4*np.sin(n*np.pi/2)/(np.pi*n*n);omega=np.sqrt(n*n-h*h)
fig,ax=plt.subplots(figsize=(8,4.4),facecolor='white')
ax.plot(x,np.minimum(x,np.pi-x),color='black',lw=2,label='t = 0 (released from rest)')
for t in [.8,1.8,3.0,4.5]:
 u=np.sum(b*np.sin(n*x)*np.exp(-h*t)*(np.cos(omega*t)+h*np.sin(omega*t)/omega),axis=0)
 ax.plot(x,u,lw=1.8,label=f't = {t:g}')
ax.set_xticks([0,np.pi/2,np.pi],['0',r'$\pi/2$',r'$\pi$'])
ax.set(xlabel='Position x',ylabel='Displacement u',title='Fixed-end string, unit wave speed, damping h = 0.3')
ax.axhline(0,color='gray',lw=.7);ax.grid(alpha=.2);ax.legend(fontsize=9,ncol=2)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
