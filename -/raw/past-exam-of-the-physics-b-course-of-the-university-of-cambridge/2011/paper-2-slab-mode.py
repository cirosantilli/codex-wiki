"""Original dimensionless dielectric-slab mode; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
V=1.4;lo=0.;hi=min(V,np.pi/2)
for _ in range(80):
 mid=(lo+hi)/2
 if mid*np.tan(mid)>np.sqrt(V*V-mid*mid):hi=mid
 else:lo=mid
u0=(lo+hi)/2;w0=np.sqrt(V*V-u0*u0);u=np.linspace(0,V,600);s=np.linspace(-4,4,1200)
fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
axs[0].plot(u,np.sqrt(V*V-u*u),color='#246d9c',label=r'$u^2+w^2=\mathcal{V}^2$');axs[0].plot(u,u*np.tan(u),color='#bd7831',label=r'$w=u\tan u$');axs[0].plot(u0,w0,'ko',ms=5);axs[0].annotate(f'u = {u0:.3f}\nw = {w0:.3f}',xy=(u0,w0),xytext=(.12,2.1),arrowprops={'arrowstyle':'->'},fontsize=9);axs[0].set(xlabel='u = Kd',ylabel="w = K′d",xlim=(0,V),ylim=(0,2.8),title=r'First-branch crossing: $\mathcal{V}=1.4$');axs[0].legend(fontsize=8)
f=np.where(abs(s)<=1,np.cos(u0*s),np.cos(u0)*np.exp(-w0*(abs(s)-1)));axs[1].plot(s,f,color='#246d9c',lw=2);axs[1].axvspan(-1,1,color='#246d9c',alpha=.08);axs[1].axvline(-1,color='grey',ls=':',lw=.8);axs[1].axvline(1,color='grey',ls=':',lw=.8);axs[1].set(xlabel='z/d',ylabel=r'field amplitude $f(z)/E_0$',title='Nodeless core with evanescent tails',ylim=(0,1.08));axs[1].text(0,.12,'dielectric core',ha='center',fontsize=9)
for ax in axs:ax.grid(alpha=.16)
fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
