"""Original gas characteristics; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Writes basename to caller CWD; preserves MPLCONFIGDIR. Example gamma=1.4.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def minus_speed(t,x):
    if x>=t:return -1.
    disc=max(0.,(1+6*t)**2-14*(t-x))
    tau=((1+6*t)-np.sqrt(disc))/7
    return -1-4*min(1.,max(0.,tau))

fig,ax=plt.subplots(figsize=(7,4.6),facecolor='white')
t=np.linspace(0,1.25,500);piston=-2.5*t*t;edge=np.where(t<=1,piston,-2.5-5*(t-1))
ax.fill_betweenx(t,piston,edge,where=t>=1,color='#f6ddbd',label='Vacuum gap')
ax.plot(piston,t,color='black',lw=2,label='Piston')
ax.plot(edge[t>=1],t[t>=1],color='#ad4737',lw=2,label='Gas edge after vacuum')
for j,tau in enumerate(np.linspace(0,1,11)):
    tt=np.linspace(tau,1.25,160);xx=-2.5*tau*tau+(1-6*tau)*(tt-tau)
    ax.plot(xx,tt,color='#256b8f',lw=.9,label=r'Outgoing $C_+$' if j==0 else None)
for j,x0 in enumerate([.3,.7,1.1,1.5,2.]):
    tt=np.linspace(0,1.25,1400);xs=np.empty_like(tt);xs[0]=x0
    for i in range(len(tt)-1):
        h=tt[i+1]-tt[i];s=tt[i];x=xs[i]
        k1=minus_speed(s,x);k2=minus_speed(s+h/2,x+h*k1/2);k3=minus_speed(s+h/2,x+h*k2/2);k4=minus_speed(s+h,x+h*k3)
        xs[i+1]=x+h*(k1+2*k2+2*k3+k4)/6
    ax.plot(xs,tt,'--',color='#6c963d',lw=.9,label=r'Incoming $C_-$' if j==0 else None)
ax.scatter([-2.5],[1],color='#ad4737',s=24,zorder=5)
ax.annotate('Vacuum first forms',(-2.5,1),xytext=(-3.5,.66),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set_xlim(-4.25,2.05);ax.set_ylim(0,1.25);ax.set_xlabel(r'$x/(c_0t_v)$');ax.set_ylabel(r'$t/t_v$');ax.set_title('Accelerating withdrawal: rarefaction characteristics')
ax.legend(loc='upper right',fontsize=9);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('paper-2-piston-characteristics.png'),dpi=150,facecolor='white',transparent=False);plt.close(fig)
