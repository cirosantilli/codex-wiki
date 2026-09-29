"""Original physiological-model figures; writes PNGs to output CWD.
Tested Python3.14.4, numpy2.3.5, matplotlib3.10.7; repository pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
def rk4(fun,y0,end,dt):
 t=np.arange(0,end+dt/2,dt);out=np.empty((len(t),len(y0)));out[0]=y0
 for i in range(len(t)-1):
  y=out[i];k1=fun(y);k2=fun(y+dt*k1/2);k3=fun(y+dt*k2/2);k4=fun(y+dt*k3);out[i+1]=y+dt*(k1+2*k2+2*k3+k4)/6
 return t,out
m3=lambda v:1/(1+np.exp(-25*(v-.2)))
ninf=lambda v:.8/(1+np.exp(-20*v))
g=lambda v,n:.1*(v+.2)*n**4-(1-v)*(.8-n)*m3(v)
v=np.linspace(-.199999,1,1700);lo=np.zeros_like(v);hi=np.full_like(v,.8)
for _ in range(55):
 mid=(lo+hi)/2;take=g(v,mid)<0;lo=np.where(take,mid,lo);hi=np.where(take,hi,mid)
null=(lo+hi)/2
fun=lambda y:np.array([-g(y[0],y[1])/.01,ninf(y[0])-y[1]])
t,orbit=rk4(fun,[.3,.5],45,.001)
fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
vv=np.linspace(-.2,1,1000)
for nn in [.4,.6,.75]:axes[0].plot(vv,g(vv,nn),label=f'n={nn:g}')
axes[0].axhline(0,color='black',lw=.8);axes[0].set(xlabel='v',ylabel='g(v,n)',title='Activation permits three voltage roots');axes[0].legend(fontsize=8)
axes[1].plot(v,null,color='#b24c2d',lw=2,label='g(v,n)=0');axes[1].plot(v,ninf(v),color='#218151',ls='--',label='n=n∞(v)');last=orbit[t>35];axes[1].plot(last[:,0],last[:,1],color='#216ba0',lw=1.2,label='Oscillating trajectory');axes[1].set(xlabel='v',ylabel='n',title='One admissible fast–slow example',xlim=(-.22,1.02),ylim=(0,.84));axes[1].legend(fontsize=8)
for ax in axes:ax.grid(alpha=.2)
fig.suptitle('Planar conductance model: illustrative sigmoid activation',fontsize=12);fig.savefig('2011-gating-phase-plane.png',dpi=140,facecolor='white');plt.close(fig)
