"""Write an opaque 1000x500 PNG basename; respect caller's MPLCONFIGDIR."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(10,5),dpi=100,facecolor='white')
pi=np.pi
for j in [-1,0,1]:
 lo=max(-2*pi,(2*j-1)*pi);hi=min(2*pi,(2*j+1)*pi)
 z=np.linspace(lo+1e-6,hi-1e-6,300)
 axes[0].plot(z,z-2*pi*j,color='#3274a1',lw=2)
for z in [-pi,pi]:
 axes[0].plot([z,z],[-pi,pi],':',color='#999999',lw=1)
 axes[0].scatter([z,z],[-pi,pi],s=28,facecolor='white',edgecolor='#3274a1',zorder=4)
 axes[0].scatter([z],[0],s=16,color='#313131',zorder=5)
z=np.linspace(-2*pi,2*pi,1200);even=np.abs((z+pi)%(2*pi)-pi)
axes[1].plot(z,even,color='#c24a32',lw=2)
axes[0].set_title('Odd extension: sawtooth\nFourier jump value = 0', fontsize=11)
axes[1].set_title('Even extension: continuous triangular wave', fontsize=11)
for ax in axes:
 ax.axhline(0,color='#333333',lw=.7);ax.axvline(0,color='#333333',lw=.7)
 ax.set(xlim=(-2*pi,2*pi),ylim=(-1.2*pi,1.2*pi),xlabel='x',ylabel='extension value')
 ax.set_xticks([-2*pi,-pi,0,pi,2*pi],['−2π','−π','0','π','2π']);ax.set_yticks([-pi,0,pi],['−π','0','π']);ax.grid(alpha=.2)
fig.tight_layout(pad=1.5)
fig.savefig(Path('paper-1-periodic-extensions.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
