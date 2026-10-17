import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,2,figsize=(9.6,6.4),layout='constrained')
x=np.linspace(-5,5,1000);t=np.linspace(0,8*np.pi,1600)
axes[0,0].plot(x,1/(np.pi*(1+x*x)),color='#2475aa',lw=2)
axes[0,0].set(xlabel=r'Detuning $(\omega-\omega_0)/\Gamma$',ylabel=r'$\Gamma S/\int S\,d\omega$',title=r'Lorentzian: half-width $\Gamma$')
axes[1,0].plot(t/np.pi,np.exp(-t/np.pi),color='#2475aa',lw=2)
axes[1,0].set(xlabel=r'Delay $\Gamma|\tau|$',ylabel=r'Visibility $|g^{(1)}|$',title='One line: exponential coherence envelope',xlim=(0,8),ylim=(0,1.05))
for f in [-.5,.5]:
 axes[0,1].annotate('',xy=(f,.5),xytext=(f,0),arrowprops=dict(arrowstyle='->',lw=2.5,color='#c94a39'))
 axes[0,1].text(f,.54,r'area $1/2$',ha='center',fontsize=10)
axes[0,1].set(xlim=(-1.2,1.2),ylim=(0,.68),yticks=[],xlabel=r'Detuning $(\omega-\bar\omega)/\Delta\omega_{12}$',title='Two ideal spectral lines: delta functions',ylabel='Normalized line weight')
axes[1,1].plot(t/(2*np.pi),abs(np.cos(t/2)),color='#c94a39',lw=2)
axes[1,1].set(xlabel=r'Delay $\Delta\omega_{12}\tau/(2\pi)$',ylabel=r'Visibility $|g^{(1)}|$',title='Two lines: cancellation and exact revivals',xlim=(0,4),ylim=(0,1.05))
for ax in axes.flat:ax.grid(alpha=.2)
fig.savefig('paper-1-oe2012-coherence-spectra.png',dpi=160,facecolor='white')
