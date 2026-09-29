"""Original schematic, not a fitted atomic-rate table. Python 3.14 / root deps.
Writes PNG basename to cwd and leaves caller MPLCONFIGDIR unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(4,8,900);xp=np.array([4,np.log10(15000),4.55,5,5.3,5.8,6.2,7,8]);yp=np.array([-23.5,-21.8,-22.5,-22.15,-22.6,-23.15,-23.25,-23,-22.5]);y=np.interp(x,xp,yp)
metals=y+.85*np.exp(-((x-5.65)/.8)**2);photo=y-1.4*np.exp(-((x-4.5)/.5)**2)-.35*np.exp(-((x-5.1)/.45)**2)
fig,ax=plt.subplots(figsize=(10,5.8),dpi=100,facecolor='white')
ax.plot(x,y,color='#2166ac',lw=2.8,label='Primordial H/He: schematic collisional equilibrium')
ax.plot(x,metals,color='#1b7837',ls='--',lw=2,label='Illustrative metal enrichment')
ax.plot(x,photo,color='#b35806',ls=':',lw=2.4,label='Illustrative photoionization suppression (not net cooling)')
ax.scatter([np.log10(15000),7],[-21.8,-23],color='black',s=25,zorder=5,label='Two normalization anchors supplied in the paper')
ax.annotate('H bound-state losses',xy=(4.18,-21.8),xytext=(4.03,-21.15),arrowprops={'arrowstyle':'->'})
ax.annotate('He excitation / ionization',xy=(5,-22.15),xytext=(4.85,-21.35),arrowprops={'arrowstyle':'->'})
ax.annotate('Highly ionized gas\nloses line coolants',xy=(6.1,-23.22),xytext=(5.85,-24.05),arrowprops={'arrowstyle':'->'})
ax.text(7.13,-22.75,r'Free-free: $\Lambda\propto T^{1/2}$',rotation=16,color='#2166ac')
ax.set(xlim=(4,8),ylim=(-25,-20.8),xlabel=r'$\log_{10}(T/{\rm K})$',ylabel=r'$\log_{10}[\Lambda/({\rm erg\,cm^3\,s^{-1}})]$',title='Primordial cooling features and qualitative composition / radiation effects')
ax.legend(loc='lower right',fontsize=8.7,framealpha=1);ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-60-cooling.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
