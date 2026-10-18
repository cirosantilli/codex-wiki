"""Original oscillator calculations. Python 3.14; NumPy 2.3; Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(2,2,figsize=(10,7.2),layout='constrained')
t=np.linspace(0,32,2401);g=.08;w=np.sqrt(1-g*g)
x=np.exp(-g*t)*(np.cos(w*t)+g/w*np.sin(w*t));v=-np.exp(-g*t)*np.sin(w*t)/w
ax[0,0].plot(t,x,label='underdamped, initial velocity zero');ax[0,0].plot(t,np.exp(-g*t),'--',color='.5',lw=1);ax[0,0].plot(t,-np.exp(-g*t),'--',color='.5',lw=1)
ax[0,0].set(xlabel=r'time $\omega_0t$',ylabel=r'$x/x_0$',title=r'Weak damping: $\gamma/\omega_0=0.08$');ax[0,0].legend(fontsize=9)
ax[0,1].plot(t,x*x+v*v,label='exact mechanical energy');ax[0,1].plot(t,np.exp(-2*g*t),'--',label='leading exponential')
ax[0,1].axhline(.5,color='.65',lw=1);ax[0,1].axvline(np.log(2)/(2*g),color='.65',lw=1,ls=':');ax[0,1].set(xlabel=r'time $\omega_0t$',ylabel=r'$E/E_0$',title='Energy half-life is approximate');ax[0,1].legend(fontsize=9)
for g in [.3,1,1.5]:
 if g<1:
  w=np.sqrt(1-g*g);y=np.exp(-g*t)*(np.cos(w*t)+g/w*np.sin(w*t))
 elif g==1:y=(1+t)*np.exp(-t)
 else:
  a=np.sqrt(g*g-1);r1=-g+a;r2=-g-a;y=(-r2*np.exp(r1*t)+r1*np.exp(r2*t))/(r1-r2)
 ax[1,0].plot(t,y,label=rf'$\gamma/\omega_0={g:g}$')
ax[1,0].set(xlim=(0,12),xlabel=r'time $\omega_0t$',ylabel=r'$x/x_0$',title='Transition through critical damping');ax[1,0].legend(fontsize=9)
tr=np.linspace(0,32,2401);xr=.5*tr*np.sin(tr)
ax[1,1].plot(tr,xr,lw=1.5,label='zero initial displacement and velocity');ax[1,1].plot(tr,.5*tr,'--',color='.5',lw=1);ax[1,1].plot(tr,-.5*tr,'--',color='.5',lw=1)
ax[1,1].set(xlabel=r'time $\omega_0t$',ylabel=r'$x/(F_0/m\omega_0^2)$',title='Undamped forcing at resonance');ax[1,1].legend(fontsize=8,loc='upper left')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
