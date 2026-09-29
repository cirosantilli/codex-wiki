from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(8,3.5));x=np.linspace(1.001,3,1000);y=x/np.sqrt(x*x-1)
ax.plot(-x,y,color='tab:blue');ax.plot(x,y,color='tab:blue',label='Ideal BCS, zero temperature');ax.plot([-1,1],[0,0],color='tab:blue',lw=2)
ax.axhline(1,color='gray',ls='--',label='Normal-state density of states')
for xx in [-1,1]:ax.axvline(xx,color='gray',ls=':',lw=.8)
ax.text(0,.25,'No ideal single-particle states',ha='center',fontsize=9)
ax.set(xlim=(-3,3),ylim=(-.05,3.7),xlabel=r'Energy $E/\Delta$',ylabel=r'$N_s(E)/N_n(0)$',title='Predicted tunnelling spectrum; this is not an experimental data plot');ax.legend(fontsize=8,loc='upper right')

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
