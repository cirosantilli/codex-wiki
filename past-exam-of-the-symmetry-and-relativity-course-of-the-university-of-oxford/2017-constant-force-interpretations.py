"""Two consistent constant-force conventions for a massive particle. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'figure.facecolor':'white'})
t=np.linspace(0,8,800)
u=np.linspace(0,5,1200)
t4=.5*(u*np.sqrt(1+u*u)+np.arcsinh(u))
fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
axes[0].plot(t,t/np.sqrt(1+t*t),lw=2.5,label=r'Constant $dp_x/dt=f$')
axes[0].plot(t4,u/np.sqrt(1+u*u),lw=2,linestyle='--',label=r'Constant $F^x=f$ only')
axes[0].axhline(1,color='#777777',linestyle=':',lw=1)
axes[0].set_ylim(0,1.07);axes[0].set_ylabel(r'Normalized velocity $\beta=v/c$')
axes[1].plot(t,np.sqrt(1+t*t),lw=2.5)
axes[1].plot(t4,np.sqrt(1+u*u),lw=2,linestyle='--')
axes[1].set_ylim(.8,8.5);axes[1].set_ylabel(r'Lorentz factor $\gamma$')
for ax in axes:
    ax.set_xlim(0,8);ax.set_xlabel(r'Lab time $ft/(M_0c)$');ax.grid(alpha=.2)
axes[0].legend(frameon=False,loc='lower right')
fig.suptitle('A constant complete nonzero four-force is incompatible with fixed rest mass',fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
