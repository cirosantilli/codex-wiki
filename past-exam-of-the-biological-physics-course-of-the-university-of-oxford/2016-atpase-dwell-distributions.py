"""Original conceptual figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.2,4.4),constrained_layout=True,facecolor='white')
u=np.linspace(0,5,600)
ax.plot(u,np.exp(-u),label='One event, mean 1',lw=2)
ax.plot(u,4*u*np.exp(-2*u),label='Two equal-rate events, mean 1',lw=2)
ax.plot(u,1.5*(np.exp(-u)-np.exp(-3*u)),label='Two unequal-rate events',lw=2)
ax.set(xlabel='Dwell time (chosen time unit)',ylabel='Probability density',title='Serial chemistry suppresses the shortest dwells',xlim=(0,5),ylim=(0,1.08))
ax.legend(frameon=False);ax.grid(alpha=.18)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
