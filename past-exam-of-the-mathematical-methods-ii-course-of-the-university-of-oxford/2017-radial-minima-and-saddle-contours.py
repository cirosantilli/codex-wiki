"""Original analytic level plots for degenerate minima and saddle topology. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(10.8,5.1),layout='constrained');x,y=np.meshgrid(np.linspace(-10,10,651),np.linspace(-10,10,651));f=np.cos(np.hypot(x,y));im=axs[0].pcolormesh(x,y,f,shading='nearest',cmap='coolwarm',vmin=-1,vmax=1,rasterized=True)
t=np.linspace(0,2*np.pi,1001)
for n in [1,3]:axs[0].plot(n*np.pi*np.cos(t),n*np.pi*np.sin(t),color='black',lw=1.5,label='minimum circles' if n==1 else None)
axs[0].plot(2*np.pi*np.cos(t),2*np.pi*np.sin(t),'--',color='white',lw=1.2,label='maximum circle');axs[0].plot(0,0,'o',color='white',mec='black',ms=5);axs[0].set(title=r'$f=\cos\sqrt{x^2+y^2}$',xlabel='x',ylabel='y');axs[0].set_aspect('equal');axs[0].legend(fontsize=8,loc='upper left');fig.colorbar(im,ax=axs[0],shrink=.65,label='function value')
x,y=np.meshgrid(np.linspace(-2,2,701),np.linspace(-2,2,701));f=4*x*y-x**4-y**4;c=axs[1].contour(x,y,f,levels=[-12,-5,-1,.3,1,1.7],cmap='viridis',linewidths=1);axs[1].clabel(c,inline=True,fontsize=8)
for off in [0,np.pi]:
 th=np.linspace(0,np.pi/2,1001)+off;r=np.sqrt(np.maximum(0,8*np.sin(2*th)/(3+np.cos(4*th))));axs[1].plot(r*np.cos(th),r*np.sin(th),color='tab:red',lw=1.8,label='saddle contour f = 0' if off==0 else None)
axs[1].plot(0,0,'x',color='black',ms=8,mew=2);axs[1].plot([1,-1],[1,-1],'o',color='black',ms=5);axs[1].annotate('global maxima',xy=(1,1),xytext=(.1,1.75),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].set(title=r'$f=4xy-x^4-y^4$',xlabel='x',ylabel='y',xlim=(-2,2),ylim=(-2,2));axs[1].set_aspect('equal');axs[1].legend(fontsize=8,loc='lower right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
