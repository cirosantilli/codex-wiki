"""Scalar Landau phase diagram and metastable branch geometry.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7.
Writes only paper-46-phases.png in caller CWD; respects supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
u=np.linspace(-1.2,0,401)
ax.plot(u,3*u*u/16,color='#9b2529',lw=2.2,label='First-order coexistence')
ax.plot([0,1.2],[0,0],color='#216c9e',lw=2.2,label='Continuous transition')
ax.plot(u,u*u/4,color='#777777',ls=':',lw=1.6,label='Ordered spinodal')
ax.plot([-1.2,0],[0,0],color='#777777',ls='--',lw=1.6,label='Disordered spinodal')
ax.scatter([0],[0],color='black',s=45,zorder=5)
ax.annotate('Tricritical point',(0,0),xytext=(12,-32),textcoords='offset points',arrowprops={'arrowstyle':'-'},fontsize=10)
ax.text(.43,.21,'Disordered\nM = 0',ha='center',fontsize=12)
ax.text(-.6,-.105,'Ordered\nM = +M₀ or −M₀',ha='center',fontsize=11)
ax.set(xlim=(-1.25,1.25),ylim=(-.18,.42),xlabel='Quartic coefficient u',ylabel='Quadratic coefficient r',title='Sextic potential: h = 0, v = 1')
ax.legend(loc='upper right',fontsize=8)
ax.grid(alpha=.18)
# For r=-1,u=1, stationary equation h=M^3-M.
m=np.linspace(-1.5,1.5,1601)
sp=1/np.sqrt(3);hs=2/(3*np.sqrt(3))
for part in [m<-sp,m>sp]:
    bx.plot((m**3-m)[part],m[part],color='#216c9e',lw=2.1)
mid=np.abs(m)<=sp
bx.plot((m**3-m)[mid],m[mid],color='#a96522',ls='--',lw=1.6,label='Unstable stationary branch')
bx.plot([],[],color='#216c9e',lw=2.1,label='Locally stable branches')
bx.plot([0,0],[-1,1],color='#666666',ls=':',lw=1.3,label='Equilibrium switch at h = 0')
# No-nucleation switching paths at the local-stability limits.
for x,y0,y1,col in [(hs,-sp,2*sp,'#9b2529'),(-hs,sp,-2*sp,'#74519a')]:
    bx.annotate('',(x,y1),(x,y0),arrowprops={'arrowstyle':'->','color':col,'lw':2})
    bx.scatter([x],[y0],color=col,s=30,zorder=5)
bx.annotate('Increasing h:\nmetastable limit',(hs,-sp),xytext=(-120,-37),textcoords='offset points',fontsize=9,color='#9b2529')
bx.annotate('Decreasing h:\nmetastable limit',(-hs,sp),xytext=(-104,15),textcoords='offset points',fontsize=9,color='#74519a')
bx.set(xlim=(-.7,.7),ylim=(-1.4,1.4),xlabel='Conjugate field h',ylabel='Stationary magnetization M',title='Quartic potential: r = −1, u = 1')
bx.grid(alpha=.18)
bx.legend(loc='upper left',fontsize=8)
fig.suptitle('Tricritical coexistence and local-stability limits')
fig.savefig(Path.cwd()/'paper-46-phases.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
