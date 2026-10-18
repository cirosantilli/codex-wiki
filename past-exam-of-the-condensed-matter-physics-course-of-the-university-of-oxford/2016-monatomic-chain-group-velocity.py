"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.4,4.4),constrained_layout=True,facecolor='white')
for side in [-1,1]:
 q=np.linspace(side*1e-6,side,401);ax.plot(q,side*4*np.cos(np.pi*q/2),lw=2,color='#1864ab')
ax.scatter([0,0],[-4,4],s=40,facecolors='white',edgecolors='#1864ab',zorder=3)
ax.axhline(0,color='.7',lw=1);ax.set(xlabel=r'Wavevector $k/(\pi/a)$',ylabel='Signed group velocity (km/s)',title='Opposite acoustic limits at the positive-frequency cusp',xlim=(-1.03,1.03),ylim=(-4.5,4.5));ax.set_xticks([-1,-.5,0,.5,1]);ax.grid(alpha=.16)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
