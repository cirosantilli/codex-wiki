"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(8,3.5));t=np.linspace(0,10,2000);n=np.arange(11);ax.plot(t,np.cos(2*np.pi*.2*t),color='#176d97',label='0.2 fs cosine');ax.plot(t,np.cos(2*np.pi*.8*t),color='#bc7725',ls='--',lw=1,label='0.8 fs cosine');ax.scatter(n,np.cos(2*np.pi*.2*n),color='black',s=22,label='Identical samples',zorder=3);ax.set(xlabel='Time × sample rate',ylabel='Signal amplitude',xlim=(-.1,10.1),ylim=(-1.15,1.5));ax.legend(frameon=False,fontsize=9,ncols=3,loc='upper center');ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
