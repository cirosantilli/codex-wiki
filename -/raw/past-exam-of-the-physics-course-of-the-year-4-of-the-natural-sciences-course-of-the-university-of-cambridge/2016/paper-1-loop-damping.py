"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

u=np.linspace(0,3,600);fig,ax=plt.subplots(figsize=(6.8,4));ax.plot(u,np.exp(-u),label='Falling speed deficit: exp(−t/τt)',lw=2);ax.plot(u,np.exp(-3*u),label='Rotating angular speed: exp(−3t/τt)',lw=2);ax.plot(u,np.exp(-6*u),label='Rotational kinetic energy: exp(−6t/τt)',lw=2);ax.scatter([np.log(20)],[.05],color='black');ax.annotate('95% of terminal speed',(np.log(20),.05),(1.7,.3),arrowprops={'arrowstyle':'->'});ax.set(xlabel='Time t/τt   (τt = 2.403072 ms)',ylabel='Normalized decaying quantity',title='Mechanical decay with negligible circuit self-inductance',ylim=(0,1.05));ax.legend(fontsize=9);ax.grid(alpha=.2)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
