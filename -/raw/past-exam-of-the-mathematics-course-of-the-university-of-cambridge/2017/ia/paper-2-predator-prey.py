"""Original phase portrait; write a same-basename opaque PNG into cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def velocity(z):
    x, y = z
    return np.array([x*(1-x-y), y*(4*x-1)/8])

def trajectory(initial, dt=0.02, count=7000):
    z=np.array(initial,dtype=float)
    states=[z.copy()]
    for _ in range(count):
        k1=velocity(z)
        k2=velocity(z+dt*k1/2)
        k3=velocity(z+dt*k2/2)
        k4=velocity(z+dt*k3)
        z=z+dt*(k1+2*k2+2*k3+k4)/6
        assert np.all(z>0)
        states.append(z.copy())
        if np.linalg.norm(z-[0.25,0.75])<0.001:
            break
    return np.array(states)

fig,ax=plt.subplots(figsize=(10,6),dpi=90,facecolor='white')
x,y=np.meshgrid(np.linspace(0.03,1.22,21),np.linspace(0.03,1.47,21))
u=x*(1-x-y);v=y*(4*x-1)/8
speed=np.hypot(u,v)
ax.quiver(x,y,u/speed,v/speed,color='#c2c7cc',angles='xy',scale_units='xy',scale=27,width=0.003)
xx=np.linspace(0,1,200)
ax.plot(xx,1-xx,'--',color='#56697e',linewidth=1.5,label=r'$\dot x=0$: $x+y=1$')
ax.axvline(0.25,color='#9b698c',linestyle='--',linewidth=1.5,label=r'$\dot y=0$: $x=1/4$')
colors=['#c45b27','#277da8','#629732','#8a589d','#bb365c','#997528']
starts=[(1.1,.3),(.1,.08),(.03,1.3),(1.,1.2),(.2,.3),(.5,.75)]
for initial,color in zip(starts,colors):
    orbit=trajectory(initial)
    ax.plot(orbit[:,0],orbit[:,1],color=color,linewidth=1.6)
    ax.scatter(*initial,color=color,s=18,zorder=4)
    for fraction in [.12,.35,.6]:
        i=int(fraction*(len(orbit)-30))
        ax.annotate('',xy=orbit[i+25],xytext=orbit[i],arrowprops=dict(arrowstyle='->',color=color,lw=1.7))
ax.scatter([0,1],[0,0],s=55,facecolors='white',edgecolors='black',zorder=6,label='Boundary saddles')
ax.scatter([.25],[.75],s=65,c='black',zorder=6,label='Stable spiral')
ax.annotate(r'$(1/4,3/4)$',(.25,.75),xytext=(.48,.97),arrowprops=dict(arrowstyle='-',color='black'),fontsize=11)
ax.set(xlim=(-.035,1.26),ylim=(-.035,1.53),xlabel=r'$x$',ylabel=r'$y$',title='Logistic predator–prey phase portrait')
ax.legend(loc='upper right',fontsize=9,framealpha=.95)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout(pad=1.8)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=90,facecolor='white',transparent=False)
plt.close(fig)
