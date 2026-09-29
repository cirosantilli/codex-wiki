"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

t=np.linspace(0,20,6000);x=np.sin(2.1*np.pi*t)*np.sin(.1*np.pi*t);env=np.abs(np.sin(.1*np.pi*t));fig,ax=plt.subplots(figsize=(8,3.8));ax.plot(t,x,lw=1,color='royalblue',label='x₂/a');ax.plot(t,env,'--',color='darkred',label='±|sin(πt/10)|');ax.plot(t,-env,'--',color='darkred');ax.scatter([5,10,15],[1,0,1],color='black',s=20);ax.annotate('first full transfer',(5,1),(1,1.32),arrowprops={'arrowstyle':'->'});ax.annotate('original state restored',(10,0),(11,1.22),arrowprops={'arrowstyle':'->'});ax.set(xlabel='Time (s)',ylabel='Displacement / a',title='Beating of the two pendulum modes',xlim=(0,20),ylim=(-1.15,1.5));ax.legend(loc='lower right');ax.grid(alpha=.2)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
