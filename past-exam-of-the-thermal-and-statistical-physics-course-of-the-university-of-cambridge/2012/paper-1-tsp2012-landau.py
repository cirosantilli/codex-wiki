import numpy as np
import matplotlib.pyplot as plt
eta=np.linspace(-1.7,1.7,800);t=np.linspace(-1,1,500)
fig,axes=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
for tau,col in [(.6,'#c94a39'),(0,'#888'),(-.6,'#2475aa')]:
 axes[0].plot(eta,.5*tau*eta**2+.25*eta**4,color=col,label=rf'$a(T-T_c)={tau:g}$')
 if tau<0:
  eq=np.sqrt(-tau);axes[0].scatter([-eq,eq],[-tau*tau/4]*2,color=col,zorder=5)
axes[0].set(xlabel=r'Order parameter $\eta$',ylabel=r'$f-f_0$ (normalized)',ylim=(-.14,1.3),title='Quartic minima at zero conjugate field');axes[0].legend(frameon=False,fontsize=9)
y=np.sqrt(np.maximum(-t,0));axes[1].plot(t,y,color='#2475aa',lw=2);axes[1].plot(t,-y,color='#2475aa',lw=2)
axes[1].axvline(0,color='#888',ls=':');axes[1].set(xlabel=r'$a(T-T_c)$, with $b=1$',ylabel=r'Equilibrium $\eta$',title='Two stable ordered branches')
for ax in axes:ax.grid(alpha=.2)
fig.savefig('paper-1-tsp2012-landau.png',dpi=150,facecolor='white')
