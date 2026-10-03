"""Dimensionless conceptual curves, not observational fits. Python 3.14 / root deps.
Writes only PNG basename to cwd and respects caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q=np.logspace(-4,2,900);halo=q**(-.9)*np.exp(-q);gal=q**(-.25)*np.exp(-q)
M=np.logspace(8,15,900);r=M/1e12;eff=.4/(r**(-.8)+r**(.7))
fig,(a,b)=plt.subplots(1,2,figsize=(11,5.4),dpi=100,facecolor='white')
a.loglog(q,halo/halo[np.argmin(abs(q-1))],color='#636363',lw=2,label='Halo counts per log mass: schematic')
a.loglog(q,gal/gal[np.argmin(abs(q-1))],color='#2166ac',lw=2,label='Galaxy counts per log luminosity: schematic')
a.set(xlim=(1e-4,20),ylim=(1e-5,1e5),xlabel=r'$M/M_h^*$ or $L/L^*$',ylabel='Relative abundance per logarithmic interval',title='Faint-end flattening and bright-end cutoff');a.legend(fontsize=8.5,loc='lower left',framealpha=1);a.grid(alpha=.15)
b.semilogx(M,eff,color='#1b7837',lw=3);b.set(xlim=(1e8,1e15),ylim=(0,.25),xlabel=r'Halo mass $M_h/M_\odot$',ylabel=r'$\epsilon_*=M_*/(f_bM_h)$',title='Integrated baryon-to-star conversion: schematic')
b.text(1.4e8,.085,'Photoheating, winds,\nsupernova feedback',fontsize=9);b.text(2e12,.09,'Slow cooling, hot halo,\nAGN feedback',fontsize=9);b.axvline(1e12,color='#888',ls=':',lw=1);b.grid(alpha=.15)
fig.tight_layout();fig.savefig('paper-60-luminosity.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
