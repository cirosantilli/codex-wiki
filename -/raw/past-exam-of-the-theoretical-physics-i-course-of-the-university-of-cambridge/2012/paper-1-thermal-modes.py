"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(figsize=(8,4.4),layout='constrained');u=np.linspace(0,8,1000)
for ratio,col in [(0,'#777777'),(.5,'#2d719e'),(1,'#b87a2e'),(2,'#925b8e')]:
 if ratio==1:y=2*u*np.exp(-u)
 elif ratio<1:
  d=np.sqrt(1-ratio*ratio);y=2*np.exp(-u)*np.sinh(d*u)/d
 else:
  d=np.sqrt(ratio*ratio-1);y=2*np.exp(-u)*np.sin(d*u)/d
 label={0:'uniform: k = 0',.5:'overdamped: k/(αc) = 0.5',1:'critical: k/(αc) = 1',2:'underdamped: k/(αc) = 2'}[ratio]
 ax.plot(u,y,color=col,label=label,lw=1.8)
ax.axhline(0,color='k',lw=.7);ax.axhline(1,color='grey',lw=.6,ls=':');ax.set(xlim=(0,8),ylim=(-.16,1.12),xlabel=r'elapsed time $\alpha c^2(t-t_0)$',ylabel=r'normalized impulse response $2\alpha G_k$',title='Retarded thermal modes: common initial slope, distinct late-time behaviour');ax.legend(fontsize=8);ax.grid(alpha=.15)

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
