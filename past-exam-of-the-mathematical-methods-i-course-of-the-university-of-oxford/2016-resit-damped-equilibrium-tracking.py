"""Underdamped free motion and exact tracking of a moving equilibrium."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

w=4.;gam=.5;wd=np.sqrt(w*w-gam*gam/4);t=np.linspace(0,14,1800)
fig,axes=plt.subplots(1,3,figsize=(12,4.6),layout='constrained')
q=np.exp(-gam*t/2)*(np.cos(wd*t)+gam/(2*wd)*np.sin(wd*t));axes[0].plot(t,q,color='#176ca6',lw=1.6)
envelope=np.sqrt(1+(gam/(2*wd))**2)*np.exp(-gam*t/2)
axes[0].plot(t,envelope,'--',color='.5',lw=1);axes[0].plot(t,-envelope,'--',color='.5',lw=1);axes[0].set(title='Free motion: decaying oscillations',ylabel='Displacement from fixed equilibrium')
for ax,alpha in [(axes[1],gam),(axes[2],1.5)]:
 equilibrium=np.exp(-alpha*t);F=w*w/(alpha*alpha-gam*alpha+w*w);x=F*equilibrium+(1-F)*np.exp(-gam*t/2)*(np.cos(wd*t)+(gam/2-alpha)/wd*np.sin(wd*t));ax.plot(t,x,color='#176ca6',lw=2,label='body x(t)');ax.plot(t,equilibrium,ls='--',color='#c56e22',lw=1.5,label='moving equilibrium');ax.set(ylabel='Position / d');ax.legend(fontsize=8)
axes[1].set_title(r'Exact tracking: $\alpha=\gamma$');axes[2].set_title(r'Extra transient: $\alpha=1.5$')
for ax in axes:ax.set(xlabel='Time',xlim=(0,14));ax.axhline(0,color='.5',lw=.6);ax.grid(alpha=.15)
fig.suptitle(r'$\omega_0=4,\quad\gamma=0.5$',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
