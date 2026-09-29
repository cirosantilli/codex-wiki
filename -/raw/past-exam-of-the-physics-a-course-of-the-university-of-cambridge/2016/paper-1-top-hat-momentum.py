"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7,3.7));u=np.linspace(-5,5,1600);amp=np.sinc(u);ax.plot(u,amp,color='#176d97',label='Momentum amplitude / central amplitude');ax.plot(u,amp**2,color='#bc7725',ls='--',label='Momentum density / central density');ax.axhline(0,color='.5',lw=.7);ax.set(xlabel='p a / (2πℏ)',ylabel='Scaled amplitude or density',ylim=(-.3,1.12),xticks=range(-5,6));ax.legend(frameon=False,fontsize=8,loc='upper right');ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
