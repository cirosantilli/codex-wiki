"""Homologous dust collapse and its two linear density modes.

Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write only paper-64-collapse-modes.png to caller CWD; honor MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
phi=np.linspace(0, np.pi, 701)
r=(1+np.cos(phi))/2
t=(phi+np.sin(phi))/np.pi
phase=np.linspace(.015,np.pi-.12,601)
r_modes=(1+np.cos(phase))/2
growth=np.sin(phase)/(1+np.cos(phase))**2
integral=4/np.tan(phase/2)+np.sin(phase)-3*(np.pi-phase)
decay=growth*integral/2
assert np.all(decay>0)
fig,axs=plt.subplots(1,2,figsize=(9,3.6),dpi=120,facecolor='white')
for ax in axs:
    ax.set_facecolor('white')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(color='#dddddd',lw=.6)
axs[0].plot(t,r,color='#244d73',lw=2)
axs[0].set(xlabel=r'$t/t_c$',ylabel=r'$R/R_0$',title='Collapse from rest',xlim=(0,1),ylim=(0,1.05))
axs[1].loglog(r_modes,growth,color='#9a4e16',lw=2,label=r'Growing branch $\delta_g$')
axs[1].loglog(r_modes,decay,color='#244d73',lw=2,label=r'Decaying branch $\delta_d/2$')
axs[1].set(xlabel=r'$R/R_0$ (decreases during collapse)',ylabel='Fractional-density mode amplitude',title='One growing and one decaying branch')
axs[1].set_xlim(1,.0035)
axs[1].legend(fontsize=8,loc='best')
fig.tight_layout()
fig.savefig('paper-64-collapse-modes.png',facecolor='white',transparent=False)
plt.close(fig)
