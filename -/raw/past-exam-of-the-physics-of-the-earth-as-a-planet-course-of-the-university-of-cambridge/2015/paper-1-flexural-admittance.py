from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.geomspace(.01,12,500)
fig,ax=plt.subplots(figsize=(7.4,4.2),layout='constrained')
for h in [0,.3,1]:ax.semilogx(x,1-np.exp(-h*x)/(1+x**4),lw=2,label=fr'$t/\ell_f={h:g}$')
ax.axhline(1,color='gray',ls='--');ax.axvline(1,color='gray',ls=':',lw=1)
ax.annotate('long waves:\ncompensation',(.04,.04),(.012,.35),arrowprops=dict(arrowstyle='->'),fontsize=10)
ax.annotate('bending transition',(.85,.55),(.14,.8),arrowprops=dict(arrowstyle='->'),fontsize=10)
ax.text(2.1,.9,'short waves:\nsurface-sheet limit',fontsize=10)
ax.set(xlabel=r'$k\ell_f$',ylabel=r'$Z/(2\pi G\rho_c)$',ylim=(-.02,1.07),title='Gravity response to a surface load')
ax.legend(loc='center right',fontsize=10);ax.grid(alpha=.2)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
