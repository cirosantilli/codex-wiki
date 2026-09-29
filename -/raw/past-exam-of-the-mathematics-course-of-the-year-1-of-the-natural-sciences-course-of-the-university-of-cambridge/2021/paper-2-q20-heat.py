"""Original heat solutions; Python 3.14, NumPy 2.3, Matplotlib 3.10.
The PNG is written to cwd. Dirichlet curves use the derived sine coefficients.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
x=np.linspace(0,1,500)
times=[0,.08,.3,1,3]
colors=['0.18','#3285b4','#49a178','#d99237','#b64b65']
odd=np.arange(1,602,2,dtype=float)
b=8/(np.pi*odd*(4-odd*odd))
sines=np.sin(np.pi*odd[:,None]*x[None,:])
fig,axs=plt.subplots(1,2,figsize=(9.2,3.8),layout='constrained')
for tau,color in zip(times,colors):
    insulated=.5*(1-np.exp(-4*tau)*np.cos(2*np.pi*x))
    fixed=np.sin(np.pi*x)**2 if tau==0 else (b*np.exp(-odd*odd*tau))@sines
    for ax,curve in zip(axs,[insulated,fixed]):ax.plot(x,curve,color=color,lw=1.8,label=f'$\\tau={tau:g}$')
axs[0].axhline(.5,color='0.6',ls=':',lw=1)
for ax,title in zip(axs,['Insulated ends: mean conserved','Zero-temperature ends: heat escapes']):
    ax.set(xlim=(0,1),ylim=(-.02,1.05),xlabel='$x/L$',ylabel=r'$\Theta/T_0$',title=title)
    ax.spines[['top','right']].set_visible(False)
axs[1].legend(loc='upper right',frameon=False,fontsize=9)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
