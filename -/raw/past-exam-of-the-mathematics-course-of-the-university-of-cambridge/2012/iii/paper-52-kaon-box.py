"""Draw an original charged-current kaon box, emitting a PNG basename to cwd.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 system +dfsg1.
Caller MPLCONFIGDIR remains unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
fig,ax=plt.subplots(figsize=(9.8,5.2001),dpi=100,facecolor='white')
ax.set(xlim=(0,10),ylim=(0,5.6));ax.axis('off')
color='#243546'
for y in [1.6,3.8]:ax.plot([.7,9.3],[y,y],color=color,lw=1.8)
for y in [1.6,3.8]:
 for x in [1.4,4.35,7.65]:
  a,b=((x,y),(x+.6,y)) if y>2 else ((x+.6,y),(x,y))
  ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,lw=1.3,color=color))
for x in [3.0,7.0]:
 t=np.linspace(0,1,300);ax.plot(x+.12*np.sin(2*np.pi*8*t),1.6+2.2*t,color='#2175a0',lw=1.8)
ax.scatter([3,3,7,7],[1.6,3.8,1.6,3.8],s=30,color=color,zorder=5)
for x,y,t in [(1,4.15,r'$d\ \mathrm{in}$'),(9,4.15,r'$s\ \mathrm{out}$'),(1,1.1,r'$\bar s\ \mathrm{in}$'),(9,1.1,r'$\bar d\ \mathrm{out}$'),(5,4.18,r'$u_i$'),(5,1.14,r'$\bar u_j$'),(2.55,2.7,r'$W^-$'),(7.50,2.7,r'$W^+$')]:ax.text(x,y,t,ha='center',va='center',fontsize=16)
ax.text(.6,2.7,r'$K^0=d\bar s$',ha='left',fontsize=16)
ax.text(9.4,2.7,r'$\bar K^0=s\bar d$',ha='right',fontsize=16)
ax.text(5,5.15,'One-loop charged weak box for neutral-kaon mixing',ha='center',fontsize=17,weight='bold')
ax.text(5,.62,r'$i,j\in\{u,c,t\}$; each weak vertex carries a CKM factor',ha='center',fontsize=14)
ax.text(5,.18,'Arrows show fermion flow; the internal quark flavors are summed.',ha='center',fontsize=12)
fig.subplots_adjust(left=.015,right=.985,bottom=.015,top=.985)
fig.savefig('paper-52-kaon-box.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
