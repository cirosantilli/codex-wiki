"""Original ideal Planck radiance per wavelength at 2.7 K; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
h=6.62607015e-34;c=299792458.;kb=1.380649e-23;T=2.7
lm=np.linspace(.08,5,1200)*1e-3
B=2*h*c*c/(lm**5*np.expm1(h*c/(lm*kb*T)))
peak=2.897771955e-3/T
bp=2*h*c*c/(peak**5*np.expm1(h*c/(peak*kb*T)))
fig,ax=plt.subplots(figsize=(7,3.8),layout='constrained')
ax.plot(lm*1e3,B*1e3,color='#2158a0',lw=2)
ax.plot(peak*1e3,bp*1e3,'o',color='#b24b18');ax.annotate('Wavelength peak: 1.07 mm',xy=(peak*1e3,bp*1e3),xytext=(2.1,bp*1e3*.86),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Wavelength (mm)',ylabel=r'$B_\lambda$ ($\mu$W m$^{-2}$ sr$^{-1}$ mm$^{-1}$)',title='Ideal black-body radiance per wavelength at 2.7 K',xlim=(0,5),ylim=(0,bp*1e3*1.16))
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-planck.png',dpi=155,facecolor='white')
