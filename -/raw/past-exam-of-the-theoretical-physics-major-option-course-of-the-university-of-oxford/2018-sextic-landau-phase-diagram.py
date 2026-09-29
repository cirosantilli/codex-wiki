"""Original sextic Landau phase diagram, c=1; Python 3.14/numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(9,5.8),layout='constrained',facecolor='white')
b=np.linspace(-3,2,901);transition=np.where(b<0,3*b*b/16,0)
ax.fill_between(b,-.65,transition,color='#d9e9f4',label='Ordered global minima')
ax.fill_between(b,transition,2.6,color='#f7ebd4',label='Disordered global minimum')
neg=np.linspace(-3,0,401);pos=np.linspace(0,2,301)
ax.plot(neg,3*neg**2/16,color='#a33142',lw=2.7,label=r'First order: $a=3b^2/16$')
ax.plot(pos,np.zeros_like(pos),color='#126782',lw=3,label='Continuous transition: a = 0, b > 0')
ax.plot(neg,neg**2/4,color='#704d85',lw=1.8,ls='--',label=r'Ordered spinodal: $a=b^2/4$')
ax.plot(neg,np.zeros_like(neg),color='#5d6470',lw=1.8,ls=':',label='Disordered spinodal: a = 0, b < 0')
ax.plot(0,0,'ko',ms=6)
ax.annotate('Tricritical point',xy=(0,0),xytext=(.35,.38),arrowprops={'arrowstyle':'->','lw':1},fontsize=11)
ax.annotate('Ordered metastable',xy=(-2.5,1.4),xytext=(-2.8,2.35),arrowprops={'arrowstyle':'->','lw':1},fontsize=10)
ax.text(-2.8,.5,'Disordered metastable',fontsize=10)
ax.text(.5,1.1,r'$m=0$',fontsize=16)
ax.text(.6,-.4,r'$m=\pm\sqrt{x_+}$',fontsize=15)
ax.set(xlim=(-3,2),ylim=(-.65,2.6),xlabel='Quartic coefficient b',ylabel='Quadratic coefficient a',title='Sextic Landau free energy: equilibrium and metastability (c = 1)')
ax.set_facecolor('white');ax.grid(alpha=.15)
ax.legend(loc='upper right',fontsize=9,framealpha=.96)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
