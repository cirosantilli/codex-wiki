"""Original Rayleigh sketch. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from the mirrored _media directory; the white PNG is saved to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

q=np.linspace(0,4.5,700)
f=q*np.exp(-q*q/2)
fig,ax=plt.subplots(figsize=(6.5,4.0),layout='constrained',facecolor='white')
ax.plot(q,f,color='#0072b2',lw=2)
ax.plot(1,np.exp(-.5),'o',color='#d55e00',ms=5)
ax.annotate(r'Mode: $x/\sigma=1$',(1,np.exp(-.5)),xytext=(.05,.69),fontsize=10,
            arrowprops={'arrowstyle':'-', 'color':'#777777'})
mean=np.sqrt(np.pi/2)
ax.axvline(mean,color='#009e73',ls='--',lw=1.2)
ax.text(1.5,.65,r'Mean: $\sqrt{\pi/2}$',color='#007a55',fontsize=10)
ax.set(xlim=(0,4.5),ylim=(0,.76),xlabel=r'$x/\sigma$',ylabel=r'$\sigma f(x)$',
       title='Rayleigh probability density')
ax.grid(alpha=.18)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
