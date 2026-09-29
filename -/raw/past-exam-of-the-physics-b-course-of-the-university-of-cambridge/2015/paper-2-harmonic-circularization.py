"""Original solution diagram. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

t=np.linspace(0,2*np.pi,700);fig,ax=plt.subplots(figsize=(7,4.4));ax.plot(4*np.cos(t),np.sin(t),label='Original harmonic orbit',color='steelblue',lw=2);ax.plot(2*np.cos(t),2*np.sin(t),'--',color='darkorange',label='Circular orbit: r = 2 r₀');ax.scatter([0],[0],color='black',s=25);p=np.array([4/np.sqrt(5),2/np.sqrt(5)]);er=p/2;v=np.array([-8/np.sqrt(5),1/np.sqrt(5)]);dv=3*er;after=v+dv
ax.scatter(*p,s=30,color='black')
for vec,color,label in [(v,'navy','Incoming velocity'),(dv,'darkred','Radial impulse / m'),(after,'darkgreen','Circular velocity')]:
 ax.annotate('',p+.4*vec,p,arrowprops={'arrowstyle':'->','lw':2,'color':color});ax.plot([],[],color=color,label=label)
ax.plot([0,p[0]],[0,p[1]],':',color='.5');ax.set(xlabel='x / r₀',ylabel='y / r₀',title='A radial impulse removes radial motion while preserving angular momentum',xlim=(-4.4,4.5),ylim=(-2.5,2.7));ax.set_aspect('equal');ax.legend(fontsize=8,loc='lower left');ax.grid(alpha=.15)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
