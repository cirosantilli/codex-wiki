from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ks=list(range(1,17));ns=[2**k-1 for k in ks]
early=[k-1+k/n for k,n in zip(ks,ns)];saved=[k-e for k,e in zip(ks,early)]
assert early[0]==1 and all(0<=x<1 for x in saved)
fig,axes=plt.subplots(1,2,figsize=(7.6,3.6),dpi=100,facecolor='white')
axes[0].plot(ks,ks,'o-',color='#2166ac',label='Boundary search: k')
axes[0].plot(ks,early,'s-',color='#d6604d',label='Early equality return')
axes[0].set_ylabel('Expected iterations');axes[0].set_title('Both grow logarithmically')
axes[0].legend(fontsize=8,frameon=False,loc='upper left')
axes[1].plot(ks,saved,'o-',color='#d6604d');axes[1].axhline(1,color='#555555',ls='--',lw=1)
axes[1].set_ylim(-.05,1.15);axes[1].set_ylabel('Expected iterations saved');axes[1].set_title('The saving stays below one')
for ax in axes:ax.set_facecolor('white');ax.set_xlabel('k, with array length 2^k - 1');ax.set_xticks([1,4,8,12,16]);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
