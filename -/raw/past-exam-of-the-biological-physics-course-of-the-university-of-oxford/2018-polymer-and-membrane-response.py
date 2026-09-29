"""Original model illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(2,2,figsize=(10,7.8),layout='constrained')
u=np.linspace(.0001,18,1201);L=1/np.tanh(u)-1/u
for T,color in [(298.15,'tab:blue'),(333.15,'tab:red')]:
    f=1.380649e-23*T*u/(.4e-9)*1e12
    axs[0,0].plot(14*L,f,label=f'{T-273.15:.0f} °C',color=color,lw=2)
    x=np.linspace(0,8,100);k=3*1.380649e-23*T/(35*(.4e-9)**2)*1e3
    axs[0,0].plot(x,k*x,'--',color=color,alpha=.7)
axs[0,0].axvline(14,color='.4',ls=':',label='inextensible contour 14 nm')
axs[0,0].set(xlabel='mean extension (nm)',ylabel='force (pN)',xlim=(0,15.8),ylim=(0,120),title='FJC response; dashed lines are weak-force limits');axs[0,0].legend(fontsize=8,loc='upper left')
t=np.linspace(0,6,401);n=1-np.exp(-t)
axs[0,1].plot(t,n,label=r'$n=1-e^{-t/\tau}$',lw=2);axs[0,1].plot(t,n**4,label=r'$n^4$',lw=2)
axs[0,1].set(xlabel=r'time $t/\tau$',ylabel='normalized availability / conductance',title='Four permissive gates delay the current');axs[0,1].legend()
ax=axs[1,0];ax.set(xlim=(-.5,4.6),ylim=(-.1,4.9));ax.axis('off');ax.set_title('Membrane circuit: parallel C and ionic branches')
ax.plot([0,4],[4,4],color='black');ax.plot([0,4],[.5,.5],color='black')
ax.text(-.35,4.1,r'$V_m$',ha='center');ax.text(-.25,.25,'outside',fontsize=9)
for x,label in [(0,'C'),(1,'Na'),(2,'K'),(3,'Cl'),(4,'leak')]:
    if x==0:
        ax.plot([x,x],[4,2.55],color='black');ax.plot([x-.22,x+.22],[2.55,2.55],color='black');ax.plot([x-.22,x+.22],[2.3,2.3],color='black');ax.plot([x,x],[2.3,.5],color='black');ax.text(x-.32,2.6,r'$C_m$',ha='right',fontsize=10)
    else:
        ax.plot([x,x],[4,3.35],color='black')
        yy=np.linspace(3.35,2.1,9);xx=x+np.array([0,.13,-.13,.13,-.13,.13,-.13,.13,0]);ax.plot(xx,yy,color='black')
        ax.plot([x,x],[2.1,1.55],color='black');ax.plot([x-.23,x+.23],[1.55,1.55],color='black');ax.plot([x-.12,x+.12],[1.35,1.35],color='black');ax.plot([x,x],[1.35,.5],color='black')
        ax.text(x+.19,2.7,f'$g_{{{label}}}$',fontsize=10);ax.text(x+.15,.95,f'$E_{{{label}}}$',fontsize=10)
for g,label in [(3,'large chloride conductance'),(1.2,'reduced chloride conductance')]:
    v=(1-np.exp(-g*t))/g;axs[1,1].plot(t,v,label=label,lw=2)
axs[1,1].set(xlabel='normalized time',ylabel='voltage perturbation / applied current',title='Passive response: less chloride shunting');axs[1,1].legend(fontsize=8)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
