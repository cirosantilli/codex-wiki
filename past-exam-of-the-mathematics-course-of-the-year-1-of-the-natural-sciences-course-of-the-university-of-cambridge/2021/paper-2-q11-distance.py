"""Original distance sketch; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from mirrored _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
t=np.linspace(-5,3,600)
d=np.sqrt((t+1)**2+.5)
fig,ax=plt.subplots(figsize=(6.4,4.0),layout='constrained')
ax.plot(t,d,color='#256c9c',lw=2.3,label=r'$d(t)$')
ax.plot(t,t+1,'--',color='#a35c2c',lw=1.3,label=r'$d=t+1$')
ax.plot(t,-t-1,'--',color='#6c689f',lw=1.3,label=r'$d=-t-1$')
ax.axvline(-1,color='0.6',ls=':',lw=1)
ax.plot(-1,1/np.sqrt(2),'o',color='#256c9c')
ax.annotate(r'$(-1,1/\sqrt{2})$',xy=(-1,1/np.sqrt(2)),xytext=(-.3,1.35),arrowprops={'arrowstyle':'->','color':'0.4'})
ax.set(xlim=(-5,3),ylim=(0,4.4),xlabel='$t$',ylabel='Perpendicular distance',title='A smooth minimum between two linear asymptotes')
ax.legend(loc='upper center',frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
