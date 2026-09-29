"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

C=np.array([1.5,2.5,8.5,12.])
G=np.array([54.,62.5,75.5,79.])
# Use the published solution fit; illustrative concentrations sample that fit.
M=.00989;B=.01197;ginf=1/B;b=B/M
fig,axes=plt.subplots(1,2,figsize=(9.5,3.7),layout='constrained')
z=np.linspace(0,.75,300)
axes[0].plot(z,M*z+B,color='#2166ac',lw=2)
axes[0].scatter(1/C,1/G,color='#222',s=32,zorder=3)
axes[0].set(xlabel=r'$1/C$ (m$^3$ mmol$^{-1}$)',ylabel=r'$1/\Gamma$ (m$^2$ mmol$^{-1}$)',title='Requested reciprocal-fit line')
axes[0].text(.05,.018,r'$M=0.00989$'+'\n'+r'$B=0.01197$',fontsize=10)
c=np.linspace(0,14,400)
axes[1].plot(c,ginf*b*c/(1+b*c),color='#2166ac',lw=2)
axes[1].scatter(C,G,color='#222',s=32,zorder=3)
axes[1].axhline(ginf,color='#d6604d',ls='--',label=r'$\Gamma_\infty=83.5$')
axes[1].set(xlabel=r'$C$ (mmol m$^{-3}$)',ylabel=r'$\Gamma$ (mmol m$^{-2}$)',title='Reconstructed Langmuir isotherm',ylim=(0,95))
axes[1].legend(fontsize=9)
fig.suptitle('Algebraic fit; the printed surface-density units fail a molecular-size check')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
