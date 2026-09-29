"""Original Ricker graph; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Writes basename to caller CWD and leaves MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
r=2.7
x=np.linspace(0,3.2,500);y=x*np.exp(r*(1-x));xm=1/r;ym=xm*np.exp(r-1)
fig,ax=plt.subplots(figsize=(5.7,3.6),facecolor='white')
ax.plot(x,y,label=r'$f(N)/K$, example $r=2.7$');ax.plot(x,x,'--',color='gray',label=r'$N/K$')
ax.plot([xm,xm],[0,ym],':',color='#ad4737');ax.plot([0,xm],[ym,ym],':',color='#ad4737')
ax.scatter([xm,1],[ym,1],color='#ad4737',zorder=4)
ax.annotate(r'$N_{\max}/K=e^{r-1}/r$',(xm,ym),xytext=(.62,2.25),arrowprops={'arrowstyle':'->'})
ax.set_xticks([0,xm,1,2,3],['0',r'$1/r$','1','2','3']);ax.set_xlabel(r'Population $N/K$');ax.set_ylabel(r'Updated population $f(N)/K$')
ax.set_ylim(0,2.6);ax.legend(loc='upper right');ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('paper-2-ricker.png'),dpi=150,facecolor='white',transparent=False);plt.close(fig)
