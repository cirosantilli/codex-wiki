"""Original explanatory plot. Python 3.14, numpy, matplotlib.
Run from the destination directory; writes a PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');x=np.linspace(-4.5,6.5,3000)
for ax,eta in zip(axs,[.15,1.5]):
 exact=np.exp(-(x-np.sqrt(2)*eta)**2)/np.sqrt(np.pi);trunc=np.exp(-x*x)*(1+np.sqrt(2)*eta*x)**2/(np.sqrt(np.pi)*(1+eta*eta))
 ax.plot(x,exact,label='Exact translated ground state',lw=2,color='#1766a5');ax.plot(x,trunc,'--',label='Normalized two-state truncation',lw=1.8,color='#c33c29');ax.axvline(np.sqrt(2)*eta,color='gray',ls=':');ax.set(xlabel=r'$x\sqrt{m\omega/\hbar}$',ylabel='Probability density in scaled coordinate',title=fr'$\eta={eta}$, displacement $\sqrt{{2}}\eta$',xlim=(-3,6),ylim=(0,.72));ax.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-displaced-oscillator.png',dpi=170);plt.close(fig)
