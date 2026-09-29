"""Original exact oscillator calculation, including first velocity zero. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
eps=.08;wm=1.;wp=np.sqrt(1+2*eps);mean=(wm+wp)/2;delta=(wp-wm)/2
vel=lambda t:.5*(-wm*np.sin(wm*t)+wp*np.sin(wp*t))
lo=np.pi/(2*mean);hi=np.pi/mean
for _ in range(70):
 mid=(lo+hi)/2
 if vel(mid)>0:lo=mid
 else:hi=mid
turn=(lo+hi)/2;transfer=np.pi/(wp-wm)
fig,axs=plt.subplots(2,2,figsize=(10.5,7.4),layout='constrained');t=np.linspace(0,6,1201);x1=.5*(np.cos(wm*t)+np.cos(wp*t));x2=.5*(np.cos(wm*t)-np.cos(wp*t))
axs[0,0].plot(t,x1,label=r'$x_1/d$');axs[0,0].plot(t,x2,label=r'$x_2/d$');axs[0,0].axvline(turn,color='.5',ls=':');axs[0,0].set(xlabel=r'time $\omega_- t$',ylabel='displacement / d',title='Early displacement');axs[0,0].legend(fontsize=9)
axs[0,1].plot(t,vel(t),color='tab:orange',label=r'$\dot x_2/(d\omega_-)$');axs[0,1].plot(turn,0,'o',color='black');axs[0,1].axhline(0,color='.6',lw=.8);axs[0,1].annotate(f'first stop: t = {turn:.3f}',xy=(turn,0),xytext=(2.7,.075),arrowprops={'arrowstyle':'->'},fontsize=9);axs[0,1].set(xlabel=r'time $\omega_- t$',ylabel='second velocity',title='The first stop is on a fast timescale');axs[0,1].legend(fontsize=9,loc='lower left')
t=np.linspace(0,2.1*transfer,8001)
for ax,signal,env,name in [(axs[1,0],.5*(np.cos(wm*t)+np.cos(wp*t)),np.abs(np.cos(delta*t)),r'$x_1/d$'),(axs[1,1],.5*(np.cos(wm*t)-np.cos(wp*t)),np.abs(np.sin(delta*t)),r'$x_2/d$')]:
 ax.plot(t,signal,lw=.8,label=name);ax.plot(t,env,'--',color='black',lw=1,label='slow envelope');ax.plot(t,-env,'--',color='black',lw=1);ax.axvline(transfer,color='tab:red',ls=':',label='first envelope transfer');ax.set(xlabel=r'time $\omega_- t$',ylabel='displacement / d',title='Weak-coupling beats');ax.legend(fontsize=8,loc='upper right')
fig.suptitle(r'Symmetric coupled oscillators: $k^\prime/k=0.08$',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
