"""Original dimensionless Planck spectra; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,15,2001);fig,ax=plt.subplots(figsize=(6.5,3.8),layout='constrained')
for ratio,color in [(.6,'#5577ad'),(.8,'#388f71'),(1,'#b55732')]:
 den=np.expm1(x/ratio);curve=np.divide(x**3,den,out=np.zeros_like(x),where=den>0);ax.plot(x,curve,color=color,lw=2,label=fr'$T/T_0={ratio}$; area ratio {ratio**4:.2f}')
ax.set(xlabel=r'$\hbar\omega/(k_BT_0)$',ylabel='Spectral energy density (common units)',title='Planck spectra: peak frequency ∝ T; integrated energy ∝ T⁴',xlim=(0,15),ylim=(0,1.6));ax.legend(fontsize=9)
fig.savefig('paper-1-tsp2013-blackbody.png',dpi=140,facecolor='white')
