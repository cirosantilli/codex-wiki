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
x=np.logspace(-2,1,400);inner=.6*x**-1.5;outer=x**-2;fig,ax=plt.subplots(figsize=(8,4.8));mask=x<.45;outermask=x>1;ax.loglog(x[mask],inner[mask],lw=2,label='Inner free-fall asymptote: r⁻³ᐟ²');ax.loglog(x[outermask],outer[outermask],lw=2,label='Undisturbed envelope: r⁻²');ax.loglog(x[~mask],inner[~mask],':',color='#1f77b4',alpha=.5);ax.loglog(x[~outermask],outer[~outermask],':',color='#ff7f0e',alpha=.4);ax.axvline(1,color='.4',ls='--',label='Expansion front rf = aT t');ax.axvspan(.45,1,color='.8',alpha=.25);ax.text(.58,12,'Transition\nnot solved here',ha='center',fontsize=9);ax.set(xlabel='Radius / expansion-front radius',ylabel='Density / arbitrary normalization',title='Inner and outer asymptotes; no artificial exact join');ax.legend(fontsize=9);ax.grid(which='both',alpha=.12);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
