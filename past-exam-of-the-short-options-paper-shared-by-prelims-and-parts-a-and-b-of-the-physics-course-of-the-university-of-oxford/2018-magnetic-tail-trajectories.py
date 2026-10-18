from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})

fig,axes=plt.subplots(1,2,figsize=(9,5.8),layout='constrained')
# Dimensionless dynamics m=a=P=1: x''=-2*x^3 and z'=x^2.
dt=.002;state=np.array([0.,1.,0.]);trace=[state.copy()]
def rhs(q):return np.array([q[1],-2*q[0]**3,q[0]**2])
for _ in range(5000):
 k1=rhs(state);k2=rhs(state+dt*k1/2);k3=rhs(state+dt*k2/2);k4=rhs(state+dt*k3)
 state+=dt*(k1+2*k2+2*k3+k4)/6;trace.append(state.copy())
trace=np.array(trace);ax=axes[0]
ax.plot(trace[:,0],trace[:,2],color='#16659c',lw=2)
for i in [400,1300,2300,3400,4500]:
 ax.annotate('',(trace[i+40,0],trace[i+40,2]),(trace[i,0],trace[i,2]),arrowprops={'arrowstyle':'->','color':'#16659c','lw':2})
ax.axvline(0,color='#aaaaaa',ls=':');ax.axvline(-1,color='#777777',ls='--');ax.axvline(1,color='#777777',ls='--')
ax.text(.04,.25,r'$\dot z=0$ at every $x=0$',fontsize=10)
ax.set(title=r'(i) $p_z=0$: crossing orbit',xlabel=r'$x/\sqrt{P/a}$',ylabel=r'$z/\sqrt{P/a}$',xlim=(-1.3,1.3))
ax.set_xticks([-1,0,1]);ax.grid(alpha=.15)
u=np.linspace(-4.5,4.5,1801);x=np.sqrt(2)/np.cosh(u);z=(2*np.tanh(u)-u)/np.sqrt(2);ax=axes[1]
ax.plot(x,z,color='#b45b14',lw=2)
for i in [70,350,650,1050,1400,1700]:
 ax.annotate('',(x[i+22],z[i+22]),(x[i],z[i]),arrowprops={'arrowstyle':'->','color':'#b45b14','lw':2})
u0=np.arccosh(np.sqrt(2));z0=(2*np.tanh(u0)-u0)/np.sqrt(2)
ax.scatter([1,1],[z0,-z0],color='#b22428');ax.annotate(r'$\dot z=0$',(1,z0),(.45,.8),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.axvline(0,color='#aaaaaa',ls=':');ax.axvline(np.sqrt(2),color='#777777',ls='--')
ax.annotate(r'$x_{\max}=\sqrt{2P/a}$',(np.sqrt(2),0),(.38,-1.15),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.text(.14,1.55,r'$x\to0$ as $t\to-\infty$',fontsize=10);ax.text(.14,-1.65,r'$x\to0$ as $t\to+\infty$',fontsize=10)
ax.set(title=r'(ii) $p_z=-P$: one-sided separatrix',xlabel=r'$x/\sqrt{P/a}$',ylabel=r'$z/\sqrt{P/a}$',xlim=(-.15,1.65),ylim=(-1.9,1.9));ax.grid(alpha=.15)
fig.suptitle(r'Positive charge in $B_y=B_0x/L$, with $P=\sqrt{2mH_0}$',fontsize=13)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
