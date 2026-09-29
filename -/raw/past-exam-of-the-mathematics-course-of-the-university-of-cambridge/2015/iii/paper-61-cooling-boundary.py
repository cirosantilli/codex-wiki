"""Cooling/free-fall sketch; emit an opaque PNG basename in caller cwd only."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
xt=np.array([4.0,np.log10(15000),4.35,4.65,4.85,5.0,5.2,5.5,5.9,6.2,6.6,7.0,7.5,8.0])
yt=np.array([-23.8,-21.8,-22.0,-22.7,-22.4,-22.15,-22.55,-23.1,-23.5,-23.4,-23.2,-23.0,-22.75,-22.5])
T=np.geomspace(1e4,1e8,800);lam=10**np.interp(np.log10(T),xt,yt)
G=6.67e-8;mp=1.67e-24;k=1.38e-16;X=.76;chi=2+3*(1-X)/(4*X);mu=1/(X*chi);msun=1.989e33
nc=32*G*mp/(3*np.pi*X)*(1.5*chi*k*T/lam)**2
fig,ax=plt.subplots(figsize=(9,4.8),dpi=100,facecolor='white');ax.set_facecolor('white')
ax.fill_between(T,nc,1e4,color='#dce9f8',alpha=.85)
ax.loglog(T,nc,color='#254c83',lw=2.5,label=r'$t_{\rm cool}=t_{\rm ff}$')
for mass,col in [(1e10,'#5c9263'),(1e12,'#aa4936'),(1e14,'#8c709f')]:
 n=3*X/(4*np.pi*mp*(mass*msun)**2)*(5*k*T/(G*mu*mp))**3
 ax.loglog(T,n,color=col,ls='--',lw=1.4,label=rf'Uniform-sphere $M=10^{{{int(np.log10(mass))}}}M_\odot$')
ax.axhline(2e-7,color='#777',ls=':',lw=1.4)
ax.text(1.4e6,3.2e-7,r'Present mean $n_{H,0}=2\times10^{-7}\,\mathrm{cm^{-3}}$',fontsize=9,color='#555')
ax.text(1.8e4,30,r'$t_{\rm cool}<t_{\rm ff}$: rapid cooling',fontsize=11,color='#254c83')
ax.text(1.8e5,2e-10,r'$t_{\rm cool}>t_{\rm ff}$: slower cooling',fontsize=10,color='#555')
ax.set_xlim(1e4,1e8);ax.set_ylim(1e-11,1e4);ax.set_xlabel(r'Virial temperature $T$ (K)',fontsize=12);ax.set_ylabel(r'Hydrogen density $n_H$ ($\mathrm{cm^{-3}}$)',fontsize=12)
ax.set_title('Primordial gas: cooling versus uniform-sphere free fall',fontsize=14)
ax.legend(loc='upper right',fontsize=8);ax.grid(which='major',alpha=.17)
fig.text(.5,.025,r'Schematic curve; self-gravitating gas, $X=0.76$, fixed ionized particle ratio. Virial coefficient: 5.',ha='center',fontsize=9,color='#444')
fig.subplots_adjust(left=.09,right=.98,bottom=.16,top=.9)
fig.savefig('paper-61-cooling-boundary.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
