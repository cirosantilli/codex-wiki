"""Generate the opaque 800x320 PNG in cwd using the repository dependencies.
Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(8,3.2),dpi=100,facecolor='white')
fig.subplots_adjust(left=.03,right=.97,bottom=.09,top=.88)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
t=np.linspace(0,1,600);vx,vy=.43,.5
ax.plot(.08+(.43-.08)*t,.5+.022*np.sin(2*np.pi*9*t),color='#246ba1',lw=2)
for end,direction in [((.9,.84),1),((.9,.16),-1)]:
 ax.plot([vx,end[0]],[vy,end[1]],color='#222222',lw=2)
 a=np.array([vx,vy])+.43*(np.array(end)-[vx,vy]);b=np.array([vx,vy])+.65*(np.array(end)-[vx,vy])
 if direction<0:a,b=b,a
 ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',mutation_scale=15,color='#222222',lw=1.8))
ax.plot(vx,vy,'o',color='#222222',ms=5)
ax.text(.18,.59,r'$W^+(p)$',fontsize=15)
ax.text(.91,.84,r'$q(k)$',fontsize=15,ha='left',va='center')
ax.text(.91,.16,r'$\bar q\prime(k\prime)$',fontsize=15,ha='left',va='center')
ax.text(.61,.48,r'$\frac{g}{2\sqrt{2}}V_{qq\prime}$',fontsize=15,va='center')
ax.set_title('One charged-current vertex; arrows show fermion-number flow',fontsize=12)
fig.savefig(Path.cwd()/'paper-305-w-decay.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
