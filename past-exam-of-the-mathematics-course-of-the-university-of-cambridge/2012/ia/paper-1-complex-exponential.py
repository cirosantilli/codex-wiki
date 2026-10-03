"""Complex exponential diagram. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Write the PNG basename to cwd and preserve the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axes=plt.subplots(1,2,figsize=(8,4),dpi=120,facecolor='white')
for ax in axes:
    ax.axhline(0,color='#888888',linewidth=.8)
    ax.axvline(0,color='#888888',linewidth=.8)
    ax.set(xlim=(-3.4,3.4),ylim=(-3.4,3.4),aspect='equal',xlabel='Real part',ylabel='Imaginary part')
    ax.grid(alpha=.15)
axes[0].plot([1,1],[-3.25,3.25],color='#0072B2',linewidth=2.3)
for start,end in [(2.75,3.3),(-2.75,-3.3)]:
    axes[0].annotate('',xy=(1,end),xytext=(1,start),arrowprops={'arrowstyle':'->','color':'#0072B2','lw':2.3})
axes[0].text(1.15,1.8,r'$z=1+iy$',color='#0072B2')
axes[0].set_title(r'Input: $\operatorname{Re}(z)=1$')
theta=np.linspace(0,2*np.pi,721)
axes[1].plot(np.e*np.cos(theta),np.e*np.sin(theta),color='#D55E00',linewidth=2.3)
axes[1].plot([0,np.e],[0,0],color='#D55E00',linewidth=1.3)
axes[1].text(1.25,.15,r'Radius $e$',color='#D55E00')
axes[1].set_title(r'Image: $|e^z|=e$')
fig.suptitle('A vertical line maps to a circle under the complex exponential',fontsize=11)
fig.tight_layout()
fig.savefig(Path('paper-1-complex-exponential.png'),facecolor='white',transparent=False)
plt.close(fig)
