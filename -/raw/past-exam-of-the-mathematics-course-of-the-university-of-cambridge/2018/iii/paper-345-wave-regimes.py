"""Original schematic; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write the opaque PNG to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
fig,axs=plt.subplots(1,2,figsize=(10,4.8),dpi=100,facecolor='white')
for ax in axs:
 ax.set(xlim=(0,6),ylim=(0,4),xlabel='$x$',ylabel='$z$')
 ax.axhline(0,color='black',lw=2)
 ax.spines[['top','right']].set_visible(False)
 ax.set_xticks([]);ax.set_yticks([]);ax.set_aspect('equal')
ax=axs[0]
for offset in np.arange(-6,7,1.3):
 x=np.linspace(0,6,200);ax.plot(x,.7*x+offset,color='#9dc8df',lw=1.4)
for start,direction,label,color in [((2.4,2.2),(1,-1.43),'phase velocity','#bd3c31'),((2.4,2.2),(1.6,1.12),'group velocity','#146a36')]:
 ax.annotate('',xy=np.add(start,direction),xytext=start,arrowprops={'arrowstyle':'->','lw':2.5,'color':color})
 ax.text(*(np.add(start,direction)+[.1,0]),label,color=color,fontsize=10,ha='center')
ax.annotate('',xy=(1.9,1.43),xytext=(.9,.73),arrowprops={'arrowstyle':'<->','lw':2,'color':'#444444'})
ax.text(.4,1.6,'particle oscillation',fontsize=10)
ax.set_title('Propagating: $0<\\omega<N$')
ax=axs[1]
for z in [.6,1.5,2.4,3.3]:
 for x in [1.2,3,4.8]:
  scale=.65*np.exp(-.45*z)
  ax.add_patch(Ellipse((x,z),scale,1.35*scale,fill=False,color='#317da8',lw=1.6))
z=np.linspace(0,4,200)
ax.plot(5.9-.7*np.exp(-.6*z),z,color='#bd3c31',lw=2)
ax.text(4.2,3.6,'decay envelope',fontsize=10,color='#bd3c31')
ax.annotate('pattern travels',xy=(4.2,.2),xytext=(2,.2),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set_title('Evanescent: $\\omega>N$')
fig.tight_layout()
fig.savefig('paper-345-wave-regimes.png',dpi=100,facecolor='white',transparent=False)
