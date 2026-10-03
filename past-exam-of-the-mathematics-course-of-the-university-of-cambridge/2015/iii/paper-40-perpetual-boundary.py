"""Perpetual option value; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
s=np.linspace(.01,5,1000)
fig,axes=plt.subplots(1,2,figsize=(9,3.4),dpi=100,facecolor='white')
for ax,alpha in zip(axes,[.35,.65]):
    b=alpha/(1-alpha)
    value=np.where(s<=b,1/(1+s),1/(1+b)*(s/b)**(-alpha))
    ax.set_facecolor('white');ax.plot(s,1/(1+s),label='Immediate payout',color='#6d6d6d',ls='--',lw=2)
    ax.plot(s,value,label='Option value',color='#225c92',lw=2)
    ax.axvline(b,color='#276f44',ls=':',lw=1.8)
    ax.axvspan(0,b,color='#e5f1e8',alpha=1)
    ax.set(xlim=(0,5),ylim=(0,1),xlabel='Stock price s',ylabel='Value',title=rf'$\alpha={alpha},\quad b={b:.3f}$')
    ax.text(.04,.09,'Exercise in shaded region',transform=ax.transAxes,fontsize=9)
    ax.legend(frameon=False,fontsize=8);ax.grid(alpha=.15)
fig.subplots_adjust(left=.075,right=.98,bottom=.18,top=.86,wspace=.3)
fig.savefig(Path.cwd()/'paper-40-perpetual-boundary.png',facecolor='white',transparent=False)
plt.close(fig)
