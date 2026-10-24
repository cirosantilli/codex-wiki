# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Run in desired output directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,ax=plt.subplots(figsize=(6,5))
y=np.linspace(0,5,200);ax.fill_betweenx(y,-y,y/2,color='#dceaf5',label='both initial feet supplied')
x=np.linspace(-3,3,200);ax.plot(x,2*x,'#2171b5',lw=1.7,label=r'$y=2x$');ax.plot(x,-x,'#e58b2a',lw=1.7,label=r'$y=-x$')
ax.plot([0,0],[0,5],'#0d6b40',lw=3,label='given initial half-line')
P=np.array([.65,3.6]);ax.plot([0,P[0]],[P[1]-2*P[0],P[1]],'--',color='#2171b5');ax.plot([0,P[0]],[P[1]+P[0],P[1]],'--',color='#e58b2a');ax.plot(*P,'ko');ax.text(P[0]+.12,P[1],'P')
ax.set(xlim=(-3,3),ylim=(0,5),xlabel='$x$',ylabel='$y$',title=r'Determined sector $y>\max(2x,-x)$');ax.legend(fontsize=8,loc='lower left');ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('2008-hyperbolic-sector.png'),dpi=150,facecolor='white');plt.close(fig)
