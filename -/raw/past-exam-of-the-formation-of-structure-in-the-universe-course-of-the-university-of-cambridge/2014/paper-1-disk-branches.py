"""Original marginal-fluid branches and supplied flat-disk Q. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(10.2,4.3),layout='constrained',facecolor='white')
for lo,hi,col,label in [(0,1,'#186b9c','Long-wave branch'),(1,4,'#ca692b','Short-wave branch')]:
 x=np.linspace(lo,hi,200);ax[0].plot(x,x-1,color=col,lw=2,label=label);ax[0].plot(x,1-x,color=col,lw=2)
for s in [-1,1]:ax[0].axhline(s,color='.5',ls='--',lw=.8)
ax[0].scatter([3],[2],color='black',s=22);ax[0].annotate('Valid short wave\noutside resonance interval',xy=(3,2),xytext=(1.45,2.65),arrowprops=dict(arrowstyle='->'),fontsize=8)
ax[0].set(xlim=(0,4),ylim=(-3.3,3.3),xlabel=r'$a_0|k|/\kappa$',ylabel=r'$n(\Omega_P-\Omega)/\kappa$',title=r'Marginal fluid disk, $Q=1$');ax[0].legend(loc='lower left',fontsize=8)
G=4.3009e-3;rcrit=np.sqrt(2)*100*40/(np.pi*G*100)/1000
for lo,hi,col,label in [(.7,rcrit,'#186b9c','Locally stable'),(rcrit,12,'#ca692b','Axisymmetrically unstable')]:
 r=np.linspace(lo,hi,250);ax[1].plot(r,rcrit/r,color=col,lw=2.3,label=label)
ax[1].axhline(1,color='.5',ls='--',lw=.8);ax[1].axvline(rcrit,color='.6',ls=':',lw=.8);ax[1].text(4.6,1.8,f'Marginal radius\n{rcrit:.2f} kpc',fontsize=9)
ax[1].set(xlim=(.7,12),ylim=(0,5),xlabel='Radius (kpc)',ylabel='Fluid Toomre parameter Q',title=r'Flat rotation curve: $Q\propto1/r$');ax[1].legend(fontsize=8)
for a in ax:a.grid(alpha=.16)
fig.savefig('paper-1-disk-branches.png',dpi=150,facecolor='white')
