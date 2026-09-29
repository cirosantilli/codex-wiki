"""Original RC fluctuation-dissipation spectra; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
u=np.logspace(-3,3,1001);fig,(a,b)=plt.subplots(1,2,figsize=(8.5,3.3),layout='constrained')
for ratio,color in [(1,'#246e9d'),(10,'#b25731')]:
 s=ratio/(1+(ratio*u)**2);a.loglog(u,s,color=color,label=fr'$R/R_0={ratio}$',lw=2);b.semilogx(u,2/np.pi*np.arctan(ratio*u),color=color,lw=2)
a.set(xlabel=r'$2\pi fR_0C$',ylabel=r'$S_V^{(1)}(f)/(4k_BTR_0)$',title='Height-width compensation');a.legend(fontsize=9)
b.axhline(1,color='0.6',ls='--');b.set(xlabel=r'$2\pi f_{\max}R_0C$',ylabel='Fraction of full voltage variance',title='Same integrated variance',ylim=(-.02,1.08))
fig.savefig('paper-1-tsp2013-equilibrium-noise.png',dpi=140,facecolor='white')
