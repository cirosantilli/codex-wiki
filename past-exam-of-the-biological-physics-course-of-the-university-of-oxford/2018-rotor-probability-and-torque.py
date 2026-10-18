"""Original model illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

def occupation(theta,beta):
    t=np.mod(theta,2*np.pi);alpha=1/(1+np.exp(-np.pi*beta))
    return np.where(t<=np.pi,alpha*np.exp(-beta*t),1-alpha*np.exp(-beta*(t-np.pi)))
def phase(beta):
    z=np.pi*beta/2
    return np.pi/2-(np.logaddexp(z,-z)-np.log(2))/beta
fig,axs=plt.subplots(2,2,figsize=(10,7.6),layout='constrained')
theta=np.linspace(0,2*np.pi,1801)
for ax,beta in zip(axs[0],[10,.2]):
    s=phase(beta);q=np.mod(theta-s,2*np.pi)/np.pi;pot=np.where(q<=1,q,2-q)
    ax.plot(theta/np.pi,occupation(theta,beta),label=r'$P_A$',lw=2)
    ax.plot(theta/np.pi,1-occupation(theta,beta),label=r'$P_B$',lw=2)
    ax.plot(theta/np.pi,pot,'--',color='black',label=r'optimal $U_A/U_0$')
    ax.set(xlabel=r'angle $\theta/\pi$',ylabel='probability / normalized potential',ylim=(-.05,1.08),title=rf'{"Slow" if beta>1 else "Fast"} rotation: $k_0/\omega={beta:g}$')
    ax.legend(fontsize=9,ncol=2)
ss=np.linspace(0,2*np.pi,301)
for beta in [.2,1,5]:
    # Independent numerical angular integration of the two torque halves.
    t=np.linspace(0,np.pi,1601)
    torque=np.array([np.trapezoid(-occupation(s+t,beta)+occupation(s+np.pi+t,beta),t)/(2*np.pi) for s in ss])
    axs[1,0].plot(ss/np.pi,torque,label=rf'$k_0/\omega={beta:g}$')
    axs[1,0].plot(phase(beta)/np.pi,(np.logaddexp(np.pi*beta/2,-np.pi*beta/2)-np.log(2))/(np.pi*beta),'o',ms=5)
axs[1,0].axhline(0,color='.7',lw=.8);axs[1,0].set(xlabel=r'potential phase $s/\pi$',ylabel=r'mean torque $\overline{T}/T_0$',title='Circles mark the optimum');axs[1,0].legend(fontsize=9)
v=np.geomspace(.01,100,401);b=1/v;z=np.pi*b/2
axs[1,1].semilogx(v,(np.logaddexp(z,-z)-np.log(2))/(np.pi*b),lw=2)
axs[1,1].axhline(.5,color='.6',ls='--',label='slow-speed limit 1/2')
axs[1,1].set(xlabel=r'rotation speed $\omega/k_0$',ylabel=r'optimal torque $\overline{T}_{\max}/T_0$',ylim=(0,.53),title='Occupation cannot follow rapid rotation');axs[1,1].legend(fontsize=9)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
