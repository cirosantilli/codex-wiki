"""Original equilibrium diagrams, Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes only paper-1-bifurcations.png to caller CWD, opaque white background.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
blue='#1769aa';red='#c74444'
fig,axes=plt.subplots(1,3,figsize=(10.6,3.9),dpi=120,facecolor='white')
a=np.linspace(-.3,1.6,900)
for mask,color,style in [(a<0,red,'--'),((a>=0)&(a<=1),blue,'-'),(a>1,red,'--')]:axes[0].plot(a[mask],a[mask]**2,color=color,ls=style)
p=np.linspace(0,1.6,650)
axes[0].plot(p,-np.sqrt(p),color=red,ls='--')
axes[0].plot(p[p<=1],np.sqrt(p[p<=1]),color=red,ls='--')
axes[0].plot(p[p>=1],np.sqrt(p[p>=1]),color=blue)
axes[0].scatter([0,1],[0,1],color='black',s=18,zorder=6)
axes[0].set(xlabel='$a$',ylabel='equilibrium $x=y$',title='Unperturbed branches',ylim=(-1.4,2.7))
eps=.004
for aa in np.linspace(-.04,.25,700):
 for z in np.roots([1,0,-aa,eps]):
  if abs(z.imag)<1e-8:
   stable=3*z.real*z.real-aa<0
   axes[1].plot(aa,z.real,'.',color=blue if stable else red,markersize=1.6)
axes[1].set(xlabel='$a$',ylabel='$x$',title=r'Near $a=0$: broken pitchfork')
eps2=.006;mu=np.linspace(-.23,.23,800);d=9*mu*mu-8*eps2;valid=d>=0
axes[2].plot(mu[valid & (mu<0)],(5*mu[valid & (mu<0)]-np.sqrt(d[valid & (mu<0)]))/4,color=blue)
axes[2].plot(mu[valid & (mu>0)],(5*mu[valid & (mu>0)]-np.sqrt(d[valid & (mu>0)]))/4,color=blue)
for mask in [valid & (mu<0),valid & (mu>0)]:axes[2].plot(mu[mask],(5*mu[mask]+np.sqrt(d[mask]))/4,color=red,ls='--')
axes[2].axvspan(-np.sqrt(8*eps2)/3,np.sqrt(8*eps2)/3,color='#eef0f2')
axes[2].set(xlabel=r'$\mu=a-1$',ylabel='$u=x-1$',title=r'Near $a=1$: gap and folds')
for ax in axes:ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.legend(handles=[Line2D([0],[0],color=blue,label='attracting'),Line2D([0],[0],color=red,ls='--',label='saddle / unstable slow direction')],loc='lower center',ncol=2,fontsize=9)
fig.suptitle('Positive forcing breaks the crossings (unfolded panels show leading local forms)',fontsize=11)
fig.tight_layout(rect=(0,.08,1,.94));fig.savefig('paper-1-bifurcations.png',facecolor='white',transparent=False);plt.close(fig)
