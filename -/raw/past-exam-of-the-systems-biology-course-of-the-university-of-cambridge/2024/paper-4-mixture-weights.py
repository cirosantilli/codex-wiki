"""Original illustrative mixture curves; no exam data are digitized."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-3.5,4,600)
a=np.exp(-.5*((x+1)/.5)**2)/(.5*np.sqrt(2*np.pi))
b=np.exp(-.5*((x-1)/.75)**2)/(.75*np.sqrt(2*np.pi))
fig,axes=plt.subplots(1,3,figsize=(10,3.7),layout='constrained',facecolor='white')
for ax,p in zip(axes,[.1,.5,.9]):
 ax.plot(x,(1-p)*a,'--',color='.4',label='Component 0 contribution')
 ax.plot(x,p*b,':',color='.2',label='Component 1 contribution')
 ax.plot(x,(1-p)*a+p*b,color='#245c9f',linewidth=2,label='Mixture density')
 ax.set(xlabel='Illustrative current (arbitrary units)',ylabel='Probability density',ylim=(0,.8),title=f'Component 1 fraction = {p:.1f}')
 ax.spines[['top','right']].set_visible(False)
axes[1].legend(fontsize=8,loc='upper right')
fig.savefig(Path('paper-4-mixture-weights.png'),dpi=130,facecolor='white');plt.close(fig)
