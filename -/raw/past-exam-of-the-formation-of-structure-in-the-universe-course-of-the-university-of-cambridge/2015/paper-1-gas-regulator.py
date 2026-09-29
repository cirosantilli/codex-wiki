"""Original analytic solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(0,6,400);fig,axs=plt.subplots(1,2,figsize=(10.6,4.5))
for ratio in [.3,1,2]:
 gas=1+(ratio-1)*np.exp(-x);stars=x+(ratio-1)*(1-np.exp(-x));axs[0].plot(x,gas,lw=2,label='Initial Mg / Meq = %.1f'%ratio);axs[1].plot(x,stars,lw=2,label='Initial Mg / Meq = %.1f'%ratio)
axs[0].axhline(1,color='.4',ls=':');axs[0].set(ylabel='Gas mass / Meq',title='Stable gas equilibrium');axs[1].set(ylabel='Stellar mass / Meq',title='Stellar mass grows after gas settles')
for ax in axs:ax.set(xlabel='Time × ε');ax.legend(fontsize=8);ax.grid(alpha=.15)
fig.suptitle('Constant inflow: Meq = Φ/ε, no outflow or recycled gas');fig.tight_layout(rect=(0,0,1,.94))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
