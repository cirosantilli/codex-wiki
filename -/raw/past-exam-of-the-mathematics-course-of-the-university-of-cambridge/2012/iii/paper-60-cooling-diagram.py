"""Uniform self-gravitating gas-cloud sketch; no rate table is claimed.
Python 3.14 / root deps. Cwd PNG output; respect caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
G=6.67e-8;mp=1.673e-24;k=1.38e-16;X=.76;mu=1/(2*X+3*(1-X)/4);chi=1/(mu*X);fg=1.;msun=1.989e33
x=np.linspace(4,8,1000);T=10**x;xp=np.array([4,np.log10(15000),4.55,5,5.3,5.8,6.2,7,8]);yp=np.array([-23.5,-21.8,-22.5,-22.15,-22.6,-23.15,-23.25,-23,-22.5]);L=10**np.interp(x,xp,yp)
ncrit=32*G*mp/(3*np.pi*X*fg)*(1.5*chi*k*T/L)**2
fig,ax=plt.subplots(figsize=(11,6.8),dpi=100,facecolor='white')
ax.fill_between(x,np.log10(ncrit),2,color='#e0f3db',label='Cooling faster than free fall')
ax.fill_between(x,-10.5,np.log10(ncrit),color='#fff1df',label='Cooling slower than free fall')
ax.plot(x,np.log10(ncrit),color='#2166ac',lw=3,label=r'$t_{\rm cool}=t_{\rm ff}$')
for mass,col in [(1e8,'#542788'),(1e10,'#8073ac'),(1e12,'#b35806'),(1e14,'#636363')]:
 n=375*X*fg*k**3*T**3/(4*np.pi*G**3*mu**3*mp**4*(mass*msun)**2)
 ax.plot(x,np.log10(n),color=col,lw=1.2,ls='--',label=rf'$M=10^{{{int(np.log10(mass))}}}\,M_\odot$')
for z in [0,3,10]:
 n=18*np.pi**2*2e-7*(1+z)**3;ax.axhline(np.log10(n),color='#444',lw=1,ls=':');ax.text(7.95,np.log10(n)+.09,rf'$n_{{\rm vir}}(z={z})$',ha='right',fontsize=9)
ax.scatter([np.log10(15000),7],[np.log10(32*G*mp/(3*np.pi*X)*(1.5*chi*k*15000/10**-21.8)**2),np.log10(32*G*mp/(3*np.pi*X)*(1.5*chi*k*1e7/1e-23)**2)],color='black',s=24,zorder=5)
ax.set(xlim=(4,8),ylim=(-10.5,2),xlabel=r'$\log_{10}(T/{\rm K})$',ylabel=r'$\log_{10}(n_H/{\rm cm^{-3}})$',title='Cooling diagram: fixed composition and uniform self-gravitating gas')
ax.text(4.05,1.15,r'$X=0.76,\ \mu=0.59,\ f_g=1$; ionization factors held fixed',fontsize=9)
ax.legend(loc='lower right',fontsize=8.5,ncol=2,framealpha=1);ax.grid(alpha=.12);fig.tight_layout();fig.savefig('paper-60-cooling-diagram.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
