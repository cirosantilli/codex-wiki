"""Original timelike Schwarzschild launch orbits. Python 3.14, numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def trajectory(delta,steps=9000,phi_max=10*np.pi):
    # Units G=M=c=1; local launch speed, with static station at R=12.
    R=12.
    vc=np.sqrt(1/(R-2))
    v=vc*(1+delta)
    ell=R*v/np.sqrt(1-v*v)
    A=1/(ell*ell)
    step=phi_max/steps
    phi=np.linspace(0,phi_max,steps+1)
    values=np.empty((steps+1,2));values[0]=[1/R,0]
    def rhs(y): return np.array([y[1],A-y[0]+3*y[0]**2])
    for j in range(steps):
        y=values[j]
        k1=rhs(y);k2=rhs(y+step*k1/2);k3=rhs(y+step*k2/2);k4=rhs(y+step*k3)
        values[j+1]=y+step*(k1+2*k2+2*k3+k4)/6
    return phi,1/values[:,0],ell

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(9,4.5),layout='constrained')
angle=np.linspace(0,2*np.pi,500)
for ax,delta,color in zip(axes,[.03,-.03],['#126782','#aa3377']):
    phi,r,_=trajectory(delta)
    ax.plot(12*np.cos(angle),12*np.sin(angle),'--',color='.55',lw=1.3,label='Circular orbit r=R')
    ax.plot(r*np.cos(phi),r*np.sin(phi),color=color,lw=1.6,label='Perturbed orbit')
    ax.scatter([12],[0],color='#d65b24',s=48,zorder=5,label='Fixed station')
    ax.add_patch(plt.Circle((0,0),2,color='#333333'))
    ax.set(xlabel=r'$x/(GM/c^2)$',ylabel=r'$y/(GM/c^2)$',title=rf'$\Delta v/v_c={delta*100:+.0f}\%$; $R=12GM/c^2$',aspect='equal',xlim=(-16,16),ylim=(-16,16))
axes[0].legend(fontsize=9,loc='lower left',frameon=False)
fig.suptitle('Bound launch orbits: periapsis precession and repeated visits to the launch radius',fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
