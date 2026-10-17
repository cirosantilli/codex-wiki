"""Original phase diagram from analytic constrained energy minimization."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
x=np.linspace(0,10,700);y=np.linspace(.00001,4,500);X,Y=np.meshgrid(x,y);reg=np.where(X<=2,0,np.where(X>=2+2*Y,2,1))
fig,ax=plt.subplots(figsize=(7.5,4.6),layout='constrained');ax.pcolormesh(X,Y,reg,cmap=ListedColormap(['#d9e8f2','#fde4a2','#bfd8b5']),shading='auto',vmin=0,vmax=2,rasterized=True)
ax.axvline(2,color='black',lw=1.5);ax.plot([2,10],[0,4],color='black',lw=1.5)
ax.text(.25,2,'Unwrapped\n'+r'$\xi=0$',fontsize=11);ax.text(3,3.25,'Partly wrapped\n'+r'$\xi=(\bar w-2)/\bar\sigma$',fontsize=11);ax.text(6.5,.65,'Fully wrapped\n'+r'$\xi=2$',fontsize=11)
ax.plot(2,0,'ko',ms=5);ax.set(xlim=(0,10),ylim=(0,4),xlabel=r'$\bar w=wr_0^2/\kappa$',ylabel=r'$\bar\sigma=\sigma r_0^2/\kappa$',title='Constrained minimum of the bound-cap energy')
fig.savefig('paper-1-wrapping-phases.png',dpi=170,facecolor='white');plt.close(fig)
