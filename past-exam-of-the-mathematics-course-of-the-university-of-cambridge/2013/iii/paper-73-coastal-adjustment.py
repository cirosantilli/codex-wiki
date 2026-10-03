"""Original coastal-adjustment profiles. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes one opaque PNG basename to cwd and preserves caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.2),dpi=100,facecolor='white')
for ax,ell,label in zip(axes,[.25,4.],['Narrow initial strip','Wide initial strip']):
 x=np.linspace(-ell-4,0,1601);inside=x>=-ell
 eta=np.where(inside,1-np.exp(-ell)*np.cosh(x),np.exp(x)*np.sinh(ell))
 v=np.where(inside,-np.exp(-ell)*np.sinh(x),np.exp(x)*np.sinh(ell))
 initial=np.where(inside,1,0)
 ax.set_facecolor('white');ax.plot(x,initial,color='#888888',linestyle='--',linewidth=1.5,label='Initial height')
 ax.plot(x,eta,color='#164f83',linewidth=2.3,label='Adjusted height')
 ax.plot(x,v,color='#aa4d20',linewidth=1.8,label='Alongshore velocity')
 ax.axvline(-ell,color='#777777',linewidth=.8,alpha=.5);ax.axvline(0,color='#333333',linewidth=2)
 ax.set(xlim=(x[0],.12),ylim=(-.03,1.12),xlabel=r'Offshore coordinate $x/a$',title=f'{label}:  L/a = {ell:g}')
 ax.grid(alpha=.2);ax.legend(fontsize=8,loc='upper left')
axes[0].set_ylabel(r'Height $\eta/\eta_0$ and velocity $v/[g\eta_0/(fa)]$')
fig.suptitle('Coastal geostrophic adjustment: conserved mass and zero wall velocity',fontsize=12)
fig.tight_layout();fig.savefig('paper-73-coastal-adjustment.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
