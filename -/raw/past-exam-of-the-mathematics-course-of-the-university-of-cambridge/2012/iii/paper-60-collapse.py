"""Python 3.14; numpy 2.3.5, matplotlib 3.10.7. Writes only the PNG basename to cwd.
The caller supplies MPLCONFIGDIR; no environment variable is changed here.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
th=np.linspace(0,2*np.pi,1200);t=(th-np.sin(th))/np.pi;r=(1-np.cos(th))/2
fig,ax=plt.subplots(figsize=(10,5),dpi=100,facecolor='white')
ax.plot(t,r,'--',color='#8b929a',lw=2,label='Ideal pressureless top-hat (formal collapse)')
mask=th<=1.5*np.pi
ax.plot(t[mask],r[mask],color='#2166ac',lw=3,label='Expansion and infall before relaxation')
ax.plot([t[mask][-1],2.45],[.5,.5],color='#2166ac',lw=3,label='Schematic virialized size')
ax.scatter([1,2],[1,0],s=40,color=['#2166ac','#8b929a'])
ax.axhline(.5,color='#b35806',ls=':',lw=1.5);ax.axvline(1,color='#aaa',ls=':',lw=1);ax.axvline(2,color='#aaa',ls=':',lw=1)
ax.annotate('Turnaround',xy=(1,1),xytext=(1.18,1.1),arrowprops={'arrowstyle':'->'})
ax.text(2.02,.55,r'$R_{\rm vir}=R_{\rm ta}/2$',color='#2166ac');ax.text(1.92,.09,'Formal collapse',ha='right',color='#65696e')
ax.set(xlim=(0,2.45),ylim=(0,1.23),xlabel=r'$t/t_{\rm ta}$',ylabel=r'$R/R_{\rm ta}$',title='Spherical collapse and energy-conserving virialization')
ax.legend(loc='lower left',fontsize=9,framealpha=1);ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-60-collapse.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
