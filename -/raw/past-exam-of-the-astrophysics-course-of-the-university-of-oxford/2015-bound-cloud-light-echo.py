"""Original explanatory figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(8,5.1),layout='constrained')
star=np.array([0.,0.]);cloud=np.array([2.7,1.7]);top=4.3
ax.plot([0,0],[0,top],color='#666666',ls='--',lw=1.8,label='Direct path')
ax.annotate('',xy=cloud,xytext=star,arrowprops={'arrowstyle':'-|>','lw':2.5,'color':'#126782'})
ax.annotate('',xy=(cloud[0],top),xytext=cloud,arrowprops={'arrowstyle':'-|>','lw':2.5,'color':'#a44418'})
ax.plot(*star,'*',ms=17,color='#a44418');ax.plot(*cloud,'o',ms=10,color='#126782')
ax.text(-.15,-.45,'Quasar',ha='center');ax.text(3.,1.55,'Cloud',ha='left')
ax.annotate('',xy=(2.7,-.05),xytext=(0,-.05),arrowprops={'arrowstyle':'<->','color':'#777777'})
ax.text(1.35,-.38,r'Projected $R_\perp$',ha='center')
ax.plot([0,2.7],[1.7,1.7],ls=':',color='#aaaaaa');ax.text(-.21,.85,r'$s$',ha='right',fontsize=14)
ax.text(1.05,1.03,r'$r=\sqrt{R_\perp^2+s^2}$',rotation=32,color='#126782')
ax.text(1.3,4.45,'Parallel outgoing paths to a distant observer',ha='center')
ax.text(1.3,-1.05,r'Extra path: $r-s$; observed delay: $(1+z)(r-s)/c$',ha='center',fontsize=13)
ax.set(aspect='equal',xlim=(-1.2,4.3),ylim=(-1.4,4.8));ax.axis('off')
ax.set_title('A projected separation does not determine an echo delay\nPositive depth s points toward the observer; schematic, not to scale')

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
