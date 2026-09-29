"""Original theoretical illustration; Python3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(10.5,4.5),constrained_layout=True,facecolor='white')
u=np.linspace(0,12,500);axs[0].plot(u,1/(1+u),lw=2,color='#1864ab');axs[0].scatter([1],[.5],color='#1864ab');axs[0].set(xlabel=r'Intensity $I/I_s$',ylabel=r'Gain ratio $\alpha/\alpha_0$',title='Homogeneous saturation');axs[0].grid(alpha=.15)
z=np.linspace(0,9,450)
for u0,col in [(.08,'#1864ab'),(4,'#c92a2a')]:
 lo=np.full_like(z,u0);hi=u0+z
 for _ in range(65):
  mid=(lo+hi)/2;f=np.log(mid/u0)+mid-u0-z;hi=np.where(f>0,mid,hi);lo=np.where(f>0,lo,mid)
 sol=(lo+hi)/2;axs[1].plot(z,sol,lw=2,color=col,label=f'Input I/Is = {u0:g}')
axs[1].set(xlabel=r'Distance $\alpha_0 z$',ylabel=r'Intensity $I/I_s$',title='Positive-gain propagation approaches slope one');axs[1].legend(frameon=False);axs[1].grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
