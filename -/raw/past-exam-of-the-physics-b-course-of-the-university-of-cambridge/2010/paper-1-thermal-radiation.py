import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');tau=np.linspace(.02,3,700);u=1/np.expm1(1/tau);ax[0].plot(tau,u,label='Zero-point-subtracted oscillator');ax[0].plot(tau,tau,'k--',label='Classical high-T limit');ax[0].set(xlabel=r'$k_BT/(\hbar\omega)$',ylabel=r'$U/(\hbar\omega)$',title='Thermal excitation freezes out');ax[0].legend(fontsize=8)
x=np.linspace(.001,12,1200)
for t in [.7,1.,1.4]:ax[1].plot(x,x**3/np.expm1(x/t),label=fr'$T/T_{{ref}}={t}$')
ax[1].set(xlabel=r'$\hbar\omega/(k_BT_{ref})$',ylabel='Scaled energy per angular frequency',title='Planck volume-energy spectra');ax[1].legend(fontsize=9)
fig.suptitle('Original thermal models, not spectral radiance or measured radiation data',fontsize=11)
fig.savefig('paper-1-thermal-radiation.png',dpi=155)
