"""Original explanatory figure. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

kb=1.380649e-23;hbar=1.054571817e-34;me=9.1093837139e-31
n=4/(.36e-9)**3;TF=hbar*hbar*(3*np.pi**2*n)**(2/3)/(2*me*kb);theta=hbar*2700*(6*np.pi**2*n)**(1/3)/kb
nodes,weights=np.polynomial.legendre.leggauss(180)
def debye_heat_capacity(T):
    limit=np.minimum(theta/np.asarray(T),80.)
    x=(nodes[:,None]+1)*limit[None,:]/2
    integrand=x**4*np.exp(-x)/np.expm1(-x)**2
    integral=np.sum(weights[:,None]*integrand,axis=0)*limit/2
    return 9*(np.asarray(T)/theta)**3*integral
T=np.geomspace(.1,1200,650);ce=np.pi**2/2*T/TF;ph=debye_heat_capacity(T)
crossover=np.sqrt(5*theta**3/(24*np.pi**2*TF))
fig,axs=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
axs[0].loglog(T,ce,color='#126782',lw=2.4,label='Electrons')
axs[0].loglog(T,ph,color='#a44418',lw=2.4,label='Phonons: full Debye integral')
axs[0].axvline(crossover,color='#777777',ls='--',lw=1);axs[0].axhline(3,color='#777777',ls=':',lw=1)
axs[0].annotate('Crossover: 3.38 K',xy=(crossover,np.pi**2/2*crossover/TF),xytext=(.15,.025),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=11)
axs[0].set(xlabel='Temperature (K)',ylabel=r'$C/(n k_B)$',title='Each heat capacity uses its valid model')
axs[0].legend(fontsize=10,loc='lower right');axs[0].grid(alpha=.22,which='both')
axs[1].loglog(T,ce/ph,color='#126782',lw=2.4)
axs[1].axhline(1,color='#777777',ls='--',lw=1);axs[1].plot(300,.0064249863,'o',color='#a44418')
axs[1].annotate('300 K: ratio 0.0064',xy=(300,.0064249863),xytext=(8,.07),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=11)
axs[1].set(xlabel='Temperature (K)',ylabel=r'$C_e/C_{\rm ph}$',title='Electron domination is confined to low T');axs[1].grid(alpha=.22,which='both')
fig.suptitle(r'Copper model: $T_F=8.23\times10^4$ K, $\theta_D=354$ K',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
