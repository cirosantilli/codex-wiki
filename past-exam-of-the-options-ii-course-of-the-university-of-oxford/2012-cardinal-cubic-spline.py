"""Original AO2 spline illustration. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from any output directory; creates the PNG in the current directory.
"""
from pathlib import Path
from math import comb
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-.45,4.45,1401)
y=sum((-1)**k*comb(4,k)*np.maximum(x-k,0)**3 for k in range(5))
y[(x<=0)|(x>=4)]=0
fig,ax=plt.subplots(figsize=(8,4.5),facecolor='white')
ax.set_facecolor('white')
ax.axhline(0,color='#555555',lw=.8)
ax.axvline(2,color='#8c9aa3',lw=1,ls='--',alpha=.7)
ax.plot(x,y,color='#126d9e',lw=2.7,label=r'$S_{(3)}(x)$')
ax.fill_between(x,0,y,color='#126d9e',alpha=.08)
ax.scatter(np.arange(5),[0,1,4,1,0],color='#c95a20',s=45,zorder=4,label='Knot values')
for t,v in enumerate([0,1,4,1,0]):ax.annotate(f'({t}, {v})',(t,v),xytext=(0,11),textcoords='offset points',ha='center',fontsize=10)
ax.set(xlim=(-.45,4.45),ylim=(-.25,4.7),xlabel='$x$',ylabel=r'$S_{(3)}(x)$',xticks=np.arange(5),yticks=np.arange(5),title='A natural cubic spline with compact support ($h=1$)')
ax.spines[['top','right']].set_visible(False)
ax.grid(alpha=.16);ax.legend(loc='upper left',frameon=False)
fig.tight_layout()
fig.savefig(Path.cwd()/'2012-cardinal-cubic-spline.png',dpi=170,facecolor='white')
