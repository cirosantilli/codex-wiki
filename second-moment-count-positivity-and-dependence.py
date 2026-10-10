"""Exact positivity probabilities and second-moment bounds for toy counts.

No observations are represented. Save matching white PNG in CWD.
Versions and dependencies: pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

n=10;p=np.linspace(0.005,0.5,300)
actual=1-(1-p)**n;lower=n*p/(1-p+n*p)
fig,axes=plt.subplots(1,2,figsize=(10.6,4.8),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white');ax.grid(axis='y',alpha=0.17)
axes[0].plot(p,actual,color='#368565',lw=2.2,label='Exact: 1 − (1−p)¹⁰')
axes[0].plot(p,lower,color='#286f99',lw=2.2,label='Lower bound: 10p/(1−p+10p)')
axes[0].scatter([0.1,0.1],[1-0.9**10,10/19],color=['#368565','#286f99'],s=33,zorder=5)
axes[0].annotate('p = 0.1\nActual ≈ 0.6513\nBound ≈ 0.5263',(0.1,10/19),xytext=(0.22,0.25),fontsize=10,
                 arrowprops={'arrowstyle':'->','color':'#286f99'})
axes[0].set(xlim=(0,0.5),ylim=(0,1.04),xlabel='Success probability p > 0',ylabel='Probability of a positive count',
            title='Ten independent Bernoulli trials')
axes[0].legend(loc='upper left',fontsize=8.6,framealpha=0.96)
positions=np.arange(2);w=0.32
axes[1].bar(positions-w/2,[1-0.9**10,0.1],width=w,color='#368565',label='Exact positivity probability')
axes[1].bar(positions+w/2,[10/19,0.1],width=w,color='#286f99',label='Second-moment lower bound')
for x,y in zip(np.r_[positions-w/2,positions+w/2],[1-0.9**10,0.1,10/19,0.1]):
    axes[1].text(x,y+0.025,f'{y:.3f}',ha='center',fontsize=10)
axes[1].set(xticks=positions,xticklabels=['Independent trials\nVar(N) = 0.9','All trials share B\nVar(N) = 9'],
            ylim=(0,1.02),ylabel='Probability of N > 0',title='Same ten marginals and mean count 1')
axes[1].legend(loc='upper right',fontsize=8.5,framealpha=0.96)
fig.text(0.5,0.025,'Right: p = 0.1 for every trial. Shared model N = 10B attains the lower bound exactly.',
         ha='center',fontsize=10)
fig.subplots_adjust(left=0.065,right=0.98,top=0.9,bottom=0.19,wspace=0.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
