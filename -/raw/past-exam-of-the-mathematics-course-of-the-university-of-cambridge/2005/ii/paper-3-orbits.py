"""Energy orbits; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Writes one opaque PNG basename to the caller's current directory. MPLCONFIGDIR
is left under caller control. No source image or external data are used.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mu=1.0
fig,axes=plt.subplots(1,2,figsize=(9,4.2),layout='constrained',facecolor='white')
for ax,E in zip(axes,[0.05,25.0]):
    q0=mu*np.sqrt(E/(E+1));p0=mu*np.sqrt(E)
    theta=np.linspace(0,2*np.pi,700)
    ax.plot(q0*np.cos(theta),p0*np.sin(theta),color='#165a96',lw=2.1)
    ax.annotate('',xy=(q0*np.cos(1.35),p0*np.sin(1.35)),
        xytext=(q0*np.cos(1.8),p0*np.sin(1.8)),
        arrowprops={'arrowstyle':'->','color':'#165a96','lw':2})
    ax.axhline(0,color='0.55',lw=.8);ax.axvline(0,color='0.55',lw=.8)
    extent=max(q0*1.18,0.26)
    ax.set_xlim(-extent,extent);ax.set_ylim(-1.18*p0,1.18*p0)
    ax.set_facecolor('white');ax.set_xlabel(r'Position $q$');ax.set_ylabel(r'Momentum $p$')
    ax.set_title(('Low energy' if E<1 else 'High energy')+fr': $E={E:g}$')
    ax.grid(alpha=.2)
    ax.set_aspect('equal',adjustable='box')
    if E>1:
        for wall in [-mu,mu]:ax.axvline(wall,color='#ad4335',ls='--',lw=1)
        ax.text(0,-1.11*p0,r'Dashed lines: $q=\pm\mu$',ha='center',fontsize=9)
fig.suptitle(r'Periodic energy curves, $\mu=1$: $p^2+(E+1)q^2=E$')
fig.savefig('paper-3-orbits.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
