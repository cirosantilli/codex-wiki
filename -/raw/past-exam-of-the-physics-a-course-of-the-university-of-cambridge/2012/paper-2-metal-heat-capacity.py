"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
xg,wg=np.polynomial.legendre.leggauss(100)
def phonon(t):
 upper=np.minimum(1/t,100);x=(xg[:,None]+1)*upper[None,:]/2;val=x**4*np.exp(-x)/(1-np.exp(-x))**2;return 3*t**3*(wg[:,None]*val).sum(axis=0)*upper/2
fig,axs=plt.subplots(1,2,figsize=(10,4),facecolor='white',layout='constrained')
for ax,t in [(axs[0],np.geomspace(1e-4,1,700)),(axs[1],np.linspace(.002,3,700))]:
 cp=phonon(t);ce=.015*t;ax.plot(t,cp+ce,color='#286747',label='Total');ax.plot(t,cp,color='#296c9e',ls='--',label='Debye lattice');ax.plot(t,ce,color='#ad5932',ls=':',label='Sommerfeld electrons');ax.set(xlabel=r'$T/\Theta_D$',ylabel=r'$C/(3Nk_B)$');ax.grid(alpha=.2)
axs[0].set_xscale('log');axs[0].set_yscale('log');axs[0].set(title='Low temperature: linear plus cubic terms',ylim=(1e-7,2));axs[0].legend(fontsize=9)
axs[1].axhline(1,color='.5',ls=':',lw=.8);axs[1].set(title='Lattice approaches its classical limit');axs[1].text(.03,.12,r'Illustration: $\gamma\Theta_D/(3Nk_B)=0.015$'+'\nNot a fitted magnesium curve',transform=axs[1].transAxes,fontsize=9)
fig.savefig('paper-2-metal-heat-capacity.png',dpi=150,facecolor='white');plt.close(fig)
