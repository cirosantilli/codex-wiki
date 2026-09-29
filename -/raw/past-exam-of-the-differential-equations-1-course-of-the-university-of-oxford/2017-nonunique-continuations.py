"""Original continuously differentiable waiting-time solutions; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,1001)
fig,ax=plt.subplots(figsize=(7.6,4.8),dpi=100,facecolor='white')
for c,color in [(2,'#1264a3'),(2.7,'#c04b19'),(3.5,'#2d873b'),(float('inf'),'#8056a5')]:
    y=np.where(x<=2,(1-x/2)**2-1,-1-np.maximum(x-c,0)**2/4)
    label='never departs'if not np.isfinite(c)else f'departs at c = {c:g}'
    ax.plot(x,y,color=color,lw=2,label=label)
ax.axhline(-1,color='#666666',ls=':',lw=1,zorder=0)
ax.axvline(2,color='#999999',ls=':',lw=1,zorder=0)
ax.scatter([2],[-1],color='#202020',s=25,zorder=5)
ax.annotate('common arrival at (2, −1)',xy=(2,-1),xytext=(.2,-2.5),fontsize=10,
            arrowprops=dict(arrowstyle='->',color='#333333'))
ax.set(xlim=(0,5),ylim=(-3.5,.15),xlabel='x',ylabel='y',title=r'Nonunique continuations of $y^\prime=-\sqrt{|1+y|}$')
ax.grid(alpha=.18);ax.legend(loc='lower left',fontsize=9,framealpha=.95)
fig.subplots_adjust(left=.10,right=.97,top=.89,bottom=.13)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
