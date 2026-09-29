"""Original local/quantum GHZ outcome histograms with explicit noise model; Python 3.14."""
from pathlib import Path
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
states=list(itertools.product([1,-1],repeat=3));parity=np.prod(states,axis=1)
labels=[''.join('+' if q==1 else '−' for q in state) for state in states]
fig,axes=plt.subplots(2,1,figsize=(9.8,6.8),facecolor='white')
fig.subplots_adjust(left=.10,right=.97,bottom=.16,top=.89,hspace=.55)
for ax,error,title in zip(axes,[0.,.08],['Ideal: disjoint allowed parity sectors','8% phase-flip mixture; specified local shared-error model']):
    visibility=1-2*error;qm=(1+visibility*parity)/8;local=(1-visibility*parity)/8;x=np.arange(8)
    ax.bar(x-.18,local,.35,color='#a34100',label='Local shared-error model' if error else 'Local prediction')
    ax.bar(x+.18,qm,.35,color='#126782',label='Quantum mechanics')
    ax.set(xticks=x,xticklabels=labels,ylim=(0,.36),ylabel='Probability',title=title)
    ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True);ax.legend(loc='upper right',fontsize=9)
    for xx,pl,pq in zip(x,local,qm):
        if pl:ax.text(xx-.18,pl+.006,f'{pl:.2f}',ha='center',fontsize=9)
        if pq:ax.text(xx+.18,pq+.006,f'{pq:.2f}',ha='center',fontsize=9)
axes[1].set_xlabel('YYY outcome signs; + = R, − = L')
axes[1].text(.01,-.31,'General noisy local bound: P(product +) ≤ 0.24; quantum prediction: 0.92',transform=axes[1].transAxes,fontsize=10)
fig.suptitle('YYY outcomes: ideal and 8% phase-flip ensembles',fontsize=16,y=.98)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
