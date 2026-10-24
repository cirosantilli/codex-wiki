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
alpha=-.25;beta=.4;eps=.01
def piece(v):return -v if v<=alpha else (1-v if v>=beta else ((1-beta+alpha)*v-alpha)/(beta-alpha))
fun=lambda y:np.array([(piece(y[0])-y[1])/eps,y[0]])
t,o=rk4(fun,[.7,.3],25,.0005);vv=np.linspace(-.9,1.1,700)
fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
axes[0].plot(vv,[piece(x) for x in vv],color='#b24c2d',lw=2,label='w=g(v)');axes[0].axvline(0,color='#218151',ls='--',label='v=0');last=o[t>20];axes[0].plot(last[:,0],last[:,1],color='#216ba0',lw=1.3,label='Small-ε cycle');axes[0].set(xlabel='v',ylabel='w',xlim=(-.8,1),ylim=(.1,.75),title='Slow branches and fast horizontal jumps');axes[0].legend(fontsize=8)
mask=t>20;axes[1].plot(t[mask]-20,o[mask,0],label='v');axes[1].plot(t[mask]-20,o[mask,1],label='w');axes[1].set(xlabel='Time',ylabel='State',title='Relaxation waveform');axes[1].legend(fontsize=8)
for ax in axes:ax.grid(alpha=.2)
T=np.log((1+alpha)/beta)+np.log((1-beta)/(-alpha));fig.suptitle(f'Piecewise linear oscillator: α={alpha:g}, β={beta:g}, leading period {T:.3f}',fontsize=12);fig.savefig('2011-piecewise-relaxation.png',dpi=140,facecolor='white');plt.close(fig)
