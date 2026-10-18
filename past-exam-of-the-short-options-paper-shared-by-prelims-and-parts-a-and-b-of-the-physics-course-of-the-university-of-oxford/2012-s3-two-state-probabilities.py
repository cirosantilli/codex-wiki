"""Original probabilities for a coherent pair of energy levels, in recurrence units."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
u=np.linspace(0,2,600)
fig,axes=plt.subplots(1,2,figsize=(10,4.3),layout='constrained',facecolor='white')
axes[0].plot(u,np.sin(np.pi*u)**2,lw=2.2,color='#176b87',label='Antisymmetric state')
axes[0].plot(u,np.cos(np.pi*u)**2,'--',lw=1.5,color='#c05229',label='Symmetric state')
axes[0].set(title='Projection probabilities from the initial plus state',xlabel=r'$t/\tau$',ylabel='Probability',xlim=(0,2),ylim=(-.03,1.03))
axes[0].legend(fontsize=10,frameon=False,loc='upper right')
axes[1].plot(u,.5+4/(3*np.pi)*np.cos(2*np.pi*u),lw=2.2,color='#176b87')
axes[1].axhline(.5,color='.6',lw=.8,ls='--')
axes[1].set(title='Left half of an infinite well: first two levels',xlabel=r'$t/\tau$',ylabel='Position probability',xlim=(0,2),ylim=(-.03,1.03))
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',metadata={'Software':'matplotlib'})
