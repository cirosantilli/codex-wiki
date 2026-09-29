"""Original educational diagram; Python 3.14, NumPy and Matplotlib. Saves a basename PNG to the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
t=np.linspace(.008,3,1800);x=1/t;n=1/np.expm1(x);U=.5+n;cv=x*x*np.exp(-x)/(1-np.exp(-x))**2
fig,axs=plt.subplots(1,2,figsize=(8.5,3.6),layout='constrained')
axs[0].plot(t,U,color='#225c91',label='Quantum oscillator');axs[0].plot(t,t,'--',color='#b25424',label=r'Classical $U=k_BT$');axs[0].scatter([0],[.5],color='#225c91');axs[0].annotate('Zero-point energy = 1/2',xy=(0,.5),xytext=(.45,1.45),arrowprops={'arrowstyle':'->','color':'#777'},fontsize=9)
axs[0].set(ylabel=r'$U/(\hbar\Omega)$',xlabel=r'$k_BT/(\hbar\Omega)$',xlim=(0,3),ylim=(0,3.2));axs[0].legend(fontsize=9)
axs[1].plot(t,cv,color='#225c91');axs[1].axhline(1,color='#b25424',ls='--');axs[1].text(1.8,1.035,r'$C_V\to k_B$',ha='center');axs[1].annotate('Excitations freeze out',xy=(.055,.02),xytext=(.65,.25),arrowprops={'arrowstyle':'->','color':'#777'},fontsize=9)
axs[1].set(ylabel=r'$C_V/k_B$',xlabel=r'$k_BT/(\hbar\Omega)$',xlim=(0,3),ylim=(0,1.12))
for ax in axs:ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2014-oscillator.png',dpi=150,facecolor='white');plt.close(fig)
