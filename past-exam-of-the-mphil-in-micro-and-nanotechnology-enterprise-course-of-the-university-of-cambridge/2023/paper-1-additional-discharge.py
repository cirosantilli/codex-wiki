"""Original illustrative discharge/loss model; Python 3.14, numpy, matplotlib.

No measured battery data. Save a literal PNG basename into the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fraction=np.linspace(0,1,600)
equilibrium=3.60-.20*fraction-.30*fraction**10
ohmic=np.full_like(fraction,.15)
activation=np.full_like(fraction,.12)
phase=.24*np.exp(-fraction/.025)
concentration=.02*fraction/(1.03-fraction)
loaded=equilibrium-ohmic-activation-phase-concentration
fig,axes=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
fig.patch.set_facecolor('white')
axes[0].plot(fraction,equilibrium,'--',color='#5c6b75',label='Equilibrium voltage')
axes[0].plot(fraction,loaded,color='#285f83',lw=2,label='Loaded terminal voltage')
axes[0].plot([0,0],[equilibrium[0],loaded[0]],':',color='#aa5b38',lw=1.7)
axes[0].set(xlabel='Discharged fraction (chosen scale)',ylabel='Voltage (illustrative V)',title='Initial transient, plateau and late decline')
axes[0].legend(fontsize=9,loc='lower left')
for values,label,color,style in [
    (ohmic,'Ohmic','#a0502a','-'),(activation,'Activation','#537b47','--'),
    (phase,'Phase / nucleation','#92569c','-'),(concentration,'Concentration','#2f7b91','-')]:
    axes[1].plot(fraction,values,label=label,color=color,ls=style,lw=1.8)
axes[1].set(xlabel='Discharged fraction (chosen scale)',ylabel='Voltage loss (illustrative V)',title='Distinct stipulated contributions')
axes[1].legend(loc='upper left',fontsize=9)
for ax in axes:
    ax.set_xlim(0,1)
    ax.grid(alpha=.18)
    ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-additional-discharge.png',dpi=160,facecolor='white')
plt.close(fig)
