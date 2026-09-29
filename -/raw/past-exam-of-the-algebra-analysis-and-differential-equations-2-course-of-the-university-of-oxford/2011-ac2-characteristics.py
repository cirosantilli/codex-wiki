"""Python 3.14; numpy and matplotlib. Output PNG goes to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(.03,2.6,400)
fig,ax=plt.subplots(figsize=(6.5,4),layout='constrained',facecolor='white')
for c in [-2,-1,0,1,2]:
 ax.axhline(c,color='#2d6a96',lw=1.25,label=r'$\xi=y$ constant'if c==-2 else None)
 ax.plot(x,x*x/2+c,color='#aa493a',lw=1.4,label=r'$\eta=y-x^2/2$ constant'if c==-2 else None)
ax.axvline(1,color='#444444',lw=1,ls='--',label='Data line $x=1$')
ax.set(xlabel='$x$',ylabel='$y$',xlim=(0,2.6),ylim=(-2.2,3.2),title='Characteristic coordinate curves')
ax.legend(loc='upper left',fontsize=9,framealpha=.95);ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2011-ac2-characteristics.png',dpi=145,facecolor='white')
