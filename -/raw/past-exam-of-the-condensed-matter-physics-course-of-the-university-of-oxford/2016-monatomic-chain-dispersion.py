"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.4,4.4),constrained_layout=True,facecolor='white')
q=np.linspace(-1,1,801);ax.plot(q,4*np.abs(np.sin(np.pi*q/2)),lw=2,color='#1864ab');ax.scatter([-1,0,1],[4,0,4],s=25,color='#1864ab')
ax.set(xlabel=r'Wavevector $k/(\pi/a)$',ylabel=r'Angular frequency $\omega$ ($10^{13}$ rad/s)',title='One scalar acoustic branch, two propagation directions',xlim=(-1.03,1.03),ylim=(0,4.4));ax.set_xticks([-1,-.5,0,.5,1]);ax.text(-.96,.6,r'$a=0.2$ nm'+'\n'+r'$v_s=4$ km/s'+'\n'+r'$\pi/a=15.71$ nm$^{-1}$',fontsize=10);ax.grid(alpha=.16)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
