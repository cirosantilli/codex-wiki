"""Plot the requested kink. Python 3.14; root matplotlib/numpy dependencies.

Run from the desired media output directory. The only figure output is cwd /
paper-308-kink.png; main's Make workflow supplies the publication _media cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=np.linspace(-5,5,601)
fig,ax=plt.subplots(figsize=(6.4,3.2),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,np.tanh(x),color='#1764ab',lw=2.4,label=r'$\phi=\tanh(x-a)$')
ax.axhline(1,color='#7a7a7a',ls='--',lw=.8)
ax.axhline(-1,color='#7a7a7a',ls='--',lw=.8)
ax.axvline(0,color='#aaaaaa',ls=':',lw=.8)
ax.scatter([0],[0],s=20,color='#1764ab',zorder=5)
ax.set_xlim(-5,5);ax.set_ylim(-1.23,1.23)
ax.set_xlabel(r'$x-a$');ax.set_ylabel(r'$\phi$')
ax.set_yticks([-1,0,1]);ax.set_xticks([-4,-2,0,2,4])
ax.set_title('A kink connects two isolated vacuum values',fontsize=11)
ax.legend(loc='upper left',frameon=False,fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-308-kink.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
