"""Original solution diagram. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

x=np.linspace(0,2,700);fig,axs=plt.subplots(1,2,figsize=(8.6,3.8));pdf=4*np.exp(-4*x);axs[0].plot(x,pdf,lw=2);axs[0].fill_between(x,0,pdf,where=x>=1,color='darkorange',alpha=.65);axs[0].axvline(1,color='darkorange',ls='--');axs[0].set(xlabel='Height z/h',ylabel='Height density h P(z)',title='P(z) = (4/h) exp(−4z/h)',ylim=(0,4.2));axs[0].annotate('Tail area = e⁻⁴ ≈ 1.83%',(1.1,4*np.exp(-4.4)),(.5,1.8),arrowprops={'arrowstyle':'->'})
axs[1].semilogy(x,np.exp(-4*x),lw=2);axs[1].scatter([1],[np.exp(-4)],color='darkorange');axs[1].axhline(np.exp(-4),color='darkorange',ls=':');axs[1].set(xlabel='Threshold height z/h',ylabel='Fraction above that height',title='Exponential tail probability');axs[1].annotate('At release height h: 1.83%',(1,np.exp(-4)),(.3,.12),arrowprops={'arrowstyle':'->'})
for ax in axs:ax.grid(alpha=.15)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
