"""Step-forced first-order solution. Python3.14, numpy2.3.5, matplotlib3.10.7.

Output goes to caller CWD; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1000)
y=1/np.cosh(x)+np.where(x>0,np.tanh(x),0)
fig,ax=plt.subplots(figsize=(7.2,3.8),facecolor='white')
ax.plot(x,y,color='#185eac',lw=2.3,label='continuous solution')
ax.axhline(1,color='#666666',ls='--',lw=1,label='right asymptote')
ax.axhline(0,color='black',lw=.7);ax.axvline(0,color='black',lw=.7)
xm=np.arcsinh(1)
ax.scatter([0,xm],[1,np.sqrt(2)],color='#185eac',zorder=4)
ax.annotate('maximum '+r'$\sqrt{2}$',(xm,np.sqrt(2)),xytext=(2,1.58),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('derivative jumps at 0',(0,1),xytext=(-3.8,1.32),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlabel='x',ylabel='y',xlim=(-5,5),ylim=(-.08,1.75),title='Continuous solution under a unit step forcing')
ax.legend(loc='lower right',frameon=False,fontsize=9)
fig.tight_layout();fig.savefig(Path.cwd()/'paper-2-step-solution.png',dpi=150,facecolor='white',transparent=False);plt.close(fig)
