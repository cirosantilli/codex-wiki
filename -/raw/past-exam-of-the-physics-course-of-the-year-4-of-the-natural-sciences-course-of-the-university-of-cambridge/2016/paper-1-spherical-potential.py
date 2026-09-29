"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

s=np.linspace(0,5,700);v=np.where(s<=1,2-s,1/np.maximum(s,1e-12))
fig,ax=plt.subplots(figsize=(6.8,4));ax.plot(s,v,lw=2.5);ax.axvline(1,color='grey',ls='--');ax.scatter([0,1],[2,1]);ax.annotate('finite central limit = 2',(0,2),(.8,1.9),arrowprops={'arrowstyle':'->'});ax.annotate('continuous value and slope',(1,1),(1.7,1.4),arrowprops={'arrowstyle':'->'});ax.text(2.7,.55,'exterior: 1/s');ax.text(.12,.62,'interior: 2 − s');ax.set(xlabel='Radius s = r/a',ylabel=r'Potential $\phi/[Aa/(2\epsilon_0)]$',ylim=(0,2.25),xlim=(0,5),title='Potential of an inverse-radius spherical charge cloud');ax.grid(alpha=.2)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
