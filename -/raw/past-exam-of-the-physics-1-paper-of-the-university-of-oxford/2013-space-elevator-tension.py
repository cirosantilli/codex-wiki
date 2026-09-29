"""Original uniform-cable tension plot; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes the matching opaque PNG basename in the current working directory only.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
G=6.6743e-11
rho=5500
omega=2*np.pi/86164
eta=(4*np.pi*G*rho/(3*omega**2))**(1/3)
end=(np.sqrt(1+8*eta**3)-1)/2
x=np.linspace(1,end,700)
tension=eta**3*(1-1/x)-.5*(x*x-1)
peak=eta**3-1.5*eta**2+.5
fig,ax=plt.subplots(figsize=(6.8,3.8),layout='constrained',facecolor='white')
ax.plot(x,tension,color='#27678e',lw=2)
ax.axvline(eta,color='#b86422',ls='--',lw=1)
ax.plot([1,eta,end],[0,peak,0],'o',color='#b86422')
ax.annotate(f'Geostationary radius\n$\\eta={eta:.3f}$',xy=(eta,peak),xytext=(10.2,peak*.82),arrowprops=dict(arrowstyle='->'),ha='left')
ax.annotate(f'Free outer end\n$\\eta\\prime={end:.3f}$',xy=(end,0),xytext=(end-6,peak*.18),arrowprops=dict(arrowstyle='->'))
ax.set(xlabel=r'Radial position $r/R$',ylabel=r'Tension $T/(\lambda\omega^2R^2)$',xlim=(.5,end+1),ylim=(-peak*.03,peak*1.13))
ax.grid(alpha=.25)
fig.savefig('2013-space-elevator-tension.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
