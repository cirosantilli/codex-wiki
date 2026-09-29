"""Original educational diagram; Python 3.14, NumPy and Matplotlib. Saves a basename PNG to the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
m=np.linspace(-1.35,1.35,1201);fig,axs=plt.subplots(1,2,figsize=(8.5,3.7),layout='constrained');colors=['#225c91','#b25424','#388773']
for r,col in zip([.4,0,-.4],colors):axs[0].plot(m,r*m*m/2+m**4/4,color=col,label=f'r = {r:g}')
for r,col in zip([.28,3/16,.08],colors):axs[1].plot(m,r*m*m/2-m**4/4+m**6/6,color=col,label=f'r = {r:g}')
axs[0].set(title='Second order: positive quartic term',ylim=(-.08,.35));axs[1].set(title='First order: stable sextic potential',ylim=(-.065,.16))
axs[1].scatter([0,-np.sqrt(.75),np.sqrt(.75)],[0,0,0],color='#b25424',s=18,zorder=4);axs[1].text(0,.06,r'At $r_t=3/16$, three equal-depth minima',ha='center',fontsize=9)
for ax in axs:ax.axhline(0,color='#777',lw=.7);ax.set(xlabel='Order parameter m',ylabel='Reduced free energy');ax.legend(fontsize=9,loc='upper center');ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2014-landau.png',dpi=150,facecolor='white');plt.close(fig)
