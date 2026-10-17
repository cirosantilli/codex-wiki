"""Original analytic disk stability and two-fluid curves; Python3.14,NumPy,Matplotlib; output cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4.1),facecolor='white',layout='constrained')
k=np.linspace(0,4,500)
for Q,col in [(.7,'#b3542c'),(1,'#28694b'),(1.5,'#2567a5')]:
 axs[0].plot(k,1+k*k-2*k/Q,label=f'Q = {Q:g}',color=col)
axs[0].axhline(0,color='.3',lw=.9);axs[0].set(xlabel=r'$|k|c_s/\kappa$',ylabel=r'$\omega^2/\kappa^2$',title='Local axisymmetric gas-disk stability',ylim=(-1.5,6))
axs[0].text(.06,.08,'Negative squared frequency: exponential instability',transform=axs[0].transAxes,fontsize=8)
axs[0].legend(fontsize=9);axs[0].grid(alpha=.2)
x=np.geomspace(1,1501,500)
axs[1].plot(x,1-1/x,label='Constant relative offset; matched initial growth velocities',color='#2567a5')
axs[1].plot(x,1-3/x+2/x**1.5,label='Zero initial baryon density and growth velocity',color='#b3542c',ls='--')
axs[1].axhline(1,color='.4',ls=':',lw=.9);axs[1].set_xscale('log')
axs[1].set(xlabel=r'Scale-factor ratio $x=R/R(z_0)$',ylabel=r'$\Delta_B/\Delta_D$',title='Two distinct baryon catch-up transients',ylim=(-.03,1.04))
axs[1].legend(fontsize=8,loc='lower right');axs[1].grid(alpha=.2)
fig.savefig('paper-1-disk-stability-baryon-catchup.png',dpi=150,facecolor='white');plt.close(fig)
