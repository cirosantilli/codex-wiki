"""Original local-contour models; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Output is always written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
x=np.linspace(-1.6,1.6,301)
X,Y=np.meshgrid(x,x)
fig,axs=plt.subplots(1,3,figsize=(9,3.1),layout='constrained')
models=[(-X*X-Y*Y,[-3,-2,-1,-.3],'Maximum: $-x^2-y^2$'),(X*X+Y*Y,[.3,1,2,3],'Minimum: $x^2+y^2$'),(X*X-Y*Y,[-2,-1,-.3,.3,1,2],'Saddle: $x^2-y^2$')]
for ax,(F,levels,title) in zip(axs,models):
    cs=ax.contour(X,Y,F,levels=levels,cmap='coolwarm',linewidths=1.3)
    ax.clabel(cs,inline=True,fontsize=8,fmt='%g')
    ax.plot(0,0,'o',color='0.2',ms=4)
    ax.set(xlim=(-1.6,1.6),ylim=(-1.6,1.6),aspect='equal',xlabel='$x$',ylabel='$y$',title=title)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
axs[2].plot(x,x,'--',color='0.35',lw=1)
axs[2].plot(x,-x,'--',color='0.35',lw=1)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
