"""Original geometry from the coordinate definitions, not a recovered exam figure.
Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7. The only output is a
same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained')
R=1.1;s=1.85
for radius in [1.6,2.55]:
    ax.add_patch(Circle((0,0),radius,fill=False,color='#d2d9df',lw=1.2,ls='--'))
ax.plot([-3.1,3.2],[R,R],color='#69717a',lw=1.6)
ax.annotate('',xy=(3.4,R),xytext=(3.0,R),arrowprops={'arrowstyle':'-|>','color':'#69717a','lw':1.7})
ax.text(3.05,R-.36,'To observer',ha='center',fontsize=11)
ax.annotate('',xy=(s,R),xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':'#126782','lw':2.5})
ax.text(.95,.31,r'$r$',color='#126782',fontsize=17)
ax.annotate('',xy=(0,R),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':'#a44418','lw':2.0})
ax.text(-.25,R/2,r'$R$',ha='right',va='center',color='#a44418',fontsize=16)
ax.annotate('',xy=(s,R+.46),xytext=(0,R+.46),arrowprops={'arrowstyle':'<->','color':'#555555','lw':1.7})
ax.text(s/2,R+.56,r'$s$',ha='center',fontsize=16)
ax.plot([s,s],[R,R+.4],ls=':',color='#999999',lw=1)
ax.plot([0,0],[R,R+.4],ls=':',color='#999999',lw=1)
ax.plot([0,0,s],[0,R,R],'o',color='#126782',ms=5)
ax.text(-.12,-.27,'Galaxy centre',ha='right',fontsize=11)
ax.text(-.15,R+.14,r'$s=0$',ha='right',fontsize=11)
ax.text(s+.12,R+.14,'Tracer star',fontsize=11)
ax.plot([0,.17,.17],[R-.17,R-.17,R],color='#999999',lw=1)
ax.text(-2.7,R+.17,'Line of sight',fontsize=11,color='#555555')
ax.text(.1,-1.7,r'$r^2=R^2+s^2$; on the positive half-line, $ds/dr=r/\sqrt{r^2-R^2}$',ha='center',fontsize=13)
ax.set(xlim=(-3.3,3.7),ylim=(-2.0,2.05),aspect='equal')
ax.axis('off')
ax.set_title('Original spherical-projection geometry\nSchematic from the coordinate definitions; not the recovered exam illustration',fontsize=13)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
