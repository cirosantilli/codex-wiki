"""Original antiplane crack-tip characteristic sketch; Python 3.14.

Run from the desired output directory. Uses root NumPy/Matplotlib dependencies.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig,ax=plt.subplots(figsize=(7.8,5.6),facecolor='white')
ax.set_facecolor('white')
ax.add_patch(Wedge((0,0),1.5,-90,90,facecolor='#e8f2fb',edgecolor='none'))
for angle in np.linspace(-np.pi/2,np.pi/2,9):
 ax.plot([0,1.5*np.cos(angle)],[0,1.5*np.sin(angle)],color='#467ca4',lw=1.1)
ax.plot([0,0],[-1.65,1.65],color='#163e63',lw=2.5)
ax.plot([-1.65,0],[0,0],color='#292929',lw=3)
ax.scatter([0],[0],s=24,color='#292929',zorder=5)
ax.annotate('',xy=(1.8,0),xytext=(0.1,0),arrowprops={'arrowstyle':'->','color':'#444444'})
ax.text(1.77,.10,r'$x_1$',ha='left',va='bottom',fontsize=11)
ax.annotate(r'$x_2$',xy=(0,1.9),xytext=(0,1.72),arrowprops={'arrowstyle':'->','color':'#444444'},ha='center',va='center')
ax.text(-1.52,.10,'traction-free crack',fontsize=10,color='#292929')
ax.text(-1.55,.9,'constant stress\n'+r'$(\sigma_{13},\sigma_{23})=(-A,0)$',fontsize=10)
ax.text(-1.55,-1.1,'constant stress\n'+r'$(\sigma_{13},\sigma_{23})=(A,0)$',fontsize=10)
ax.text(.7,.72,'forward fan\nradial characteristics',fontsize=10,ha='center',color='#163e63',bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(.12,1.46,r'$\phi=\pi/2$',fontsize=11)
ax.text(.12,-1.49,r'$\phi=-\pi/2$',fontsize=11)
ax.text(.02,-.12,'tip',ha='left',va='top',fontsize=9)
ax.set_xlim(-1.78,1.98);ax.set_ylim(-1.72,2.0);ax.set_aspect('equal');ax.axis('off')
ax.set_title('Elliptic yield surface: vertical fan boundaries',fontsize=13,pad=12)
fig.tight_layout(pad=1.0)
fig.savefig(Path.cwd()/'paper-78-plastic-fan.png',dpi=160,facecolor='white',transparent=False)
plt.close(fig)
