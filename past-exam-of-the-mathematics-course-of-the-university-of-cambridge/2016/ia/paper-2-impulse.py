"""Draw the original solution sketch. Run from the output directory.
Tested with Python 3.14.4, matplotlib 3.10.7 and NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,np.pi/2,300)
fig,ax=plt.subplots(figsize=(6.8,3.5),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,np.cos(x),color='#196b9c',lw=2.5)
ax.plot([np.pi/2,2*np.pi],[0,0],color='#196b9c',lw=2.5)
ax.scatter([0,np.pi/2],[1,0],color='#196b9c',zorder=4,s=25)
ax.annotate('unit velocity jump: −1 → 0',xy=(np.pi/2,0),xytext=(2.1,.55),arrowprops={'arrowstyle':'->','color':'#444'},fontsize=10)
ax.axhline(0,color='#999',lw=.6,zorder=0)
ax.axvline(0,color='#999',lw=.6,zorder=0)
ax.set(xlim=(-.1,2*np.pi+.1),ylim=(-.12,1.15),xlabel='$x$',ylabel='$y(x)$')
ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$'])
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.1,right=.97,bottom=.18,top=.94)
fig.savefig('paper-2-impulse.png',facecolor='white',transparent=False)
plt.close(fig)
