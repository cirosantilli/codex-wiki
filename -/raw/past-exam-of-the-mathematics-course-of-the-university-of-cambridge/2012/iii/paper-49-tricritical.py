"""Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7; write opaque PNG to cwd."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6,4),dpi=100,layout='constrained')
u=np.linspace(-2,2,601);boundary=np.where(u<0,3*u*u/16,0)
ax.fill_between(u,boundary,1.05,color='#e5f1ff');ax.fill_between(u,-.65,boundary,color='#fff0d8')
x=np.linspace(-2,0,200)
ax.plot(x,3*x*x/16,color='#9b2d27',lw=2.6,label='Three-phase coexistence')
ax.plot([0,2],[0,0],color='#176d41',lw=2.6,label='Continuous transition')
ax.plot(x,x*x/4,color='#9b2d27',lw=1,ls=':',label='Metastability limits')
ax.plot([-2,0],[0,0],color='#9b2d27',lw=1,ls=':')
ax.scatter([0],[0],s=35,c='black',zorder=6);ax.annotate('Tricritical point',(0,0),(.2,.19),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.text(.7,.58,'Disordered: M = 0',ha='center',fontsize=10)
ax.text(0,-.43,'Ordered: symmetry-related ±M',ha='center',fontsize=10)
ax.set(xlim=(-2,2),ylim=(-.65,1.05),xlabel='Quartic coefficient u',ylabel='Quadratic coefficient r',title='Sextic Landau theory: h = 0, v = 1')
ax.legend(loc='upper left',fontsize=8,framealpha=1);ax.grid(alpha=.17)
fig.savefig(Path.cwd()/'paper-49-tricritical.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
