"""Original evanescent density calculation; Python 3.14, NumPy, Matplotlib.
CODATA2022 electron mass; exact e and h. Unit incident beam density.
Writes the basename PNG to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
me=9.1093837139e-31;e=1.602176634e-19;hb=6.62607015e-34/(2*np.pi)
alpha=np.sqrt(2*me*e)/hb*1e-9
x=np.linspace(0,1.2,601);density=8/3*np.exp(-2*alpha*x);at1=8/3*np.exp(-2*alpha)
fig,ax=plt.subplots(figsize=(7.8,4.6),layout='constrained')
ax.semilogy(x,density,color='#286da5',lw=2.5)
ax.scatter([1],[at1],color='#a64728',zorder=4)
ax.annotate('Density at 1 nm = 9.46 × 10⁻⁵',xy=(1,at1),xytext=(.13,2.2e-4),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.axhline(1,color='gray',linestyle=':',label='Incident density')
ax.set(xlabel='Distance into the step (nm)',ylabel='Density / incident density',title='Nonzero evanescent density, zero transmitted current',xlim=(0,1.2),ylim=(8e-6,4))
ax.grid(alpha=.2,which='both');ax.legend(loc='upper right')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=145,facecolor='white')
