"""Original switch-on trajectories, with mass ratio ten for illustration."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
t=np.linspace(0,2*np.pi,600)
fig,axes=plt.subplots(1,3,figsize=(12,4.1),layout='constrained')
axes[0].plot(np.cos(t)-1,-np.sin(t),color='#126782',lw=2.4)
axes[0].scatter([0],[0],color='#b44b35',zorder=5,label='Switch-on')
axes[0].scatter([-1],[0],marker='+',color='.4')
axes[0].set(xlabel=r'$k_x/K$',ylabel=r'$k_y/K$',title='Crystal momentum: shifted circle',aspect='equal',xlim=(-2.2,.2),ylim=(-1.2,1.2))
axes[0].legend(fontsize=10,frameon=False,loc='lower left')
axes[1].plot(np.sin(t)-t,.1*(np.cos(t)-1),color='#126782',lw=2.4)
axes[1].scatter([0],[0],color='#b44b35',zorder=5)
axes[1].set(xlabel=r'$(x-x_0)/L_x$',ylabel=r'$(y-y_0)/L_x$',title=r'Real space: drift, $m_y/m_x=10$',ylim=(-.23,.03))
axes[1].text(.04,.91,'Different axis scales',transform=axes[1].transAxes,fontsize=10,color='.4')
axes[2].plot(np.sin(t),.1*np.cos(t),color='#126782',lw=2.4)
axes[2].set(xlabel=r'$(x-x_0+L_x\omega t)/L_x$',ylabel=r'$(y-y_0+L_y)/L_x$',title='Moving frame: elliptic oscillation',aspect='equal',xlim=(-1.2,1.2),ylim=(-.7,.7))
fig.suptitle(r'$K=eE_0/(\hbar\omega)$; $L_i=eE_0/(m_i\omega^2)$',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
