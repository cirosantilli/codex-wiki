"""Original normalized charge-model comparison; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
r=np.linspace(0,2.4,800);sigma=1/np.sqrt(5)
rho_s=np.where(r<1,3/(4*np.pi),0)
rho_g=np.exp(-r*r/(2*sigma*sigma))/(2*np.pi*sigma*sigma)**1.5
q=np.linspace(.001,10,3000)
F=3*(np.sin(q)-q*np.cos(q))/q**3
G=np.exp(-q*q/10)
fig,axes=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
axes[0].plot(r,rho_s,label='Uniform sharp sphere',color='#2158a0')
axes[0].plot(r,rho_g,label='Gaussian, same rms radius',color='#b24b18')
axes[0].set(xlabel=r'$r/R$',ylabel=r'$\rho_{ch} R^3/(Ze)$',title='Different charge profiles');axes[0].legend(fontsize=8)
axes[1].semilogy(q,F*F,color='#2158a0',label='Sphere')
axes[1].semilogy(q,G*G,color='#b24b18',label='Gaussian')
axes[1].axvline(4.49340946,color='.6',ls='--',lw=.8)
axes[1].set(xlabel=r'$qR$ (q is momentum transfer/$\hbar$)',ylabel=r'$|F(q)|^2$',ylim=(1e-5,1.2),title='Only the sharp sphere has these zeros')
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-charge-form-factor.png',dpi=155,facecolor='white')
