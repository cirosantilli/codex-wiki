"""Original analytic solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
x=np.geomspace(1,100,450);constant=1-1/x;zero=1-3/x+2/x**1.5;fb=.2;finite=(1-fb)*(x-1)/((1-fb)*x+fb);fig,ax=plt.subplots(figsize=(8.5,4.9));ax.semilogx(x,constant,lw=2,label='Constant relative offset; dark-matter dominated');ax.semilogx(x,zero,lw=2,label='Initially zero baryon contrast and velocity');ax.semilogx(x,finite,'--',lw=2,label='Constant offset; illustrative fB = 0.2');ax.axhline(1,color='.4',ls=':');ax.set(xlabel='Scale factor / recombination scale factor',ylabel='Baryon contrast / dark-matter contrast',title='Catch-up is robust, but early transients depend on the initial mode',ylim=(-.02,1.05));ax.legend(fontsize=9);ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
