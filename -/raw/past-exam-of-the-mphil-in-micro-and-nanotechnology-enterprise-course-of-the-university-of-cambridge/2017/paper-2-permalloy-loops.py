"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.6));h=np.linspace(-1.5,1.5,1000)
axs[0].plot(h,np.where(h>.15,1,-1),color='#176b9a',label='Increasing H');axs[0].plot(h,np.where(h<-.15,-1,1),color='#c27422',label='Decreasing H');axs[1].plot(h,np.clip(h,-1,1),color='#176b9a')
for ax,t in zip(axs,['Along easy axis','Along in-plane hard axis']):
 ax.set(xlim=(-1.5,1.5),ylim=(-1.2,1.2),xlabel='μ0H (mT; symbolic field ticks)',ylabel='M (A/m; symbolic values)',yticks=[-1,0,1],yticklabels=['−Ms','0','Ms'],xticks=[-1,0,1],xticklabels=['−μ0Hk','0','μ0Hk'],title=t);ax.grid(alpha=.15)
axs[0].annotate('±Hc',xy=(.15,-.9),xytext=(.65,-.5),arrowprops={'arrowstyle':'->'});axs[0].legend(fontsize=8,frameon=False,loc='upper left');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
