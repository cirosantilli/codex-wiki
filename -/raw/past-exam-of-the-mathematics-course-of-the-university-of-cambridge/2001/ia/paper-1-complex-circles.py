"""Original complex circle sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Emit PNG basename to caller CWD, retaining caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
ax.set_facecolor('white')
t=np.linspace(0,2*np.pi,800)
for a,color in zip((-2,-1,-.5,.5,1),('#2066a8','#e77922','#33964b','#a449a2','#c52f35')):
    center=1/a;radius=np.sqrt(1-a)/abs(a)
    label=rf'$\alpha={a:g}$: center ${center:g}$, radius ${radius:.3g}$'
    if radius:
        ax.plot(center+radius*np.cos(t),radius*np.sin(t),color=color,lw=2,label=label)
        ax.plot(center,0,'+',color=color,ms=9,mew=2)
    else:
        ax.plot(center,0,'o',color=color,ms=8,label=label)
ax.axhline(0,color='#777777',lw=.7)
ax.axvline(0,color='#777777',lw=.7)
ax.set_aspect('equal')
ax.set_xlim(-4.8,3.7);ax.set_ylim(-2.8,2.8)
ax.set_xlabel(r'$\operatorname{Re}z$',fontsize=12)
ax.set_ylabel(r'$\operatorname{Im}z$',fontsize=12)
ax.set_title(r'Circle loci for $\beta=\gamma=1$; $\alpha=1$ is a single point',fontsize=14)
ax.legend(loc='upper right',fontsize=9,framealpha=1)
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig('paper-1-complex-circles.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
