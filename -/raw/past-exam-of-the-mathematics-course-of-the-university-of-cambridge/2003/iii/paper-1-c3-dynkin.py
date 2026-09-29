"""Original diagram; tested with Python 3.14, NumPy and Matplotlib.
Write the matching PNG basename to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(6.6,2.15),dpi=145,facecolor='white')
for x,label,length in [(0,r'$\beta$',r'$\|\beta\|=\sqrt{2}$'),(1.6,r'$\alpha$',r'$\|\alpha\|=1$'),(3.2,r'$\gamma$',r'$\|\gamma\|=1$')]:
 ax.add_patch(Circle((x,0),.18,facecolor='white',edgecolor='#222222',lw=1.8,zorder=3))
 ax.text(x,.3,label,ha='center',fontsize=18);ax.text(x,-.5,length,ha='center',fontsize=12)
for y in [-.06,.06]:ax.plot([.18,1.42],[y,y],color='#222222',lw=1.5)
ax.plot([.68,.88,.68],[.17,0,-.17],color='#222222',lw=1.6)
ax.plot([1.78,3.02],[0,0],color='#222222',lw=1.5)
ax.set_title('C3: the arrow points toward the short root',fontsize=14,pad=12)
ax.set_xlim(-.65,3.85);ax.set_ylim(-.75,.7);ax.axis('off')
fig.tight_layout();fig.savefig('paper-1-c3-dynkin.png',facecolor='white',transparent=False);plt.close(fig)
