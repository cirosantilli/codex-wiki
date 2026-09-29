"""Original dimensionless Maxwell response; output to current working directory."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained')
t=np.linspace(0,5,400);x=np.logspace(-2,2,500)
axs[0].plot(t,np.exp(-t),lw=2);axs[0].set(xlabel=r'$t/\tau_M$',ylabel=r'$G(t)/G_0$',title='Stress relaxation',ylim=(0,1.05));axs[0].grid(alpha=.2)
axs[1].loglog(x,x*x/(1+x*x),label=r"$G'/G_0$",lw=2);axs[1].loglog(x,x/(1+x*x),label=r"$G''/G_0$",lw=2);axs[1].axvline(1,color='grey',ls=':',lw=1);axs[1].set(xlabel=r'$\omega\tau_M$',ylabel='Normalized modulus',title='Oscillatory response');axs[1].legend();axs[1].grid(alpha=.2)
fig.savefig('paper-1-viscoelastic-response.png',dpi=170,facecolor='white');plt.close(fig)
