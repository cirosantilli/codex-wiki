"""Original pressure-coordinate infrared sensitivity sketch; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
r=np.linspace(0,1,501)
fig,ax=plt.subplots(figsize=(7.4,5.2),constrained_layout=True,facecolor='white')
ax.plot(-4*r*(1-r),r,lw=2.3,color='#1864ab',label='Per equal pressure interval')
ax.plot(-(27/4)*r*r*(1-r),r,lw=2.2,ls='--',color='#d9480f',label='Per equal log-pressure interval')
ax.plot([-1],[.5],'o',color='#1864ab');ax.plot([-1],[2/3],'o',color='#d9480f')
ax.annotate(r'$p=p_0/2$',xy=(-1,.5),xytext=(-.79,.41),arrowprops={'arrowstyle':'->','color':'#1864ab'},color='#1864ab')
ax.annotate(r'$p=2p_0/3$',xy=(-1,2/3),xytext=(-.78,.77),arrowprops={'arrowstyle':'->','color':'#d9480f'},color='#d9480f')
ax.axvline(0,color='.5',lw=1)
ax.set(xlim=(-1.12,.06),ylim=(1,0),xlabel='Signed kernel / its largest magnitude',ylabel=r'$p/p_0$  (pressure increases downward)',title='Absorber sensitivity depends on the vertical measure')
ax.grid(alpha=.18);ax.legend(frameon=False,loc='lower right',fontsize=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
