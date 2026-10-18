"""Original adiabats and latent heat from the specified empirical fit; Python 3.14."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10.5,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(12,4.1),layout='constrained',facecolor='white')
p=np.geomspace(1e-4,1,500);ratio=2/7;colors=['#355a9b','#bd7820','#269572']
for b,color in zip([0,1,3],colors):
 lo=np.full_like(p,1e-10);hi=np.ones_like(p)
 for _ in range(80):
  mid=(lo+hi)/2;v=np.log(mid)+b*(mid-1)-ratio*np.log(p);hi=np.where(v>0,mid,hi);lo=np.where(v<=0,mid,lo)
 T=(lo+hi)/2;axes[0].plot(T,p,color=color,lw=2,label=f'b = {b}')
 z=np.linspace(0,1+b/2,500);theta=1-z if b==0 else (np.sqrt((1+b)**2-2*b*z)-1)/b
 axes[1].plot(theta,z,color=color,lw=2,label=f'b = {b}')
axes[0].set(yscale='log',ylim=(1,1e-4),xlabel='T / Ts',ylabel='p / ps',title='A  Warmer at a given pressure');axes[0].legend(frameon=False)
axes[1].set(xlabel='T / Ts',ylabel='g z / (A Ts)',title='B  Larger formal atmospheric depth');axes[1].legend(frameon=False)
L=lambda T:461.5*np.log(10)*643.758*(T/(T-198.043))**2/1e6
T=np.linspace(380,573,400);ext=np.linspace(573,647,200);axes[2].plot(T,L(T),lw=2,color=colors[0],label='fit interval');axes[2].plot(ext,L(ext),'--',color=colors[1],label='invalid extrapolation');axes[2].scatter([647],[0],color='#a43838',zorder=4,label='critical latent heat = 0')
axes[2].set(xlabel='temperature (K)',ylabel='latent heat (MJ kg⁻¹)',ylim=(-.1,3.2),title='C  Antoine-fit limitation');axes[2].legend(frameon=False,fontsize=8.5)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
