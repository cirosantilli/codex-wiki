"""Original explanatory plot. Python 3.14, numpy, matplotlib.
Run from the destination directory; writes a PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','savefig.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
r=np.linspace(.12,3.6,900);E=(r+1/r)/4
fig,ax=plt.subplots(figsize=(7.2,3.8),layout='constrained');ax.plot(r,E,lw=2,color='#1766a5',label='Trial energy');ax.axhline(.5,color='#c33c29',ls='--',label='Exact ground energy');ax.plot(1,.5,'ko');ax.annotate(r'Minimum: $\beta=m\omega/\hbar$',(1,.5),(1.65,.9),arrowprops=dict(arrowstyle='->'));ax.set(xlabel=r'$r=\beta\hbar/(m\omega)$',ylabel=r'$E/(\hbar\omega)$',ylim=(.35,2.25),title='Localization and spreading costs balance');ax.legend(frameon=False);fig.savefig('paper-1-variational.png',dpi=170);plt.close(fig)
