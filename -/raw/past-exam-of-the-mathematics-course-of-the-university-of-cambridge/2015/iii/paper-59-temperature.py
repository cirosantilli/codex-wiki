"""Atmospheric-profile sketches; root pyproject dependencies, Python 3.14.
Only opaque basename PNG output in the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
tau=np.geomspace(1e-4,100,600)
fig,axes=plt.subplots(1,2,figsize=(8.6,4.4),dpi=100,facecolor='white')
axes[0].semilogy((.75*(tau+2/3))**.25,tau,lw=2.5,color='#245786')
axes[0].axvline(2**(-.25),color='#777777',ls='--',lw=1)
axes[0].set(xlabel=r'$T/T_{\rm int}$',title='Weak irradiation: intrinsic grey solution',xlim=(.65,3.2))
# Illustrative shapes, deliberately not labelled as numerical atmosphere models.
base=1400+200*np.log1p(tau)
inverted=1200+230*np.log1p(tau)+500*np.exp(-tau/.05)
axes[1].semilogy(base,tau,lw=2.5,color='#245786',label='No strong upper absorber')
axes[1].semilogy(inverted,tau,lw=2.5,color='#b36335',label='Upper heating: inversion')
axes[1].set(xlabel='Illustrative temperature (K)',title='Strong irradiation: possible shapes',xlim=(1000,2600))
axes[1].legend(fontsize=8,loc='lower left')
for ax in axes:
 ax.set_ylim(100,1e-4);ax.set_ylabel('Inward optical depth τ');ax.grid(alpha=.18);ax.set_facecolor('white')
fig.tight_layout(pad=1.2)
fig.savefig(Path.cwd()/'paper-59-temperature.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
