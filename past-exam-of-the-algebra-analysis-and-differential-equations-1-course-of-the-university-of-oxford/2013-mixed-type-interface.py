"""Python 3.14; numpy and matplotlib. Output is written in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-1,1,501);y=np.linspace(-1,1,501);X,Y=np.meshgrid(x,y)
U=np.where(Y<0,-2*np.cos(np.pi*X)*np.sin(np.pi*Y),0.)
U=np.ma.masked_where(Y<np.abs(X)-1,U)
fig,axes=plt.subplots(1,2,figsize=(9.3,3.7),layout='constrained',facecolor='white')
a=axes[0];im=a.pcolormesh(X,Y,U,cmap='RdBu_r',vmin=-2,vmax=2,rasterized=True,shading='auto')
a.plot([-1,-1,1,1,0,-1],[0,1,1,0,-1,0],color='#333333',lw=1.1)
a.axhline(0,color='black',lw=1,ls='--');a.set(xlabel='$x$',ylabel='$y$',title='Continuous solution',aspect='equal',xlim=(-1.05,1.05),ylim=(-1.05,1.05));fig.colorbar(im,ax=a,label='$u$')
a=axes[1];a.plot(x,-2*np.pi*np.cos(np.pi*x),color='#a13838',lw=2,label=r'Lower trace $u_y(x,0^-)$');a.plot(x,np.zeros_like(x),color='#275b8a',lw=2,label=r'Upper trace $u_y(x,0^+)$');a.scatter([-.5,.5],[0,0],s=20,color='black',zorder=5)
a.set(xlabel='$x$',ylabel='Normal derivative',title='Traces disagree except at two points',xlim=(-1,1));a.legend(loc='upper center',fontsize=8);a.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2013-mixed-type-interface.png',dpi=140,facecolor='white')
