"""Original exact currents for the two switch positions of a parallel RL load."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
L=4*np.pi*1e-7*2000**2*np.pi*.01**2*.5
R1,R2,V0=10.,100.,100.
tau=L/(R1*R2/(R1+R2));toff=L/R2
fig,axs=plt.subplots(1,2,figsize=(10.8,4.8),layout='constrained')
t=np.linspace(0,5*tau,400)
axs[0].plot(t*1e6,V0/R1*(1-np.exp(-t/tau)),label=r'$i_L$',color='#326e96',lw=2)
axs[0].plot(t*1e6,V0/(R1+R2)*np.exp(-t/tau),label=r'$i_2$',color='#bb5545',lw=2)
axs[0].set_title(r'Connected: $\tau=86.9\,\mu\mathrm{s}$')
t=np.linspace(0,5*toff,400)
axs[1].plot(t*1e6,V0/R1*np.exp(-t/toff),label=r'$i_L$',color='#326e96',lw=2)
axs[1].plot(t*1e6,-V0/R1*np.exp(-t/toff),label=r'$i_2$',color='#bb5545',lw=2)
axs[1].set_title(r'Disconnected: $\tau_{\rm off}=7.90\,\mu\mathrm{s}$')
for ax in axs:
    ax.axhline(0,color='0.5',lw=.8);ax.set(xlabel='Time from switching (microseconds)',ylabel='Current (A; positive down each branch)');ax.grid(alpha=.2);ax.legend()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white',transparent=False)
