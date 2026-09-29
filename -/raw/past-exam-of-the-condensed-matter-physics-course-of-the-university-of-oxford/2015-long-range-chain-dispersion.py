"""Original explanatory figure. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

q=np.linspace(-2*np.pi,2*np.pi,1500)
w1=np.abs(np.sin(q/2));w2=np.sqrt(np.sin(q/2)**2+.5*np.sin(q)**2)
fig,ax=plt.subplots(figsize=(9,4.5),layout='constrained')
ax.axvspan(-1,1,color='#e8edf1',zorder=0,label='First Brillouin zone')
ax.plot(q/np.pi,w1,color='#126782',lw=2.4,label=r'$C_2=0$')
ax.plot(q/np.pi,w2,color='#a44418',lw=2.4,label=r'$C_2=C_1/2$')
for sign in [-1,1]:ax.plot(sign*2/3,3/(2*np.sqrt(2)),'o',color='#a44418')
ax.annotate(r'Interior maximum: $ka=\pm2\pi/3$',xy=(2/3,3/(2*np.sqrt(2))),xytext=(.02,1.23),arrowprops={'arrowstyle':'->','color':'#777777'},ha='center',fontsize=11)
ax.set(xlim=(-2,2),ylim=(0,1.35),xlabel=r'Wavevector $ka/\pi$',ylabel=r'$\omega/[2\sqrt{C_1/M}]$',title='One acoustic branch per chain, repeated over reciprocal periods')
ax.set_xticks([-2,-1,0,1,2]);ax.legend(loc='lower center',ncol=3,fontsize=10);ax.grid(alpha=.20)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
