"""Original analytic harmonic-oscillator normalized wavefunctions."""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,1001)
psi0 = np.pi**(-.25)*np.exp(-x*x/2)
psi1 = np.sqrt(2)*x*psi0
fig, axes = plt.subplots(1,2,figsize=(10,4.2),facecolor='white',layout='constrained')
for ax in axes:
    ax.axhline(0,color='.65',lw=.8); ax.set(xlim=(-4,4),xlabel=r'$x/\ell$')
axes[0].plot(x,psi0,label=r'$\sqrt{\ell}\,\psi_0$',lw=2,color='#235d87')
axes[0].plot(x,psi1,label=r'$\sqrt{\ell}\,\psi_1$',lw=2,color='#bd671b')
axes[0].set(title='Even ground state; odd first excited state',ylabel='Scaled wavefunction'); axes[0].legend()
axes[1].plot(x,psi0**2,label=r'$\ell\,|\psi_0|^2$',lw=2,color='#235d87')
axes[1].plot(x,psi1**2,label=r'$\ell\,|\psi_1|^2$',lw=2,color='#bd671b')
axes[1].set(title='Both probability densities integrate to 1',ylabel='Scaled probability density'); axes[1].legend()
fig.savefig('paper-1-gp2012-oscillator.png',dpi=165,facecolor='white')
plt.close(fig)
