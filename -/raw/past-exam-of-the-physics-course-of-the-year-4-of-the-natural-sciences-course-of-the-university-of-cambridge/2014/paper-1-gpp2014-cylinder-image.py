"""Original educational plot; Python 3.14, NumPy and Matplotlib. Writes a basename PNG in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Circle
fig,axs=plt.subplots(1,2,figsize=(8.7,3.8),layout='constrained');x=np.linspace(-2,3.3,420);y=np.linspace(-2.1,2.1,360);X,Y=np.meshgrid(x,y);r=np.hypot(X,Y);r1=np.hypot(X-2,Y);r2=np.hypot(X-.5,Y)
phi=np.log(2*np.maximum(r2,1e-7)/np.maximum(r1,1e-7));phi[(r<1)|(r1<.045)]=np.nan
axs[0].contour(X,Y,phi,levels=[.1,.25,.5,.7,1,1.5,2],colors='#225c91',linewidths=1)
axs[0].add_patch(Circle((0,0),1,facecolor='#ececec',edgecolor='black',lw=1.5));axs[0].scatter([2],[0],color='#ad4e27',s=35);axs[0].text(2.15,.1,r'$+\lambda$',color='#ad4e27');axs[0].text(0,0,'Grounded\nconductor',ha='center',va='center',fontsize=9)
axs[0].set(xlabel='x/a',ylabel='y/a',aspect='equal',xlim=(-2,3.3),ylim=(-2.1,2.1),title='Calculated exterior equipotentials');axs[0].grid(alpha=.15)
th=np.linspace(-np.pi,np.pi,800);sigma=-3/(5-4*np.cos(th));axs[1].plot(th/np.pi,sigma,color='#225c91');axs[1].set(xlabel=r'$\theta/\pi$ (zero toward real line)',ylabel=r'$2\pi a\sigma/\lambda$',title='Negative induced surface charge',xlim=(-1,1),ylim=(-3.15,0));axs[1].grid(alpha=.2)
fig.savefig('paper-1-gpp2014-cylinder-image.png',dpi=150,facecolor='white');plt.close(fig)
