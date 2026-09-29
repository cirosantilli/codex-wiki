"""Python 3.14; numpy 2.3.5 / matplotlib 3.10.7. Emit opaque PNG to caller CWD.
MPLCONFIGDIR remains under caller control. Both noise conventions are labelled.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def xlogx(x):
 x=np.asarray(x,dtype=float);r=np.zeros_like(x);m=x>0;r[m]=x[m]*np.log2(x[m]);return r
def capacities(p):
 p=np.asarray(p,dtype=float)
 z=2*p/3
 c=1+xlogx(z)+xlogx(1-z)
 ce=2+xlogx(1-p)+3*xlogx(p/3)
 return np.maximum(c,0),np.maximum(ce,0)
fig,axes=plt.subplots(1,2,figsize=(10,4.3),dpi=135,facecolor='white',sharey=True)
for ax in axes:
 ax.set_facecolor('white');ax.grid(alpha=.22);ax.set_ylim(0,2.08);ax.set_xlim(0,1)
p=np.linspace(0,1,751);c,ce=capacities(p)
axes[0].plot(p,c,lw=2.2,label=r'$C_{\rm prod}$',color='#2459a6');axes[0].plot(p,ce,lw=2.2,label=r'$C_E$',color='#b44b12')
axes[0].axvline(.75,color='#666666',ls='--',lw=1)
axes[0].annotate('Both vanish\nat $p=3/4$',xy=(.75,0),xytext=(.52,.76),arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=11)
axes[0].set_xlabel('Total nonidentity Pauli-error probability $p$')
axes[0].set_ylabel('Classical capacity (bits per channel use)')
axes[0].set_title(r'$(1-p)\rho+(p/3)\sum_j\sigma_j\rho\sigma_j$')
q=np.linspace(0,1,751);c,ce=capacities(.75*q)
axes[1].plot(q,c,lw=2.2,label=r'$C_{\rm prod}$',color='#2459a6');axes[1].plot(q,ce,lw=2.2,label=r'$C_E$',color='#b44b12')
axes[1].set_xlabel('Replacement probability $q$ ($p=3q/4$)')
axes[1].set_title(r'$(1-q)\rho+qI/2$')
axes[1].text(.47,1.3,r'$C_E/C_{\rm prod}\longrightarrow 3$'+'\n'+r'as $q\longrightarrow1$',ha='center',fontsize=13)
for ax in axes:ax.legend(loc='upper right',framealpha=.95)
fig.tight_layout(pad=1.2)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
