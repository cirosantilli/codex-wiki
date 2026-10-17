"""Original power-law particle-horizon angle comparison; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
r=np.geomspace(1e-7,1e-2,700);r0=250000/(14e9)
fig,ax=plt.subplots(figsize=(7.5,4.2),layout='constrained')
for p,col,label in [(2/3,'#2158a0','Matter-only: p = 2/3'),(.5,'#b24b18','Radiation-only: p = 1/2')]:
    u=r**(1-p);theta=u/(1-u)*180/np.pi
    ax.loglog(r,theta,color=col,lw=2,label=label)
    u0=r0**(1-p);th0=u0/(1-u0)*180/np.pi
    ax.plot(r0,th0,'o',color=col)
    ax.annotate(f'{th0:.3g} degrees',xy=(r0,th0),xytext=(r0*2.5,th0*.8),arrowprops={'arrowstyle':'->','color':col},color=col)
ax.axvline(r0,color='.6',ls='--',lw=.9)
ax.set(xlabel=r'$t_{\rm rec}/t_0$',ylabel=r'One horizon length: $D_p/d_A$ (degrees)',title='Pure power-law histories, R proportional to t raised to p')
ax.legend(fontsize=9,loc='upper left');ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-horizon-angles.png',dpi=155,facecolor='white')
