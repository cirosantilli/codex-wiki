"""Original rotor probability revival; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
phi=np.linspace(0,2*np.pi,601);times=np.linspace(0,1,401)
rho=lambda phi,t:(1+np.cos(2*phi)**2+2*np.cos(2*phi)*np.cos(2*np.pi*t))/(3*np.pi)
fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
im=axes[0].pcolormesh(phi/np.pi,times,rho(phi[None,:],times[:,None]),shading='auto',cmap='viridis',vmin=0,vmax=4/(3*np.pi))
axes[0].set(xlabel=r'Angle $\phi/\pi$',ylabel=r'Time $t/T$',title=r'Density over one revival, $T=\pi I/\hbar$')
fig.colorbar(im,ax=axes[0],label=r'$|\psi|^2$')
for t,ls in [(0,'-'),(.125,'--'),(.25,':'),(.5,'-.')]:axes[1].plot(phi/np.pi,rho(phi,t),lw=2,ls=ls,label=f't/T = {t:g}')
axes[1].set(xlabel=r'Angle $\phi/\pi$',ylabel=r'$|\psi|^2$',title='Profiles change shape and return at t/T = 1',xlim=(0,2),ylim=(-.01,.62))
axes[1].legend(loc='upper center',fontsize=8,ncol=2);axes[1].grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
