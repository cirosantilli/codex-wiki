from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})

fig,ax=plt.subplots(figsize=(7.4,4.5),layout='constrained')
x=np.linspace(-1,0,700);xd=np.linspace(-2/3,0,700)
ax.plot(x,1+x,lw=2.5,label='Empty coasting model',color='#b45b14')
ax.plot(xd,np.maximum(1+1.5*xd,0)**(2/3),lw=2.5,label='Flat matter-only model',color='#16659c')
ax.plot([-1,0],[0,1],ls=':',color='#777777')
ax.scatter([-1,-2/3,0],[0,0,1],color=['#b45b14','#16659c','#222222'])
ax.annotate(r'Age $H_0^{-1}$',(-1,0),(-.99,.22),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate(r'Age $2/(3H_0)$',(-2/3,0),(-.58,.13),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.text(-.32,.86,'Same present value\nand tangent slope',fontsize=10)
ax.set(xlim=(-1.05,.05),ylim=(-.04,1.08),xlabel=r'Time relative to present: $H_0(t-t_0)$',ylabel=r'Normalized scale factor $a(t)$',title='Expansion age depends on past deceleration')
ax.grid(alpha=.2);ax.legend(loc='upper left')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
