"""Original Einstein-de Sitter distances and complete counts. Python 3.14; numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(12,3.9),layout='constrained',facecolor='white')
z=np.linspace(0,12,900);u=1/np.sqrt(1+z);DM=2*(1-u);DA=DM/(1+z)
ax[0].plot(z,DM,label=r'$d_M$');ax[0].plot(z,DA,label=r'$d_A=d_M/(1+z)$');ax[0].scatter([1.25],[8/27],color='C1',s=20);ax[0].set(xlabel='Redshift z',ylabel=r'Distance / $(c/H_0)$',title='Two operational distances');ax[0].legend(fontsize=8)
counts=4*(1-u)**2/(1+z)**1.5;ax[1].plot(z,counts,color='#176a9a');zp=16/9;ax[1].scatter([zp],[.13824],color='#176a9a',s=20);ax[1].annotate(r'Peak at $z=16/9$',xy=(zp,.13824),xytext=(4.2,.115),arrowprops=dict(arrowstyle='->'),fontsize=9)
ax[1].set(xlabel='Redshift z',ylabel=r'$(dN/dz)/[n_0(c/H_0)^3]$',title='Differential count per solid angle')
zf=np.geomspace(.01,1000,700);frac=(1-1/np.sqrt(1+zf))**3;ax[2].semilogx(zf,frac,color='#b66c25');ax[2].axhline(1,color='.5',ls='--',lw=.8);ax[2].set(xlabel=r'Formation redshift $z_f$',ylabel=r'$N(<z_f)/N_\infty$',ylim=(0,1.05),title='Cumulative fraction of horizon count')
for a in ax:a.grid(alpha=.17)
fig.savefig('paper-1-eds-distance-counts.png',dpi=150,facecolor='white')
