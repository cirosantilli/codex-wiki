# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Run in desired output directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,ax=plt.subplots(figsize=(7,5))
T=2.7
for xi in np.arange(-3.5,0,.4):
    t=np.linspace(0,min(T,np.sqrt(-2*xi)),200);ax.plot(xi+t*t,t,color='#2171b5',lw=1)
for xi in np.arange(.4,4.5,.4):
    t=np.linspace(0,min(T,np.sqrt(2*xi)),200);ax.plot(np.full_like(t,xi),t,color='#e58b2a',lw=1)
t=np.linspace(0,T,240);ax.plot(t*t/2,t,'k',lw=2.5,label=r'shock $x_s=t^2/2$')
ax.text(-2,.55,r'$\rho=1$',color='#2171b5',fontsize=13);ax.text(3.4,.55,r'$\rho=0$',color='#b26915',fontsize=13)
ax.set(xlim=(-3.5,4.3),ylim=(0,T),xlabel='$x$',ylabel='$t$',title='Characteristics end at the accelerating shock')
ax.legend(loc='upper left');ax.grid(alpha=.2);fig.tight_layout();fig.savefig(Path('2008-accelerating-shock.png'),dpi=150,facecolor='white');plt.close(fig)
