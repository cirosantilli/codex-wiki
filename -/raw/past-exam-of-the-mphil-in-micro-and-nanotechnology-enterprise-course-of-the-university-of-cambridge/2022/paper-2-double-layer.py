"""Original linear-screening double-layer model; Python 3.14/numpy/matplotlib.

Positive surface, dimensionless diffuse potential e*psi_d/kT=0.4.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
fig.patch.set_facecolor('white')
x=np.linspace(0,6,500)
u=.4*np.exp(-x)
ax=axes[0]
ax.plot(x,np.exp(-x),color='#2d718b',label=r'Potential $\psi/\psi_d$')
ax.plot(x,np.exp(-u),color='#b6623e',label=r'Co-ions $n_+/n_\infty$')
ax.plot(x,np.exp(u),color='#9274a0',label=r'Counterions $n_-/n_\infty$')
ax.axhline(1,color='.7',lw=.8)
ax.axvline(1,color='.7',ls=':')
ax.text(1.06,.18,r'$\lambda_D$',fontsize=11)
ax.set(xlabel=r'Distance from Stern-layer edge / $\lambda_D$',ylabel='Scaled potential or concentration',
       title='Diffuse profiles: positive plate',ylim=(0,1.7))
ax.legend(fontsize=9);ax.grid(alpha=.15)
ax=axes[1];ax.set(xlim=(-.65,5.7),ylim=(-.2,4.3),aspect='equal');ax.axis('off')
ax.add_patch(Rectangle((-.6,0),.35,4,facecolor='.6'))
ax.add_patch(Rectangle((-.25,0),.75,4,facecolor='#f0e3ce'))
for y in [.4,1.2,2,2.8,3.6]:ax.text(-.43,y,'+',ha='center',va='center',fontsize=15)
for y in [.5,1.5,2.5,3.5]:
    ax.add_patch(Circle((.12,y),.12,facecolor='#c8b8da'))
    ax.text(.12,y,'−',ha='center',va='center',fontsize=9)
# More counterions near the positive wall; the bulk becomes nearly balanced.
for px,py,sign in [(1,.3,'−'),(1.05,1.1,'−'),(.85,1.9,'−'),(1.15,2.8,'−'),(.8,3.6,'−'),
                    (2,.7,'−'),(2.3,2.1,'−'),(2.1,3.5,'+'),(3.3,.45,'+'),(3.5,1.5,'−'),
                    (3.6,2.7,'+'),(4.5,.85,'−'),(4.65,2,'+'),(4.6,3.2,'−'),(5.2,3.7,'+')]:
    ax.add_patch(Circle((px,py),.14,facecolor='#c8b8da' if sign=='−' else '#e6b7a1'))
    ax.text(px,py,sign,ha='center',va='center',fontsize=10)
ax.axvline(.5,color='.45',ls='--',lw=1)
ax.text(.13,4.12,'Stern',ha='center',fontsize=9)
ax.text(2.8,4.12,'Diffuse layer → bulk',ha='center',fontsize=11)
fig.savefig('paper-2-double-layer.png',dpi=150,facecolor='white')
plt.close(fig)
