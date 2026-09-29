"""Blackbody contrast sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The current working directory is the only output destination; Make installs media.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
wavelength=np.geomspace(.3,1000,1000)
c2=1.438776877e4
r=.01*np.expm1(c2/(wavelength*5800))/np.expm1(c2/(wavelength*1500))
limit=.01*1500/5800
fig,ax=plt.subplots(figsize=(8,4.3),dpi=100,facecolor='white')
ax.semilogx(wavelength,1e6*r,color='#245786',lw=2.5,label=r'$T_p=1500$ K, $T_s=5800$ K, $R_p/R_s=0.1$')
ax.axhline(1e6*limit,color='#bd713a',ls='--',label='Rayleigh–Jeans limit for both bodies')
ax.set(xlabel='Wavelength (µm)',ylabel='Planet / star flux ratio (ppm)',ylim=(0,2850),xlim=(.3,1000))
ax.set_title('Thermal contrast: negligible in the visible, constant at long wavelengths')
ax.grid(alpha=.18);ax.legend(loc='lower right',fontsize=9)
ax.set_facecolor('white');fig.tight_layout()
fig.savefig(Path.cwd()/'paper-59-contrast.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
