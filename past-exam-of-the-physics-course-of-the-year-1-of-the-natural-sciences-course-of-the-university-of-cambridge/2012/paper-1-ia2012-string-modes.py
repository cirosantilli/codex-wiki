import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1,1200);s1=np.sin(np.pi*x);s2=np.sin(2*np.pi*x)
fig,axes=plt.subplots(1,3,figsize=(11.5,3.6),sharey=True,layout='constrained')
axes[0].plot(x,s1+s2,color='#2475aa',lw=2);axes[0].scatter([2/3],[0],color='#2475aa',s=22)
axes[0].set_title(r'$t=0$: both cosine factors are 1')
axes[1].plot(x,-s2,color='#2475aa',lw=2);axes[1].set_title(r'$t_1=\pi/(2\omega_1^{(0)})$: ideal string')
eta=.04;c1=np.cos(np.pi/2*np.sqrt(1+eta));c2=np.cos(np.pi*np.sqrt(1+4*eta))
axes[2].plot(x,-s2,color='#777',ls='--',label='ideal')
axes[2].plot(x,c1*s1+c2*s2,color='#c94a39',lw=2,label=rf'$\eta={eta:g}$')
axes[2].set_title('Same original time, weak stiffness');axes[2].legend(frameon=False)
for ax in axes:
 ax.axhline(0,color='#888',lw=.7);ax.grid(alpha=.2);ax.set(xlabel=r'$x/L$',xlim=(0,1),ylim=(-1.4,1.9),xticks=[0,.5,1]);ax.scatter([0,1],[0,0],color='black',s=20,zorder=5)
axes[0].set_ylabel(r'Displacement $y/A$')
fig.savefig('paper-1-ia2012-string-modes.png',dpi=160,facecolor='white')
