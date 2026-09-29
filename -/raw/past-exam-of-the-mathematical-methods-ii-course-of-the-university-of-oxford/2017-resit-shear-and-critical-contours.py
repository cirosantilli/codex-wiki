"""Original analytic field and contour plots. Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(10.8,4.8),layout='constrained')
x,y=np.meshgrid(np.linspace(-2,2,11),np.linspace(-2,2,17));v=np.exp(-y*y);curl=2*y*v
axs[0].quiver(x,y,v,np.zeros_like(v),curl,cmap='coolwarm',clim=(-.9,.9),scale=12,width=.004)
axs[0].axhline(0,color='.7',ls='--',lw=.8);axs[0].text(-1.9,1.82,'positive vorticity: anticlockwise',fontsize=9);axs[0].text(-1.9,-1.96,'negative vorticity: clockwise',fontsize=9)
axs[0].set(xlim=(-2.2,2.5),ylim=(-2.2,2.2),xlabel='x',ylabel='y',title=r'Gaussian shear: $v_x/v_0=e^{-y^2}$');axs[0].set_aspect('equal')
x,y=np.meshgrid(np.linspace(-4,4,700),np.linspace(-1.8,3.5,600));f=x*x+2*y*y-x*x*y
c=axs[1].contour(x,y,f,levels=[-12,-4,0,.3,1,1.7,3,5,9,15],cmap='viridis',linewidths=.9);axs[1].clabel(c,inline=True,fontsize=8)
xx=np.linspace(-3.2,3.2,500);axs[1].plot(xx,np.ones_like(xx),color='tab:red',lw=1.8,label='saddle contour f = 2');axs[1].plot(xx,xx*xx/2-1,color='tab:red',lw=1.8)
axs[1].plot(0,0,'o',color='black');axs[1].plot([-2,2],[1,1],'x',color='black',ms=8,mew=2);axs[1].annotate('local minimum',xy=(0,0),xytext=(-1.8,-.9),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].set(xlim=(-3.5,3.5),ylim=(-1.5,3),xlabel='x',ylabel='y',title=r'$f=x^2+2y^2-x^2y$');axs[1].legend(fontsize=9,loc='upper left');axs[1].set_aspect('equal')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
