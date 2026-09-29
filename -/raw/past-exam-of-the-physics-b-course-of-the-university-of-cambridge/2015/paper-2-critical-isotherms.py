"""Original solution diagram. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(9.2,4.2));x=np.linspace(0,2.25,900)
for t,col in [(1.25,'steelblue'),(1,'black'),(.8,'darkorange')]:
 y=x**3-3*x*x+3*t*x;axs[0].plot(x,y,color=col,lw=2,label=f'T/Tc = {t:g}')
 if t<1:
  l,r=1-np.sqrt(1-t),1+np.sqrt(1-t);xx=np.linspace(l,r,200);yy=xx**3-3*xx**2+3*t*xx;axs[0].plot(xx,yy,'--',color='darkred',lw=3,label='Unstable homogeneous segment')
axs[0].scatter([1],[1],s=30,color='black');axs[0].annotate('critical point',(1,1),(.2,1.9),arrowprops={'arrowstyle':'->'});axs[0].set(xlabel='Density n/nc',ylabel='Pressure p/pc',ylim=(0,5),xlim=(0,2.25),title='Cubic-density equation of state');axs[0].legend(fontsize=8,loc='upper left')
for lo,hi,col,ls,label in [(.55,.985,'darkred','--','Unstable homogeneous branch'),(1.015,1.7,'steelblue','-','Stable T > Tc branch')]:
 t=np.linspace(lo,hi,700);axs[1].plot(t,1/(t-1),color=col,ls=ls,lw=2,label=label)
axs[1].axvline(1,color='.4',ls=':');axs[1].axhline(0,color='.5',lw=.7);axs[1].set(xlabel='Temperature T/Tc',ylabel='Scaled compressibility nc kB Tc κT',ylim=(-10,10),title='Compressibility at fixed n = nc');axs[1].legend(fontsize=8,loc='lower right')
for ax in axs:ax.grid(alpha=.15)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
