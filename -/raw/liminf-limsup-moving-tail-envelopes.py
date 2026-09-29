"""Exact infinite-tail bounds for a_n=(-1)^n(1+1/n).

Run from the desired output directory. Dependencies/versions: pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

n=np.arange(1,41)
a=(-1.0)**n*(1+1/n)
e=n+(n%2)
o=n+(1-n%2)
upper=1+1/e
lower=-1-1/o
fig,axes=plt.subplots(1,2,figsize=(10.6,4.6),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white'); ax.grid(alpha=0.16)
    ax.axhline(1,color='#a16b35',linestyle='--',linewidth=1.3)
    ax.axhline(-1,color='#176c91',linestyle='--',linewidth=1.3)
axes[0].scatter(n[n%2==0],a[n%2==0],s=28,color='#a16b35',label='Even indices → 1')
axes[0].scatter(n[n%2==1],a[n%2==1],s=28,color='#176c91',label='Odd indices → −1')
axes[0].set(xlim=(0,41),ylim=(-2.15,1.9),xlabel='Index n',ylabel='aₙ',title='An oscillating sequence has two limiting edges')
axes[0].legend(loc='center right',fontsize=10,framealpha=0.95)
axes[1].step(n,upper,where='post',color='#a16b35',linewidth=2.3,label='uₙ: supremum of the whole tail')
axes[1].step(n,lower,where='post',color='#176c91',linewidth=2.3,label='lₙ: infimum of the whole tail')
axes[1].fill_between(n,lower,upper,step='post',color='#e4edf0',alpha=0.65)
axes[1].set(xlim=(1,40),ylim=(-2.15,1.9),xlabel='First remaining index N',ylabel='Exact tail bound',title='Removing early terms tightens the bounds')
axes[1].legend(loc='center right',fontsize=9,framealpha=0.95)
fig.text(0.5,0.025,'Bounds use all infinitely many later terms: first remaining odd/even indices determine the extrema.',ha='center',fontsize=10)
fig.subplots_adjust(left=0.065,right=0.98,top=0.89,bottom=0.16,wspace=0.25)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
