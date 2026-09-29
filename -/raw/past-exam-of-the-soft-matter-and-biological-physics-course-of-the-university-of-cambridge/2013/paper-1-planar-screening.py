"""Original exact planar PB profiles; illustrative dimensionless surface potentials."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained');z=np.linspace(0,5,500)
for u0,col in [(2,'#2166ac'),(6,'#b2182b')]:
 exact=4*np.arctanh(np.tanh(u0/4)*np.exp(-z));axs[0].plot(z,exact,color=col,lw=2,label=rf'Nonlinear, $u_0={u0}$');axs[0].plot(z,u0*np.exp(-z),color=col,ls='--',lw=1.4,label=rf'Linear, $u_0={u0}$')
axs[0].set(xlabel=r'$\kappa_Dz$',ylabel=r'$u=e\psi/(k_BT)$',title='Planar surface screening');axs[0].legend(fontsize=8);axs[0].grid(alpha=.2)
u=np.linspace(-6,6,500);axs[1].plot(u,np.cosh(u/2),lw=2);axs[1].axhline(1,color='grey',ls=':',label='Linear limit');axs[1].set(xlabel=r'$u_0=e\psi_0/(k_BT)$',ylabel=r'$C_D/(\varepsilon\kappa_D)$',title='Diffuse-layer capacitance');axs[1].legend();axs[1].grid(alpha=.2)
fig.savefig('paper-1-planar-screening.png',dpi=170,facecolor='white');plt.close(fig)
