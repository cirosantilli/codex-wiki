"""Original normalized expiry payoffs; no premium or financing cost included."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
s=np.linspace(0,2,500)
fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained',facecolor='white')
axes[0].plot(s,np.maximum(s-1,0),lw=2.3,label='Long call',color='#176b87')
axes[0].plot(s,np.maximum(1-s,0),lw=2.3,label='Long put',color='#c05229')
axes[1].plot(s,s-1,lw=2.3,label='Long forward',color='#176b87')
axes[1].plot(s,1-s,lw=2.3,label='Short forward',color='#c05229')
for ax in axes:
 ax.axhline(0,color='.6',lw=.8)
 ax.axvline(1,color='.6',lw=.8,ls=':')
 ax.set(xlabel=r'Terminal price $S_T/K$',ylabel='Payoff / K',xlim=(0,2),ylim=(-1.1,1.1))
 ax.legend(frameon=False)
axes[0].set_title('Options truncate the unfavourable payoff')
axes[1].set_title('Forward contracts allow gains and losses')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',metadata={'Software':'matplotlib'})
