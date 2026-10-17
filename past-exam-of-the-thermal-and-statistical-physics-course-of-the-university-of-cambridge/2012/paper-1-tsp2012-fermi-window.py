import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(.001,14,1000);RT=X/np.sinh(X);ratio=6*(1-RT)/X**2
fig,axes=plt.subplots(1,2,figsize=(9.3,3.8),layout='constrained')
axes[0].plot(X,RT,color='#2475aa',lw=2.4);axes[0].set(ylabel=r'Full-potential damping $X/\sinh X$',title='Oscillatory grand potential')
axes[1].plot(X,ratio,color='#c94a39',lw=2.4,label='Exact ratio envelope')
mask=X>=3;axes[1].plot(X[mask],6/X[mask]**2,color='#888',ls='--',label=r'Asymptote $6/X^2$')
axes[1].set(ylabel=r'Thermal-change ratio $\mathcal{R}/|\alpha|$',title=r'Oscillation amplitude in $\Phi(T)-\Phi(0)$');axes[1].legend(frameon=False,fontsize=9)
for ax in axes:ax.set(xlabel=r'$X=2\pi^2k_BT/\Delta$',xlim=(0,14),ylim=(0,1.04));ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2012-fermi-window.png',dpi=150,facecolor='white')
