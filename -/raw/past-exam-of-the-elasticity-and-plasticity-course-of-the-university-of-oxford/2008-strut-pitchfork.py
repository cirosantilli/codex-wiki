# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Run in desired output directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,ax=plt.subplots(figsize=(6.5,4.6))
x=np.linspace(0,1.6,300);ax.plot(x,np.sqrt(8*x),color='#2171b5',lw=2);ax.plot(x,-np.sqrt(8*x),color='#2171b5',lw=2,label='energy-minimizing branches')
ax.plot([-1,0],[0,0],color='#2171b5',lw=2);ax.plot([0,1.6],[0,0],'--',color='#c34f2d',lw=2,label='unstable straight branch');ax.plot(0,0,'ko',ms=4)
ax.set(xlabel=r'$\lambda_1$',ylabel=r'$A_0$',title='Supercritical angular-strut buckling response',xlim=(-1,1.6));ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=8)
fig.tight_layout();fig.savefig(Path('2008-strut-pitchfork.png'),dpi=150,facecolor='white');plt.close(fig)
