# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
eps=.05;K=.5;lam=.2
def fun(y):
    s,c=y;return np.array([eps*(-s+(s+K-lam)*c),s-(s+K)*c])
y=np.array([1.,0.]);ys=[y.copy()];dt=.025
for _ in range(32000):
    a=fun(y);b=fun(y+dt*a/2);c=fun(y+dt*b/2);e=fun(y+dt*c);y=y+dt*(a+2*b+2*c+e)/6;ys.append(y.copy())
ys=np.array(ys);ss=np.linspace(0,1.05,400);fig,ax=plt.subplots(figsize=(7,4.8))
ax.plot(ss,ss/(ss+K),'--',color='#2171b5',label=r'$\dot C=0$');ax.plot(ss,ss/(ss+K-lam),':',color='#606060',lw=2,label=r'$\dot S=0$');ax.plot(ys[:,0],ys[:,1],color='#c34f2d',lw=2,label='kinetic trajectory')
for i in [20,450,1500,5000]:
    ax.annotate('',ys[i+35],ys[i],arrowprops={'arrowstyle':'->','color':'#c34f2d','lw':1.8})
ax.plot(1,0,'ko');ax.annotate('initial layer',(ys[30,0],ys[30,1]),(.65,.12),arrowprops={'arrowstyle':'->'},fontsize=9);ax.annotate('slow depletion',(ys[2200,0],ys[2200,1]),(.1,.72),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlabel='$[S]/S_0$',ylabel='$[C]/E_0$',xlim=(0,1.05),ylim=(0,.85),title=r'Enzyme phase plane: $\epsilon=.05, K=.5, \lambda=.2$');ax.legend(loc='lower left',fontsize=8);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('2008-enzyme-phase-plane.png'),dpi=150,facecolor='white');plt.close(fig)
