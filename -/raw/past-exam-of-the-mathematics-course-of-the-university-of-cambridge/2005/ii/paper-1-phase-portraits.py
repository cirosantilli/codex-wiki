"""Original local phase portraits. Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes same-basename opaque PNG to caller CWD, honoring MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(7.6,3.8),dpi=120,facecolor='white')
t=np.linspace(-.5,.5,150);X,Y=np.meshgrid(t,t)
for ax,a in zip(axes,[-.08,.08]):
 U=(a-X*X)*(a*a-Y);V=X-Y
 ax.streamplot(t,t,U,V,color='#8995a5',density=1.1,linewidth=.7,arrowsize=.8)
 ax.plot(t,t,':',color='#555555',linewidth=.8,label='$y=x$')
 ax.scatter([a*a],[a*a],s=45,color='#1968ab' if a>0 else '#c43c3c',zorder=5)
 if a>0:
  q=np.sqrt(a);ax.scatter([q,-q],[q,-q],s=45,facecolor='white',edgecolor='#c43c3c',linewidth=1.6,zorder=5)
 ax.set(xlim=(-.5,.5),ylim=(-.5,.5),xlabel='$x$',ylabel='$y$',title=f'$a={a:g}$: '+('one saddle' if a<0 else 'one attractor, two saddles'))
 ax.title.set_fontsize(10);ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig('paper-1-phase-portraits.png',facecolor='white',transparent=False);plt.close(fig)
