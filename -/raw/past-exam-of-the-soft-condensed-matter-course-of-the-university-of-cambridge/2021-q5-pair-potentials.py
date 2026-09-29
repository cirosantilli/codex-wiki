"""Original DLVO comparison; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Chosen parameters are illustrative, not exam data. Output is in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
h=np.linspace(.001,3,3000)  # gap / sphere radius
r=2+h
attraction=-(40/6)*(2/(r*r-4)+2/(r*r)+np.log1p(-4/(r*r)))
repulsion=60*np.exp(-h/.35)/(1+h/2)
stabilized=attraction+repulsion
fig,ax=plt.subplots(figsize=(7.4,4.4),layout='constrained')
ax.axhline(0,color='0.6',lw=1)
ax.axvspan(-.08,0,color='0.86')
ax.axvline(0,color='0.45',ls=':',lw=1)
ax.plot(h,attraction,color='#aa4937',lw=2.2,label='without stabilization')
ax.plot(h,stabilized,color='#286fa0',lw=2.2,label='with surface charge')
i=np.argmax(stabilized)
ax.annotate('repulsive barrier',xy=(h[i],stabilized[i]),xytext=(.80,22),arrowprops={'arrowstyle':'->','color':'#286fa0'},color='#286fa0')
ax.annotate('deep primary well\n(clipped)',xy=(.035,-22),xytext=(.65,-17),arrowprops={'arrowstyle':'->','color':'0.4'},fontsize=10)
ax.text(2.35,1.2,r'$U\to0$',color='0.4')
ax.set(xlim=(-.08,3),ylim=(-25,32),xlabel=r'Surface gap $h/a$',ylabel=r'Pair energy $U/(k_BT)$',title='Electrostatic repulsion blocks access to the attractive well')
ax.legend(loc='upper right',frameon=False,fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
