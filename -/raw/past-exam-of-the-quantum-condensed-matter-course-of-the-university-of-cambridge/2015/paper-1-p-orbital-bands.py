"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

x=np.linspace(-1,1,700);fig,ax=plt.subplots(figsize=(7,4));ax.plot(x,-2*np.cos(np.pi*x),lw=2,label='p_z: side-on π hopping');ax.plot(x,4*np.cos(np.pi*x),lw=2,label='p_x: end-on σ hopping');ax.axhline(0,color='.5',lw=.7);ax.set(xlabel='Crystal momentum k/(π/a)',ylabel='Energy relative to orbital centre (illustrative units)',title='Opposite p-orbital band curvature at the zone centre');ax.set_xticks([-1,0,1],['−π/a','0','π/a']);ax.legend();ax.grid(alpha=.15);fig.text(.5,.005,'Illustration uses |tσ| = 2|tπ| and equal orbital centres; no hopping magnitudes are supplied.',ha='center',fontsize=8);fig.tight_layout(rect=(0,.03,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
