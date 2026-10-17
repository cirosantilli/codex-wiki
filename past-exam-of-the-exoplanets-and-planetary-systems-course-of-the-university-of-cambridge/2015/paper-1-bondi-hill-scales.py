"""Original solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; saves a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
x=np.logspace(-3,2,500);rb=x;rh=(x/3)**(1/3);cross=1/np.sqrt(3);fig,ax=plt.subplots(figsize=(8.2,4.8));ax.loglog(x,rb,label='Bondi radius / H',lw=2);ax.loglog(x,rh,label='Hill radius / H',lw=2);ax.loglog(x,np.minimum(rb,rh),'--',color='black',label='Smaller outer-envelope scale',lw=1);ax.axhline(1,color='.6',ls=':',label='Disk height H');ax.scatter([cross],[cross],color='black',zorder=4);ax.annotate('Crossover q/h³ = 1/√3',xy=(cross,cross),xytext=(.003,3),arrowprops={'arrowstyle':'->'});ax.set(xlabel='Planet mass ratio / h³ = q/h³',ylabel='Radius / disk scale height H',title='Thermal binding and stellar tides limit different mass regimes',ylim=(.001,30));ax.legend(fontsize=9);ax.grid(which='both',alpha=.13);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
