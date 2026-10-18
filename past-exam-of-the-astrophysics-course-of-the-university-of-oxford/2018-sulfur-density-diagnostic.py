"""Three-level rate balance with all supplied collision channels. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

h,c,kb,T=6.62607015e-34,299792458.,1.380649e-23,1e4
energy=np.array([0.,h*c/673.1e-9,h*c/671.6e-9]);weights=np.array([4,4,6])
A=np.zeros((3,3));A[2,0]=2.6e-4;A[1,0]=8.8e-4;A[2,1]=3.3e-7
q=np.zeros((3,3))
for j,i,strength in [(2,0,4.19),(1,0,2.79),(2,1,7.6)]:
    q[j,i]=8.6e-12*strength/weights[j]/np.sqrt(T)
    q[i,j]=weights[j]/weights[i]*q[j,i]*np.exp(-(energy[j]-energy[i])/(kb*T))
def populations(density):
    rates=density*q+A
    balance=rates.T.copy()
    np.fill_diagonal(balance,-rates.sum(axis=1))
    balance[-1]=1.
    return np.linalg.solve(balance,[0.,0.,1.])
density=np.logspace(6,13,500)
fractions=np.array([populations(n) for n in density])
factor=A[2,0]/A[1,0]*673.1/671.6
ratio=factor*fractions[:,2]/fractions[:,1]
observed_density=1.3474516748502523e10
plt.rcParams.update({'font.size':12,'figure.facecolor':'white'})
fig,axes=plt.subplots(2,1,figsize=(10,6.5),layout='constrained',sharex=True)
axes[0].semilogx(density,ratio,color='#205c96',lw=2.5)
axes[0].axhline(.5,color='#a43c2a',linestyle='--',label='observed optical ratio 0.50')
axes[0].scatter([observed_density],[.5],s=45,color='#a43c2a',zorder=5)
axes[0].annotate(r'$n_e=1.35\times10^{10}$',xy=(observed_density,.5),xytext=(1.5e10,.82),arrowprops={'arrowstyle':'->','color':'#a43c2a'},color='#a43c2a')
axes[0].axvspan(1.5405e9,3.9532e9,color='#888888',alpha=.15,label='upper-level critical densities')
axes[0].set_ylabel(r'$j_{31}/j_{21}$')
axes[0].set_ylim(.35,1.58)
axes[0].legend(loc='upper right',fontsize=10)
for j,color in enumerate(['#333333','#33905b','#a43c2a']):
    axes[1].semilogx(density,fractions[:,j],color=color,lw=2,label=rf'$f_{j+1}$')
for ax in axes:
    ax.axvline(1e12,color='#777777',linestyle=':',lw=1.5)
    ax.grid(alpha=.2)
    ax.set_xlim(density[0],density[-1])
axes[1].text(1.15e12,.53,'abundance calculation\nuses this density',fontsize=10,color='#555555')
axes[1].set_ylabel('Fraction of ions in each level')
axes[1].set_xlabel(r'Electron density $n_e$ ($\mathrm{m^{-3}}$)')
axes[1].set_ylim(-.02,1.03)
axes[1].legend(loc='center left',fontsize=11)
fig.suptitle(r'Three-level sulfur diagnostic at $T_e=10^4$ K',fontsize=16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
