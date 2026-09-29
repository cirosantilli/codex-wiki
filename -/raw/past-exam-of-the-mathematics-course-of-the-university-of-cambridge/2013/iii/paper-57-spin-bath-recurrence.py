"""Generate the Paper 57 Q4(c)(i) sketch; tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. Emit only the PNG basename to cwd.
The caller supplies MPLCONFIGDIR; never override its value.
"""
import os
from pathlib import Path
if 'MPLCONFIGDIR' not in os.environ:
    raise RuntimeError('Caller must supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,4,1601)
z=np.cos(np.pi*t)*np.cos(np.pi*t/2)**2
fig,ax=plt.subplots(figsize=(8.4,4.8),dpi=100,facecolor='white')
ax.set_facecolor('white')
ax.plot(t,z,color='#165aa7',linewidth=2.4,label=r'$z(t)=\cos(\pi t)\cos^2(\pi t/2)$')
ax.axhline(0,color='#555555',linewidth=0.9)
ax.axhline(-1/8,color='#777777',linewidth=0.8,linestyle=':')
ax.scatter([0,2,4],[1,1,1],s=34,color='#165aa7',zorder=4)
zeros=np.array([.5,1,1.5,2.5,3,3.5])
ax.scatter(zeros,zeros*0,s=20,color='#555555',zorder=4)
mins=np.array([2/3,4/3,8/3,10/3])
ax.scatter(mins,mins*0-1/8,s=27,color='#b44823',zorder=4)
ax.annotate('full coherence returns',xy=(2,1),xytext=(2,0.77),ha='center',arrowprops=dict(arrowstyle='->',color='#555555'),fontsize=10)
ax.annotate('double zero',xy=(1,0),xytext=(1,.27),ha='center',arrowprops=dict(arrowstyle='->',color='#555555'),fontsize=10)
ax.annotate('minimum −1/8',xy=(10/3,-1/8),xytext=(3.05,-.30),ha='center',arrowprops=dict(arrowstyle='->',color='#555555'),fontsize=10)
ax.set(xlim=(-.04,4.04),ylim=(-.37,1.12),xlabel='time t',ylabel='coherence factor z(t)',title='Three-spin bath: coherence revives with period 2')
ax.set_xticks(np.arange(0,4.01,.5))
ax.grid(alpha=.18)
ax.legend(loc='upper right',fontsize=10)
fig.tight_layout()
fig.savefig(Path('paper-57-spin-bath-recurrence.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
