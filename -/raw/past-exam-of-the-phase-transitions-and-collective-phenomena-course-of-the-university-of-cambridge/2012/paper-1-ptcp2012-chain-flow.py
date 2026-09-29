"""Original exact chain recursion, iterations, and correlation length."""
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.4),facecolor='white',layout='constrained')
v=np.linspace(0,1,601);axes[0].plot(v,v*v,lw=2,color='#235f8a',label=r"$v'=v^2$")
axes[0].plot(v,v,ls='--',color='.5',label=r"$v'=v$")
x=.93
for i in range(6):
    y=x*x
    axes[0].plot([x,x,y],[x,y,y],color='#b65e1c',lw=1.2)
    x=y
axes[0].scatter([0,1],[0,1],color=['#235f8a','#b65e1c'],s=40,zorder=4)
axes[0].set(xlabel=r'$v=\tanh K$',ylabel=r"$v'$",xlim=(-.02,1.02),ylim=(-.02,1.02),title='Finite-temperature couplings flow to zero');axes[0].legend(loc='upper left')
K=np.linspace(.05,5,901);length=-1/np.log(np.tanh(K))
axes[1].semilogy(K,length,lw=2,color='#235f8a',label=r'Exact $-1/\log\tanh K$')
axes[1].semilogy(K,np.exp(2*K)/2,lw=1.5,ls='--',color='#b65e1c',label=r'Low-T $e^{2K}/2$')
axes[1].set(xlabel=r'$K=J/(k_B T)$',ylabel=r'$\xi/a$',title='Divergence only as temperature tends to zero');axes[1].legend();axes[1].grid(alpha=.15)
fig.savefig('paper-1-ptcp2012-chain-flow.png',dpi=165,facecolor='white')
plt.close(fig)
