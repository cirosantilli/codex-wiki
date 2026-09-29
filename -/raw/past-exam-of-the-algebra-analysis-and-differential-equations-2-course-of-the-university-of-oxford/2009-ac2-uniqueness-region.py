"""Original characteristic-domain sketch. Python3.14,numpy2.3.5,matplotlib3.10.7.
Writes the matching basename PNG into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(.22,3.3,700)
fig,ax=plt.subplots(figsize=(6.5,4.7),facecolor='white')
ax.set_facecolor('white')
ax.fill_between(x,np.maximum(x,1/x),5,color='#d8ebf7',label='Uniquely determined region')
ax.plot(x,x,lw=1.8,color='#27628e',label=r'$y=x$')
ax.plot(x,1/x,lw=1.8,color='#7b4b91',label=r'$xy=1$')
s=np.linspace(1,np.sqrt(5),300)
ax.plot(s,s*s,lw=2,color='#2d7c42',label=r'Data arc $y=x^2$, $x\geq1$')
ax.plot([1],[1],'ko',ms=4)
ax.annotate('$(1,1)$',(1,1),xytext=(.5,.45),arrowprops={'arrowstyle':'->','lw':.8})
ax.annotate('',(2.9,4.8),(2.9,4.1),arrowprops={'arrowstyle':'->','color':'#27628e'})
ax.set(xlim=(0,3.3),ylim=(0,5),xlabel='$x$',ylabel='$y$',title=r'$x>0$, $y\geq\max(x,1/x)$')
ax.grid(alpha=.18)
ax.legend(fontsize=9,loc='upper left')
fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=160,facecolor='white')
