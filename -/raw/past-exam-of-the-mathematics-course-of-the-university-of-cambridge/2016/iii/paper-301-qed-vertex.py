"""Generate an opaque 720 x 280 QED vertex PNG in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7+dfsg1 and numpy 2.3.5.
Make chooses the output directory; this script does not mirror media files.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.2, 2.8), dpi=100, facecolor='white')
ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off')
y=.34
ax.plot([.08,.92],[y,y],color='#202a35',linewidth=2.2)
for a,b in [(.23,.35),(.66,.78)]:
 ax.annotate('',xy=(b,y),xytext=(a,y),arrowprops={'arrowstyle':'-|>','color':'#202a35','lw':2})
t=np.linspace(0,1,400)
ax.plot(.5+.018*np.sin(12*np.pi*t), y+.47*t,color='#0077ad',linewidth=2.2)
ax.plot([.5],[y],'o',color='#202a35',markersize=6)
ax.text(.14,.18,r'$u_s(p)$',ha='center',fontsize=14)
ax.text(.86,.18,r'$\bar u_{s\prime}(p\prime)$',ha='center',fontsize=14)
ax.text(.16,.43,r'$p$',ha='center',fontsize=13)
ax.text(.86,.43,r'$p\prime=p+k$',ha='center',fontsize=13)
ax.text(.58,.68,r'$k,\ a$',ha='left',fontsize=13,color='#0077ad')
ax.text(.5,.04,r'$-ie\gamma^a$',ha='center',fontsize=15)
ax.text(.5,.91,'One photon meets an oriented fermion line',ha='center',fontsize=13)
fig.subplots_adjust(left=.02,right=.98,bottom=.04,top=.97)
fig.savefig(Path.cwd()/'paper-301-qed-vertex.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
