"""Original pressure profiles of the constant-density interior solution."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def pressure_ratio(x,C):
    s=np.sqrt(1-C*np.asarray(x)**2)
    sr=np.sqrt(1-C)
    return (s-sr)/(3*sr-s)

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(9.5,4.3),layout='constrained')
x=np.linspace(0,1,700)
for C,col in zip([.2,.5,.8,.88],['#4477aa','#228833','#cc7722','#aa3377']):
    axes[0].plot(x,pressure_ratio(x,C),label=rf'$C={C:g}$',lw=2,color=col)
axes[0].set(xlabel=r'$r/R$',ylabel=r'$p/(\rho c^2)$',title='Interior pressure: constant density',xlim=(0,1),ylim=(0,17))
axes[0].legend(frameon=False,fontsize=10)
C=np.linspace(.01,8/9-1e-4,1500)
axes[1].semilogy(C,pressure_ratio(0,C),color='#126782',lw=2)
axes[1].axvline(8/9,color='#aa3377',ls='--',label=r'$C=8/9$')
axes[1].set(xlabel=r'Compactness $C=2GM/(c^2R)$',ylabel=r'$p_c/(\rho c^2)$',title='Central pressure diverges at the bound',xlim=(0,.95),ylim=(.001,2000))
axes[1].legend(frameon=False,fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
