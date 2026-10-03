"""Original Ising-chain dispersion sketches; PNG output goes to caller cwd.
Tested with Python3.14.4, NumPy2.3.5, Matplotlib3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k=np.linspace(-np.pi,np.pi,1001)
fig,axes=plt.subplots(1,3,figsize=((1080+1e-6)/100,(360+1e-6)/100),dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('Ising quasiparticle spectrum: flat, field-gapped and critical',fontsize=13,y=.985)
for ax,g,title,top in zip(axes,[0,6,1],['Zero field: g = 0','Large field: g = 6 (representative)','Critical field: g = 1'],[3.2,15,5]):
    energy=2*np.sqrt(1+g*g-2*g*np.cos(k))
    ax.plot(k,energy,color='#1f77b4',linewidth=2)
    ax.set_title(title,fontsize=11)
    ax.set_ylim(0,top)
    ax.set_xlim(-np.pi,np.pi)
    ax.set_xticks([-np.pi,0,np.pi],[r'$-\pi$',r'$0$',r'$\pi$'])
    ax.set_xlabel('Wavenumber k (unit lattice spacing)')
    ax.set_ylabel(r'$\epsilon_k/J$')
    ax.grid(alpha=.18)
axes[0].annotate('Flat branch at 2J',xy=(.8,2),xytext=(-2.7,2.65),arrowprops={'arrowstyle':'->','color':'#444'},fontsize=10)
axes[1].plot(k,12-2*np.cos(k),'--',color='#d95f02',linewidth=1,label='Leading large-g form')
axes[1].legend(loc='lower right',fontsize=9)
axes[2].annotate('Gap closes; slope 2J',xy=(.1,.2),xytext=(-2.8,2),arrowprops={'arrowstyle':'->','color':'#444'},fontsize=10)
fig.subplots_adjust(left=.055,right=.98,bottom=.18,top=.80,wspace=.32)
fig.savefig(Path.cwd()/'paper-75-ising-dispersion.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
