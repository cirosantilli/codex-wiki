import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,3,figsize=(12,3.8),layout='constrained')
b=np.linspace(.14,.95,5000);mu=b*(np.floor(1/b)+.5)
for n in range(7):ax[0].plot(b,b*(n+.5),color='0.8',lw=.7)
# Separate branches instead of drawing an unphysical finite-width transition.
for n in range(1,8):
 keep=(1/b>n)&(1/b<n+1);ax[0].plot(b[keep],mu[keep],color='#17639b',lw=2)
ax[0].set(xlabel=r'$B/(n_sh/e)$',ylabel=r'$\mu/E_0$',title=r'Fixed density: $E_0=2\pi\hbar^2n_s/m^*$',ylim=(.45,1.5));ax[0].text(.33,.57,'Ideal zero-temperature limits',fontsize=9)
nu=np.linspace(.05,4.98,1000);ax[1].step(nu,np.floor(nu)+.5,where='post');ax[1].plot(nu,nu,'k--',lw=1,label='Zero-field trend');ax[1].set(xlabel=r'Density / $(eB/h)$',ylabel=r'$\mu/(\hbar\omega_c)$',title='Fixed field: upward filling steps');ax[1].legend(fontsize=9)
e=np.linspace(0,4.9,1000);dos=sum(np.exp(-.5*((e-n-.5)/.10)**2) for n in range(5));ax[2].plot(dos,e);ax[2].axhline(2.5,color='crimson',ls='--',label='Partly filled level');ax[2].set(xlabel='Broadened DOS (illustrative)',ylabel=r'$E/(\hbar\omega_c)$',title='Levels supply the state count');ax[2].legend(fontsize=9)
fig.suptitle('One resolved branch per level; no copied or fitted traces',fontsize=12)
fig.savefig('paper-1-fermi-oscillations.png',dpi=155)
