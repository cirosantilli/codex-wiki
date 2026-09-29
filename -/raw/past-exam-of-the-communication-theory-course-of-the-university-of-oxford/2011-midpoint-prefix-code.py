"""Original midpoint-code diagram; Python 3.14 and Matplotlib 3.10.
The generated PNG is saved in the current directory.
"""
from pathlib import Path
from fractions import Fraction
from math import ceil,log2
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Patch
probs=[Fraction(2,5),Fraction(3,10),Fraction(1,5),Fraction(1,10)]
fig,ax=plt.subplots(figsize=(10,4.4),facecolor='white');ax.set_facecolor('white')
f=Fraction(0)
for k,p in enumerate(probs,1):
 g=f+p/2;ell=ceil(-log2(float(p)))+1;index=(g.numerator*2**ell)//g.denominator;left=Fraction(index,2**ell);width=Fraction(1,2**ell);y=5-k
 ax.add_patch(Rectangle((float(f),y-.17),float(p),.34,facecolor='#d9eaf4',edgecolor='#779caf',lw=1))
 ax.add_patch(Rectangle((float(left),y-.12),float(width),.24,facecolor='#db8b36',edgecolor='#ab6017',lw=1.2))
 ax.plot(float(g),y,'o',color='#1e2427',ms=5,zorder=4)
 ax.text(-.025,y,f'$k={k}$',ha='right',va='center',fontsize=11)
 ax.text(1.03,y,format(index,f'0{ell}b'),ha='left',va='center',fontsize=12,family='monospace')
 f+=p
ax.text(1.03,4.57,'Codeword',fontsize=11)
ax.set(xlim=(-.12,1.23),ylim=(.4,4.8),xticks=[0,.25,.5,.75,1],yticks=[],xlabel='Cumulative probability')
ax.spines[['top','right','left']].set_visible(False);ax.grid(axis='x',alpha=.17)
ax.legend(handles=[Patch(facecolor='#d9eaf4',edgecolor='#779caf',label='Probability cell'),Patch(facecolor='#db8b36',edgecolor='#ab6017',label='Dyadic code interval')],loc='lower left',bbox_to_anchor=(0,-.29),frameon=False,ncol=2)
fig.suptitle('Disjoint code intervals stay inside their midpoint probability cells',fontsize=14)
fig.tight_layout(rect=(0,.05,1,.94));fig.savefig(Path.cwd()/'2011-midpoint-prefix-code.png',dpi=170,facecolor='white')
